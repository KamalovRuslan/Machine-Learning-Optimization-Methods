import numpy as np
from sklearn.datasets import load_svmlight_file
from logistic import LossFuncSum
from optim import sgd, svrg
from logistic import predict_labels

def calc_error(x):
    b_hat = predict_labels(A_test, x)
    err = np.mean(b_test != b_hat)
    return err

A_train, b_train = load_svmlight_file('E:\Programms\Py\MOMO\Data\w5a.txt')

fsum = LossFuncSum(A_train, b_train, reg_coef=1/A_train.shape[0])

x0 = np.zeros(A_train.shape[1])

x_sgd, hist_sgd = sgd(fsum, x0, n_iters=10*fsum.n_funcs, step_size=0.01, trace=True)
x_svrg, hist_svrg = svrg(fsum, x0, n_stages=2, trace=True)

A_test, b_test = load_svmlight_file('E:\Programms\Py\MOMO\Data\w5a.t', n_features=A_train.shape[1])

print('Initial error: %g' % calc_error(x0))
print('SGD result: %g' % calc_error(x_sgd))
print('SVRG result: %g' % calc_error(x_svrg))
