#!/usr/bin/python

current_frequency = 0
global_frequency_list = set([0])
iteration = 1

def iterate(frequency, frequency_list):
	input_file = "input.txt"
	fh = open(input_file, "r")
	for line in fh:
		# Look to see if it's a positive or a negative number
		sign = line[0]
		if sign == "+":
			frequency = frequency + int(line[1:])
		elif sign == "-":
			frequency = frequency - int(line[1:])
		else:
			print "Terrible things happened."
			exit()

		# Check if frequency already exists in list. If so exit 
		if frequency in frequency_list:
			print "Frequency matched a previous. Final result of challenge 2 is: " + str(frequency)
			exit()	
		else:
			frequency_list.add(frequency)
	fh.close()
	return frequency, frequency_list

# 1000 is an arbitrary number
while(iteration < 1000):
	current_frequency, global_frequency_list = iterate(current_frequency, global_frequency_list)
	if(iteration == 1):
		print "Final result for challenge 1 is: " + str(current_frequency)
	iteration = iteration + 1
