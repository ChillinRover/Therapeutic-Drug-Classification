import numpy as np
import urllib as url

'''
extrair uma familia e as suas referencias do kegg
ver peso molecular, formula, massa, estrutura(?)
construir um classificador com essas features e as drugs que interage
dado nova molecula ver com quais esta pode interagir
'''


def famPicker():
    family = '''br08340  Antineoplastics
br08350  Antibacterials
br08351  Antivirals
br08352  Antifungals
br08353  Antiparasitics
br08361  Antidiabetics
br08365  Hypolipidemic agents
br08368  Osteoporosis drugs
br08364  Cardiovascular agents
br08363  Psychiatric agents
br08367  Neurological agents
br08362  Anti-allergic agents
br08366  Antirheumatic and antigout drugs
br08369  Anesthetics, analgesics and anti-inflammatory drugs
br08372  Respiratory agents
br08371  Gastrointestinal agents
br08373  Endocrine and hormonal agents
br08370  Dermatological agents'''

    family = family.split('\n')
    family = [family[i].split('  ') for i in range(0, len(family))]

    print('''1   Antineoplastics
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
18  Dermatological agents''')

    index = int(input('Choose the drug family you want to test the interaction with: '))
    link = family[index - 1][0]
    return link, index

if __name__ == "__main__":
    famPicker()
