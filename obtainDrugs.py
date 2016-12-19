import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
import urllib


save_path = "txt/briteTablePro.txt"
save_file_path = os.path.join(script_dir, save_path)

save_path2 = "txt/dBrite.txt"
save_file_path2 = os.path.join(script_dir, save_path2)

'''
f = open(save_file_path, 'r')
f = f.read()

f2 = open(save_file_path2, 'w')

array = []

f = f.split('-----')

for j in f:
    array.append(j)

for i in range (0, len(array)):
    array[i] = array[i].split('\n')

for i in range (0, len(array)):
    array[i][:] = array[i][1:]

array = array[1:]

for i in range(0, len(array)):
    array[i]= array[i][:-2]


for j in array:
    print j


dArray = []

for k in range(0, len(array)):
    print 'WORKING....'
    count1 = 0;
    for i in array[k]:
        if count1 == 0:
            dArray.append('-----')
            count1 +=1
        url = urllib.urlopen('http://rest.kegg.jp/get/' + i)
        url = url.read()
        url = url.split('\n')
        count = 0;
        for j in url:
            if j.startswith('FOR') or j.startswith('EXACT') or j.startswith('MOL'):
                if count == 0:
                    dArray.append(i)
                    count +=1
                dArray.append(j)

for kk in dArray:
    f2.write(kk+'\n')
'''

