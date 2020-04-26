## Busqueda de list
import time
## Metodo indice
list_numbers = [12,13,14,15,16,17,18,19,20,22,24,26,27,843]

def binary_search(needle, haystack):
    imin, imax = 0, len(haystack)
    while True:
        if imin >= imax:
            return -1
        midpoint = (imin + imax) // 2
        if haystack[midpoint] > needle:
            imax = midpoint
        elif haystack[midpoint] < needle:
            imin = midpoint + 1
        else:
            return midpoint

#index = binary_search(13, list_numbers)

## MODULE BISECT
import bisect
import random
## Encontrar valores cercanos en una lista
def find_closest(haystack, needle):
    # Localiza el punto de insercion, para que se mantenga ordenado la lista
    i = bisect.bisect_left(haystack, needle)
    if i == len(haystack):
        return i - 1
    elif haystack[i] == needle:
        return i
    elif i > 0:
        j = i - 1
        if haystack[i] - needle > needle - haystack[j]:
            return j
    return i

for i in range(10):
    new_number = random.randint(0, 1000)
    bisect.insort(list_numbers, new_number)

print(list_numbers)
