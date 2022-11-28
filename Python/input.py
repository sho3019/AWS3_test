import json 

json_open = open('../sample.json', 'r')
json_load = json.load(json_open)

Data = ["Data1" , "Data2"]
data = []

error_flag = 0
for i in Data:
    if(type(json_load[i]) == int):
        data.append(json_load[i])
    else:
        error_flag = 1

if(error_flag == 0):
    num1 = data[0]
    num2 = data[1]
    operation = json_load['type']


