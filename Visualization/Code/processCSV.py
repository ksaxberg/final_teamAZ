import os

datasources = "/Users/danielkapellusch/Documents/ACIC2016/Final/rcp45Data/"
#"/Users/danielkapellusch/Documents/ACIC2016/Final/rcp85Data"

files = os.listdir(datasources)
newFile = '/Users/danielkapellusch/Documents/ACIC2016/Final/TESTrcp45Data.csv'

with open(newFile,'w') as csv:
    for f in files:
        with open(datasources+f,'r') as data:
            lines = data.readlines()
        lat = f[6:11]
        lon = f[12:19]
        for line in lines:
            if line == lines[0]:
                csv.write("Lat,Lon,Year,Month,Day,Tmax,Tmin,Prcp(mm),T_ave,Prcp(cm),Rh_ave,Abundance\n")
            else:
                #TAKE OUT ABUNDANCE FOR REAL THING
                csv.write(lat +","+lon+","+line[:-1]+","+"0\n")
