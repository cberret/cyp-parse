import csv

# Denote text source and routput csv
path = "cyp-1992.txt"
csvfile = "cyp.csv"

# read emails into memory
textfile = open(path, "r")
alltext = textfile.read()

# Split each email at header
eachemail = []
eachemail = alltext.split("From cypherpunks@MHonArc.venona")
# print eachemail[40]

# Write each email into a CSV
with open(csvfile, "wb") as output:
	writeit = csv.writer(output, delimiter=',')
	writeit.writerow(eachemail[0:])

