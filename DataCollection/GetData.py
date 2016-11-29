import pyGDP
import sys

#[0] = state [1] = h or f [2] = zone [3]= # of years (default all)
commandlineArgs = sys.argv[1:]

if len(commandlineArgs) < 3 or len(commandlineArgs) > 4:
    sys.exit("ERROR: Incorrect number of arguments! (state, model, zone, number of years)")

state = commandlineArgs[0]
model = commandlineArgs[1]
zone = commandlineArgs[2]
yrs = commandlineArgs[3]

pyGDP = pyGDP.pyGDPwebProcessing()  # initialize a pyGDP wps object

filePath = state + 'Grid.zip'  #which shapefile to use

# upload the file to geoserver
try:
    shpfile = pyGDP.uploadShapeFile(filePath)

except Exception:
    print 'A file of this name already exists, it has not been replaced.'
    shpfile = 'upload:testUpload'
else:
    print 'Shapefile Uploaded'

# Grab the file and set its attributes:
Stateshapefile = shpfile

usr_attribute = 'id'
ids = []  #list of ids/zones

values = pyGDP.getValues(Stateshapefile,usr_attribute)
for val in values:
    if val != None:
        ids.append(val)

if int(zone) < (len(ids) - 1):
    usr_value = ids[int(zone)]
else:
     sys.exit("ERR0R: Invalid zone")

if model == 'h':
    datasetURI = 'http://cida.usgs.gov/thredds/dodsC/macav2metdata_daily_historical'
    dataType = ['tasmax_GFDL-ESM2M_r1i1p1_historical', 'tasmin_GFDL-ESM2M_r1i1p1_historical',
                'pr_GFDL-ESM2M_r1i1p1_historical',
                'rhsmax_GFDL-ESM2M_r1i1p1_historical', 'rhsmin_GFDL-ESM2M_r1i1p1_historical']
    timeStart = '1950-01-01T00:00:00.000Z'
    if len(commandlineArgs) == 3:
        timeEnd = '2005-12-31T00:00:00.000Z'
    if len(commandlineArgs) == 4:
        finalYear = 1949 + int(yrs)
        timeEnd = str(finalYear) + '-12-31T00:00:00.000Z'
    time = 'hist'
if model == 'f':
    datasetURI = 'http://cida.usgs.gov/thredds/dodsC/macav2metdata_daily_future'
    dataType = ['tasmax_GFDL-ESM2M_r1i1p1_future', 'tasmin_GFDL-ESM2M_r1i1p1_future',
                'pr_GFDL-ESM2M_r1i1p1_future',
                'rhsmax_GFDL-ESM2M_r1i1p1_future', 'rhsmin_GFDL-ESM2M_r1i1p1_future']
    timeStart = '2006-01-01T00:00:00.000Z'
    if len(commandlineArgs) == 3:
        timeEnd = '2099-12-31T00:00:00.000Z'
    if len(commandlineArgs) == 4:
        finalYear = 2005 + int(yrs)
        timeEnd = str(finalYear) + '-12-31T00:00:00.000Z'
    time = 'fut'

print "Gathering Data"
outputFile_handle = pyGDP.submitFeatureWeightedGridStatistics(Stateshapefile, datasetURI, dataType, timeStart, timeEnd,
                                                             usr_attribute, usr_value)

input = outputFile_handle
#output file naming example: STATE_hist_1950_2005_5.csv
output = state + '_'+ time + '_' + timeStart[0:4] + '_' + timeEnd[0:4] + '_' + zone + '.csv'
numberOfVariables = 5

print "Creating CSV"
with open(input, 'r') as reader:
    data = [x.replace("\n", ",").split(",") for x in reader.readlines()]
factorToSkipBy = (len(data) / numberOfVariables)

with open(output, 'w') as csv:
    csv.write("Year,Month,Day,T_max,T_min,Precip(mm),T_ave,Precip(cm),rh_ave\n")
    for i in range(3, factorToSkipBy - 1):
        year, month, day = data[i][0].split("-")
        csv.write(", ".join((year, month, day[:2], str(float(data[i][1]) -273.15), str(float(data[i + factorToSkipBy][1])-273.15),
                         data[i + factorToSkipBy * 2][1],
                         str(((float(data[i][1]) + float(data[i + factorToSkipBy][1])) / 2)-273.15),
                         str(float(data[i + factorToSkipBy * 2][1]) / 10),
                         str((float(data[i + factorToSkipBy * 3][1]) + float(
                             data[i + factorToSkipBy * 4][1]) / 2))))+'\n')




