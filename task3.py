string = input("Введіть елементи массиву через пробіл ")
arr = [int(x) for x in string.split()]

print("Ви ввели массив ", arr)

def sorting(arr):
    return sorted(arr)
def sortingReverse(arr):
    return sorted(arr, reverse=True)
print("Введений массив впорядкований за зростанням ", sorting(arr)," і за спаданням", sortingReverse(arr))