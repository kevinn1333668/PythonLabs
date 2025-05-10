import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Читаем данные из CSV файла
dates = []
passengers = []

with open('airpassengers.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # пропускаем заголовок
    for row in reader:
        dates.append(datetime.strptime(row[0], '%Y-%m'))
        passengers.append(int(row[1]))

# Конвертируем в NumPy массивы
dates = np.array(dates)
passengers = np.array(passengers)

# Рисуем линейный график пассажиропотока за все время
plt.figure(figsize=(12,5))
plt.plot(dates, passengers, marker='o', linestyle='-', color='blue')
plt.title('Пассажиропоток за всё время')
plt.xlabel('Год')
plt.ylabel('Количество пассажиров')
plt.grid(True)
plt.tight_layout()
plt.show()

# Гистограмма распределения пассажиров (1951-1955 гг. по месяцам)
start_date = datetime(1951,1,1)
end_date = datetime(1955,12,31)

filtered_dates = []
filtered_passengers = []

for date, pas in zip(dates, passengers):
    if start_date <= date <= end_date:
        filtered_dates.append(date.month)
        filtered_passengers.append(pas)

filtered_dates = np.array(filtered_dates)
filtered_passengers = np.array(filtered_passengers)

# Месяцы
months = np.arange(1,13)

# Суммируем пассажиров по месяцам
month_passengers = [filtered_passengers[filtered_dates==month].sum() for month in months]

# Строим гистограмму по месяцам
plt.figure(figsize=(9,4))
plt.bar(months, month_passengers, color='orange', edgecolor='black', alpha=0.7)
plt.xticks(months, ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.xlabel('Месяц')
plt.ylabel('Общее число пассажиров')
plt.title('Распределение пассажиров по месяцам (1951-1955 гг.)')
plt.grid(axis='y')
plt.tight_layout()
plt.show()