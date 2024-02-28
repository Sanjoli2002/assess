import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the data
df=pd.read_csv("/home/knoldus/PycharmProjects/wine_model/src/data/winequality-red - winequality-red.csv")

# Split the data into features and target
wine_data = [line.split() for line in data.strip().split('\n')]
columns =df.columns
df = pd.DataFrame(wine_data, columns=columns)
X = df.drop('quality', axis=1).astype(float)
y = df['quality'].astype(int)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions
y_pred = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
