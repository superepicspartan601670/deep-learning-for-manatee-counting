import h5py
import numpy as np
import matplotlib.pyplot as plot
import os

path = r"../../dataset/ground_truth_anisotropy_1_4/above0-07-30.h5"
path1 = r"../../dataset/ground_truth_dot/above0-07-30.h5"
path2 = r"../../dataset/ground_truth_line/above0-07-30.h5"
path3 = r"../../dataset/ground_truth_circle/above0-07-30.h5"

path4 = r"../../dataset/ground_truth_anisotropy_1_4/B.h5"
path5 = r"../../dataset/ground_truth_dot/B.h5"
path6 = r"../../dataset/ground_truth_line/B.h5"
path7 = r"../../dataset/ground_truth_circle/B.h5"

path8 = r"../../dataset/ground_truth_anisotropy_1_4/C.h5"
path9 = r"../../dataset/ground_truth_dot/C.h5"
path10 = r"../../dataset/ground_truth_line/C.h5"
path11 = r"../../dataset/ground_truth_circle/C.h5"

with h5py.File(path5, "r") as hf:
    p = np.array(hf['density'])

plot.imshow(p)
plot.show()