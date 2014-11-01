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
#######################################################
#aadhaar_genearated_reducer.py

def reducer():

    aadhaar_generated = 0
    old_key = None

    #Cycle through the list of key-value pairs emitted
    #by your mapper, and print out each key once,
    #along with the total number of Aadhaar generated,
    #separated by a tab.  Assume that the list of key-
    #value pairs will be ordered by key.  Make sure
    #each key-value pair is formatted correctly!
    #Here's a sample final key-value pair: "Gujarat\t5.0"
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        thisKey, thisGen = data
        if old_key and old_key != thisKey:
            print "{0}\t{1}".format(old_key, aadhaar_generated)
            aadhaar_generated = 0
        old_key = thisKey
        aadhaar_generated += float( thisGen)
    if old_key != None:
        print "{0}\t{1}".format(old_key, aadhaar_generated)
        
reducer()
