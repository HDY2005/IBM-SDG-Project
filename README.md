# 🌱 Food Wastage Prediction System

A Machine Learning project developed as part of an **IBM SkillsBuild / SDG-focused virtual internship** to predict food wastage based on different food, event, storage, and quantity-related factors.

The project combines **Data Analysis, Machine Learning, Feature Engineering, XGBoost, and Flask** to create an end-to-end food wastage prediction system.

---

## 🎯 Objective

Food wastage is an important sustainability challenge. This project aims to use Machine Learning to estimate the amount of food that may be wasted based on historical data.

The system allows users to enter information about a food or event scenario and receive an estimated food wastage amount.

This project is aligned with:

**SDG 12 – Responsible Consumption and Production**

---

## 🚀 Features

- 📊 Exploratory Data Analysis
- 🧹 Data cleaning and preprocessing
- 🔧 Feature engineering
- 🤖 Multiple Machine Learning models
- ⚡ XGBoost regression
- 🎯 Hyperparameter tuning using `RandomizedSearchCV`
- 🔢 Categorical feature encoding using `OneHotEncoder`
- 🌐 Flask web application
- 📝 User-friendly prediction form
- 🔽 Dropdown menus for categorical inputs
- 🔢 Numerical inputs for guests and food quantity
- 🧠 Automatic handling of missing numerical inputs
- 🔍 Similar-record based value completion
- 📈 Food wastage prediction

---

## 🧠 Machine Learning Workflow

```text
Dataset
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
XGBoost Model
   ↓
Model + Preprocessor Saved
   ↓
Flask Web Application
   ↓
Food Wastage Prediction
```

---

## 📂 Dataset

The dataset contains information related to food, events, storage conditions, purchasing patterns, quantity of food, number of guests, and food wastage.

### Features

| Feature               | Type        |
| --------------------- | ----------- |
| Type of Food          | Categorical |
| Event Type            | Categorical |
| Storage Conditions    | Categorical |
| Purchase History      | Categorical |
| Seasonality           | Categorical |
| Preparation Method    | Categorical |
| Geographical Location | Categorical |
| Pricing               | Categorical |
| Number of Guests      | Numerical   |
| Quantity of Food      | Numerical   |

### Engineered Feature

A new feature called `Food_Per_Guest` is created:

```text
Food_Per_Guest = Quantity of Food / Number of Guests
```

### Target Variable

```text
Wastage Food Amount
```

---

## 🤖 Machine Learning Models

The project compares multiple regression algorithms:

| Model             |    MAE |   RMSE |     R² |
| ----------------- | -----: | -----: | -----: |
| Random Forest     | 1.7127 | 2.8073 | 0.9256 |
| Gradient Boosting | 2.0579 | 2.8921 | 0.9210 |
| Linear Regression | 3.4910 | 4.4388 | 0.8139 |
| XGBoost           | 1.9204 | 2.8259 | 0.9246 |

The XGBoost model was further tuned using `RandomizedSearchCV`.

The trained XGBoost model and its preprocessing pipeline are saved together as:

```text
food_waste_xgb_pipeline.pkl
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis & Machine Learning

* Pandas
* NumPy
* Scikit-learn
* XGBoost

### Data Visualization

* Matplotlib

### Web Development

* Flask
* HTML
* CSS

### Model Saving

* Joblib

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 🌐 Web Application

The project includes a Flask-based web application that allows users to interact with the trained Machine Learning model.

### Application Workflow

1. The user enters information through the web form.
2. Categorical values are selected using dropdown menus.
3. Numerical values such as the number of guests and quantity of food can be entered.
4. If a numerical value is left blank, the application searches for a similar record in the dataset.
5. The missing numerical value is automatically filled.
6. The `Food_Per_Guest` feature is calculated.
7. The saved preprocessing pipeline transforms the input data.
8. The processed data is passed to the XGBoost model.
9. The estimated food wastage amount is displayed on the webpage.

---

## 📁 Project Structure

```text
SDG Project - Food Wastage/
│
├── templates/
│   └── index.html
│
├── app.py
├── food_waste_analysis.ipynb
├── food_waste_data.csv
├── food_waste_xgb_pipeline.pkl
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/HDY2005/MachineLearning-Projects.git
```

### 2. Navigate to the Project Directory

```bash
cd "SDG Project - Food Wastage"
```

### 3. Install Required Libraries

```bash
pip install pandas numpy scikit-learn xgboost joblib flask matplotlib
```

---

## ▶️ Running the Application

Run the Flask application using:

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

Open the address in a web browser to access the Food Wastage Prediction System.

---

## 🧪 Example Input

The application accepts information such as:

| Feature               | Example      |
| --------------------- | ------------ |
| Type of Food          | Meat         |
| Event Type            | Wedding      |
| Storage Conditions    | Refrigerated |
| Purchase History      | High         |
| Seasonality           | Summer       |
| Preparation Method    | Buffet       |
| Geographical Location | Urban        |
| Pricing               | High         |
| Number of Guests      | 200          |
| Quantity of Food      | 300          |

The application processes the provided information and generates an estimated **Wastage Food Amount**.

If a numerical input is left blank, the application attempts to identify a similar record from the dataset and uses the corresponding value.

---

## 📊 Evaluation Metrics

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and predicted values.

```text
MAE = (1/n) Σ |yᵢ - ŷᵢ|
```

Lower MAE indicates smaller average prediction errors.

### Root Mean Squared Error (RMSE)

RMSE measures the square root of the average squared prediction error.

```text
RMSE = √[(1/n) Σ(yᵢ - ŷᵢ)²]
```

Lower RMSE indicates smaller prediction errors.

### R² Score

R² measures the proportion of variance in the target variable explained by the model.

```text
R² = 1 - (SSres / SStot)
```

A higher R² indicates that the model explains a larger proportion of the variation in the target variable.

---

## 🌍 Sustainable Development Goal

### SDG 12 – Responsible Consumption and Production

This project focuses on food wastage prediction and data-driven resource planning.

By estimating potential food wastage, Machine Learning can be explored as a tool for improving food planning and reducing unnecessary waste.

---

## 🔮 Future Improvements

* Add a larger and more diverse dataset
* Improve feature engineering
* Perform further XGBoost hyperparameter tuning
* Test additional Machine Learning algorithms
* Add interactive data visualizations
* Deploy the Flask application online
* Add prediction history
* Provide food wastage reduction recommendations
* Integrate real-time event and inventory data
* Develop a dashboard for organizations and event planners

---

## 👨‍💻 Author

### Harsh Deep Yadav

**B.Tech Artificial Intelligence & Machine Learning**

### 🔗 LinkedIn

[Harsh Deep Yadav](https://www.linkedin.com/in/harsh-deep-yadav-295ba2348/)

### 💻 GitHub

[HDY2005](https://github.com/HDY2005)

---

## 📌 Project Links

**GitHub Profile:**
[https://github.com/HDY2005](https://github.com/HDY2005)

**Machine Learning Projects Repository:**
[https://github.com/HDY2005/MachineLearning-Projects](https://github.com/HDY2005/MachineLearning-Projects)

**LinkedIn:**
[https://www.linkedin.com/in/harsh-deep-yadav-295ba2348/](https://www.linkedin.com/in/harsh-deep-yadav-295ba2348/)

---

## 🙏 Acknowledgements

This project was developed as part of an **IBM SkillsBuild / SDG-focused virtual internship**, with a focus on applying Machine Learning to a real-world sustainability problem.

---

## ⭐ Conclusion

The **Food Wastage Prediction System** demonstrates an end-to-end Machine Learning workflow, from data preprocessing and exploratory analysis to model training, hyperparameter tuning, model saving, and deployment through a Flask web application.

The project demonstrates how Machine Learning can be applied to a real-world sustainability problem involving food wastage and responsible resource consumption.