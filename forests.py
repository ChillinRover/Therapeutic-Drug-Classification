from sklearn.ensemble import RandomForestClassifier
import numpy as np
import random
from sklearn.cross_validation import train_test_split
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from processarFormula import getScoreFormula
from sklearn.metrics import confusion_matrix,recall_score, classification_report

path = 'txt/data'
path1 = 'txt/formulas'
data = np.load(path)
forms = np.load(path1)

#################################
##   Removing repeated values  ##
#################################

equal = []
iPoints = []
for i in range(0, len(data[1,:])):
    x=0
    for j in range(0,len(data[1,:])):
      if data[1,i] == data[1,j] and i!=j:
          x=x+1
          iPoints.append(i)

    equal.append(x)

data = np.delete(data,iPoints,axis = 1)
forms = np.delete(forms,iPoints, axis = 0)

'''
equal = []
for i in range(0, len(data[2,:])):
    x=0
    for j in range(0,len(data[2,:])):
      if data[2,i] == data[2,j] and i!=j:
          x=x+1

    equal.append(x)
'''

data = np.delete(data, (1), axis = 0)


#########################################################
####      Random Forest with Mol. Weight and Mass    ####
#########################################################

'''
target = data[0,:].transpose()
features = data[1:3,:].transpose()
#print features

X_train, X_test, y_train, y_test= train_test_split( features, target, test_size=0.2, random_state=1 )

RFclassifier = RandomForestClassifier(n_estimators = 100)
RFclassifier.fit(X_train,y_train)

pred = RFclassifier.predict(X_test)
sc=RFclassifier.score(X_test,y_test)

print sc
#print y_test
#print pred

# Acc. around 0.20

'''

###################################################
##########         Using the formula    ###########
###################################################

# Building the Formulas Score Matrix
formsFeatures = np.zeros((len(forms),111))

# Get score from formulas
for i in range(0,len(forms)):
    string = forms[i]
    array = getScoreFormula(string)

    for j in range(0,len(array)):
        formsFeatures[i,j] = array[j]


# Running the model several times
max=200
exacs=[]
sensVect = []
exacsbyclass=np.zeros((18,max))
for k in range(0,max):

    target1 = data[0,:].transpose()
    X_train1, X_test1, y_train1, y_test1= train_test_split(formsFeatures, target1, test_size=0.2 )

    RFclassifier1 = RandomForestClassifier(n_estimators = 1000)
    RFclassifier1.fit(X_train1,y_train1)

    pred1 = RFclassifier1.predict(X_test1)
    sc=RFclassifier1.score(X_test1,y_test1)
    sens = recall_score(y_test1,pred1,average = 'macro')
    exacs.append(sc)
    sensVect.append(sens)
    #print sc
    cm = confusion_matrix(y_test1,pred1)

    #plt.show()

    num= 0
    exac = np.zeros((18,1))
    for i in range(0,17):
        num=(cm[i,i])/(float(cm[i,:].sum()))
        exac[i,0]=num

    for j in range(0,17):
        exacsbyclass[j,k] = exac[j,0]

finalExacsVect = np.zeros((18,1))
finalExac = sum(exacs)/float(len(exacs))
finalSens = sum(sensVect)/float(len(exacs))

for i in range(0,17):
    finalExacsVect[i,0] = exacsbyclass[i,:].sum()/float(len(exacs))

plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()
print finalExacsVect
print finalExac
print finalSens