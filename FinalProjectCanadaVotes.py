# Ambreen Chaudhri
# Obtaining Roll Call Votes for Canadian Parliament

from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os
import csv
import re


# Parliamentary Session WebSites

Parl38Ses1 ='http://www.parl.gc.ca/HouseChamberBusiness/ChamberVoteList.aspx?Language=E&Mode=1&Parl=38&Ses=1' #190
Parl39Ses1 ='http://www.parl.gc.ca/HouseChamberBusiness/ChamberVoteList.aspx?Language=E&Mode=1&Parl=39&Ses=1' #219
Parl39Ses2 ='http://www.parl.gc.ca/HouseChamberBusiness/ChamberVoteList.aspx?Language=E&Mode=1&Parl=39&Ses=2' #161
Parl40Ses1 ='http://www.parl.gc.ca/HouseChamberBusiness/ChamberVoteList.aspx?Language=E&Mode=1&Parl=40&Ses=1' #1
Parl40Ses2 ='http://www.parl.gc.ca/HouseChamberBusiness/ChamberVoteList.aspx?Language=E&Mode=1&Parl=40&Ses=2' #158
Parl40Ses3 ='http://www.parl.gc.ca/HouseChamberBusiness/ChamberVoteList.aspx?Language=E&Mode=1&Parl=40&Ses=3' #204
Parl41Ses1 ='http://www.parl.gc.ca/HouseChamberBusiness/ChamberVoteList.aspx?Language=E&Mode=1&Parl=41&Ses=1' #760
Parl41Ses2 ='http://www.parl.gc.ca/HouseChamberBusiness/ChamberVoteList.aspx?Language=E&Mode=1&Parl=41&Ses=2' #467

# File Paths to Save data

pathParl38Ses1 = '/Users/ambreenchaudhri/Desktop/Canada/Parl38Ses1/' #done x
pathParl39Ses1 = '/Users/ambreenchaudhri/Desktop/Canada/Parl39Ses1/' #done x
pathParl39Ses2 = '/Users/ambreenchaudhri/Desktop/Canada/Parl39Ses2/' #done x
pathParl40Ses1 = '/Users/ambreenchaudhri/Desktop/Canada/Parl40Ses1/' #done x
pathParl40Ses2 = '/Users/ambreenchaudhri/Desktop/Canada/Parl40Ses2/' #done x
pathParl40Ses3 = '/Users/ambreenchaudhri/Desktop/Canada/Parl40Ses3/' #done x
pathParl41Ses1 = '/Users/ambreenchaudhri/Desktop/Canada/Parl41Ses1/' #done
pathParl41Ses2 = '/Users/ambreenchaudhri/Desktop/Canada/Parl41Ses2/' #done


################################################
## These are the inputs I change each time I run 
## the code for a different Parliamentary Session
#################################################
# STEP 1: 

csvname = 'CanadaParl41Ses1.csv'
csvname2 = 'CanadaParl41Ses1_mpvotes.csv'
web_address = Parl41Ses1
path = str(pathParl41Ses1)

#################################################
#################################################
# STEP 2: 
# This saves all the vote page url's using 'Next Page' 

web_page = urllib2.urlopen(web_address) 
soup = BeautifulSoup(web_page.read(), "html.parser" ) 

next_pages = [str(web_address)]

def find_next_page(mysoup):
  try:
  	a_tag=mysoup.find_all('a',{'id':'ctl00_PageContent_hlNextPage'})[0]
  	next_address='http://www.parl.gc.ca/HouseChamberBusiness/'+a_tag['href']
  	next_pages.append(next_address)
  	print next_address
  	next_page=urllib2.urlopen(next_address)
  	next_soup=BeautifulSoup(next_page.read(),'html.parser')
  	find_next_page(next_soup)
  except:
		return next_pages
		
find_next_page(soup)
 
###########################
# STEP 4: 
# Empty Lists

list_weblinks = []
list_vote_number = []
list_vote_name = []
list_vote_passed = []
list_session_date = []
list_vote_total = []
list_yea_votes = []
list_nay_votes = []
list_total_votes = []
list_paired_votes = []

###########################
# STEP 5: 
# Functions to Pull Data and Create soups for General Info on Votes

def createsoups():
	for np in range (0, len(next_pages)):
		web_addressx = next_pages[np]
		web_pagex = urllib2.urlopen(web_addressx)
		soupx = BeautifulSoup(web_pagex.read(), "html.parser" )
# Here we get the list of web links.
		vote_tags_links = [div.a for div in soupx.find_all('div',{'class':"voteListingTitle"})]
		for i in range (0, len(vote_tags_links)):
			list_weblinks.append('http://www.parl.gc.ca'+vote_tags_links[i]['href'])
# Here we get a list of vote numbers. 
		vote_number = [div.a for div in soupx.find_all('div',{'class':"voteListingTitle"})]
		for i in range (0, len(vote_number)):
			x_vnum = vote_number[i]
			y_vnum = x_vnum.contents[-1]
			list_vote_number.append(y_vnum)
# Here we get a list of vote names. 
		vote_name = soupx.find_all('div',{'class':'voteDescription'})
		for i in range (0, len(vote_name)):
			x_vname = vote_name[i]
			z_vname = re.sub(r'<[^>]+>', '', str(x_vname))
			list_vote_name.append(z_vname)
# Here we get a list of votes passed. 
		vote_passed = soupx.find_all('div',{'class':'voteResult'})
		for i in range (0, len(vote_passed)):
			x_vpass = vote_passed[i]
			y_vpass = x_vpass.contents[-2]
			z_vpass = re.sub(r'<[^>]+>', '', str(y_vpass))
			list_vote_passed.append(z_vpass)
# Here we get a list of vote names. 
		session_date = soupx.find_all('div',{'class':'voteDate'})
		for i in range (0, len(session_date)):
			x_sesdate = session_date[i]
			y_sesdate = x_sesdate.contents[-1]
			list_session_date.append(y_sesdate)  
# Here we get a string with the vote totals
		vote_total = soupx.find_all('div',{'class':'voteTotals'})
		for i in range (0, len(vote_total)):
			x_votes = vote_total[i]
			y_votes = x_votes.contents[-1]
			list_vote_total.append(y_votes)

createsoups()

# A function that will clean strings
def listToStringWithoutBrackets(list1):
    return str(list1).replace('[','').replace(']','')

# Another way of getting the vote totals for yea, nay, total and paired votes		
def createsoupvotes():		
# 		for i in range (0, len(list_weblinks)):
		for i in range (500, 600):  # I pulled data from 25 vote pages at a time so I could verify more easily
			vote_webaddy = list_weblinks[i]
			vote_webpage = urllib2.urlopen(vote_webaddy)
			soupv = BeautifulSoup(vote_webpage.read(), "html.parser" )
			yea_votes = soupv.find_all('td',{'headers':"totalYeas"})
			yea_votes = re.sub(r'<[^>]+>', '', str(yea_votes))
			yea_votes = int(listToStringWithoutBrackets(yea_votes))
			list_yea_votes.append(yea_votes)
			nay_votes = soupv.find_all('td',{'headers':"totalNays"})
			nay_votes = re.sub(r'<[^>]+>', '', str(nay_votes))
			nay_votes = int(listToStringWithoutBrackets(nay_votes))
			list_nay_votes.append(nay_votes)
			total_votes = soupv.find_all('td',{'headers':"totalVotes"})
			total_votes = re.sub(r'<[^>]+>', '', str(total_votes))
			total_votes = int(listToStringWithoutBrackets(total_votes))
			list_total_votes.append(total_votes)
			total_paired = soupv.find_all('td',{'headers':"totalPaired"})
			total_paired = re.sub(r'<[^>]+>', '', str(total_paired))
			total_paired = int(listToStringWithoutBrackets(total_paired))
			list_paired_votes.append(total_paired)

createsoupvotes()


###########################
# STEP 6: 
# Check the lists before saving to a csv file 

len(list_weblinks)
len(list_vote_number)
len(list_vote_name)
len(list_vote_passed)
len(list_session_date)
len(list_vote_total)
len(list_yea_votes)
len(list_nay_votes)
len(list_total_votes)
len(list_paired_votes)


###########################
# STEP 7: 
# Saving to a csv file

with open( csvname , 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames=("URLs", "Vote Numbers", "Vote Names", "Passed", "Session Dates", "Vote Totals", "Yea Votes", "Nay Votes", "Total Votes", "Paired Votes"))
  my_writer.writeheader()
  for i in range(0, len(list_weblinks)):
    my_writer.writerow({"URLs":list_weblinks[i], "Vote Numbers":list_vote_number[i], "Vote Names":list_vote_name[i], "Passed":list_vote_passed[i], "Session Dates":list_session_date[i], "Vote Totals":list_vote_total[i], "Yea Votes":list_yea_votes[i], "Nay Votes": list_nay_votes[i], "Total Votes": list_total_votes[i], "Paired Votes": list_paired_votes[i]})	


###########################
# STEP 8: 
# Downloading all Webpages

# Function to download pages
def download_page(address,path,filename,wait=5):
	time.sleep(random.uniform(0,wait))
	page = urllib2.urlopen(address)
	page_content = page.read()
	if os.path.exists(path+filename)==False:
		with open(path+filename, 'w') as p_html:
			p_html.write(page_content)
	else:
		print "Can't overwrite file" + filename

list_weblinks1 = list_weblinks[160:161]  #I downloaded 50 pages at a time so I could look them over. 
list_vote_number1 = list_vote_number[160:161]

for vote, page in zip(list_vote_number1, list_weblinks1):
	download_page(page,path,vote)

#######################
# STEP 9: 
# Getting Individual Vote Data from a Webpage	

list_mp_names = []
list_mp_votes = []
list_mp_votenums = []
list_mp_parties = []
list_size = len(list_total_votes) 


def createMPvotes():
	for j in range (150, 204):  # I pulled data from 25 vote pages at a time so I could verify more easily
# 	for j in range (0, list_size):
		ministers_number = list_total_votes[j]
		ministers_votenum = list_vote_number [j]
		vote_webaddy = list_weblinks[j]
		vote_webpage = urllib2.urlopen(vote_webaddy)
		soupy = BeautifulSoup(vote_webpage.read(), "html.parser" )
		# Get MP Names & Party
		mp_names = soupy.find_all('td',{'headers':"Member"})
		init_a = len(mp_names) - ministers_number
		mp_party = soupy.find_all('td',{'headers':"Caucus"})
# 		for i in range (init_a, 3):
		for i in range (init_a, len(mp_names)):
			mp_name1 = mp_names[i]
			mp_name1 = mp_name1.contents[-4]
			mp_name1 = re.sub(r'<[^>]+>', '', str(mp_name1))
			mp_name1 = mp_name1.rstrip('\n')
			mp_name1 = mp_name1.lstrip('\n')
			list_mp_names.append(mp_name1)
			mp_party1 = mp_party[i]
			mp_party1 = mp_party1.contents[-1]
			list_mp_parties.append(mp_party1)
			list_mp_votenums.append(ministers_votenum)
		# Get MP Votes
		mp_vote = soupy.findAll('img', src=True)
		init_b = len(mp_vote) - ministers_number
# 		for i in range (init_b, 8):
		for i in range (init_b, len(mp_vote)):
			mp_vote1 = mp_vote[i]
			mp_vote1 = mp_vote1["alt"]
			list_mp_votes.append(mp_vote1)

createMPvotes()



###########################
# STEP 10: 
# Check the lists before saving to a csv file 

len(list_mp_names)
len(list_mp_votes)
len(list_mp_parties)
len(list_mp_votenums)

newlist_mp_parties = []

for i in range(0, len(list_mp_parties)):
	mp_partynew = list_mp_parties[i]
	mp_partynew = mp_partynew.encode('utf-8')
	newlist_mp_parties.append(mp_partynew)


###########################
# STEP 11: 
# Save to another excel file (that will be pivoted)

with open( csvname2 , 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames=("MP Name", "MP Party", "MP Vote Number", "MP Vote"))
  my_writer.writeheader()
  for i in range(0, len(list_mp_names)):
    my_writer.writerow({"MP Name":list_mp_names[i], "MP Party":newlist_mp_parties[i], "MP Vote Number":list_mp_votenums[i], "MP Vote":list_mp_votes[i]})	



