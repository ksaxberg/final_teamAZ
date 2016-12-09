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
        csv.write("Lat,Lon,Time,Tmax,Tmin,Prcp(mm),T_ave,Prcp(cm),Rh_ave,Abundance\n")
        rows = []
        for line in lines:
            rows.append(line.split(','))

        #ORIGINAL HEADERS: Year,Month,Day,Tmax,Tmin,Prcp(mm),T_ave,Prcp(cm),Rh_ave
        for row in rows:
            if row != rows[0]:
                year = row[0]
                month = row[1]
                day = row[2]
                #TAKE OUT ABUNDANCE FOR REAL THING
                # csv.write(lat +","+lon+","+year+"-"+month+"-"+day+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+
                #           ","+str(float(row[8]))+",0\n")
                csv.write(lat +","+lon+","+row[0]+"-"+row[1]+"-"+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+
                          ","+str(float(row[8]))+",0\n")
