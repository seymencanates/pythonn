import json
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier  
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


print("deneme")
# Load the JSON file
with open("data.json", "r+") as file:
    data = json.load(file)

# Extract data into lists
preparedData = {
    'name': [],
    'surname': [],
    'age': []
}

print("deneme2")
# Convert nested dictionary to lists

for key, person in data['people'].items():  # Iterate over dictionary key-value pairs
    preparedData['name'].append(person['name'])
    preparedData['surname'].append(person['surname'])
    preparedData['age'].append(int(person['age']))
  # Convert age to integer


print("deneme3")
# Convert to Pandas DataFrame
df = pd.DataFrame(preparedData) 



# Encode categorical data (names and surnames) to numerical values
le_name = LabelEncoder()
le_surname = LabelEncoder()

df['name_encoded'] = le_name.fit_transform(df['name'])

df['surname_encoded'] = le_surname.fit_transform(df['surname'])

print("deneme4")
# Define features (X) and labels (y)
X = df[['name_encoded','surname_encoded']]

y = df['age']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("deneme5")
# Train the Decision Tree model
model = DecisionTreeClassifier(criterion="gini", max_depth=90, random_state=42)
model.fit(X_train, y_train)
print("deneme6")
# Test the model with a new sample (Example: Predict the age of a new person)
new_person = pd.DataFrame({
    'name_encoded': [le_name.transform(['cem'])[0]],  # Encode 'iclal' using trained encoder
    'surname_encoded': [le_surname.transform(['baysal'])[0]]  # Encode 'akça' using trained encoder
})

print("deneme7")
predicted_age = model.predict(new_person)
print("Predicted Age: ", predicted_age[0])
print("deneme8")