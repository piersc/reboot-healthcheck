#!/usr/bin/python

from __future__ import print_function
import os
import shared
from shared import print_msg

__version__ = "1.0"

def get_screen_tmux_sessions():
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

    for pid in pids:
        try:
            cmdline = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
            if cmdline.startswith("screen"):
                print_msg("screen is running, PID {0}".format(pid), "WARN")
            elif cmdline.startswith("tmux"):
                print_msg("tmux is running, PID {0}".format(pid), "WARN")
        except IOError: # proc has already terminated
            continue

get_screen_tmux_sessions()
