import pyGDP
import sys
import os

#[0] = state [1] = historical, future rcp45, or future rcp85 [2] = zone [3]= # of years (default all) [4] = model (default GFDL-ESM2M)
commandlineArgs = sys.argv[1:]

if len(commandlineArgs) < 3 or len(commandlineArgs) > 5:
    sys.exit("ERROR: Incorrect number of arguments! (state, data type, zone, number of years(optional), and model (optional)")

state = commandlineArgs[0]
model = commandlineArgs[1]
climateModel = 'GFDL-ESM2M'
if len(commandlineArgs) == 4 or len(commandlineArgs) == 5:
    yrs = commandlineArgs[3]
    if len(commandlineArgs) == 5:
        climateModel = commandlineArgs[4]

pyGDP = pyGDP.pyGDPwebProcessing()  # initialize a pyGDP wps object

filePath = '/final_teamAZ/DataCollection/StateGrids/state_' + state + 'Grid.zip'  #which shapefile to use

# upload the file to geoserver
try:
    shpfile = pyGDP.uploadShapeFile(filePath)

except Exception:
    print 'A file of this name already exists, it has not been replaced.'
    shpfile = 'upload:state_' + state + 'Grid'
else:
    print 'Shapefile Uploaded'

# Grab the file and set its attributes:
Stateshapefile = shpfile

usr_attribute = 'id'
usr_value = commandlineArgs[2]

if model == 'historical':
    datasetURI = 'http://cida.usgs.gov/thredds/dodsC/macav2metdata_daily_historical'
    dataType = ['tasmax_' + climateModel+ '_r1i1p1_historical', 'tasmin_' + climateModel + '_r1i1p1_historical',
                'pr_' + climateModel +'_r1i1p1_historical','rhsmax_' + climateModel+ '_r1i1p1_historical',
                'rhsmin_' + climateModel + '_r1i1p1_historical']
    timeStart = '1950-01-01T00:00:00.000Z'
    if len(commandlineArgs) == 3:
        timeEnd = '2005-12-31T00:00:00.000Z'
    if len(commandlineArgs) == 4:
        finalYear = 1949 + int(yrs)
        timeEnd = str(finalYear) + '-12-31T00:00:00.000Z'
    time = 'hist'
if model == 'future45':
    datasetURI = 'http://cida.usgs.gov/thredds/dodsC/macav2metdata_daily_future'
    dataType = ['tasmax_' + climateModel + '_r1i1p1_rcp45', 'tasmin_' + climateModel +'_r1i1p1_rcp45',
                'pr_' + climateModel +'_r1i1p1_rcp45','rhsmax_' + climateModel + '_r1i1p1_rcp45',
                'rhsmin_' + climateModel + '_r1i1p1_rcp45']
    timeStart = '2006-01-01T00:00:00.000Z'
    if len(commandlineArgs) == 3:
        timeEnd = '2099-12-31T00:00:00.000Z'
    if len(commandlineArgs) == 4:
        finalYear = 2005 + int(yrs)
        timeEnd = str(finalYear) + '-12-31T00:00:00.000Z'
    time = 'fut45'
if model == 'future85':
    datasetURI = 'http://cida.usgs.gov/thredds/dodsC/macav2metdata_daily_future'
    dataType = ['tasmax_' + climateModel + '_r1i1p1_rcp85', 'tasmin_' + climateModel +'_r1i1p1_rcp85',
                'pr_' + climateModel +'_r1i1p1_rcp85','rhsmax_' + climateModel + '_r1i1p1_rcp85',
                'rhsmin_' + climateModel + '_r1i1p1_rcp85']
    timeStart = '2006-01-01T00:00:00.000Z'
    if len(commandlineArgs) == 3:
        timeEnd = '2099-12-31T00:00:00.000Z'
    if len(commandlineArgs) == 4:
        finalYear = 2005 + int(yrs)
        timeEnd = str(finalYear) + '-12-31T00:00:00.000Z'
    time = 'fut85'

print "Gathering Data"
File_handle = pyGDP.submitFeatureWeightedGridStatistics(Stateshapefile, datasetURI, dataType, timeStart, timeEnd,
                                                             usr_attribute, usr_value)

input = File_handle
output = climateModel + '_' + state + '_'+ time + '_' + timeStart[0:4] + '_' + timeEnd[0:4] + '_' + usr_value + '.csv'
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
os.remove(File_handle)
os.remove('owslib.log')




