# Healthcare Costs Prediction System Using Linear Regression

## Summary
- The system uses linear regression to predict healthcare costs, enabling healthcare providers to target resources effectively towards individuals likely to incur significant costs. The system helps providers design medical aid packages with appropriate premiums and deductibles, ensuring financial sustainability. The insights gained from the system can aid healthcare providers and medical aid organizations in their general business planning and decision-making processes. For individuals, having prior knowledge of their projected costs enables them to choose suitable medical aid packages and make informed lifestyle changes to manage their healthcare expenses.

## Repository Structure

This repository contains the following files:

 - App.py: The main Python script that runs the Streamlit web application.
 - HCPS.pkl: A pre-trained regression model used for predicting healthcare costs.
 - images/: A folder containing the images used in the web application.
 - database/: A folder containing an exact replicate of the dataset used to train the regression model for exploration purposes.
 - HealthCareCostPredictionSystem.ipynb: A Jupyter Notebook file containing the code for building the regression model.
 - insurance.csv: The dataset used to train the regression model.
 - requirements.txt: A text file containing the required Python packages.

## Steps for implementation:
Running the System
1. Building and Training the Model
 - Open the HealthcareCostPredictionSystem.ipynb file in your Jupyter Notebook environment.
 - Run all the cells in the notebook to load the dataset, pre-process the data, split it into training and testing sets, build the linear regression model, train the model, and save the trained model to a pickle file.

2. Running the Streamlit Web App
 - Open a terminal or command prompt and navigate to the directory where you unzipped the files and install the required Python libraries by running the following command: pip install -r requirements.txt
 - Run the Streamlit web app by executing the following command: streamlit run App.py. This will start the Streamlit web application and open it in your default web browser.

Using the System
 - The web interface has a sidebar menu with three options: ‘Medical Aid Provider’, ‘Policy Holder’, and ‘Healthcare Provider’.
 - Select the appropriate option based on your role.
 - Enter the required details such as gender, age, BMI, number of children, smoking status, and region.
 - Click the "Predict" button to see the predicted healthcare costs.
 - The application will also provide recommendations and suggested medical aid packages based on the predicted costs.
 - The application includes a chatbot feature that provides real time responses about anything.
 - The ‘Explore Dataset’ feature allows users to explore the dataset used to train the predictive model.

Additional Requirements
 - Create a folder named .streamlit in your project directory and inside it, create a file named secrets.toml. file with the following content:: REPLICATE_API_TOKEN = "replicate API key".
 - Replace 'replicate API key' with your own replicate API key which you can create on: https://replicate.com/
