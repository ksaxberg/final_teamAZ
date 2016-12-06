import sys
import os

arg = sys.argv[1]

files = os.listdir(arg)

with open("Makeflow.makeflow", "w") as f:
    run = ""
    for line in files:
        if (line.endswith(".csv")): 
            run = "{0}: {1} GetMoLS.sh RunModel.py\n".format(line.strip(), os.path.join(arg, line.strip()))
            run += "    bash ./Get_MoLS.sh\n"
            run += "    python RunModel.py {0}\n\n".format(line.strip())
            f.write(run)
