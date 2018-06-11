# ref:　https://www.cnblogs.com/fangbei/p/8409110.html
import numpy as np


def ForwardAlgo(A, B, Pi, O):
    N = A.shape[0]
    M = A.shape[1]
    H = O.shape[1]

    sum_alpha_1 = np.zeros((M, N))
    alpha = np.zeros((N, H))
    r = np.zeros((1, N))
    alpha_1 = np.multiply(Pi[0, :], B[:, O[0, 0] - 1])

    alpha[:, 0] = np.array(alpha_1).reshape(1, N)

    for h in range(1, H):
        for i in range(N):
            for j in range(M):
                sum_alpha_1[i, j] = alpha[j, h - 1] * A[j, i]
            r = sum_alpha_1.sum(1).reshape(1, N)
            alpha[i, h] = r[0, i] * B[i, O[0, h] - 1]
    p = alpha.sum(0).reshape(1, H)
    P = p[0, H - 1]
    print("alpha matrix: \n %r" % alpha)
    print("Observation Probability: \n %r" % P)
    return alpha, P


A = np.array([[.5,.2,.3],[.3,.5,.2],[.2,.3,.5]])
B = np.array([[.5,.5],[.4,.6],[.7,.3]])
Pi = np.array([[.2,.4,.4]])
O = np.array([[1,2,1]])
ForwardAlgo(A, B, Pi, O)