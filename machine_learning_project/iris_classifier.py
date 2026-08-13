"""Train, test, and use a beginner-friendly Iris flower classifier."""

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main():
    # 1. Load the dataset.
    iris = load_iris()
    features = iris.data
    labels = iris.target

    # 2. Split the data: 80% for training and 20% for testing.
    x_train, x_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, random_state=42, stratify=labels
    )

    # 3. Train a K-Nearest Neighbors classification model.
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train, y_train)

    # 4. Test the trained model with unseen data.
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    print("=== Iris Flower Classification ===")
    print(f"Dataset records: {len(features)}")
    print(f"Training records: {len(x_train)}")
    print(f"Testing records: {len(x_test)}")
    print(f"Model accuracy: {accuracy:.2%}")
    print("\nClassification report:")
    print(classification_report(y_test, predictions, target_names=iris.target_names))

    # 5. Predict the type of a new flower.
    sample_flower = [[5.1, 3.5, 1.4, 0.2]]
    predicted_class = model.predict(sample_flower)[0]
    probabilities = model.predict_proba(sample_flower)[0]

    print("New flower measurements (cm):")
    print("Sepal length: 5.1, Sepal width: 3.5, Petal length: 1.4, Petal width: 0.2")
    print(f"Predicted flower: {iris.target_names[predicted_class].title()}")
    print(f"Prediction confidence: {probabilities[predicted_class]:.2%}")


if __name__ == "__main__":
    main()
