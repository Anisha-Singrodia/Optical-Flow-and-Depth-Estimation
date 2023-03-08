import numpy as np

def compute_planar_params(flow_x, flow_y, K,
                                up=[256, 0], down=[512, 256]):
    """
    params:
        @flow_x: np.array(h, w)
        @flow_y: np.array(h, w)
        @K: np.array(3, 3)
        @up: upper left index [i,j] of image region to consider.
        @down: lower right index [i,j] of image region to consider.
    return value:
        sol: np.array(8,)
    """
    """
    STUDENT CODE BEGINS
    """
    focal_x = K[0][0]
    focal_y = K[1][1]
    A = []
    B = []
    for i in range(up[0], down[0]):
        for j in range(up[1], down[1]):
            x = np.array([j, i, 1])
            x_new = np.matmul(np.linalg.inv(K), x)
            i1 = x_new[0]
            j1 = x_new[1]
            A.append([i1**2, i1*j1, i1, j1, 1, 0, 0, 0])
            A.append([i1*j1, j1*j1, 0, 0, 0, j1, i1, 1])
            B.append(flow_x[i][j]/focal_x)
            B.append(flow_y[i][j]/focal_y)
            
    A = np.array(A)
    B = np.array(B)
    sol = np.linalg.lstsq(A, B, rcond=-1)[0]

    """
    STUDENT CODE ENDS
    """
    return sol
    
