## Busqueda de list
import time
## MODULE BISECT
import bisect
import random
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
start_time = time.time()
test_random = 9000000
""" for i in range(test_random):
    new_number = random.randint(0, test_random)
    bisect.insort(list_numbers, new_number) """
list_numbers = [random.randint(0, test_random) for i in range(test_random)]
list_numbers.sort()
end_time = time.time() - start_time
print("Inserción demora", end_time)
print("==BUSQUEDA INDEX()==")
start_time = time.time()
try:
    for i in range(200):
        indice = list_numbers.index(random.randint(0, test_random))
except:
    indice = -1
end_time = time.time() - start_time
print("Indice", indice)
print("Busqueda tomo con metodo index", end_time)
print("==BUSQUEDA INDEX()==")
start_time = time.time()
for i in range(200):
    indice = binary_search(random.randint(0, test_random), list_numbers)
end_time = time.time() - start_time
print("Indice", indice)
print("Busqueda con metodo binario", end_time)
