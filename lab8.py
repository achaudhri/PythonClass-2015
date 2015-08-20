import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()

# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if keyword.search(line):
    print line 

# TODO: print all lines that DO NOT contain "the "

keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if not keyword.search(line):
    print line

# TODO: print lines that contain a word of any length starting with s and ending with e
#\b^s(.*)e\b
# ^s(.*)e$
#^s.+e$
# ^s.+e
#\bs(.*)\w+e
#keyword2 = re.compile(r'\bs(.*)\w+e\b ')

keyword3 = re.compile(r'\bs.*e\b')

for line in text:
  if keyword3.search(line):
    print line

mydata = raw_input('Please enter a date in the format MM.DD.YY:')
mydata 

# *Ask for a date as a raw input and spit back the month
pattern = re.compile(r'(\d*).(\d*).(\d*)')
mysearch=pattern.search(mydata)
mysearch.groups()
mysearch.group(1)

# date = raw_input("Please enter a date in the format MM.DD.YY: ")
# Print the date input in the following format:
# Month: MM
# Day: DD
# Year: YY

def FormatDate(input):
		pattern = re.compile(r'(\d*).(\d*).(\d*)')
		mysearch=pattern.search(input)
		month = mysearch.group(1)
		day = mysearch.group(2)
		year = mysearch.group(3)
		print'Month: %s \nDay: %s \nYear: %s' %(month,day,year)

  
# date = raw_input("Please enter a date in the format MM.DD.YY: ")
# Print the date input in the following format:
# Month: MM
# Day: DD
# Year: YY
