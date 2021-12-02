import math

def finab(num):

    f = int(math.sqrt(num))
    return (f * f == num)

def cek(array, f):

    count = 0
    for i in range(f):
    
        if (finab(5 * array[i] * array[i] + 4) or
            finab(5 * array[i] * array[i] - 4)):
        
            print(array[i], " ", end ="");
            count = count + 1
        
    
    if (count == 0):
        print("bukan finabochi");

array = [1, 2, 4, 5, 6, 7, 55, 89, 23]
f = len(array)

cek(array, f)