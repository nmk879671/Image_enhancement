import cv2
import numpy as np
import math
import time
import os

def bilinear(src_img):   

    img_height=src_img.shape[0]
    img_width=src_img.shape[1]
    channel=src_img.shape[2]

    
    new_img=np.zeros([img_height,img_width,channel],dtype=np.uint8)

    for i in range(0,img_width):
        for j in range(0,img_height):
            if (i >= 0 and i < img_width and j >= 0 and j < img_height):
                src_x, src_y = i, j
                src_x_0 = int(src_x)
                src_y_0 = int(src_y)
                src_x_1 = min(src_x_0 + 1, img_width - 1)
                src_y_1 = min(src_y_0 + 1, img_height - 1)
                
                value0 = (src_x_1 - src_x) * src_img[src_y_0, src_x_0, :] + (src_x - src_x_0) * src_img[src_y_0, src_x_1, :] 
                value1 = (src_x_1 - src_x) * src_img[src_y_1, src_x_0, :] + (src_x - src_x_0) * src_img[src_y_1, src_x_1, :]
                
                new_img[j,i,:] = ((src_y_1 - src_y) * value0 + (src_y - src_y_0) * value1 + 0.5).astype('uint8')
    return new_img


if __name__ == "__main__":
    img = cv2.imread('test/test.JPG')
    
    t = time.perf_counter()

    new_img = bilinear(img)
    print(time.perf_counter()-t)

    cv2.imwrite('Panorama.jpg',new_img)
