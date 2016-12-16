from timeit import default_timer as timer
from MoLS import Run_Model
import os
import shutil

singleYear = "./singleYear.csv"
fiveYear = "./fiveYear.csv"
yearTimings = []
for i in range(5):
    newFileName = singleYear[:-4]+str(i)+".csv"
    shutil.copyfile(singleYear, newFileName)
    start = timer()
    Run_Model.model(os.getcwd(), newFileName[:-4])
    end = timer()
    yearTimings.append(end-start)
newFiveYearName = fiveYear[:-4]+"1"+".csv"
shutil.copyfile(fiveYear, newFiveYearName) 
start = timer()
Run_Model.model(os.getcwd(), newFiveYearName[:-4])
end = timer()
fiveYearTime = end-start
with open("timings.csv", "w") as f:
    for i in range(len(yearTimings)):
        f.write(str(yearTimings[i])+"\n")
    f.write(str(fiveYearTime)+"\n")
