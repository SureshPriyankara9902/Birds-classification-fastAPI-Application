*Bird Classification FastAPI Application*

This project is a machine learning web application that uses FastAPI to classify bird species based on an uploaded image. The model is built using a pre-trained ResNet-50 architecture from PyTorch. The API provides endpoints for predicting bird species from an image and retrieving class labels.

*Features*

#Classify bird species from an image.
#Access bird class labels through a GET request.
#REST API using FastAPI framework.
#Deployed with a pre-trained ResNet-50 model.

*Files Included*

#main.py: Main application file containing API routes for prediction and class retrieval.
#trained_model_resnet50.pt: The pre-trained PyTorch model for bird classification.
#index_to_class_label.json: JSON file mapping class indices to bird species labels.
#requirements.txt: Python dependencies needed to run the project.
#classes.json: Contains bird class labels for the model's predictions.

*Prerequisites*

Python 3.9
pip (Python package installer)

*Setup Instructions*

1. git clone <repository_url>
2. cd Birds clasification fastAPI
3. pip install -r requirements.txt
4. uvicorn main:app --reload
This will start the FastAPI server, and you can access the API at http://127.0.0.1:8000.

*API Endpoints*

Prediction Endpoint (POST)
URL: /predict/
Method: POST
Description: Upload a bird image for classification.
Request: Upload file using the form field file.

*Response*
json
{
  "prediction": {
    "class": "species_name",
    "probability": 0.95
  }
}

*Class Labels Endpoint (GET)*
URL: /classes/
Method: GET
Description: Retrieve the list of bird species class labels.

Read Root (GET)
curl -X 'GET' \
'http://127.0.0.1:8000/' \
-H 'accept: application/json'
Description: Returns a basic message indicating the API is running.

 *Example Usage*
Using curl for image prediction:

curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@your_image.jpg'

*Using a browser or HTTP client:*
Visit http://127.0.0.1:8000/docs to access the Swagger UI for interactive API testing.
Upload images and view predictions directly from the documentation interface.
