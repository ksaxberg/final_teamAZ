"""Takes the output of Data Collection and formats it into a csv for running in the MoLS """

import sys
import os

arguments = sys.argv[1:]

if arguments[0] == '-h' or arguments[0] == '--h' or arguments[0] == '--help':
    print "DataProcessing.py takes two arguments:"
    print "(1) Input CSV file"
    print "(2) Output CSV file"
    sys.exit()

if len(arguments) != 2:
    print "Incorrect number of arguments"
    print "DataProcessing.py -h for more information"
    sys.exit()

inputFile = arguments[0]
outputFile = arguments[1]

with open(inputFile,'r') as input:
    lines = input.readlines()

rows = []
for line in lines:
    rows.append(line.split(','))

with open(outputFile,'w') as output:
    output.write("Year,Month,Day,Tmax,Tmin,Prcp(mm),T_ave,Prcp(cm),Rh_ave\n")
    ln = 0
    for row in rows:
        if ln >= 16:
            yr = row[0][0:4]
            mon = row[0][5:7]
            day = row[0][8:10]
            tmin = str(float(row[1]) -274.15)
            tmax = str(float(row[2]) - 274.15)
            tave = str((float(tmin) + float(tmax))/2.0)
            prcpMM = str(float(row[5]))
            prcpCM = str(float(row[5])/10.0)
            rhave = str((float(row[3]) + float(row[4]))/2.0)
            output.write(yr +"," + mon + "," + day + "," + tmax + "," + tmin + "," + prcpMM + "," + tave + "," + prcpCM + "," +rhave +"\n")
        elif ln < 16:
            ln += 1

os.remove(inputFile)

