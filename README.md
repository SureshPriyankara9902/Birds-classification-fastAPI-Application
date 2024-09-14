## Bird Classification FastAPI Application

This project is a machine learning web application that uses FastAPI to classify bird species based on an uploaded image.The API provides endpoints for predicting bird species from an image and retrieving class labels.

deployed the fastapi application using render : https://birds-classification-wt3j.onrender.com

![Screenshot (274)](https://github.com/user-attachments/assets/88c549cb-4d3c-446e-bce9-030198d4fc79)

![Screenshot (275)](https://github.com/user-attachments/assets/3097ccda-0e90-48e9-be94-0112a2afb6a7)


# Features

1. Classify bird species from an image.
2. calculate the probability of birds speies
3. Access bird class labels through a GET request.
4. REST API using FastAPI framework.
5. Deployed using render 

# Files Included

1. main.py: Main application file containing API routes for prediction and class retrieval.
2. Birds_classify_model.pt: The PyTorch model for bird classification.
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
   
# This will start the FastAPI server, and you can access the API at http://127.0.0.1:8000.

![Screenshot (278)](https://github.com/user-attachments/assets/90047d12-da62-41ae-8c4d-27e8e5ebfc46)

# Using a browser or HTTP client:
Visit http://127.0.0.1:8000/docs to access the Swagger UI for interactive API testing.
Upload images and view predictions directly from the documentation interface.


![Screenshot (279)](https://github.com/user-attachments/assets/5e564ed8-e61e-4370-aae8-49959dc2ef1f)




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


![Screenshot (271)](https://github.com/user-attachments/assets/53c1994c-7571-4dc8-80a7-426f47337757)



# Read Root (GET)
curl -X 'GET' \
'http://127.0.0.1:8000/' \
-H 'accept: application/json'
Description: Returns a basic message indicating the API is running.

*Response*
{
  "message": "Bird Classification API is running."
}


![Screenshot (276)](https://github.com/user-attachments/assets/22520159-2a9a-48d6-b0b0-76af723f8233)


# Class Labels Endpoint (GET)
- URL: /classes/
- Method: GET
- Description: Retrieve the list of bird species class labels.
- curl -X 'GET' \
  'http://127.0.0.1:8000/classes/' \
  -H 'accept: application/json'

*Response*
  "classes": {
    "0": "African Crowned Crane",
    "1": "African Firefinch",
    "2": "Albatross",
    "3": "Alexandrine Parakeet",
    "4": "American Avocet",
    "5": "American Bittern",
        ...............
        }

        
  ![Screenshot (277)](https://github.com/user-attachments/assets/4e58de70-315d-4f15-9efd-122bfbfe4d71)




![Screenshot (273)](https://github.com/user-attachments/assets/f5132654-0d58-451c-ab9b-43b5ed0f161d)






