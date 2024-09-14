# Bird Classification FastAPI Application

This project is a machine learning web application that uses FastAPI to classify bird species based on an uploaded image. The model is built using a pre-trained ResNet-50 architecture from PyTorch. The API provides endpoints for predicting bird species from an image and retrieving class labels.

deployed the fastapi application using render : https://birds-classification-wt3j.onrender.com/

# Features

1. Classify bird species from an image.
2. calculate the probability of birds speies
3. Access bird class labels through a GET request.
4. REST API using FastAPI framework.
5. Deployed with a pre-trained ResNet-50 model.

# Files Included

1. main.py: Main application file containing API routes for prediction and class retrieval.
2. trained_model_resnet50.pt: The PyTorch model for bird classification.
3. requirements.txt: Python dependencies needed to run the project.
4. classes.json: Contains bird class labels for the model's predictions.

# Prerequisites

Python 3.9
pip (Python package installer)

*Setup Instructions*

1. git clone https://github.com/SureshPriyankara9902/Birds-classification-fastAPI-Application.git
2. cd Birds clasification fastAPI
3. pip install -r requirements.txt
4. uvicorn main:app --reload
   
*This will start the FastAPI server, and you can access the API at http://127.0.0.1:8000.*

# API Endpoints

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
![Screenshot (269)](https://github.com/user-attachments/assets/5cd9979e-5ac3-4d22-955c-d75bb0b3c9e6)

# Class Labels Endpoint (GET)
URL: /classes/
Method: GET
Description: Retrieve the list of bird species class labels.
![Screenshot (270)](https://github.com/user-attachments/assets/d53e19c0-30c0-4b9b-80de-03906dc1e776)

# Read Root (GET)
curl -X 'GET' \
'http://127.0.0.1:8000/' \
-H 'accept: application/json'
Description: Returns a basic message indicating the API is running.
![Screenshot (271)](https://github.com/user-attachments/assets/bd9cfb4b-115a-4732-b000-da15d56b83d3)



*Using a browser or HTTP client:*
Visit http://127.0.0.1:8000/docs to access the Swagger UI for interactive API testing.
Upload images and view predictions directly from the documentation interface.


![Screenshot (273)](https://github.com/user-attachments/assets/f5132654-0d58-451c-ab9b-43b5ed0f161d)






