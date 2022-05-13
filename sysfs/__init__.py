#!/usr/bin/python -tt

"""
Simplistic Python SysFS interface.

Shamelessly stolen from:
    http://stackoverflow.com/questions/4648792/

Usage::
    from sysfs import sys

    for bdev in sys.block:
        print bdev, str(int(bdev.size) / 1024 / 1024) + 'M'
"""

__all__ = ['sys', 'Node']
__license__ = "MIT"

from pathlib import Path, PosixPath

class Node(object):
    __slots__ = ['_path_', '__dict__']

    def __init__(self, path: str='/sys'):
        self._path_ = Path(path).resolve()
        if not str(self._path_).startswith('/sys') and Path(self._path_).is_dir():
            raise RuntimeError('Using this on non-sysfs files is dangerous!')

        self.__dict__.update(dict.fromkeys([_ for _ in self._path_.iterdir()]))

    def __repr__(self):
        return '<sysfs.Node "%s">' % self._path_

    def __str__(self):
        return self._path_.name

    def __setattr__(self, name: str, val):
        if name.startswith('_'):
            return object.__setattr__(self, name, val)

        path = self._path_ / name
        if path.is_file():
            with path.open('w') as fp:
                fp.write(val)
        else:
            raise RuntimeError('Cannot write to non-files.')

    def __getattribute__(self, name):
        if name.startswith('_'):
            return object.__getattribute__(self, name)

        path = self._path_ / name
        if path.is_file():
            with path.open('r') as fp:
                return fp.read().strip()
        elif path.is_dir():
            return Node(path)

    def __setitem__(self, name, val):
        return setattr(self, name, val)

    def __getitem__(self, name):
        return getattr(self, name)

    def __iter__(self):
        return iter(getattr(self, name) for name in self._path_.iterdir())


sys = Node()

# vim:set sw=4 ts=4 et:
# -*- coding: utf-8 -*-
