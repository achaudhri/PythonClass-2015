# Ambreen Chaudhri
# HW 4 Sorting Algorithm Times for Graphs

import csv
import random
import math
import time
import HW4sort

# recorded time will be average of 100 trials on 90 random lists

# number of elements in each list to range from 10 to 100
nlo = 10
nhi = 100
sort_n = range(nlo, nhi)

# draw 100 random samples (trials)
trials = 100

# empty lists for each function to store its times in
quicksort_times = []
bubblesort_times = []

random_list = random.sample(range(1,11),10)

# Here are the times for quicksort 
for draw in range(nlo, nhi):
    start = time.clock()
    for attempt in range(trials):
        inputlist = random.sample(range(0,nhi), int(draw))
        HW4sort.quicksort(inputlist)
    end = time.clock()
    quicksort_times.append((end-start)/100)

# Here are the times for bubblesort 
for draw in range(nlo, nhi):
    start = time.clock()
    for attempt in range(trials):
        inputlist = random.sample(range(0,nhi), int(draw))
        HW4sort.bubblesort(inputlist)
    end = time.clock()
    bubblesort_times.append((end-start)/100)

#Write these times to a csv names times.csv where each time gets its own column

with open('times.csv', 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames=("n", "quicksort", "bubblesort"))
  my_writer.writeheader()
  for i in range(0,len(quicksort_times)):
    my_writer.writerow({"n":sort_n[i], "quicksort":quicksort_times[i], "bubblesort":bubblesort_times[i]})	

