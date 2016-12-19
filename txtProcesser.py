import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in


rel_path = "txt/briteTable.txt"
abs_file_path = os.path.join(script_dir, rel_path)
save_path = "txt/briteTablePro.txt"
save_file_path = os.path.join(script_dir, save_path)

'''
f = open(abs_file_path, 'r')
f = f.read()
save = open(save_file_path, 'w')

f = f.split('KEGG DRUG')

writeToDocument = []

for j in range(0, len(f)):
    writeToDocument.append(str(j))
    subList = f[j]
    subList = subList.split()
    for i in range(0, len(subList)):
        string = subList[i]
        if string.startswith('D') and (string.startswith('0', 1) or string.startswith('1', 1)) and len(string)==6:
            writeToDocument.append(string)

    writeToDocument.append('\n')

for x in writeToDocument:
    save.write(x+'\n')


save_path = "txt/briteTablePro.txt"
save_file_path = os.path.join(script_dir, save_path)

f = open(save_file_path, 'r')
f = f.read()

array = f.split('\n')
newArray = [s for s in array if len(s) > 0]
array = [];
for j in newArray:
    if len(j)==1:
        array.append(j)
    if len(j)==2:
        array.append(j)
    if len(j)>2:
        if j[1:].isdigit():
            array.append(j)


save = open(save_file_path, 'w')
for j in array:
    save.write(j+'\n')
'''