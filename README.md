# Healthcare Costs Prediction System Using Linear Regression

## Summary
- The system uses linear regression to predict healthcare costs, enabling healthcare providers to target resources effectively towards individuals likely to incur significant costs. The cost prediction model helps providers design medical aid packages with appropriate premiums and deductibles, ensuring financial sustainability. The insights gained from the cost prediction model can aid healthcare providers and medical aid organizations in their general business planning and decision-making processes. For individuals, having prior knowledge of their projected costs enables them to choose suitable medical aid packages and make informed lifestyle changes to manage their healthcare expenses.

## Repository Structure

This repository contains the following files:

 - HealthcareCostsPredictionSystem.ipynb: A Jupyter Notebook file that includes the code for data collection, preprocessing, visualization, splitting, model development, training, and evaluation.
 - HCPS.pkl: A pickle file that stores the trained linear regression model, which is used in the Streamlit web application.
 - requirements.txt: A file that lists all the necessary Python libraries and their versions required to run the project.
 - app.py: The code for the Streamlit web application that allows users to input data and receive predictions of their healthcare costs.

## Steps for implementation:
1) Data Collection  
   - Collecting required data  (https://www.kaggle.com/datasets/mirichoi0218/insurance)
   - Loading required libraries
     
2) Data Preparation  
   - Data Cleaning  
   - Data Normalization  
   - Categorical Data Encoding  
   - Data Analysis  
   - Splitting the data
      
3) Model Training    

4) Model Evaluation and Validation   
   - Graphical Representation of the predicted values  
   - Metrics Evaluation  
   - Prediction using new data
         
5) Model Deployment  
   - Deploying a model is a method of implementing a machine learning model to real use. In this model, the Streamlit library is used to develop a Graphical User Interface where the users give the necessary inputs required for the prediction.

## Steps to run the web app
   - In VSCode, open the app.py file.
   - Click the "Run" button or press Ctrl+F5 (Windows/Linux) or Cmd+F5 (macOS) to run the application.
   - Run the following command to display the web app in your browser.
   - In the VSCode terminal, type the command 'streamlit run app.py'. This will launch the web application in your default web browser.
