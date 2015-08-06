# We are creating a class called Clock1.  
class Clock1(object):  
    def __init__(self, hour, minutes=0):  # 'Self' must be the generic first argument used.
    									  # If we designate minutes = 0, we do not have to
    									  # provide a value for this variable.	
    									  
        self.minutes = minutes  # The object or instance variable 'minutes' is an 
        						# attribute for the class Clock. It is important to note
        						# that we need to add the module name ('self') before the
        						# global name 'minutes'
        self.hour = hour
		# This first function uses "class instantiation" to create a generic instance of 
		# the class that will be populated later when creating a particular instance.  


    def __str__(self):	# Here is an example of a function that we can create within the
    					# Clock class.  It returns the time in two digits for the hour and
    					# minutes. 
    	print "%02d:%02d" %(self.hour, self.minutes) # Note that %02d tells Python to 
    						     # return two digits for any number
    						     # entered. 


# If stop here, we have to call the method from a particular instance only. 

myclock = Clock1(2,45)
myclock.__str__()

#
#
#

# Again, we can create a class called Clock.  This time we will use the @classmethod
# so that we can call the method from either the instance or a class. 

class Clock(object):
    def __init__(self, hour, minutes=0):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)
 
 # Now we do not have to use the function names to call a method. 


    def __str__(self):
    	return "%02d:%02d" %(self.hour, self.minutes)
 
 # Here we create a new function that adds additional minutes to the existing instances
 # we created before.  
 
    def __add__(self,minutes):
    	newminutes = self.minutes + minutes # First we take the additional minutes and add
    					    # them to the previous minutes
    										
    	updatedminutes = (newminutes)%60	# If the updated minutes exceed 60, we take the 
    						# remainder when dividing by 60. 
    										
    	updatedhour = (self.hour + newminutes/60)%24  # For the updated hour we take the
    						      # new minutes and divide by 60 which
    						      # gives us an integer variable for 
    						      # every hour the new minutes exceed
    						      # We can then add these hours to the 
    						      # existing hour.  However, if the 
    						      # total hours exceed 24, we take the 
    						      # remainder of the new hours after 
    						      # dividing by 24. 
    	return Clock(updatedhour, updatedminutes)
    	
    def __sub__(self,minutes):
    	newminutes = (self.hour*60+self.minutes) - minutes # First we convert the time to 
    							   # minutes and subtract the new
    							   # minutes.  
    	updatedminutes = (newminutes)%60
    	updatedhour = (newminutes/60)%24
    	return Clock(updatedhour, updatedminutes)

    def __eq__(self, other):
    	return (self.minutes == other. minutes) and (self.hour == other.hour) 
    
    def __ne__(self, other):
    	return (self.minutes != other. minutes) or (self.hour != other.hour) 
 

# The first test:
myclock=Clock.at(8)
myclock2=Clock.at(8,23)
print myclock
print myclock2

# The second test:
print myclock+24
print myclock2+10000

# The third test:
print myclock-10
print myclock2-105

# The fourth test:
myclock3=Clock.at(8,23)
myclock4=Clock.at(4,12)
print myclock2==myclock3
print myclock2==myclock4

# The fifth test:
myclock3=Clock.at(8,23)
myclock4=Clock.at(4,12)
print myclock2!=myclock3
print myclock2!=myclock4
