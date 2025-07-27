# Dengue Fever Prediction API for African Countries

## Mission

Our mission is to build a predictive model that addresses an aspect of the global dengue fever epidemic, specifically focusing on its incidence in African countries. By leveraging historical case data, this project aims to provide insights into the progression of outbreaks, contributing to better understanding and potential mitigation strategies in previously less affected or emerging regions due as a possible link to climate change.

## Dataset Description and Source

**Description:**
The dataset utilized in this project, `Data on rise of fever in Africa - Dataset.csv`, contains aggregated dengue fever case numbers for various African countries over two specific years: 2023 and 2024. For each country, it provides the total number of cases for each year, as well as a grand total. This data allows for the analysis of year-over-year trends and the overall burden of the disease in these regions.

**Source:**
This dataset is derived from reported cases by the World Health Organization (WHO) as provided in the initial project brief.

## Data Visualizations

To understand the characteristics and trends within the dataset, several meaningful visualizations were created, which directly informed the modeling process:

1.  **Variable Distributions (Bar Plots):** Bar plots were used to visualize the total dengue cases per country, as well as the distribution of cases for 2023 and 2024 individually. These visualizations highlighted countries with the highest burden and revealed significant year-over-year changes in case numbers for specific nations (e.g., Eritrea and Mauritius showing sharp increases, while Ethiopia showed a decrease).

2.  **Relationship between Variables (Scatter Plot):** A scatter plot was generated to illustrate the correlation between 2023 and 2024 dengue cases. This visualization was critical in understanding the linearity (or lack thereof) of the relationship, revealing that while some countries followed a general trend, others experienced outlier outbreaks. This directly affected the choice and performance of the linear regression model.

*(Note: The actual visualization images are generated during the Colab notebook execution and can be viewed there or if you saved them locally.)*

## Linear Regression Model Implementation

This project implements and compares three different regression models to predict 2024 dengue cases based on 2023 figures:

* **SGDRegressor (Linear Regression with Gradient Descent):** Used to demonstrate a basic linear relationship and visualize the training loss curve.
* **DecisionTreeRegressor:** A non-linear model for comparison.
* **RandomForestRegressor:** An ensemble method providing more robust predictions by combining multiple decision trees.

The model with the least loss (highest R-squared score) among these three was selected and saved for the prediction API.

## API Endpoint and Deployment

The best-performing model is exposed via a FastAPI web API, allowing for external prediction requests.

* **API Endpoint:** `/predict` (POST request)
* **Public URL:** Your deployed API will be available at a public URL provided by Render (e.g., `https://your-service-name.onrender.com`).
* **Swagger UI Documentation:** The interactive API documentation is accessible at the public URL followed by `/docs` (e.g., `https://your-service-name.onrender.com/docs`).
* **CORS Middleware:** Implemented to allow cross-origin requests.
* **Input Constraints:** Request variables are strongly typed and include range constraints using Pydantic's `BaseModel` to ensure data validity (e.g., `cases_2023` as a float with a range from >0 to <=50000).
