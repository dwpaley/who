from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import itertools
import make_vectors
import individual
import numpy as np


def lda_performance(train, test, standardize=False, shrinkage=False, 
        interact_terms=1):
    '''Note that train and test are lists of Creatures because we need to 
    choose whether or not to standardize their position and orientation
    '''

    if standardize:
        for c in train: c.standardize()
        for c in test: c.standardize()

    trainb = make_vectors.make_bunch(train)
    testb = make_vectors.make_bunch(test)
    (x_train,x_test,y_train,y_test) = (trainb.data, testb.data, trainb.target, 
        testb.target)

    pol1 = PolynomialFeatures(interact_terms)
    pol2 = PolynomialFeatures(interact_terms)
    x_train_poly = pol1.fit_transform(x_train)
    x_test_poly = pol2.fit_transform(x_test)

    shrinkage = 'auto' if shrinkage else False
    lda = LinearDiscriminantAnalysis(solver='lsqr', shrinkage=shrinkage)
    lda.fit(x_train_poly, y_train)
    return lda.score(x_test_poly, y_test)

def plot_h_params(start, end, step):
    options = list((p,q,r) for p,q,r in itertools.product(
        [False, True], [False, True], [1,2,3]))
    x,y = [],[]
    test = [individual.Creature() for i in range(1000)]
    for size in range(start, end, step):
        train = [individual.Creature() for i in range(size)]
        x.append(size)
        y.append([lda_performance(train, test, standardize=p, shrinkage=q, 
            interact_terms=r) for p,q,r in options])


    y = np.array(y)
    for n in range(len(y[0])):
        plt.plot(x,y[:,n])

    plt.legend(options)
    plt.show()



