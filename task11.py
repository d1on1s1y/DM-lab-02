import numpy as np

matrix = np.random.randint(-100, 101, size=(5, 5))
print("Матриця ")
print(matrix)

min_in_rows = np.amin(matrix, axis=1)
print("Найменші елементи в кожному рядку: ",min_in_rows)
max_in_rows = np.amax(matrix, axis=1)
print("Найбільші елементи в кожному рядку: ",max_in_rows)

min_in_columns = np.amin(matrix, axis=0)
print("Найменші елементи в кожному стовпці: ", min_in_columns)
max_in_columns = np.amax(matrix, axis=0)
print("Найбільші елементи в кожному стовпці: ",max_in_columns)