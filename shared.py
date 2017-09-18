#!/usr/bin/python
"""Shared code available to modules"""

import subprocess


def run_command(cmd):
    """Run executable and return stdout output"""

    try:
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except OSError, e:
        print("Error running {}: {}".format(cmd, e))

    return proc.stdout.readlines()
