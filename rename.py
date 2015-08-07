# Function that takes integers as inputs and returns 1st, 2nd, 3rd

  
def Rename(entry):
    try:
     	if entry%1==0:
    		entry = str(entry)
    		if entry[-2:] == '11':
    			return "%sth" %(entry)
    		elif entry[-2:]== '12':
    			return "%sth" %(entry)
    		elif entry[-2:]== '13':
    			return "%sth" %(entry)
    		elif entry[-1] == '1':
    			return "%sst" %(entry)
    		elif entry[-1] == '2':
    			return "%snd" %(entry)
    		elif entry[-1] == '3':
    			return "%srd" %(entry)  
    		else:
    			return  "%sth" %(entry)	
    	else:
    		return "Please do not enter decimal places." 	
    except:
    	return "Please enter an integer."
    finally: 
    	print "This is a function."
    	
print Rename(12)
print Rename(3)
print Rename('r')
print Rename(3.2)
print Rename(111)
print Rename(114)
    
