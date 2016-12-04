###
# Model run for a single point retrieval
#  python GetData.py AZ [h,f] [Omit number of years]
#
###

###
# Makeflow model run 
#   Assuming variables: $State, $ForH, $Years
#
#   For each id point in the area of interest
#
#   id123.csv: GetData.py GetMoLS.sh RunModel.py
#       bash ./GetMoLS.sh
#       python GetData.py ${State} ${ForH} ${Years}
#       python runModel.py 
###
FigureCount=$1

# Assuming getData happened before
rm Makeflow.makeflow

for ((i=0; i<${FigureCount}; i++)) do
    echo "id${i}.csv: id${i}.csv GetMoLS.sh RunModel.py" >> Makeflow.makeflow
    echo "    bash ./Get_MoLS.sh" >> Makeflow.makeflow
    echo "    python RunModel.py id${i}.csv" >> Makeflow.makeflow
done



###
# Combine and parse the data, setup for visualization
#  bash ./combineData.sh
#  python ./Visualization.py
#
#
###
