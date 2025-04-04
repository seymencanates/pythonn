

import pandas as pd
import numpy as np
import scipy
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns

import matplotlib.pyplot as plt
#This library helps us for plotting. We can create charts , boxplots , graphs with this
#library

# Loads the dataset
df = pd.read_csv('diabetes.csv')
#read_csv function helps us to call any csv file into the program



df.isnull().sum()
#Checks if null value is exist or not


print(df.head())
#This method returns the first 5 rows of the DataFrame by default

df.describe()
#abtracts some basic informations

fig, axs = plt.subplots(9,1,dpi=200, figsize=(7,17))
#9 equals to the row parameter. So this mean this is gonna have 9 rows
#1 equals to the column parameter. So this mean this is gonna have 1 column

#dpi means resolution. It was set to the 95(research for the value range)
#(Dots Per Inch) is long typing of dpi. The higher dpi equals means a sharper image
#fourth parameter is means figure size. It was set to the 7 inches wide and 17 inches tall

# fig: The entire figure (the whole canvas containing all subplots).
#axs: A list (or NumPy array) of subplot axes where each axs[i] 
# corresponds to one of the 9 subplots.

i = 0
for col in df.columns:
    axs[i].boxplot(df[col], vert=False)
    #in here we are adding all columns into the boxplot with for loop
    #vert=False makes subplots horizontal instead of vertical. It makes more readable code
    axs[i].set_ylabel(col)
    i+=1
plt.show()


# Identify the quartiles
q1, q3 = np.percentile(df['Insulin'], [25, 75])

# syntax is np.percentile(data, percentile_value) , this method helps to seperate code into the percentiles



# Calculate the interquartile range

iqr = q3 - q1
# Calculate the lower and upper bounds
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
# Drop the outliers
clean_data = df[(df['Insulin'] >= lower_bound) 
                & (df['Insulin'] <= upper_bound)]

# Identify the quartiles
q1, q3 = np.percentile(clean_data['Pregnancies'], [25, 75])
# Calculate the interquartile range
iqr = q3 - q1
# Calculate the lower and upper bounds
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
# Drop the outliers
clean_data = clean_data[(clean_data['Pregnancies'] >= lower_bound) 
                        & (clean_data['Pregnancies'] <= upper_bound)]


# Identify the quartiles
q1, q3 = np.percentile(clean_data['Age'], [25, 75])
# Calculate the interquartile range
iqr = q3 - q1
# Calculate the lower and upper bounds
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
# Drop the outliers
clean_data = clean_data[(clean_data['Age'] >= lower_bound) 
                        & (clean_data['Age'] <= upper_bound)]


# Identify the quartiles
q1, q3 = np.percentile(clean_data['Glucose'], [25, 75])
# Calculate the interquartile range
iqr = q3 - q1
# Calculate the lower and upper bounds
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
# Drop the outliers
clean_data = clean_data[(clean_data['Glucose'] >= lower_bound) 
                        & (clean_data['Glucose'] <= upper_bound)]


# Identify the quartiles
q1, q3 = np.percentile(clean_data['BloodPressure'], [25, 75])
# Calculate the interquartile range
iqr = q3 - q1
# Calculate the lower and upper bounds
lower_bound = q1 - (0.75 * iqr)
upper_bound = q3 + (0.75 * iqr)
# Drop the outliers
clean_data = clean_data[(clean_data['BloodPressure'] >= lower_bound) 
                        & (clean_data['BloodPressure'] <= upper_bound)]


# Identify the quartiles
q1, q3 = np.percentile(clean_data['BMI'], [25, 75])
# Calculate the interquartile range
iqr = q3 - q1
# Calculate the lower and upper bounds
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
# Drop the outliers
clean_data = clean_data[(clean_data['BMI'] >= lower_bound) 
                        & (clean_data['BMI'] <= upper_bound)]


# Identify the quartiles
q1, q3 = np.percentile(clean_data['DiabetesPedigreeFunction'], [25, 75])
# Calculate the interquartile range
iqr = q3 - q1
# Calculate the lower and upper bounds
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

# Drop the outliers
clean_data = clean_data[(clean_data['DiabetesPedigreeFunction'] >= lower_bound) 
                        & (clean_data['DiabetesPedigreeFunction'] <= upper_bound)]

#correlation
corr = df.corr()

plt.figure(dpi=130)
sns.heatmap(df.corr(), annot=True, fmt= '.2f')
plt.show()

corr['Outcome'].sort_values(ascending = False)

plt.pie(df.Outcome.value_counts(), 
        labels= ['Diabetes', 'Not Diabetes'], 
        autopct='%.f', shadow=True)
plt.title('Outcome Proportionality')
plt.show()

# separate array into input and output components
X = df.drop(columns =['Outcome'])
Y = df.Outcome

#shows info
df.info()
