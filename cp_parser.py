import csv
import re
from re import findall, match, sub, search

# Denote text source and routput csv
path = "cyp-1992.txt"
csvfile = "cyp92.csv"

# read emails into memory
emails = open(path).readlines()

# Pull and clean email fields
# From Field
linefrom = [t for t in emails if findall("From:",t)]
cleanfrom = [x.split("From:")[1] for x in linefrom]

# Testing whether the from parser is mangling output...
with open("from.csv", "wb") as output:
	writeit = csv.writer(output, delimiter=',')
	writeit.writerow(linefrom[0:])
	writeit.writerow(cleanfrom[0:])

# Date Field
linedate = [t for t in emails if findall("Date:",t)]
cleandate = [x.split("Date:")[1] for x in linedate]

# Subject Field
linesubj = [t for t in emails if findall("Subject:",t)]
cleansubj = [x.split("Subject:")[1] for x in linesubj]

# "ID" Field
lineid = [t for t in emails if findall("Message-ID:",t)]
cleanid = [x.split("Message-ID:")[1] for x in lineid]

# open text file
allemails = open(path, "r")

# read all emails as giant blob
alltext = allemails.read()

# split each email where the body text begins
lesstext = alltext.split("Content-Type: text/plain")

# remove the header junk that formed the first list entry
del lesstext[0]

# cut off the header that remains below the email body 
bodytext = [x.split("From cypherpunks@MHonArc.venona")[0] for x in lesstext]

# Write email fields to CSV
with open(csvfile, "wb") as output:
	writeit = csv.writer(output, delimiter=',')
	writeit.writerow(cleanfrom[0:])
	writeit.writerow(cleandate[0:])
	writeit.writerow(cleansubj[0:])
	writeit.writerow(cleanid[0:])
	writeit.writerow(bodytext[0:])

output.close()


