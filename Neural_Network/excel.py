import pandas as pd
from num2words import num2words

# Ustal zakres liczb
max_number = 100

# Przygotowanie danych - liczby i ich angielskie nazwy
numbers = list(range(1, max_number + 1))
names = [num2words(number, lang='pl') for number in numbers]  # lub 'pl' dla polskiego języka

# Tworzenie DataFrame o dwóch kolumnach (bez dużej macierzy!)
data = pd.DataFrame({
    "number": numbers,
    "name": names
})

# Zapis do pliku Excel
data.to_excel("numbers.xlsx", index=False)
print("Plik numbers.xlsx został wygenerowany.")
