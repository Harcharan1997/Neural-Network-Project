# Neural-Network-Project
Overview
This project aims to predict housing prices using machine learning models and deploy the model as a Flask web application. The process involves data selection, cleaning, exploration, feature engineering, model selection, hyperparameter tuning, and finally, deployment on a cloud platform.

Step 1: Dataset Selection
The dataset chosen for this project is the "Housing Prices" dataset, which includes information about various housing features such as size, number of bedrooms, location, etc.

Step 2: Data Cleaning
The dataset underwent a thorough cleaning process to handle missing values and outliers. Techniques like handling missing value, outliers detection & removal, feature engineering and final data cleaning were employed to ensure data integrity.

Step 3: Data Exploration
Statistical and visual methods were used to understand the dataset. Used dataset overview and checked null values for statistical and used category visualization, box plot, scatter plot, histogram, scatter plot and correlation heatmap.

Step 4: Feature Engineering
New features were created, and categorical variables were handled appropriately. Data transformation techniques were applied and some of the techniques handling inapproporiate data, adding new features and some other to enhance model performance.

Step 5: Model Selection
Multiple models were experimented with for regression, including Linear Regression, Decision Trees, and Artificial Neural Network (ANN) models. For classification, Logistic Regression, Decision Trees, Support Vector Machines (SVM), and ANN were considered.

Step 6: Hyperparameter Tuning
Model performance was optimized through hyperparameter tuning using techniques like GridSearchCV.

Step 7: Pickle Files
The trained models were saved using the pickle library to facilitate easy loading for deployment.

Step 8: Flask Web Application
A Flask web application was developed with a simple user interface. Users can input housing features, and the application will return price predictions using the trained models.

Step 9: GitHub Repository
All code files, datasets, and necessary files are included in the GitHub repository. 

Step 10: Cloud Deployment
The Flask application is deployed on a cloud platform, making it accessible to users. Cloud platforms such as Heroku, Render, AWS, Azure, or GCP can be used for deployment.

