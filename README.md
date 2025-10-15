---
title: VO2Max Predictor
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: Streamlit app that estimates VO2 max from runner metrics
license: cc
---

VO₂ Max Predictor and Coaching App
This project develops a machine learning model to predict VO₂ max and provides personalized coaching tips based on the predicted VO₂ max and other health metrics.

Project Overview
This is a lightweight AI application that predicts an individual's VO₂ max using physiological, lifestyle, and training data, and provides actionable coaching tips to improve cardiovascular fitness and overall well-being.

This project demonstrates a preventive digital health use case—offering an interpretable fitness signal (VO₂ max) coupled with personalized, easy-to-understand insights. Built entirely on CPU, it requires no GPU resources, uses synthetic or de-identified data (no PHI), and emphasizes explainable features for transparency and educational value.

Dataset
The project utilizes a synthetic dataset (vo2_real_augmented.csv) containing various features like age, sex, height, weight, lean mass, BMI, training hours, sleep metrics, heart rate data, and the target variable, VO₂ max.

Model
A RandomForestRegressor model is used for predicting VO₂ max. The data is preprocessed using StandardScaler to scale the numerical features. A pipeline is used to combine the preprocessing and the model training steps.

Coaching Tips
Based on the predicted VO₂ max and other user inputs (sleep quality, training hours, heart rate recovery), the application provides personalized coaching tips. These tips are designed to guide users towards improving their fitness and recovery.

Project Structure
vo2_real_augmented.csv: The dataset used for training and evaluation.
model/vo2_predictor.joblib: The saved machine learning pipeline.
app/app.py: (Assuming this is your Streamlit app file based on the requirements.txt) The Streamlit application code.
This notebook: Contains the code for data loading, cleaning, model training, evaluation, saving, and a function for generating coaching tips.

Setup and Usage
Clone the repository:
  cd <project_directory>
  pip install -r requirements.txt
  python -c "import joblib, pandas"
  streamlit run app/app.py

