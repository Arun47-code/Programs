import math
def primeFactors(n):
		
	while n % 2 == 0:
		print( "2")
		n = n / 2
		
	for i in range(3,int(math.sqrt(n))+1,2):
		while n % i== 0:
			print(i)
			n = n / i
	if n > 2:
		print(n)
n = 315
primeFactors(n)
def productPrimeFactors(n):
    product = 1   
    for i in range(2, n+1):
        if (n % i == 0):
            isPrime = 1
              
            for j in range(2, int(i/2 + 1)):
                if (i % j == 0):
                    isPrime = 0
                    break
            if (isPrime):
                product = product * i                 
    return product       
print (productPrimeFactors(n))
  

