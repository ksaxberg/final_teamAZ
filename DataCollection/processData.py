import sys

inputFile = sys.argv[1]

with open(inputFile,'r') as input:
    lines = input.readlines()

rows = []
for line in lines:
    rows.append(line.split(','))

with open('pData.csv','w') as output:
    output.write("Year,Month,Day,Tmax,Tmin,Prcp(mm),T_ave,Prcp(cm),Rh_ave\n")
    if 'historical' in inputFile:
        yr = 1950
    if 'rcp45' in inputFile or 'rcp85' in inputFile:
        yr = 2006
    mon= 1
    mons_with_thirty = [4,6,9,11]
    mons_with_thirtyone = [1,3,5,7,8,10,12]
    day = 1
    for row in rows:
        if row != rows[0]:
            t_ave = (float(row[1])+float(row[4]))/2.0
            prcpCM = (float(row[2])/10)
            rh_ave = (float(row[5])+float(row[3]))/2.0
            output.write(str(yr) + "," + str(mon) + "," + str(day) +","+row[1]+","+row[4]+","+row[2]+","+
                         str(t_ave)+","+str(prcpCM)+","+str(rh_ave)+"\n")

            if mon in mons_with_thirty and day == 30:
                day = 1
                mon += 1
            elif mon == 2 and day == 28:
                day = 1
                mon += 1
            elif mon in mons_with_thirtyone and day == 31:
                day = 1
                if mon == 12:
                    mon = 1
                    yr += 1
                else:
                    mon += 1
            else:
                day += 1





