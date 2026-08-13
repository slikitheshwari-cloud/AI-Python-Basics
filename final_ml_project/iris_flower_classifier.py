"""Train an Iris classifier, evaluate it, and predict a flower species."""

import argparse
from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


MODEL_FILE = Path(__file__).parent / "iris_model.joblib"


def train_model():
    """Load data, train a classifier, print evaluation results, and save it."""
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
    )

    model = make_pipeline(StandardScaler(), SVC(kernel="linear", probability=True, random_state=42))
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)
    print("=== Iris Flower Classifier ===")
    print(f"Training records: {len(x_train)}")
    print(f"Testing records: {len(x_test)}")
    print(f"Test accuracy: {accuracy_score(y_test, predictions):.2%}\n")
    print(classification_report(y_test, predictions, target_names=iris.target_names))

    joblib.dump(model, MODEL_FILE)
    print(f"Saved trained model: {MODEL_FILE.name}")
    return model, iris.target_names


def predict_flower(measurements):
    """Predict a species from four measurements in centimetres."""
    iris = load_iris()
    model = joblib.load(MODEL_FILE) if MODEL_FILE.exists() else train_model()[0]
    predicted_class = model.predict([measurements])[0]
    confidence = model.predict_proba([measurements])[0][predicted_class]
    return iris.target_names[predicted_class], confidence


def main():
    parser = argparse.ArgumentParser(description="Iris flower classification project")
    parser.add_argument("--predict", nargs=4, type=float, metavar=("SEPAL_LENGTH", "SEPAL_WIDTH", "PETAL_LENGTH", "PETAL_WIDTH"))
    arguments = parser.parse_args()

    if arguments.predict:
        species, confidence = predict_flower(arguments.predict)
        print("=== Prediction Result ===")
        print(f"Measurements (cm): {arguments.predict}")
        print(f"Predicted species: {species.title()}")
        print(f"Confidence: {confidence:.2%}")
    else:
        train_model()


if __name__ == "__main__":
    main()
