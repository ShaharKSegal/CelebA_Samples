import os
import shutil

import numpy as np
import pandas as pd

src = 'img_align_celeba'
dst = 'celeba_identity_samples'

df = pd.read_csv('identity_CelebA.txt', sep=' ', names=['image_name', 'celeb_id'])
#filter identities with less than 5 images
sample_size = 5
df_filtered = df.groupby("celeb_id").filter(lambda x: len(x) >= sample_size).reset_index(drop=True)
#samples 5 images per identity
sample_at_random_fn = lambda obj: obj.loc[np.random.choice(obj.index, sample_size, False), :]
df_sampled = df_filtered.groupby("celeb_id").apply(sample_at_random_fn)

for _, row in df_sampled.iterrows():
    image_name, celeb_id = row['image_name'], row['celeb_id']
    shutil.copyfile(os.path.join(src, image_name), os.path.join(dst, f"{celeb_id}_{image_name}"))

