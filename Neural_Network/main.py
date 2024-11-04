import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Wczytanie danych z pliku Excel
data = pd.read_excel("numbers.xlsx")

# Przygotowanie danych wejściowych (liczb) i etykiet (nazw)
numbers = data["number"].values
names = data["name"].values

# Normalizacja danych wejściowych
max_value = max(numbers)  # Przyjmujemy, że największa liczba to max_value
numbers = numbers / max_value

# Konwersja nazw na indeksy
unique_names = sorted(set(names))  # Znajdujemy unikalne nazwy
label_dict = {name: idx for idx, name in enumerate(unique_names)}
reverse_label_dict = {idx: name for name, idx in label_dict.items()}
labels = np.array([label_dict[name] for name in names])

# One-hot encoding etykiet
labels = to_categorical(labels, num_classes=len(unique_names))

# Budowa sieci neuronowej
model = Sequential([
    Dense(32, input_shape=(1,), activation='relu'),
    Dense(64, activation='relu'),
    Dense(len(unique_names), activation='softmax')  # Liczba neuronów równa liczbie unikalnych nazw
])

# Kompilacja modelu
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Trenowanie modelu
model.fit(numbers, labels, epochs=100, verbose=0)

# Ocena modelu na danych treningowych
loss, accuracy = model.evaluate(numbers, labels, verbose=0)
print(f'Dokładność modelu na danych treningowych: {accuracy:.2f}')

# Funkcja pomocnicza do przewidywania nazwy liczby
def predict_number_name(number):
    normalized_number = number / max_value  # Normalizacja liczby
    prediction = model.predict(np.array([normalized_number]))
    predicted_class = np.argmax(prediction)
    return reverse_label_dict[predicted_class]

# Pętla do wprowadzania liczby przez użytkownika
print("Wprowadź liczbę, aby uzyskać jej nazwę (lub wpisz 'exit' aby zakończyć):")
while True:
    user_input = input("Podaj liczbę: ")
    if user_input.lower() == 'exit':
        break
    try:
        number = int(user_input)
        if number > max_value:
            print(f"Proszę wprowadzić liczbę w zakresie 1 do {max_value}.")
            continue
        print(f"{number} -> {predict_number_name(number)}")
    except ValueError:
        print("Proszę wprowadzić prawidłową liczbę lub 'exit' aby zakończyć.")
