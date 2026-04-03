<h1> Customer Churn Prediction – End-to-End ML Project </h1>

This project builds and deploys a machine learning system to predict the probability of a customer churn. It covers the complete data science lifecycle — from data exploration and modeling to production-ready API deployment.

<h3>Problem Statement</h3>

Given the data of the customers of a telecom company and the churning trend of the customers.
The task is treated as a probabilistic binary classification problem and evaluated using ROC-AUC and Log Loss.

<h3> Modeling Approach</h3>

Performed EDA to understand feature distributions, imbalance, and correlations

Built robust preprocessing using scikit-learn Pipelines

Numerical scaling and imputation

Ordinal and nominal categorical encoding

Trained and compared multiple models:

- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBOOST 
(Note - Both GradientBoost and XGBoost gave comparable results in K-Fold method, Gradient Boost preferred, as it performs well in all different scenarios.)

Used K-Fold cross-validation and prediction averaging to reduce variance

Carefully avoided data leakage throughout experimentation

Final offline ROC-AUC ≈ 0.9138, with consistent leaderboard performance.

<h3> Deployment </h3>

The final GradientBoost pipeline (preprocessing + model) is deployed as a FastAPI REST service using Render.

API Features

 - /predict endpoint (POST)
 - Accepts customer data as JSON
 - Returns churning risk probability
 - Input validation using Pydantic
 - Interactive API testing via Swagger UI (/docs)
