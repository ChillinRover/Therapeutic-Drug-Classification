from sklearn.cluster import KMeans
import numpy as np
import linecache
from numpy import ndarray

# First, it is necessary to treat the dBrite data to be represented in families
'''
1   Antineoplastics
2   Antibacterials
3   Antivirals
4   Antifungals
5   Antiparasitics
6   Antidiabetics
7   Hypolipidemic agents
8   Osteoporosis drugs
9   Cardiovascular agents
10  Psychiatric agents
11  Neurological agents
12  Anti-allergic agents
13  Antirheumatic and antigout drugs
14  Anesthetics, analgesics and anti-inflammatory drugs
15  Respiratory agents
16  Gastrointestinal agents
17  Endocrine and hormonal agents
18  Dermatological agents
'''

data = open('dBrite.txt','r')
family = 0
familyArray = []
drug = []
mass = []
mol = []
form = []

for i, line in enumerate(data):
    if line.strip() == '-----':
        family=family+1

    if line[0] == 'D':
        drug.append(line.strip('\n'))
    elif line.split(' ')[0] == 'FORMULA':
        formulas = line.strip('\n').split()[1 :]
        formulas = ''.join(formulas)
        form.append(formulas)

    elif line.split(' ')[0] == 'EXACT_MASS':
        mass.append(line.strip('\n').split(' ')[2])
        familyArray.append(family)

    elif line.split(' ')[0] == 'MOL_WEIGHT':
        mol.append(line.strip('\n').split(' ')[2])

data.close()

drug = np.array(drug)
mass = np.array(mass)
mol = np.array(mol)
familyArray = np.array(familyArray)
form = np.array(form)
# print len(drug),' ',len(mass),' ',len(mol),' ',len(familyArray),' ',len(form)

''' Data stacked in vector -
Family
Drug name
Exact Mass
Mol Weight

'''

finalData=np.vstack((familyArray,drug,mass,mol))
#finalData = np.asarray([finalData])

np.set_printoptions(threshold='nan')
print(form)
np.ndarray.dump(finalData,'data')
np.ndarray.dump(form,'formulas')
# np.savetxt('data.txt',finalData,)




