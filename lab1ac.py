# def binarify(number): 
#   """convert positive integer to base 2"""
#   if num<=0: return '0'
#   digits = []
#   return ''.join(digits)
#   

def binarify(number):
 
 	
	powers=[] # first we create an empty list that we populate with elements of 2^x
	
	for i in range(0,20):
		powers.append(2**i) # this for loop adds each 2^x to the list "powers"
		
	for i in range(0,len(powers)-1):  # we go to -1 the length since python starts at 0
		if number > powers[i] and number < powers[i+1]:  # Here we find what power of two the number falls between
			myindex=i
			
	digits=[]  # Here we are creating a list that we will use to get our final number
	
	for i in range(0,myindex+1)[::-1]:  #[::-1] reverses the list so that we start at the x power and go down to 0.
		digit=str(number/(2**i))
		remainder=number %(2**i)
		number=remainder
		digits.append(digit) #append only works for strings
	return ''.join(digits)

print binarify(156)
print binarify(59)
print binarify(17)

 
# def int_to_base(num, base):
#   """convert positive integer to a string in any base"""
#   if num<=0:  return '0' 
#   digits = []
#   return ''.join(digits)

def int_to_base(number, base):
 
 	
	powers=[] # first we create an empty list that we populate with elements of 2^x
	
	for i in range(0,20):
		powers.append(base**i) # this for loop adds each 2^x to the list "powers"
		
	for i in range(0,len(powers)-1):  # we go to -1 the length since python starts at 0
		if number > powers[i] and number < powers[i+1]:  # Here we find what power of two the number falls between
			myindex=i
			
	digits=[]  # Here we are creating a list that we will use to get our final number
	
	for i in range(0,myindex+1)[::-1]:  #[::-1] reverses the list so that we start at the x power and go down to 0.
		digit=str(number/(base**i))
		remainder=number %(base**i)
		number=remainder
		digits.append(digit) #append only works for strings
	return ''.join(digits)

print int_to_base(159, 2)
print int_to_base(312, 10)

# def base_to_int(string, base):
#   """take a string-formatted number and its base and return the base-10 integer"""
#   if string=="0" or base <= 0 : return 0 
#   result = 0 
#   return result 

def base_to_int(string, base):
	length = len(string)
	result=0
	for i in string:
		result+=int(i)*base**(length-1)
		
		length-=1
	return result
	
print base_to_int("1001", 2)


 
# def flexibase_add(str1, str2, base1, base2):
#   """add two numbers of different bases and return the sum"""
#   result = int_to_base(tmp, base1)
#   return result 

def flexibase_add(str1, str2, base1, base2):
	length1 = len(str1)
	result1=0
	for i in str1:
		result1+=int(i)*base1**(length1-1)
		length1-=1
		
	length2 = len(str2)
	result2=0
	for i in str2:
		result2+=int(i)*base2**(length2-1)
		length2-=1
		
		
	return result1 + result2
	
print flexibase_add("1001", "55", 2, 10)


def flexibase_add(str1, str2, base1, base2):
	return base_to_int(str1, base1) + base_to_int(str2, base2)

print flexibase_add("1001", "55", 2, 10)

# def flexibase_multiply(str1, str2, base1, base2):
#   """multiply two numbers of different bases and return the product"""
#   result = int_to_base(tmp, base1)
#   return result 


def flexibase_multiply(str1, str2, base1, base2):
	length1 = len(str1)
	result1=0
	for i in str1:
		result1+=int(i)*base1**(length1-1)
		length1-=1
		
	length2 = len(str2)
	result2=0
	for i in str2:
		result2+=int(i)*base2**(length2-1)
		length2-=1
		
		
	return result1 * result2
	
print flexibase_multiply("1001", "55", 2, 10)


def flexibase_multiply(str1, str2, base1, base2):
	return base_to_int(str1, base1) * base_to_int(str2, base2)
	
print flexibase_multiply("1001", "55", 2, 10)





# def romanify(num):
#   """given an integer, return the Roman numeral version"""
#   result = ""
#   return result
#   
#   

if number < 4:
	print 'I' * number


