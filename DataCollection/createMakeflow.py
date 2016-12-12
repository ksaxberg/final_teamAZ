"""Generates a Makeflow file for downloading the climate data.
It takes a csv file with the list of lat/lon coordinates to get data for.
Arguments = (1)input coordinate csv (2)output makeflow file"""

import sys

args = sys.argv[1:]

coorFile = args[0]      #EXAMPLE: "filteredArizonaCoords.csv"
mfFile = args[1]        #EXAMPLE: 'Arizona.makeflow'

with open(coorFile,'r') as input:
    lines = input.readlines()

points = []
for line in lines:
    points.append(line.split(','))

with open(mfFile,'w') as output:
    for point in points:
        if point != points[0]:
            lat = point [0]
            lon = str(float(point[1]))
            output.write(": MakeRequests.py DataProcessing.py\n")
            output.write("\tpython MakeRequests.py " + lat + " " + lon +"\n")
