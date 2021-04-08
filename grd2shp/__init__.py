from .grd2shp import Grd2Shp, getaverage
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__all__ = ['Grd2Shp', 'getaverage', ]
