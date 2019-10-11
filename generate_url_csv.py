import csv
import os

import numpy as np

src = "celeba_identity_samples"
url_prefix = "https://raw.githubusercontent.com/ShaharKSegal/CelebA_Samples/master/celeba_identity_samples/"
csv_list = [f"{url_prefix}{filename}" for filename in sorted(os.listdir(src), key= lambda x: int(x.split('_')[0]))]
np.savetxt("celeba_identity_samples.csv", csv_list, delimiter=",", fmt='%s', header='image_url')
