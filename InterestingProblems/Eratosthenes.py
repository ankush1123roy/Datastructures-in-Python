
def Eratosthenes(ar):
	for i in range(len(ar)):
		No = ar[i].split();
		Primes = primes_sieve(int(No[0]),int(No[1]))
		print('\n')
                                
def primes_sieve(No1,limit):
    limitn = limit+1
    not_prime = set()
    primes = []
    for i in range(2, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        if i > No1:
			print i
    return primes

m = input()
ar = []
for i in range(m):
    ar.append(raw_input())
Eratosthenes(ar)
