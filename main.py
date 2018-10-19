import os
import pandas as pd
import re
path_input = os.path.join(os.path.expanduser('~'), 'Documents', 'ngo_input.xlsx')
path_output = path3 = os.path.join(os.path.expanduser('~'), 'Documents', 'ngo_output.xlsx')

read = pd.read_excel(path_input, sheetname="Sheet1", header=0)
#for i in range(0,len(read.get_values())):

name_arr=[]
cc_arr=[]
ss_arr=[]
dt_arr=[]
res=[]
def isNaN(num):
    return num != num
def isNotNaN(num):
    return num == num

for i in range(0,len(read.get_values())):
    name = read.get_values()[i][0]
    country_code= read.get_values()[i][1]
    search_string = read.get_values()[i][2]
    date= read.get_values()[i][4]

    result = str(read.get_values()[i][3])
    #get regex values, ie cleaned row values

    print(result)
    regex = "\d?.*res"
    if isNotNaN(regex):
        result1=str(re.findall(regex,result))
        result_final = re.findall('\d',str(result1))
        res.append("".join(result_final))
    else:
        res.append("0")
    name_arr.append(name)
    cc_arr.append(country_code)
    ss_arr.append(search_string)
    dt_arr.append(date)


data_cleaned=pd.DataFrame(columns=["page","country_code","search_string","date","result"])
for i in range(0,len(read.get_values())):
    all=data_cleaned.loc[i]=[name_arr[i],cc_arr[i],ss_arr[i],dt_arr[i],res[i]]
    data_cleaned.append(all)


writer=pd.ExcelWriter(path_output)
data_cleaned.to_excel(writer,"Sheet1")
writer.save()
#print("".join(result_final))
