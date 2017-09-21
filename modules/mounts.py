#!/usr/bin/python

from __future__ import print_function
import os
import subprocess
import shared
from shared import print_msg


__version__ = "1.0"

def get_mounts():
    """Get list of mounted filesystems and return a list of tuples
    containing (device, mountpoint)"""

    # Ignore these mount device types
    ignore = [ "cgroup", "sysfs", "securityfs", "devpts", "udev", "proc", 
               "pstore", "efivarfs", "systemd-1", "mqueue", "hugetlbfs",
               "debugfs", "fusectl", "tracefs", "gvfsd-fuse", "tmpfs",
               "rootfs", "selinuxfs", "none", "binfmt_misc", "devtmpfs",
               "configfs" ]

    procmounts = open("/proc/mounts").readlines()
    return [(f.split()[0], f.split()[1]) for f in procmounts if f.split()[0] not in ignore]

def get_fstab():
    """Parse fstab for filesystems that get mounted at boot time"""

    fstabmounts = open("/etc/fstab").readlines()
    fstabentries = [(f.split()[0], f.split()[1]) for f in fstabmounts if len(f) > 2 and not f.split()[0].startswith("#")]

    # Convert UUIDs to block devices
    for i, v in enumerate(fstabentries):
        if v[0].startswith("UUID"):
            uuid = (v[0].split("=")[1])
            fstabentries[i] = (shared.run_command(['blkid', '-U', uuid])[0].rstrip(), v[1])

    return fstabentries

def compare_mounts(current, fstab):
    for mount in current:
        if mount in fstab:
            print_msg("{0} {1} in fstab".format(mount[0], mount[1]), "OK")
        else:
            print_msg("{0} {1} not in fstab".format(mount[0], mount[1]), "WARN")

def _run():
    mounts = get_mounts()
    fstab = get_fstab()
    compare_mounts(mounts, fstab)
