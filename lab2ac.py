

class Clock(object):
    def __init__(self, hour, minutes=0):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

   
#     def __str__(self):
#     	if self.hour < 10:
# 			return "0%s:00" % (self.hour)
#     	elif self.hour < 24:
#     		return "%s:00" % (self.hour)
#     	else:
#     		return "Please re-enter time in appropriate minutes and hours."

    def __str__(self):
    	return "%02d:%02d" %(self.hour, self.minutes)
    	

    def __add__(self,minutes):
    	newminutes = self.minutes + minutes
    	newhour = int(newminutes/60)
    	updatedhour=self.hour+newhour
    	updatedminutes= (1+newhour)*60-newminutes
    	if int(updatedhour/24)<1:
    		return Clock(updatedhour, updatedminutes)
    	else int
    		
	 	

# The first test:
myclock=Clock.at(8)
myclock2=Clock.at(8,23)
print myclock
print myclock2
