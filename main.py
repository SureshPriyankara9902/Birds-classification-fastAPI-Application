from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from PIL import Image
import torch
import torchvision.transforms as transforms
import json
import torch.nn.functional as F  # Import for softmax

app = FastAPI()

# Load class labels from JSON file
def load_class_labels():
    with open('classes.json', 'r') as f:
        class_labels = json.load(f)
    return class_labels

# Function to load the model
def load_model():
    model = torch.load('trained_model_resnet50.pt', map_location=torch.device('cpu'))
    model.eval()  # Set the model to evaluation mode
    return model

# Initialize model and class labels
model = load_model()
classes = load_class_labels()

# Image preprocessing function
def transform_image(image_bytes):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    image = Image.open(BytesIO(image_bytes))
    return transform(image).unsqueeze(0)

# Inference function with probabilities
def predict(image_tensor):
    with torch.no_grad():
        outputs = model(image_tensor)
        probabilities = F.softmax(outputs, dim=1)  # Convert outputs to probabilities
        top_prob, top_class = probabilities.topk(1, dim=1)  # Get the highest probability and class index
        predicted_class = top_class.item()
        predicted_prob = top_prob.item()
        return {
            "class": classes[str(predicted_class)],  # Class label
            "probability": predicted_prob  # Probability for the predicted class
        }

# FastAPI endpoint for image prediction (POST method)
@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image_tensor = transform_image(image_bytes)
    prediction = predict(image_tensor)
    return {"prediction": prediction}

# FastAPI endpoint for a basic GET request
@app.get("/")
def read_root():
    return {"message": "Bird Classification API is running."}

# GET method to retrieve the class labels
@app.get("/classes/")
def get_classes():
    return {"classes": classes}

# Main entry point for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Get the port from environment variables, default to 8000 for local
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
