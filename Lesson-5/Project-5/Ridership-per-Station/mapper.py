#riders_per_station_mapper.py
import sys
import string

def mapper():
    """
    The input to this mapper will be the final Subway-MTA dataset.  This mapper 
    should return a line for each UNIT, along with the number of ENTRIESn_hourly for that row.
    
    An example input to the mapper may would look like this:
    R002    1050105.0
    
    The mapper should emit a key and value pair separated by a tab, for example:
    R002\t105105.0
    """
    count = 0
    for line in sys.stdin:
    	# your code here
        data = line.split(",") 
        if count == 0:
            count += 1
        else:
            print "{0}\t{1}".format(data[1],data[6])
                                    

mapper()

