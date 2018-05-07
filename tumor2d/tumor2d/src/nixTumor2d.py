# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_nixTumor2d')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_nixTumor2d')
    _nixTumor2d = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_nixTumor2d', [dirname(__file__)])
        except ImportError:
            import _nixTumor2d
            return _nixTumor2d
        try:
            _mod = imp.load_module('_nixTumor2d', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _nixTumor2d = swig_import_helper()
    del swig_import_helper
else:
    import _nixTumor2d
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _nixTumor2d.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _nixTumor2d.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _nixTumor2d.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _nixTumor2d.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _nixTumor2d.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _nixTumor2d.SwigPyIterator_equal(self, x)

    def copy(self):
        return _nixTumor2d.SwigPyIterator_copy(self)

    def next(self):
        return _nixTumor2d.SwigPyIterator_next(self)

    def __next__(self):
        return _nixTumor2d.SwigPyIterator___next__(self)

    def previous(self):
        return _nixTumor2d.SwigPyIterator_previous(self)

    def advance(self, n):
        return _nixTumor2d.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _nixTumor2d.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _nixTumor2d.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _nixTumor2d.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _nixTumor2d.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _nixTumor2d.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _nixTumor2d.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _nixTumor2d.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class DoubleVector(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def iterator(self):
        return _nixTumor2d.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _nixTumor2d.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _nixTumor2d.DoubleVector___bool__(self)

    def __len__(self):
        return _nixTumor2d.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _nixTumor2d.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _nixTumor2d.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _nixTumor2d.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _nixTumor2d.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _nixTumor2d.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _nixTumor2d.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _nixTumor2d.DoubleVector_pop(self)

    def append(self, x):
        return _nixTumor2d.DoubleVector_append(self, x)

    def empty(self):
        return _nixTumor2d.DoubleVector_empty(self)

    def size(self):
        return _nixTumor2d.DoubleVector_size(self)

    def swap(self, v):
        return _nixTumor2d.DoubleVector_swap(self, v)

    def begin(self):
        return _nixTumor2d.DoubleVector_begin(self)

    def end(self):
        return _nixTumor2d.DoubleVector_end(self)

    def rbegin(self):
        return _nixTumor2d.DoubleVector_rbegin(self)

    def rend(self):
        return _nixTumor2d.DoubleVector_rend(self)

    def clear(self):
        return _nixTumor2d.DoubleVector_clear(self)

    def get_allocator(self):
        return _nixTumor2d.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _nixTumor2d.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _nixTumor2d.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        this = _nixTumor2d.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _nixTumor2d.DoubleVector_push_back(self, x)

    def front(self):
        return _nixTumor2d.DoubleVector_front(self)

    def back(self):
        return _nixTumor2d.DoubleVector_back(self)

    def assign(self, n, x):
        return _nixTumor2d.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _nixTumor2d.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _nixTumor2d.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _nixTumor2d.DoubleVector_reserve(self, n)

    def capacity(self):
        return _nixTumor2d.DoubleVector_capacity(self)
    __swig_destroy__ = _nixTumor2d.delete_DoubleVector
    __del__ = lambda self: None
DoubleVector_swigregister = _nixTumor2d.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)


def tumor2d_interface(InitialRadius, InitialQuiescentFraction, MaxCellDivisionRate, DivisionDepth, ECMThresholdQuiescence, ECMProductionRate, ECMDegradationRate, EndTime, OutputRate, profileTime, profileDepth, rand_seed):
    return _nixTumor2d.tumor2d_interface(InitialRadius, InitialQuiescentFraction, MaxCellDivisionRate, DivisionDepth, ECMThresholdQuiescence, ECMProductionRate, ECMDegradationRate, EndTime, OutputRate, profileTime, profileDepth, rand_seed)
tumor2d_interface = _nixTumor2d.tumor2d_interface

def tumor2d_default():
    return _nixTumor2d.tumor2d_default()
tumor2d_default = _nixTumor2d.tumor2d_default


