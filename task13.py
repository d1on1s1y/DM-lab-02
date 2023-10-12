import numpy as np
list1 = ['халупа', 'сонце', 'кіт', 'молоко', 'річка']
list2 = ['молоко', 'яблуко', 'сонце', 'гора', 'дім', 'книга', 'кіт']
def same_elements(list1,list2):
    return np.intersect1d(list1, list2)
print (same_elements(list1,list2))