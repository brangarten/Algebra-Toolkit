import matplotlib.pyplot as plt
import ctypes as ct

toolkit = ct.CDLL("E:/Dev/Python/Algebra Toolkit/lib/toolkit.so")

domainElements = toolkit.domainElements
domainElements.argtypes = [ct.c_int, ct.c_int]
domainElements.restype = ct.c_int

calculateQuad = toolkit.calculateQuad
calculateQuad.argtypes = [ct.c_int, ct.c_int, ct.c_int, ct.c_int, ct.c_int]
calculateQuad.restype = ct.POINTER(ct.c_int)

#Prompt for a domain interval
minDomain = int(input("Enter min domain (UNDEF, UNDEF)\n> "))
print(' ')

maxDomain = int(input("Enter max domain (" + str(minDomain) + ", UNDEF)\n> "))
print(' ')

sizeDomain = domainElements(minDomain, maxDomain)

print("Domain is (" + str(minDomain) + ',' + str(maxDomain) + ')')
print(sizeDomain)

#(x-5)^2
#x^2 - 10x + 25
quadArr = (ct.c_int * sizeDomain)()
calculateQuad(1, -10, 25, minDomain, maxDomain)

for i in range(len(sizeDomain)):
    print(quadOutput)



plt.show()