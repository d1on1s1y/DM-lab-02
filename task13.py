import numpy as np
list1 = ['халупа', 'сонце', 'кіт', 'молоко', 'річка']
list2 = ['молоко', 'яблуко', 'сонце', 'гора', 'дім', 'книга', 'кіт']
def notsame_elements(list1,list2):
    return np.setxor1d(list1, list2)
print (notsame_elements(list1,list2))