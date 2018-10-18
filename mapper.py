#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # split the input by commas giving 6 columns 
	datain = line.strip().split(",")
	#setting the keywords for for the column [3] in array
	term = ["ReadFile", "CloseFile","Load Image"]
	#setting the keywords for for the column [2] in array
	term_pid = "1940"
	#setting the keywords for for the column [4] in array
	term_exe_font = ["C:\Windows\System32", "C:\Windows\System32\sxs.dll","C:\Windows\Fonts\sserife.fon", "C:\Windows\System32\cryptbase.dll", "C:\Windows\System32\uxtheme.dll"]
	
	

	#If statement searches for the keyterm linked to ransomware for the column [2] in array. Outputs the term if found and appends a 1.

	if datain[2] in term_pid: 

		print datain[2] + "\t" + '1'
	
		#If statement searches for the keyterm linked to ransomware for the column [2] in array. Outputs the term if found and appends a 1.

	if datain[3] in term and datain[2] in term_pid : 

		print datain[3] +"\t" + '1'

		#If statement searches for the keyterm linked to ransomware for the column [2] in array. Outputs the term if found and appends a 1.

	if datain[4] in term_exe_font and datain[2] in term_pid:

		print datain[4] +"\t" + '1'
