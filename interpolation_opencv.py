import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import glob
import os

path = "test"
for img in glob.glob(os.path.join(path,"*.jpg")):
    image = cv2.imread(img)
    t =time.perf_counter()
    result_img = cv2.resize(image, (2952, 2952), interpolation=cv2.INTER_LINEAR)
    # result_img = cv2.resize(image, (2952, 2952), interpolation=cv2.INTER_CUBIC)
    # result_img = cv2.resize(image, (2952, 2952), interpolation=cv2.INTER_LANCZOS4)
    print(time.perf_counter()-t)
    output_name = "result-2/result_"+img.split('/')[-1]
    cv2.imwrite(output_name,result_img)
    print("completely, save image to %s" % output_name)
