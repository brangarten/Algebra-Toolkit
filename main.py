import matplotlib.pyplot as plt
import ctypes as ct
import numpy as np
import os

toolkit = ct.CDLL("/home/bran/Dev/Algebra-Toolkit/lib/toolkit.so")

calculateDomainSize = toolkit.calculateDomainSize
calculateDomainSize.argtypes = [ct.c_int, ct.c_int]
calculateDomainSize.restype = ct.c_int

calculateQuad = toolkit.calculateQuad
calculateQuad.argtypes = [ct.c_int, ct.c_int, ct.c_int, ct.c_int, ct.c_int, ct.POINTER(ct.c_int)]
calculateQuad.restype = None

writeArray = toolkit.writeArray
writeArray.argtypes = [ct.c_int, ct.c_int, ct.POINTER(ct.c_int)]

minDomain : int = 0
maxDomain : int = 0


#Prompt for a domain interval
minDomain = int(input("Enter the least farthest domain (UNDEF, UNDEF)\n> "))
print(' ')

maxDomain = int(input("Enter the max farthest domain (" + str(minDomain) + ", UNDEF)\n> "))
print(' ')

domainSize = calculateDomainSize(minDomain, maxDomain)

print("Domain is (" + str(minDomain) + ',' + str(maxDomain) + ')' + "\nSize of Domain: " + str(domainSize))

# Create array & populate it
xArray = np.arange(minDomain, maxDomain, dtype=np.int32)

#int a, int b, int c, const int minDomain, const int maxDomain, int arr[]
yArray_c = (ct.c_int * domainSize)()
calculateQuad(1, -4, 4, minDomain, maxDomain, yArray_c)

yArray = np.ctypeslib.as_array(yArray_c)
print(xArray)
print(yArray)

plt.plot(xArray, yArray)

plt.show()