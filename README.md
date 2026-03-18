# Python-project-Pythone-
Задание: Построение линейной регрессии на Pythone
Ссылка: https://4nt0n1d4s.github.io/Python-project-Pythone-/

Вывод на терминале:
Исходные данные:
   Size District ComplexType  DistanceToCenter  Price
0    50        A      econom                10    150
1    60        B    business                 8    180
2    80        A      econom                12    210
3    90        C       elite                 5    230
4   100        B    business                 7    250

После кодирования:
   Size  DistanceToCenter  ...  ComplexType_econom  ComplexType_elite
0    50                10  ...                True              False
1    60                 8  ...               False              False
2    80                12  ...                True              False
3    90                 5  ...               False               True
4   100                 7  ...               False              False

[5 rows x 7 columns]

Intercept (β0): 5.078787878787864
Coefficients:
Size: 1.7488636363636363
DistanceToCenter: 7.742424242424246
District_B: -0.2454545454545388
District_C: 16.22954545454546
ComplexType_econom: -15.9840909090909
ComplexType_elite: 16.229545454545455

График:
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/d9260e33-c698-48d5-a752-cdd27a827370" />

