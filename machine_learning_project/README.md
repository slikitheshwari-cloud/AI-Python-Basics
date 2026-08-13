# Iris Flower Classification

This beginner Machine Learning project uses Scikit-learn's built-in Iris dataset to predict the species of an iris flower from four measurements.

## Machine Learning Workflow

1. **Load data**: uses 150 labelled Iris flower records.
2. **Prepare data**: separates flower measurements (features) from species names (labels).
3. **Split data**: uses 80% of records for training and 20% for testing.
4. **Train model**: creates a K-Nearest Neighbors classifier.
5. **Evaluate model**: reports accuracy and a classification report for unseen test data.
6. **Predict**: predicts the species of a new flower and shows confidence.

## Run the project

Install the required library once:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python iris_classifier.py
```

The Iris dataset is included with Scikit-learn, so no separate download is needed.
