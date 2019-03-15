import h5py
import csv

filename = '1541962108935000000_167_838.h5'



#explores all branches of the directory tree and identifies all of the datasets in the file

def traverse_datasets(hdf_file):

    def h5py_dataset_iterator(g, prefix=''):
        for key in g.keys():
            item = g[key]
            path = f'{prefix}/{key}'
            if isinstance(item, h5py.Dataset): # test for dataset
                yield (path, item)
            elif isinstance(item, h5py.Group): # test for group (go down)
                yield from h5py_dataset_iterator(item, path)

    with h5py.File(hdf_file, 'r') as f:
        for path, _ in h5py_dataset_iterator(f):
            yield path



#creates a csv file which records the names of all of the groups and datasets, and includes the size, shape and type of data in each dataset

with open('details_of_groups_and_datasets.csv', mode='w') as csv_file:
    fieldnames = ['Groups and Datasets','Type', 'Shape', 'Size']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    with h5py.File(filename, 'r') as f:
        for dset in traverse_datasets(filename):
            try:
                writer.writerow({'Groups and Datasets': dset, 'Type':f[dset].dtype, 'Shape': f[dset].shape,'Size': f[dset].size})
            except Exception:
                pass
