# Iris Flower Classification – Final Machine Learning Project

A complete beginner-friendly Machine Learning project that predicts the species of an Iris flower from four measurements:

- Sepal length
- Sepal width
- Petal length
- Petal width

The project uses the built-in Iris dataset from Scikit-learn, so no dataset download is required.

## Project Workflow

1. Load the labelled Iris dataset.
2. Split data into 80% training records and 20% unseen testing records.
3. Train a Support Vector Machine (SVM) classification model.
4. Evaluate accuracy and classification metrics.
5. Save the trained model locally.
6. Predict the species of a new flower from user-provided measurements.

## Technologies Used

- Python
- Scikit-learn
- Joblib

## Installation

Open a terminal in this folder and run:

```bash
pip install -r requirements.txt
```

## Train and Evaluate

```bash
python iris_flower_classifier.py
```

This prints the test accuracy and a classification report, then saves a local model file named `iris_model.joblib`.

## Make a Prediction

Provide four measurements in centimetres:

```bash
python iris_flower_classifier.py --predict 5.1 3.5 1.4 0.2
```

Example output:

```text
=== Prediction Result ===
Measurements (cm): [5.1, 3.5, 1.4, 0.2]
Predicted species: Setosa
Confidence: 98.00%
```

## Learning Outcomes

- Understood the basic Machine Learning workflow.
- Trained and tested a classification model.
- Used accuracy and a classification report to evaluate prediction results.
- Built a reusable command-line project and documented it for GitHub.

## GitHub Submission Checklist

- [x] Project code included
- [x] Requirements file included
- [x] README with setup and run steps included
- [x] Model output excluded from Git with `.gitignore`
