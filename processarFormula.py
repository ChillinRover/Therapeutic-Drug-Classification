import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
import urllib
import re
import numpy as np

'''
save_path = "txt/soFormula.txt"
save_file_path = os.path.join(script_dir, save_path)

f = open(save_file_path, 'r')
f = f.read()
f = f.split('-----')

save_path2 = "txt/elements.txt"
save_file_path2 = os.path.join(script_dir, save_path2)

f2 = open(save_file_path2, 'r')
f2 = f2.read()
f2 = f2.split('\n')

elementsVec = []

for j in range(0, len(f2), 3):
    f2[j] = f2[j].strip()
    elementsVec.append(f2[j])

formulasVec = []
numFormulasVec = []

for l in range(0,len(f)):
    formulasVec.append(['-----'])
    j = f[l]
    j = j.split('\n')
    for k in j:
        if len(k)>0:
            spliter = re.findall('[A-Z][^A-Z]*', k)
            formulasVec.append(spliter)


for j in range(0, len(formulasVec)):
    placehold = []
    t = formulasVec[j]
    if len(t):
        for k in t:
            if ('.') not in k:
                if ('(') not in k:
                    u = re.split('\d*\D+', k)
                    placehold.append(u)


            #numFormulasVec.append(u[1])
    numFormulasVec.append(placehold)
'''


elementsPath = os.path.join(script_dir,"txt/elementos.txt")
elementos = []

f = open(elementsPath)
f = f.read()
f = f.split('\n')
for j in f:
    j = j.split()
    elementos.append(j[3])


def getScoreFormula(formula):
    '''
    This function receives a formula has input and returns
    a vector that represents the number of elements
    '''

    elementsPath = os.path.join(script_dir, "txt/elementos.txt")
    elementos = []

    f = open(elementsPath)
    f = f.read()
    f = f.split('\n')

    for j in f:
        j = j.split()
        elementos.append(j[3])

    mult = 1
    formula = formula.split('.')
    counter = 0

    if formula[0].startswith('(') and formula[0].endswith(('0','1','2','3','4','5','6','7','8','9')):
        formula = formula[0]
        mult = int(formula[-1])
        formula = formula[:-1]
        formula = formula.replace('(', '')
        formula = formula.replace(')', '')
        counter = 1

    elif formula[0].startswith('('):
        mult = int(formula[1][-1])
        formula = formula[0]
        formula = formula[:-1]
        formula = formula.replace('(', '')
        formula = formula.replace(')', '')
        counter = 1

    if counter == 0:
        formula = formula[0]

    formulaArray =  re.findall('[A-Z][^A-Z]*', formula)
    score = np.zeros(len(elementos))

    for j in formulaArray:
        u = re.split('\d*\D+', j)
        if len(u[1])==0:
            u[1] = 1
            for k in range(0, len(elementos)):
                if j == elementos[k]:
                    score[k] = float(u[1])
        else:
            for k in range(0, len(elementos)):
                if j[:-len(u[1])] == elementos[k]:
                    score[k] = u[1]

    return score*mult


if __name__ == '__main__':
    score= getScoreFormula('(C12H14NO5S.Na)2.5H2O')
    print score