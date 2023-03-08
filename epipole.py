import numpy as np
def epipole(u,v,smin,thresh,num_iterations = 1000):
    """ Takes flow (u,v) with confidence smin and finds the epipole using only the points with confidence above the threshold thresh 
        (for both sampling and finding inliers)
        params:
            @u: np.array(h,w)
            @v: np.array(h,w)
            @smin: np.array(h,w)
        return value:
            @best_ep: np.array(3,)
            @inliers: np.array(n,) 
        
        u, v and smin are (h,w), thresh is a scalar
        output should be best_ep and inliers, which have shapes, respectively (3,) and (n,) 
    """

    """
    You can do the thresholding on smin using thresh outside the RANSAC loop here. 
    Make sure to keep some way of going from the indices of the arrays you get below back to the indices of a flattened u/v/smin
    STUDENT CODE BEGINS
    """
    ind_thr = np.where(smin>thresh)
    # print(ind_thr)
    y_temp = np.arange(0, 512*512)//512 - 256
    x_temp = np.arange(0, 512*512)%512 - 256
    x_mat = x_temp.reshape((512,512))
    # print(x_mat)
    y_mat = y_temp.reshape((512,512))
    # print(y_mat)
    # print(y_mat[ind_thr])
    # print("cross")
    # print(X_cross_U)
    
    

    """ 
    STUDENT CODE ENDS
    """

    sample_size = 2

    eps = 10**-2

    best_num_inliers = -1
    best_inliers = None
    best_ep = None

    for i in range(num_iterations): #Make sure to vectorize your code or it will be slow! Try not to introduce a nested loop inside this one
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(0,np.sum((smin>thresh))))
        sample_indices = permuted_indices[:sample_size] #indices for thresholded arrays you find above
        test_indices = permuted_indices[sample_size:] #indices for thresholded arrays you find above

        """
        STUDENT CODE BEGINS
        """
        a = np.zeros((sample_indices.shape[0], 3))
        inliers = []
        for j in range(sample_indices.shape[0]):
            ind = sample_indices[j]
            inliers.append([ind_thr[0][ind]*512 + ind_thr[1][ind]])
            ind_new = tuple([ind_thr[0][ind], ind_thr[1][ind]])
            U1 = [u[ind_new], v[ind_new], 0]
            Xp = [ x_mat[ind_new], y_mat[ind_new], 1]
            a[j] = np.cross(Xp, U1)
        Uu, S, Vt = np.linalg.svd(a)
        ep = Vt[:][-1]




        test_indices_new = tuple([ind_thr[0][test_indices], ind_thr[1][test_indices]])
        U1 = np.vstack((np.vstack((u[test_indices_new], v[test_indices_new])), np.zeros(test_indices.shape[0]))).T
        # print(U1.shape)
        # print("hihihi")
        X = np.vstack((np.vstack((x_mat[test_indices_new], y_mat[test_indices_new])), np.ones(test_indices.shape[0]))).T
        # print(X.shape)
        X_cross_U = np.cross(X, U1).T
        dist = abs(ep @ (X_cross_U))
        
        dis_ind = np.where(dist<eps)[0]
        test_ind = test_indices[dis_ind]
        # print(dis_ind)
        dis_ind_2 = [ind_thr[0][test_ind]*512 + ind_thr[1][test_ind]]
        inliers = np.append(inliers, dis_ind_2)
        """
        STUDENT CODE ENDS
        """

        #NOTE: inliers need to be indices in flattened original input (unthresholded), 
        #sample indices need to be before the test indices for the autograder
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_ep = ep
            best_inliers = inliers
    # print("best")
    # print(best_ep)
    # print(best_inliers)
    # print(best_inliers.shape)
    return best_ep, best_inliers

def get_ep(sample_indices, u, v):
    a = np.zeros((sample_indices.shape[0], 3))
    for j in range(sample_indices.shape[0]):
        ind = sample_indices[j]
        U1 = [u[ind], v[ind], 0]
        Xp = [ (ind%512)-256,  (ind//512)-256, 1]
        a[j] = np.cross(Xp, U1)
    Uu, S, Vt = np.linalg.svd(a)
    e = Vt[:][-1]
    # e = [e[1], e[0], e[2]]
    # e = e/e[2]

    return e



