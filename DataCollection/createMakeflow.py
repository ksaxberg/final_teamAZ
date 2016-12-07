coorFile = "filteredArizonaCoords.csv"
mfFile = 'Arizona.makeflow'

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

