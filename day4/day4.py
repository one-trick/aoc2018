#!/usr/bin/python

import re
from datetime import datetime

file_contents = []

input_file = "input.txt"
fh = open(input_file, 'r')

# First thing we need to do is read in our data and sort it by timestamp
for line in fh:
	line = line.rstrip()
	file_contents.append(line)
file_contents.sort()

# Now we need to parse the data. Time format: YYYY-MM-DD hh:mm. Example data:
# [1518-11-21 23:52] Guard #409 begins shift
# [1518-11-22 00:04] falls asleep
# [1518-11-22 00:08] wakes up
# So the first line, all we care about is the guard's ID number
# the next line is when he falls asleep, and the line after that is when he wakes up

# Initial data structure will be
# guard_id => minutes asleep

guard_id = ''
asleep_time = ''
wake_time = ''
dictionary = {}
for line in file_contents:
	# divide the line into parts timestamp, details
	(timestamp,details) = line.split("] ",1)
	# Now look to see what type of line it is
	print line
	if "Guard" in details:
		regex = re.compile('Guard #(.*) begins shift')
		guard_id = regex.findall(details)
		guard_id =  guard_id[0]
	if "falls" in details:
		# This is the time he fell asleep, so we need to note this
		asleep_time = datetime.strptime(timestamp[1:], "%Y-%m-%d %H:%M")
	if "wakes" in details:
		# This is the time he woke up, so we need to subtract wake from sleep
		wake_time = datetime.strptime(timestamp[1:], "%Y-%m-%d %H:%M")
		minutes_asleep = wake_time - asleep_time
#		print "Guard " + guard_id + " was asleep for " + str(minutes_asleep)
		# check if key exists, if so, we need to add the minutes to exist value. if not create it
		if guard_id in dictionary:
			dictionary[guard_id] = minutes_asleep + dictionary[guard_id]
		else:
			dictionary[guard_id] = minutes_asleep

sorted_guard_list = sorted(dictionary, key=dictionary.get, reverse=True)
# first element in our sorted dictionary should be the guard that slept the most
sleepiest_guard = sorted_guard_list[0]
sleepiest_guard_minutes = dictionary[sorted_guard_list[0]]
print "Sleepiest guard was " + sleepiest_guard + " who slept a total of " + str(sleepiest_guard_minutes) + " minutes"

# at this point we know who slept the most, but we need to figure out which minute they slept the most during
# loop back through content. if it's asleep, we need to subtract 60 by the minute they were asleep. if it's awake, go from 0 to minute
# [1518-11-21 23:52] Guard #409 begins shift
# [1518-11-22 00:04] falls asleep
# [1518-11-22 00:08] wakes up
# populate a new dictionary with the keys 0 - 60
timedict = {}
counter = 0
while counter < 60:
	timedict[counter] = 0
	counter += 1

for line in file_contents:
	# divide the line into parts timestamp, details
	(timestamp,details) = line.split("] ",1)
	if "Guard" in details:
		regex = re.compile('Guard #(.*) begins shift')
		guard_id = regex.findall(details)
		guard_id = guard_id[0]
#		print "Guard_id: " + guard_id + " Sleepiest_guard: " + sleepiest_guard
		if guard_id != sleepiest_guard:
			# guards didnt match, skipping
			guard_id = False
	if "falls" in details and guard_id:
		asleep_time = datetime.strptime(timestamp[1:], "%Y-%m-%d %H:%M")
	if "wakes" in details and guard_id:
		# This is the time he woke up, so we need to subtract wake from sleep
		wake_time = datetime.strptime(timestamp[1:], "%Y-%m-%d %H:%M")
		# First let's figure out if the hours match
		if asleep_time.date() == wake_time.date():
			# Dates match, now let's compare hour
			if asleep_time.time().hour == wake_time.time().hour:
				# Same hour! lets get a starting and ending point
#				print "HOURS MATCH - Starting minute: " + str(asleep_time.time().minute) + " Ending Minute: " + str(wake_time.time().minute)
				# loop starting with starting minute and ending with ending minute
				counter = int(asleep_time.time().minute)
				while counter < int(wake_time.time().minute):
#					print counter
					timedict[counter] = timedict[counter] + 1
					counter += 1
			else:
				# different hour - initial testing showed my input didn't match this test case, so leaving logic out for now
				print "Hours didn't match - Starting min: " + str(asleep_time.time().minute) + " Ending Min: " + str(wake_time.time().minute)
				exit()
		else:
			# initial testing revealed i dont hit this logic in my input, so ignoring for now
			print "We rolled over days"
			exit()	

# lets see what minute was the most frequent
sorted_times = sorted(timedict, key=timedict.get, reverse=True)
sleepiest_minute = sorted_times[0]
print "Sleeping minute was: " + str(sleepiest_minute)
# What is the ID of the guard you chose multiplied by the minute you chose?
print "Solution to challenge 1 is: " + str(int(sleepiest_guard) * sleepiest_minute)

fh.close()
