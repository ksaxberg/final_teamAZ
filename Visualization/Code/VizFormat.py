import os

pathToData = '/Users/danielkapellusch/Desktop/ArizonaData/'
outputFile = pathToData + "rcp45_Arizona.csv"

files = os.listdir(pathToData)

with open(outputFile,'w') as outF:
    #(0)year(1)month(2)day(3)maximum temperature(4)minimum temperature(5)precipitation in mm(6)average temperature
    # (7)precipitation in cm (8)relative humidity(9)Abundance
    outF.write('Lat,Lon,Time,T_max,T_min,Prcp(mm),T_ave,Prcp(cm),Rh_ave,Abundance\n')
    for f in files:
        #rcp45_31.35_-109.51.csv.out
        lat = ''
        lon = ''
        with open(pathToData+f,'r') as inF:
            lines = inF.readlines()
        rows = []
        for line in lines:
            rows.append(line.split(','))
        for row in rows:
            outF.write(lat+','+lon+','+row[0]+'-'+row[1]+'-'+row[2]+','+row[3]+','+row[4]+','+row[5]+','+row[6]+','+
                       row[7]+','+row[8]+','+row[9]+'\n')


