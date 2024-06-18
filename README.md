# WATER-POTABILITY-PREDICTION
This repository contains a machine learning web application for predicting the potability of water based on various water quality parameters. The model is built using a Random Forest classifier.

## Introduction
Water potability is crucial for ensuring safe drinking water. This application predicts whether water is potable or not based on parameters such as pH, hardness, solids, chloramines, sulfate, and more.

## Features
Predicts water potability using a trained Random Forest model.
User-friendly web interface for entering water quality parameters.
Provides a clear indication of whether the water is safe to drink.

## Model Details
**Algorithm:** Random Forest Classifier

**Training Data:** The model is trained on a dataset with various water quality parameters.

**Model File:** The trained model is saved as model.pkl.

## File Structure

water-potability-prediction/
│
├── model.py        # Script for training the Random Forest model
├── app.py          # Flask application script
├── model.pkl       # Pickle file containing the trained model
├── templates/
│   └── index.html  # HTML file for the web interface
├── static/
│   |___ img.png
├── requirements.txt# List of dependencies

