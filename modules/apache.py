#!/usr/bin/python

from __future__ import print_function
import os
import subprocess
import shared
from shared import print_msg


__version__ = "1.0"

def is_running():
    """Check if a process httpd is running, and return its path"""

    plist = shared.run_command(["pgrep", "-a", "httpd"])
    return {v.split()[1] for v in plist}

def httpd_config_test(httpd_processes):
    """For each httpd instance, run a configtest"""

    for v in httpd_processes:
        apache_status = (shared.run_command([v, "-S"], return_retcode=True))
        if apache_status[1] != 0:
            print_msg("Apache {0} is reporting a config error".format(v), "FAIL")

def _run():
    httpd_config_test(is_running())
