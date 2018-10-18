#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_datain = None
current_count = 0
datain = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    datain, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_datain == datain:
        current_count += count
    else:
        if current_datain:
            # write result to STDOUT
            print '%s\t%s' % (current_datain, current_count)
        current_count = count
        current_datain = datain

# do not forget to output the last word if needed!
if current_datain == datain:
    print '%s\t%s' % (current_datain, current_count)


if current_datain == datain and datain == "1940":
	
	print "ransomware detected"


if current_count <10:
	print "No suspicious activity found, there may be no ransomware on this machine"
	


  
