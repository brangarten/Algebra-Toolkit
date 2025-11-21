import ctypes

clib = ctypes.CDLL("E:/Dev/Python/Algebra Toolkit/clib.so")

display = clib.display
display.argtypes = [ctypes.c_char_p, ctypes.c_int]
display.restype = ctypes.c_char_p

add = clib.add
add.argtypes = [ctypes.c_int, ctypes.c_int]
display.restype = ctypes.c_int



values = (ctypes.c_int * 5)(1, 2, 3, 4, 5)
sumAdd = clib.sumArr(values, len(values))

print(sumAdd)

for i in range(len(values)):
    print(values[i])

display(b"John", 18)