path = "/Users/danielkapellusch/Documents/ACIC2016/Final/TESTrcp45Data.csv"

with open(path,'r') as input:
    lines = input.readlines()

rows = []
for line in lines:
    rows.append(line.split(','))

with open("/Users/danielkapellusch/Documents/ACIC2016/Final/ProcessedTest.csv",'w') as output:
    for row in rows:
        year = row[2]
        month = row[3]
        day = row[4]
        output.write(row[0] + "," + row[1] +","+year+"-"+month+"-"+day+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+"\n" )
