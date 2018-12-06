#!/usr/bin/python

input_file = "input.txt"
fh = open(input_file, "r")

two_counter = 0
three_counter = 0

two = False
three = False

for line in fh:
	# Figure out the number of times a specific letter appears
	line = line.rstrip()
	for char in line:
		count = line.count(char)
		if count == 2:
			two = True
		if count == 3:
			three = True
#		print "Letter " + char + " appears in string "+ line +" a total of " + str(count) + " times."

	# After going through each line, determine if it had two or three chars n the ID. If so, increment each counter
	if two:
		two_counter = two_counter + 1
		two = False
	if three:
		three_counter = three_counter + 1
		three = False
#print "Total boxes with two repeating characters: " + str(two_counter)
#print "Total boxes with three repeating characters: " + str(three_counter)

print "Solution for challenge 1 - Checksum: " + str(two_counter * three_counter)

fh.close()


# Part 2
input_file = "input.txt"
fh = open(input_file, "r")
idlist =[]
for line in fh:
	line = line.rstrip()
	idlist.append(line)

element_counter = 0

# Function to count the differences between two strings
def count_diff(str1, str2):
	if len(str1) != len(str2):
		print "String comparison length didn't match. This is bad..."
		exit()
	iterator = 0
	differences = 0
	answer = ""
	# iterate through the strings and count the differences
	for letter in str1:
		if letter != str2[iterator]:
			differences = differences + 1
		else:
			# This is just formultating the answer so it's "fully" automated. It's lazy but I'm tired
			answer = answer + letter
		iterator = iterator + 1
	if differences == 1:
		# Found strings with only one difference"
#		print str1 + " | " + str2
		print "Solution for challenge 2: " + answer
		exit()
	return differences

total_elements = len(idlist)
while element_counter < total_elements:
	for element in idlist:
#		print "Comparing " + idlist[element_counter] + " with " + element	
		differences = count_diff(idlist[element_counter], element)
#		print "There were a total of " + str(differences) + " differences"
	element_counter = element_counter + 1

fh.close()
