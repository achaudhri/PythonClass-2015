# GitHub Lab Exercise 6

#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

#Exercise 2
#Write a function that returns prime numbers less than 121

# Leave the function empty and return all the prime numbers less than 121


#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html


#Exercise 1: Greatest Common Divisor Functions


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
        # What this function does is that it goes through 2 simultaneous equations:
        # a = b and
        # b = a%b
        
        # When the remainder is equal to 0, it will return the smaller of the two numbers
        # If the remainder is not 0 bc the larger number comes second, it will re-arrange the
        # two numbers in order and then return the smaller number once the remainder comes to 0.
        
    return a
 
print gcd(10, 2)   

# This function uses recursion to get the prime numbers. 
 
def gcd(a, b):
if a > b:
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)
if a < b:
    r = b % a
    if r == 0:
        return a
    else:
        return gcd(a, r)

print gcd(3, 2)

#Exercise 2: Prime Number Less than 121

pp = 2
ps = [pp]
lim = 121
while pp < lim:  # While 2< 121
   pp += 1 # then pp=3
   for a in ps: # Right now 2 is the only element in ps
      if pp%a==0: # if 3 remainder 2 is 0, then break the for-loop and return to while
         break
   else: # Here 3 remainder 2 was not equal to 0, so we are adding it to the prime list.
      if pp not in ps:
         ps.append(pp)
print ps


first_prime=2
prime_list=[first_prime]
last_number=121

prime_list=	

def prime(first_prime=2, prime_list=[first_prime], last_number=121):
	first_prime +=1
	if first_prime < last_number:
		for i in prime_list:
			if first_prime%i==0:
				break
		else: 
				prime_list.append(first_prime)
	return prime(first_prime, last_number)
				
				
prime_list=[]	

def prime(first_prime=2, prime_list=[first_prime], last_number=121):
	first_prime = 2
	first_prime +=1
	if first_prime < last_number:
		for i in prime_list:
			if first_prime%i==0:
				break
		else: 
				prime_list.append(first_prime)
	return prime(first_prime, last_number)

###########
def prime():
	first_prime = 2
	last_number = 121
	prime_list=[first_prime]
	first_prime +=1
	if first_prime < last_number:
		for i in prime_list:
			if first_prime%i!=0:
				prime_list.append(first_prime)
			else: 
				return prime()
	else: 
		return prime_list


##########

pp = 2
ps = [pp]
lim = 121
if pp < lim:
	pnew = 1 + pp
	while pnew < lim:  # While 3< 121
   	for a in ps: # Right now 2 is the only element in ps
      	if pnew % a == 0: # if 3 remainder 2 is 0, then break the for-loop and return to while
         	break
   	else: # Here 3 remainder 2 was not equal to 0, so we are adding it to the prime list.
      	if pp not in ps:
         ps.append(pp)
print ps



def prime(lim=121,pp=2,primes=[],first=True):
	if first: primes=[]
	if pp==lim: return primes 
	ps=range(2,pp)
	for a in ps: # Right now 2 is the only element in ps
		if pp%a==0: # if 3 remainder 2 is 0, then break the for-loop and return to while
			return prime(lim,pp+1,primes,False)
	primes.append(pp)
	return prime(lim,pp+1,primes,False)
	
print prime()
