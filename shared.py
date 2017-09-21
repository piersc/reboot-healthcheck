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

def print_msg(msg, level):
    """Print message formatted based on level, OK, WARN, FAIL"""

    colors = { 'OK': '\033[92m', 'WARN': '\033[1;34m', 'FAIL': '\033[91m', 'DEFAULT': '\033[0m' }
    print("{0}[ {1} ]: {2} {3}".format(colors[level], level, msg, colors["DEFAULT"]))
