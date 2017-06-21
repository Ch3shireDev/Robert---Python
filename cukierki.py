primes = []

N = 10000
tab = [True for i in range(N)]

for i in range(2,N-1):
	if tab[i]:
		primes.append(i)
		for j in range(2,N//i):
			tab[i*j] = False

def faktoryzuj(n):
	factors = []
	while n>1:
		for p in primes:
			print("Testuje", p, "na",n)
			if p>n:
				break
			if n%p == 0:
				factors.append(p)
				n = n//p
				break
	return factors

print("Zaczynamy faktoryzacje...")
print(faktoryzuj(84))