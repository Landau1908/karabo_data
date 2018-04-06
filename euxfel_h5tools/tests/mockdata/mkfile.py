import h5py
from .base import write_train_ids, write_metadata

def write_file(filename, devices, ntrains, chunksize=200):
    f = h5py.File(filename, 'w')

    write_train_ids(f, 'INDEX/trainId', ntrains, chunksize=chunksize)

    data_sources = []
    for dev in devices:
        dev.ntrains = ntrains
        dev.chunksize = chunksize
        dev.write_control(f)
        dev.write_instrument(f)
        data_sources.extend(dev.datasource_ids())
    write_metadata(f, data_sources, chunksize=chunksize)
