# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:14:46 2016

@author: etu2016
"""

print(__doc__)
#importation de donnees
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt
iris_data = datasets.load_iris()
X = iris_data.data[:,:2]
y = iris_data.target

h = .02

parametres = {"kernel":['linear','poly','rbf','sigmoid'],"C":[0.1,0.5,1.0,2.0,10.0]}

#classifieur à utiliser
svmc = SVC()
#instanciation de la recherche
grille = GridSearchCV(estimator=svmc,param_grid=parametres,scoring="accuracy") #lancer l'exploration
resultats = grille.fit(X,y)

#MEILLEURS PARAMETRES
print(resultats.best_params_)

C = 0.1

kernel = 'poly'

poly_svc = SVC(kernel=kernel , degree=3, C=C).fit(X, y)



x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

Z = poly_svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

title = ['svm with polynomial (degree 3 ) kernel']

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())
plt.title(title)

plt.savefig('iris classified svm kernel_polynomial' , format = 'pdf')