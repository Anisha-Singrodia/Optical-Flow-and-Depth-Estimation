# Optical-Flow-and-Depth-Estimation

First, computed the spatiotemporal derivatives for every pixel of the given image. Each time the directions orthogonal to the differentiation direction are smoothed. Then computed the two flow components (u, v) for each pixel as well as a confidence value.
Assumed that the optical flow is constant in a local neighbourhood of 5x5 pixels, so the flow can be computed as a 25x2 linear system consisting of 25 equations Ix*u+Iy*v+It =0 where(Ix,Iy,It) are the spatiotemporal derivatives at every pixel. The smallest singular value smin of the system is used as a confidence measure. 

|![flow_1](https://user-images.githubusercontent.com/68454938/211146812-c975ea15-001b-4daf-bb7d-bf3e14afd6bf.png)
|:--:| 
| *Flow vectors for threshold of 1* |

|![flow_10](https://user-images.githubusercontent.com/68454938/211146797-40c29454-4681-4173-9761-b110dc04603d.png)
|:--:| 
| *Flow vectors for threshold of 10* |
  
|![flow_30](https://user-images.githubusercontent.com/68454938/211146805-8770c9a0-225c-4c97-a145-c8630a145222.png)
|:--:| 
| *Flow vectors for threshold of 30* |
  
After using RANSAC and thresholding the flow vectors with higher than smin confidence level, the epipoles are found.

|![epipole_1](https://user-images.githubusercontent.com/68454938/211146825-244176cb-9ddf-4a88-99b5-b8d4d8a81fa6.png)
|:--:| 
| *Epipoles for threshold of 1* |
  
|![epipole_10](https://user-images.githubusercontent.com/68454938/211146829-420d6bbb-8eb2-43e8-b403-1d1123ae5e2b.png)
|:--:| 
| *Epipoles for threshold of 10* |
  
|![epipole_30](https://user-images.githubusercontent.com/68454938/211146831-128a6d03-7046-441b-8de8-d1f0154e275a.png)
|:--:| 
| *Epipoles for threshold of 30* |

The epipoles are in the direction of the optical flow vectors. So, the number of inliers decreases as we increase the threshold.

Depth at every pixel for which flow exists is computed using the given pixel flow, confidence, epipole, and intrinsic parameters.
|![depth_1](https://user-images.githubusercontent.com/68454938/211146856-beac0359-1565-47c2-b6a3-3f276238e663.png)
|:--:| 
| *Depth for threshold of 1* |

|![depth_10](https://user-images.githubusercontent.com/68454938/211146859-05dd5f91-5536-4b10-8392-8c5575373a96.png)
|:--:| 
| *Depth for threshold of 10* |
  
|![depth_30](https://user-images.githubusercontent.com/68454938/211146862-8a34a890-95b2-443f-a04e-63aa1562dabb.png)
|:--:| 
| *Depth for threshold of 30* |
  
