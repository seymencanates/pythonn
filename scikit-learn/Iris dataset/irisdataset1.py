from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier  
from sklearn.metrics import accuracy_score 
import numpy as np


# datasets: Scikit-learn içinde bulunan hazır veri setlerini yüklemek için.
# train_test_split: Veriyi eğitim (%80) ve test (%20) olarak bölmek için.
# DecisionTreeClassifier: Karar ağacı algoritmasını kullanarak bir model oluşturmak için.
# accuracy_score: Modelin doğruluk oranını hesaplamak için.



iris = datasets.load_iris()  
X = iris.data  # Öznitelikler  
y = iris.target  # Etiketler  
# Bu kodda:

# datasets.load_iris(): Çiçek türlerini içeren hazır veri setini yüklüyoruz.
# iris.data: Çiçeklerin uzunluğu, genişliği gibi özellikleri içerir.
# iris.target: Çiçek türünü belirten etiketlerdir (0, 1, 2).
# İris veri seti aşağıdaki gibi görünür:

# Uzunluk (cm)	Genişlik (cm)	Uzunluk (cm)	Genişlik (cm)	Tür (y)
# 5.1	3.5	1.4	0.2	0 (Setosa)
# 4.9	3.0	1.4	0.2	0 (Setosa)
# 6.2	3.4	5.4	2.3	2 (Virginica)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)  

# Bu kod veriyi ikiye böler:

# %80 eğitim verisi (X_train, y_train)
# %20 test verisi (X_test, y_test)
# 🔹 test_size=0.2: Test verisinin oranı (%20).
# 🔹 random_state=42: Her çalıştırmada aynı sonucu almak için rastgelelik kontrolü.



model = DecisionTreeClassifier()  # Karar ağacı modeli  
model.fit(X_train, y_train)  # Modeli eğit  

# DecisionTreeClassifier(): Karar ağacı modeli oluşturur.
# fit(X_train, y_train): Modeli eğitmek için eğitim verisini kullanır.
# Karar ağaçları, veriyi dallara ayırarak tahmin yapar:
# 📌 Örnek:
# "Yaprak uzunluğu > 2.5 cm mi?"
# ➡ Evet → "Virginica olabilir"
# ➡ Hayır → "Setosa olabilir"

y_pred = model.predict(X_test) 
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: {accuracy:.2f}")

guess = np.array([[5.1, 3.5, 1.4, 0.2]])  # Tek bir veri noktası için tahmin
prediction = model.predict(guess)
print(f"Tahmin edilen sınıf: {prediction[0]}") 


# predict(X_test): Model, test verisi için tahmin yapar.
# accuracy_score(y_test, y_pred): Modelin test verisindeki doğruluğunu ölçer.
# accuracy:.2f: Sonucu iki basamaklı göstermek için.
# 📌 Eğer çıktı 0.95 ise model %95 doğrulukla tahmin yapıyor demektir.