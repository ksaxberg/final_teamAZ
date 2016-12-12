import os
import sys

args = sys.argv[1:]

pathToData = args[0]  #Path to directory with all the data for one scenario
outputFile = args[1]  #Path to where you want the output CSV to be

files = os.listdir(pathToData)

with open(outputFile,'w') as outF:
    #(0)year(1)month(2)day(3)maximum temperature(4)minimum temperature(5)precipitation in mm(6)average temperature
    # (7)precipitation in cm (8)relative humidity(9)Abundance
    outF.write('Lat,Lon,Time,T_max,T_min,Prcp(mm),T_ave,Prcp(cm),Rh_ave,Abundance\n')

    for f in files:
        if f != '.DS_Store':
            print f
            fName = f.split('_')
            #rcp45_31.35_-109.51.csv.out
            lat = fName[1]
            lonIndex = (fName[2]).index('.c')
            lon =fName[2][:lonIndex]
            print lat
            print lon
            with open(pathToData+f,'r') as inF:
                lines = inF.readlines()
            rows = []
            for line in lines:
                rows.append(line.split(','))
            try:
                for row in rows:
                    outF.write(lat+','+lon+','+row[0]+'-'+row[1]+'-'+row[2]+','+row[3]+','+row[4]+','+row[5]+','+row[6]+','+
                               row[7]+','+row[8]+','+row[9])
            except(Exception):
                print f


