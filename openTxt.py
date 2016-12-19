import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "txt/briteTable.txt"
abs_file_path = os.path.join(script_dir, rel_path)


f = open(abs_file_path, 'r')
f = f.read()

f = f.split('KEGG DRUG')

x = f[2]
x = x.split()
for i in range(0, len(x)):
    string = x[i]
    if string.startswith('D') and (string.startswith('0', 1) or string.startswith('1',1)) and len(string)>3:
        print string



def drugsOfFamily(index):
    tableOfIndex = f[index]

    return