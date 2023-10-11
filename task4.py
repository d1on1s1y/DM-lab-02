arr1 = [1, 2, 10, 19, 34, 69]
arr2 = [3, 4, 15, 16, 25, 70]
def newarr(arr1, arr2):
    arr3 = sorted(arr1 + arr2)
    return arr3
print(newarr(arr1, arr2))

def joinarrays(arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()
joinarrays(arr1, arr2)
print (arr1)