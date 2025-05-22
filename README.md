
# 🌱 Crop Recommendation System Using Machine Learning

Welcome to the **Crop Recommendation System**, an AI-driven solution that helps farmers make informed decisions about which crops to grow based on soil and environmental parameters. Built using Python and Streamlit, this system brings the power of data science to Indian agriculture.

---

## 🧠 Project Overview

This project aims to assist farmers and agronomists in selecting the most suitable crop based on real-time inputs like soil nutrients, temperature, pH, and rainfall. By using machine learning classification models, the system provides recommendations that optimize yield, minimize risks, and promote sustainable farming practices.

---

## 🎯 Objectives

- Recommend the best crop using soil (NPK, pH) and environmental data (temperature, humidity, rainfall)
- Help farmers make data-driven decisions and increase productivity
- Reduce resource wastage and promote sustainable farming
- Develop an easy-to-use dashboard to interact with the model in real time
- Provide a deployable solution using a lightweight Python-based web application

---

## 🛠️ Tools & Technologies Used

| Category              | Tools & Libraries                                       |
|-----------------------|----------------------------------------------------------|
| **Programming**       | Python                                                   |
| **IDE**               | Visual Studio Code                                       |
| **Web Deployment**    | Streamlit                                                |
| **Data Manipulation** | Pandas, NumPy                                            |
| **Modeling**          | Scikit-learn (Random Forest, KNN, SVM, Logistic Regression) |
| **Visualization**     | Matplotlib, Seaborn                                      |
| **Model Persistence** | Pickle                                                   |

---

## ❓ Problem Statement

Indian farmers face challenges in selecting the right crop due to:
- Variability in climate and soil conditions
- Lack of real-time agronomic insights
- Dependency on traditional knowledge

This system addresses these challenges by offering a machine learning-based tool that recommends crops suitable for a given set of environmental conditions.

---

## 📊 Dataset

- **Source**: [Kaggle](https://www.kaggle.com/datasets/shankarpriya2913/crop-and-soil-dataset)
- **Rows**: 2200
- **Features**: 
  - N (Nitrogen)
  - P (Phosphorus)
  - K (Potassium)
  - Temperature (°C)
  - Humidity (%)
  - pH (soil acidity/alkalinity)
  - Rainfall (mm)
  - Crop Label (Target)

---

## 📈 Model Evaluation

| Algorithm              | Accuracy (%) |
|------------------------|--------------|
| Random Forest          | 99.32        |
| Decision Tree          | 98.41        |
| K-Nearest Neighbors    | 97.05        |
| Support Vector Machine | 96.82        |
| Logistic Regression    | 91.81        |

✅ **Random Forest** was chosen as the final model due to its superior performance.

---

