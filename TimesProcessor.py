import csv
import sys

""" 
Function: writeTimes

Writes a list of lists of swim meet data to a csv.

Input: (str) filename, (list of lists) alltimes 
"""
def writeTimes(csvname, alltimes) :
	
	with open(csvname, "wb") as csvfile:
		w = csv.writer(csvfile, delimiter=",")
		print len(alltimes)
		print alltimes[33]
		print alltimes[34]
		for ea in alltimes:
			ea = ea.split(',')
			print ea
			w.writerow(ea)

	return



""" UNUSED
Function: toSeconds

Converts a string of time into a float 
(e.g. "45.62" -> 45.62, "1:03.74" -> 63.74)

Input: (str) time
Output: (float) converted
"""
def toSeconds(time):
	converted = 0
	time = time[:-1]
	timeList = time.split(".")
	
	if ":" in timeList[0]:
		minutes = timeList[0].split(":")
		converted += (int(minutes[0]) * 60)
		converted += float(minutes[1])
	else:
		converted += float(time)

	return converted


"""
Function: readTextData

Read a HY-TEK text file and converts it to a list of lists.

Input: (str) filename
Output: (list of lists) results
"""
def readTextData(filename):
	results = []
	with open(filename, "rb") as txtfile:
		t = txtfile.read()
		t = t.split('\n')
		for ea in t:
			ea = ' '.join(ea.split())
			ea = ','.join(ea.split()) 
			results.append(ea)
	return results


def main():
	#toSeconds("56.50")
	############################
	# OPTION: take filename as a Python input
	"""
	filename = raw_input("Enter filename (must be .txt): ")
	csvname = filename.split(".")[0] + ".csv"
	print "Data from " + filename + " will be written to " + csvname
	"""

	############################
	# OPTION: take filename as a command line argument
	"""
	filename = sys.argv[1]
	if (".txt" not in filename):
		print "ERROR: file must be .txt"
	csvname = filename.split(".")[0] + ".csv"
	"""

	alltimes = readTextData(filename)
	writeTimes(csvname, alltimes)
	return

if __name__ == "__main__":
	main()