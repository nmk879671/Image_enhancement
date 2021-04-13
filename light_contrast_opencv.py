import cv2
import numpy as np
import time
import glob
import os
 
path = "test"
for img in glob.glob(os.path.join(path,"*.jpg")):
    image = cv2.imread(img)
    # dst = modify_contrast_and_brightness(img)
    # dst = np.uint8(np.clip((1.5 * img + 100), 0, 255))
    dst = np.uint8(np.clip((1.2 * image + 10), 0, 255))
    output_name = "result/con_bri_"+img.split('/')[-1]
    cv2.imwrite(output_name,dst)

   
