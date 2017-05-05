#!/usr/bin/env python

#*******************************************************************************
#Mathwoods - Sequential Search vs. Binary Search
#A short program that compares and graphs the speed of two search algorithms
#searching ordered array of increasing size.
#Created by Mathwoods on February 13, 2017
#Tested on Python 2.7.10
#Last modified on May 2, 2017
#*******************************************************************************
from __future__ import print_function #make print work as Python 3.x function
import random
import timeit
import matplotlib.pyplot as plt


#sequential search
def seq_search(arr=None, x=None):
	i = 0
	while(i < len(arr)):
		if arr[i] == x:
			return i
		i = i + 1
	return -1

#binary search
def bin_search(arr=None, x=None):
	l, r = 0, len(arr)-1
	while l <= r:
		m = int((l+r)/2)
		if x > arr[m]:
			l = m+1
		if x < arr[m]:
			r = m-1
		if x == arr[m]:
			return m
	return -1


#wrapper function to time the search algorithms
def wrapper(func, *args, **kwargs):
	def wrapped():
		return func(*args, **kwargs)
	return wrapped


#main

#ANSI escape sequences used to format terminal text
#\x1b[... => ASCII hex for ESC, bracket added at end
#\x1b[a;b;..;..m; Selected Graphics Rendition Parameter (SGR)
#a=1 => bold or increased intensity
#b=7 => reverse video (switch background/foreground colors)
#0m  => reset all text atrributes to terminal default
print("\n" + '\x1B[1;7m'+ "SEQUENTIAL SEARCH VS BINARY SEARCH" + '\x1B[0m')

i, trial = 2, 1						#initial exponent and trial number
list_results = []					#list of maps
timeit_loops = 10					#run each search t times for each trial

#run search trials
while i <= 6:

	n = 10**i 						#10 to power of i
	tup_num = tuple(range(0, n))	#populate tuple with integers 0 to n-1

	print("\n" + '\x1B[4m'+ "ARRAY SIZE = %s (10^i where i = %s)"%(n,i) \
	 + '\x1B[0m')

	while trial <= 3:

		r = random.randint(0, n-1)
		print("TRIAL %s" % trial)
		print("Random generated value: %s" % r)

		print("Running SEQ SEARCH...", end="")

		#Calculate time
		wrapped = wrapper(seq_search, tup_num, r)
		seq_time = timeit.timeit(wrapped, number=timeit_loops)

		print("DONE!")

		print("Total time for %s searches: " \
		      "%s seconds." % (timeit_loops, seq_time))


		print("Running BIN SEARCH...", end="")

		wrapped = wrapper(bin_search, tup_num, r)
		bin_time = timeit.timeit(wrapped, number=timeit_loops)

		print("DONE!")

		print("Total time for %s searches: %s seconds."
				% (timeit_loops, bin_time))

		list_results.append({ 'power': i, 'trial': trial, 'tup_size': n,
				'rand': r, 'seq_time': seq_time, 'bin_time': bin_time,
				'timeit_loops': timeit_loops})

		trial = trial + 1

	i = i + 1
	trial = 1

print("\n" + '\x1B[1;7m'+ "To end program close graph window." + '\x1B[0m'\
 	+ "\n")

#make graph
lst_xcoordseq = []
lst_ycoordseq = []
lst_xcoordbin = []
lst_ycoordbin = []

#populate coordinate lists with data from list_results
for entry in list_results:
	lst_xcoordseq.append(entry['power'])
	lst_xcoordbin.append(entry['power'])
	lst_ycoordseq.append(entry['seq_time'])
	lst_ycoordbin.append(entry['bin_time'])

#add points to plot
#red diamonds for seq search; blue dots for bin search
plt.plot(lst_xcoordseq, lst_ycoordseq, 'rD', label='Seq Search')
plt.plot(lst_xcoordbin, lst_ycoordbin, 'bo', label='Bin Search')

#Set lower/upper bounds of axes
ymax = max(lst_ycoordseq)
plt.axis([0,7,-0.1,ymax+0.1])

plt.xlabel('Size of array (powers of 10)')
plt.ylabel('Search time (sec)')

#Set figure title
fig = plt.gcf()
fig.canvas.set_window_title('Math Woods - Sequential vs. Binary Search')

#Put grid lines at every tick on x,y axes
plt.grid(True)

#place legend
#numpoints-1 so that only one dot appears in legend
plt.legend(loc='upper left', numpoints=1)

plt.show()
