# 🌱 Food Wastage Prediction System

A machine learning project developed as part of an **IBM SkillsBuild / SDG-focused virtual internship**, designed to predict the amount of food that may be wasted based on factors such as food type, event type, storage conditions, quantity of food, number of guests, seasonality, and pricing.

The project combines **data analysis, machine learning, feature engineering, and a Flask-based web application** to provide an easy-to-use food wastage prediction system.

---

## 🎯 Project Objective

Food wastage is a significant sustainability challenge. The goal of this project is to use machine learning to estimate potential food wastage before or during an event.

The prediction system can help users understand how different factors affect expected food wastage and potentially support better food preparation and resource planning.

---

## 🚀 Features

- 📊 Exploratory Data Analysis of food wastage data
- 🤖 Machine Learning-based food wastage prediction
- 🌳 Random Forest, Gradient Boosting, Linear Regression, and XGBoost comparison
- ⚡ Tuned XGBoost model for prediction
- 🔧 Feature engineering using `Food_Per_Guest`
- 🌐 Flask-based web application
- 📝 User-friendly input form
- 🔽 Dropdown menus for categorical variables
- 🔢 Numerical inputs for guests and food quantity
- 🧠 Automatic filling of missing numerical values using a similar dataset record
- 📈 Predicted food wastage displayed directly on the website

---

## 🧠 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Train-Test Split
     ↓
Categorical Feature Encoding
     ↓
Model Training
     ↓
Hyperparameter Tuning
     ↓
XGBoost Model Selection
     ↓
Model + Preprocessor Saved
     ↓
Flask Web Application
     ↓
Food Wastage Prediction