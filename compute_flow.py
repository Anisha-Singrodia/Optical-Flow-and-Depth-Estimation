import numpy as np
import pdb

def flow_lk_patch(Ix, Iy, It, x, y, size=5):
    """
    params:
        @Ix: np.array(h, w)
        @Iy: np.array(h, w)
        @It: np.array(h, w)
        @x: int
        @y: int
    return value:
        flow: np.array(2,)
        conf: np.array(1,)
    """
    """
    STUDENT CODE BEGINS
    """
    # print("x : ", x)
    # print("y : ", y)
    # print("Ix :", Ix.shape)
    # print("Iy :", Iy.shape)
    # print("It :", It.shape)
    start_row = x
    if x-2 >= 0:
        start_row = x-2
    elif x-1 >= 0:
        start_row = x-1    
    end_row = x
    if x+2 < Ix.shape[1]:
        end_row = x+2
    elif x+1 < Ix.shape[1]:
        end_row = x+1
    start_col = y
    if y-2 >= 0:
        start_col = y-2
    elif y-1 >= 0:
        start_col = y-1    
    end_col = y
    if y+2 < Ix.shape[0]:
        end_col = y+2
    elif y+1 < Ix.shape[0]:
        end_col = y+1
    # print("start", start_row)
    # print("end", end_row)
    # print("start", start_col)
    # print("end", end_col)
    # print(Ix[start_col:end_col+1][start_row: end_row+1])
    # A = np.zeros(((end_col - start_col +1)*(end_row-start_row+1),2))
    a = []
    b = []
    for i in range(start_col, end_col+1):#top to bottom
        for j in range(start_row, end_row+1):#left to right
            a.append([Iy[i][j], Ix[i][j]])
            b.append([It[i][j]])
    A = np.array(a)
    B = np.array(b)       
    
    # A = np.hstack((Ix[start_col:end_col+1][start_row: end_row+1], Iy[start_col:end_col+1][start_row: end_row+1]))
    # print(A)
    # print(B)
    # b = It[start_col:end_col+1][start_row: end_row+1]
    f = (np.linalg.lstsq(A, -B, rcond=-1))[0].reshape(2)
    flow = np.array([f[1], f[0]])
    # print(flow)
    conf = np.sqrt(min(np.linalg.eig(np.matmul(A.T, A))[0]))
    # print(conf)
    """
    STUDENT CODE ENDS
    """
    return flow, conf


def flow_lk(Ix, Iy, It, size=5):
    """
    params:
        @Ix: np.array(h, w)
        @Iy: np.array(h, w)
        @It: np.array(h, w)
    return value:
        flow: np.array(h, w, 2)
        conf: np.array(h, w)
    """
    image_flow = np.zeros([Ix.shape[0], Ix.shape[1], 2])
    confidence = np.zeros([Ix.shape[0], Ix.shape[1]])
    for x in range(Ix.shape[1]):
        for y in range(Ix.shape[0]):
            flow, conf = flow_lk_patch(Ix, Iy, It, x, y)
            image_flow[y, x, :] = flow
            confidence[y, x] = conf
    # print(image_flow)
    # print(confidence)
    return image_flow, confidence

    

