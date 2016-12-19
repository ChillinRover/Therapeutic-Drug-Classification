from sklearn.ensemble import RandomForestClassifier
import numpy as np
import random
from sklearn.cross_validation import train_test_split
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from processarFormula import getScoreFormula
from sklearn.metrics import confusion_matrix,recall_score, classification_report,roc_curve,auc
from random import randint

path = 'txt/data'
path1 = 'txt/formulas'
data = np.load(path)
forms = np.load(path1)

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


count = 0
for i in range(0, len(data[0, :])):
    if data[0, i] != '2':
        count = count + 1
        data[0, i] = 0
    else:
        data[0,i] = 1

#print count
#print(len(data[1,:])-count)


rands = random.sample(range(1011),900)
deletes = []
for i in range(0,len(rands)):
    if data[0,rands[i]] == '1':
        deletes.append(i)

rands = np.delete(rands,deletes,axis = 0)
data = np.delete(data,rands,axis = 1)
forms = np.delete(forms,rands,axis = 0)

formsFeatures = np.zeros((len(forms),111))
for i in range(0,len(forms)):
    string = forms[i]
    array = getScoreFormula(string)

    for j in range(0,len(array)):
        formsFeatures[i,j] = array[j]


#print formsFeatures
#print data[0,:]
data[0,:].astype(int)
exacs=[]
sensVect = []
numberOfEstimators = []

#numberOfEstimators.append(i)
target = data[0, :].transpose()
X_train1, X_test1, y_train1, y_test1 = train_test_split(formsFeatures, target, test_size=0.3)

RFclassifier1 = RandomForestClassifier(n_estimators=250)
RFclassifier1.fit(X_train1, y_train1)

pred1 = RFclassifier1.predict(X_test1)
sc = RFclassifier1.score(X_test1, y_test1)
#sens = recall_score(y_test1, pred1)
#exacs.append(sc)

#plt.figure()
#plt.plot(numberOfEstimators , exacs)
#plt.show()


fpr = dict()
tpr = dict()
roc_auc = dict()
y_test1 = map(int , y_test1)
pred1 = map(int , pred1)

fpr, tpr, _ = roc_curve(y_test1, pred1, pos_label = None)
roc_auc = auc(fpr, tpr)

print sc
cm = confusion_matrix(y_test1,pred1)
print cm
plt.figure()
lw = 2
plt.plot(fpr,tpr,color='darkorange',lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()

py


#plt.matshow(cm)
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()