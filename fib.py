
def fibonacci(m):
    m = int(m)
    def fibonaccii(a,b,m,result):
        c = a+b
        result.append(c)
        if c < m:
            fibonaccii(b,c,m,result)
        return result
    return fibonaccii(0,1,m,[])

def prime(n): 
    if n <= 0: 
        return "what?" 
    elif n == 1: 
        return "it is 1" 
    for i in range(2, n): 
        if n%i == 0: 
            return "not a prime" 
    return "prime" 
 
 
def list_prime(list): 
	prime_list =[ ] 
	for i in list: 
		x = prime(i) 
		if x == "prime": 
			prime_list.append(i) 
	return prime_list 

# command that find prime numbers is Fibonacci sequence from 0 to m	 
print(list_prime(fibonacci(m))) 