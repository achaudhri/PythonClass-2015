# Go to https://petitions.whitehouse.gov/petitions
# Go to petition page for each of the petitions
# Create a .csv file with the following information for each petition:
# - Title (main page)
# - Published Date (subpage)
# - Issues (subpage)
# - Number of Signatures (main page)

from bs4 import BeautifulSoup
import urllib2 
import csv
import re	
import time

web_address='https://petitions.whitehouse.gov/petitions' # specifies the website
web_page = urllib2.urlopen(web_address) #opens the webpage
soup = BeautifulSoup(web_page.read(), "html.parser" ) #creates a soup for the entire page
soup.prettify()

def clean(object): #create function to clean html
	for link in object:
		return re.sub(r'<[^>]+>', '', str(link))


# First we go to the main url page to pull out webpages for each petition
petition_name_raw = soup.find_all('div',{'class':'title'}) # this contains the petition name and petition title from the original url.  
petition_name = [div.a for div in soup.find_all('div',{'class':'title'})] #this next step removes the "div class title" tag from each entry in the above list

# With petition_name, we can now reference each petition webpage url by referencing the tag 'href' 
firstpetition=petition_name[0]['href']
allwebpages=[]
for i in range (0, len(petition_name)): # this loop allows us to create a list of all the webpages
	allwebpages.append(petition_name[i]['href'])	
type(allwebpages) # it is a list

# We can go into a particular petition webpage to determine how to pull out all four values
web_address2='https://petitions.whitehouse.gov/petition/encourage-federal-government-adopt-open-source-technologies-wherever-possible' # specifies the website
web_page2 = urllib2.urlopen(web_address2) #opens the webpage
soup2 = BeautifulSoup(web_page2.read(), "html.parser" )
petition_title2 = soup2.find_all('h1',{'class':'title'}) # here is the title of the petition
petition_date2 = soup2.find_all('div',{'class':'date'}) # here is the publication date
# a = string(petition_date)
petition_date2 = re.sub(r'<div class="date"><strong>Published Date:</strong> ', '', str(petition_date2)) #this step removes the "Published Date:" portion of the string
petition_date2 = re.sub(r'</div>', '', str(petition_date2)) #this step removes the "Published Date:" portion of the string
petition_issues2 = soup2.find_all('div',{'class':'issues'}) # here are the issues
petition_issues2 = re.sub(r'Issues:', '', str(petition_issues2)) #this step removes the "Issues:" portion of the string
petition_signatures2 = soup2.find_all('div',{'class':'num-block num-block2'}) #here is the number of signatures

# This function extracts the Title, Publication Date, Issues, Signatures from each petition webpage
def petitioninfo_frompage(object): 
	web_page = urllib2.urlopen(object) #updates webpage for each petition
	soup = BeautifulSoup(web_page.read(), "html.parser") #redefines the soup for each petition
	petition_title = soup.find_all('h1',{'class':'title'}) #title of the petition
	petition_date = soup.find_all('div',{'class':'date'}) #publication date 
	petition_date = re.sub(r'<div class="date"><strong>Published Date:</strong> ', '', str(petition_date))
	petition_date = re.sub(r'</div>', '', str(petition_date))
	petition_issues = soup.find_all('div',{'class':'issues'}) #the issues
	petition_signatures = soup.find_all('div',{'class':'num-block num-block2'}) #number of signatures
	return {"Title":clean(petition_title), "Date":petition_date, "Issues":clean(petition_issues), "Signatures":clean(petition_signatures)} #Here we return a dictionary with the information

# with open, opens (and subsequently closes) a csv file to transfer the dictionary contents into.
with open('PetitionInfo.csv', 'wb') as f: 
	my_writer = csv.DictWriter(f, fieldnames=("Title", "Date", "Issues", "Signatures")) #places these headings into the csv file that match the dictionary
	my_writer.writeheader() 
	for item in petition_name: #this loops through each petition
		my_writer.writerow(petitioninfo_frompage(item['href'])) #href tag is used to extract the webpage for each petition


