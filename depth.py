import numpy as np

def depth(flow, confidence, ep, K, thres=10):
    """
    params:
        @flow: np.array(h, w, 2)
        @confidence: np.array(h, w, 2)
        @K: np.array(3, 3)
        @ep: np.array(3,) the epipole you found epipole.py note it is uncalibrated and you need to calibrate it in this function!
    return value:
        depth_map: np.array(h, w)
    """
    depth_map = np.zeros_like(confidence)

    """
    STUDENT CODE BEGINS
    """
    S = np.array([[1118, 0, 357], [0, 1121, 268], [0, 0 , 1]])
    y_temp = np.arange(0, 512*512)//512
    x_temp = np.arange(0, 512*512)%512
    x_mat = x_temp.reshape((512,512))
    # print(x_mat)
    y_mat = y_temp.reshape((512,512))
    ep_new = np.matmul(np.linalg.inv(K), ep)
    for i in range(confidence.shape[0]):
        for j in range(confidence.shape[1]):
            if confidence[i][j] > thres:
                flow1 = flow[i][j][0]/357
                flow2 = flow[i][j][1]/268
                X = [x_mat[i][j], y_mat[i][j], 1]
                X_new = np.matmul(np.linalg.inv(K), X)
                term1 = (X_new[0] - ep_new[0])**2 + (X_new[1] - ep_new[1])**2
                term2 = flow1**2 + flow2**2
                depth_map[i][j] = np.sqrt(term1/term2)
    """
    STUDENT CODE ENDS
    """

    truncated_depth_map = np.maximum(depth_map, 0)
    valid_depths = truncated_depth_map[truncated_depth_map > 0]
    # You can change the depth bound for better visualization if your depth is in different scale
    depth_bound = valid_depths.mean() + 10 * np.std(valid_depths)
    # print(f'depth bound: {depth_bound}')

    truncated_depth_map[truncated_depth_map > depth_bound] = 0
    truncated_depth_map = truncated_depth_map / truncated_depth_map.max()
    

    return truncated_depth_map
