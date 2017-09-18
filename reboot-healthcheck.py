#!/usr/bin/python

from __future__ import print_function
from os import listdir
from os.path import isfile, join
import importlib
import sys


def load_modules():
    """Import (i.e. run) all modules, and return list of them"""

    sys.path.append("./modules")
    modules = [f.split(".py")[0] for f in listdir("modules") if isfile(join("modules", f))]
    return [importlib.import_module(m) for m in set(modules) if not "__init__" in m and not m.startswith(".")]

def list_modules(modules):
    """Print module name and version"""
    print("\nRan these modules:")
    [print("- {0} {1}".format(m.__name__, m.__version__)) for m in modules]

plugins = load_modules()
list_modules(plugins)
