import sys

#[0] = state [1] = historical, future rcp45, or future rcp85 [2] = zone [3]= # of years (default all) [4] = model (default GFDL-ESM2M)
commandlineArgs = sys.argv[1:]
state = commandlineArgs[0]
dataType = commandlineArgs[1]
zone = commandlineArgs[2]
years = int(commandlineArgs[3])
model = commandlineArgs[4]

if dataType == 'historical':
    start = 1950
    stop = 1949 + years
if dataType == 'future45' or 'future85':
    start = 2006
    stop = 2005 + years

#GFDL-ESM2M_RhodeIsland_fut45_2006_2006_306.csv: GetData.py
#{Model}_{State}_{dataType}_start_stop_zone.csv


outputFile = model + '_' + state + '_' + dataType + '_' + str(start) + '_' + str(stop) + '_' + zone + ".csv"





