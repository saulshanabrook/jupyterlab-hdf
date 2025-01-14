""" jupyterLab_hdf : HDF5 api for Jupyter/Jupyterlab

Copyright (c) Max Klein.
Distributed under the terms of the Modified BSD License.
"""

import h5py

from .baseHandler import HdfBaseManager, HdfBaseHandler
from .util import dsetContentDict, dsetDict, groupDict, uriJoin, uriName

__all__ = ['HdfContentsManager', 'HdfContentsHandler']

## manager
class HdfContentsManager(HdfBaseManager):
    """Implements HDF5 contents handling
    """
    def _get(self, f, uri, row, col):
        obj = f[uri]

        if isinstance(obj, h5py.Group):
            return [(groupDict if isinstance(val, h5py.Group) else dsetDict)
                        (name=name, uri=uriJoin(uri, name))
                    for name,val in obj.items()]
        else:
            return dsetDict(
                name=uriName(uri),
                uri=uri,
                content=dsetContentDict(obj, row, col),
            )


## handler
class HdfContentsHandler(HdfBaseHandler):
    """A handler for HDF5 contents
    """
    managerClass = HdfContentsManager
