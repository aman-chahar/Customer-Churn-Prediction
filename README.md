# Telecom Customer Churn Prediction

### Step 1: Project Overview
This project's primary goal is to predict customer churn, which refers to the loss of customers in a telecom company. Customer churn can have a significant impact on a company's revenue and profitability. In this project, we aim to proactively identify customers at risk of leaving the service using machine learning techniques. The ultimate objective is to develop a model that assists in retaining high-risk customers and reducing churn rates.

Streamlit App Link:- https://customer-churn-prediction-uwwsvmtk6encm3qxabjveq.streamlit.app/

### Step 2: Data Collection
Gather historical customer data from the telecom company's records. The dataset should include various customer attributes such as tenure, monthly charges, contract type, internet service, and more. Additionally, it should indicate whether a customer has churned (left) or not.

### Step 3: Data Preprocessing
Data preprocessing is crucial to ensure that the data is clean and ready for analysis and modeling. This step involves:

- Handling missing values: Check for any missing data in the dataset and decide how to handle it. In your project, it seems missing values in the "TotalCharges" column were treated by removing rows with missing values.
- Encoding categorical features: Convert categorical variables into numerical format using techniques like one-hot encoding or label encoding. For example, gender, partner, and other features were encoded.
- Exploratory Data Analysis (EDA): Conduct EDA to gain insights into the data. This step includes generating summary statistics, creating visualizations, and exploring relationships between variables. EDA can reveal patterns, correlations, and potential predictive features.

### Step 4: Model Building
Once the data is prepared,I implemented Decision Tree and Random Forest classifiers.

- **Decision Trees**: A tree-like model that splits data based on attribute values.(79% accuracy)
- **Random Forest**: An ensemble of decision trees that can improve predictive accuracy.(80% accuracy)

These models are trained using historical data to learn patterns and make predictions.

### Step 5: Model Evaluation
After training the models, it's essential to assess their performance.

- **Accuracy**: The proportion of correctly predicted churn cases.
- **Recall**: The ability of the model to correctly identify churn cases (true positives).
- **Precision**: The proportion of true churn cases among the predicted churn cases.
- **F1-Score**: The harmonic mean of precision and recall.
 
On the basis of Accuracy and Recall value I choose Random Forest that predict churn with 80% accuracy.

### Step 6: Web Application Development
To make the model accessible and user-friendly, created a Streamlit web application. The application allows users to input customer information and receive real-time churn predictions. Users can interact with the application to assess whether a specific customer is likely to churn.

### Step 7: Impact
- The predictive model allows the telecom company to proactively target high-risk customers with retention strategies, reducing churn rates and preserving revenue.
- The Streamlit web application enables the company to make quick decisions based on real-time customer data.
