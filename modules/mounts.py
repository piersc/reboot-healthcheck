#!/usr/bin/python

from __future__ import print_function
import os
import subprocess
import shared


__version__ = "1.0"

def get_mounts():
    """Return set of networking listening services"""

    f = open("/proc/mounts")
    for line in f.readlines():
        print(line)
    f.close()

get_mounts()
