import math

# numerator     =   n!
# denominator   =  k!(n-k)!

#Numerator
nInput = int(input('How many individuals are in the population? '))
nFinal = math.factorial(nInput)

#Denominator
dInput = int(input('How many are you choosing for your sample?'))
nMinusk = nInput - dInput
dFacto = (math.factorial(dInput))
nMinuskfacto = (math.factorial(nMinusk))
dFinal = dFacto * nMinuskfacto
#print(nInput-dInput)

#final output
numOfCombinations = nFinal / dFinal
print(numOfCombinations)

