import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Создаем данные
# -----------------------------
data = pd.DataFrame({
    'Size': [50, 60, 80, 90, 100, 120, 150, 180, 200, 220],
    'District': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'ComplexType': ['econom', 'business', 'econom', 'elite', 'business', 'econom', 'elite', 'business', 'econom', 'elite'],
    'DistanceToCenter': [10, 8, 12, 5, 7, 11, 4, 6, 9, 3],
    'Price': [150, 180, 210, 230, 250, 300, 330, 350, 400, 450]
})

print("Исходные данные:")
print(data.head())

# -----------------------------
# 2. Кодирование категорий
# -----------------------------
data_encoded = pd.get_dummies(data, columns=['District', 'ComplexType'], drop_first=True)

print("\nПосле кодирования:")
print(data_encoded.head())

# -----------------------------
# 3. Разделяем признаки и цель
# -----------------------------
X = data_encoded.drop('Price', axis=1)
Y = data_encoded['Price']

# -----------------------------
# 4. Train/Test split
# -----------------------------
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# -----------------------------
# 5. Обучаем модель
# -----------------------------
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# 6. Параметры модели
# -----------------------------
print("\nIntercept (β0):", model.intercept_)
print("Coefficients:")

for name, coef in zip(X.columns, model.coef_):
    print(f"{name}: {coef}")

# -----------------------------
# 7. Оценка качества
# -----------------------------
from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error: {mse}")
print(f"R^2: {r2}")

# -----------------------------
# 8. Визуализация (упрощенная)
# -----------------------------
# Берем зависимость только Size vs Price

plt.scatter(data['Size'], data['Price'], color='blue', label='Реальные данные')

# фиксируем остальные параметры (средние значения)
X_line = pd.DataFrame({
    'Size': np.linspace(data['Size'].min(), data['Size'].max(), 100),
    'DistanceToCenter': [data['DistanceToCenter'].mean()] * 100
})

# добавляем фиктивные переменные (0)
for col in X.columns:
    if col not in X_line.columns:
        X_line[col] = 0

# правильный порядок колонок
X_line = X_line[X.columns]

y_line = model.predict(X_line)

plt.plot(X_line['Size'], y_line, color='red', label='Модель (при фиксированных параметрах)')

plt.title('Цена квартиры с учетом нескольких факторов')
plt.xlabel('Размер квартиры (кв.м)')
plt.ylabel('Цена')
plt.legend()
plt.grid(True)

plt.show()

# -----------------------------
# 9. Пример предсказания
# -----------------------------
# Новая квартира:
new_flat = pd.DataFrame({
    'Size': [85],
    'DistanceToCenter': [6],
    'District_B': [1],
    'District_C': [0],
    'ComplexType_business': [1],
    'ComplexType_elite': [0]
})

predicted_price = model.predict(new_flat)

print(f"\nПрогноз цены для новой квартиры: {predicted_price[0]}")