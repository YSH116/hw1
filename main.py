# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061226.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
Out = []
ls = []
id = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
for i in range(5):
    target_data = list(filter(lambda item: item['station_id'] == id[i], data)) 
    for item in target_data:
        if float(item['WDSD']) == -99.000 or float(item['WDSD']) == -999.000:
            del item
    MAX_ = target_data[0]['WDSD']
    min_ = target_data[0]['WDSD']
    for item in target_data:
        if (item['WDSD'] > MAX_): MAX_ = item['WDSD']
        if (item['WDSD'] < min_): min_ = item['WDSD']
    if len(item['station_id']) < 2: ls = [item['station_id'], 'None']
    else: ls = [item['station_id'], float(MAX_) - float(min_)]  # end = ''
    Out.append(ls)
# Retrive ten data points from the beginning.
# target_data = data[:10]
#=======================================

# Part. 4
#=======================================
# Print result
print(Out)
#========================================