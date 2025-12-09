import numpy as np          # NumPy — робота з масивами та математичними операціями
import pandas as pd         # Pandas — робота з таблицями, DataFrame
import requests             # Requests — відправка HTTP-запитів (GET, POST)
import matplotlib.pyplot as plt  # Matplotlib — побудова графіків
from math import sqrt       # Math — стандартна математика (квадратний корінь)
import random               # Random — генерація випадкових чисел
import datetime             # Datetime — робота з датами та часом
import os                   # OS — робота з файлами та директоріями
import sys                  # Sys — доступ до системних параметрів Python
import json                 # JSON — робота з JSON-форматом

# 1 Використання numpy
try:
    arr = np.array([1, 2, 3])
    print("NumPy array:", arr * 2)
except Exception as e:
    print("NumPy error:", e)

# 2 Використання pandas
try:
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    print("\nPandas DataFrame:")
    print(df)
except Exception as e:
    print("Pandas error:", e)

# 3 Використання requests
try:
    r = requests.get("https://httpbin.org/get")
    print("\nRequests status code:", r.status_code)
except Exception as e:
    print("Requests error:", e)

# 4 Використання matplotlib
try:
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Test Plot")
    plt.savefig("plot.png")   # графік збережеться у файл
    print("\nMatplotlib: plot saved as plot.png")
except Exception as e:
    print("Matplotlib error:", e)

# 5 Використання json
try:
    data = {"name": "Test", "value": 123}
    json_text = json.dumps(data)
    print("\nJSON:", json_text)
except Exception as e:
    print("JSON error:", e)