import numpy as np
import h5py
# from numba import jit

kvs = []
with open('title_id_dict.txt','r') as f:
  for line in f:
    c = line.split(' ')
    id = int(c[1].strip())
    title = c[0].strip()
    kvs.append((id, title))
kvs.sort(key=lambda pair: pair[0])
keys, values = list(zip(*kvs))
del kvs

count = 0
id2newid = {}
for key in keys:
  if key in id2newid:
    print('dup found!')
  id2newid[key] = count
  count += 1

with open('newid2title.txt', 'w') as f:
  for key, value in zip(range(len(values)), values):
    f.write('%i %s\n' % (key, value) )
del keys
del values

# with open('id2newid.txt', 'w') as f:
#   for id, newid in id2newid.items():
#     f.write('%i %i\n' % (id, newid))

# # @jit
# def update_links_ids(id2newid):
#   src = h5py.File('pagelinks_list.h5', 'r')
#   lst = src['pagelinks_list'][()]
#   src.close()
#   for i in range(len(lst)):
#     lst[i,0] = id2newid[lst[i,0]]
#     lst[i,1] = id2newid[lst[i,1]]
#   dst = h5py.File('newpagelinks_list.h5', 'w')
#   dst.create_dataset('pagelinks_list', data=lst, compression='gzip')
#   dst.close()
# update_links_ids(id2newid)
