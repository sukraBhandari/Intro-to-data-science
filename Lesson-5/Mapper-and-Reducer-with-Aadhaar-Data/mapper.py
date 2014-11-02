#aadhaar_genearated_mapper.py
import sys
import string

def mapper():
    #index = 0
    for line in sys.stdin: #cycle through lines of code
        
        #Your code goes here.  Each line will be
        #a comma-separated list of values.  The
        #header row WILL be included.  Tokenize
        #each row using the commas, and emit a key-
        #value pair containing the district and
        #Aadhaar generated, separated by a tab.
        #Make sure each row has the correct number
        #of tokens and is not the header row!
        data = line.strip().split(",")
        if len(data) != 12 or data[0] == 'Registrar':
          continue
        print "{0}\t{1}".format(data[3],data[8])
            
mapper()
