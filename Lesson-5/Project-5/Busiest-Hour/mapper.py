#busiest_hour_mapper.py
import sys
import string

def mapper():
    """
    Each line in sys.stdin will be a line from a csv file representing the contents
    of our final Subway-MTA dataset.  For each line, this mapper should return the following:
    The unit, the ENTRIESn_hourly, the DATEn, and TIMEn columns, separated by tabs.  
    Example:

    R001    100000.0    2011-05-01  01:00:00
    """

    count = 0
    for line in sys.stdin:
        # your code here
        data = line.split(",") 
        if count == 0:
            count += 1
        else:
            print "{0}\t{1}\t{2}\t{3}".format(data[1],data[6],data[2],data[3])

mapper()

