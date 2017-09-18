#!/usr/bin/python

from __future__ import print_function
import os
import subprocess
import shared


__version__ = "1.0"

def get_listening_services():
    """Return set of networking listening services"""

    netstat = shared.run_command(['/bin/netstat', '-tlnp'])
    listening_services = set()

    for line in netstat:
        if line.startswith('tcp'):
            process = line.split()[6]
            # Renamne e.g. nimbus(cdm) to nimbus
            if "(" in process:
                process = process.split('(')[0]
            if process != "-":
                listening_services.add(process.split('/')[1])

    return listening_services

def get_systemd_enabled():
    """Return list of systemctl enabled service units"""

    systemd_enabled = []

    if os.path.isfile('/bin/systemctl'):
        output = shared.run_command(['systemctl', 'list-unit-files'])

        for unit in output:
            if "service" in unit and "enabled" in unit:
                 systemd_enabled.append(unit.split()[0].split('.service')[0])

    return systemd_enabled

def get_sysv_enabled():
    """Return list of sysv enabled services"""

    sysv_enabled = []

    if os.path.isfile('/sbin/chkconfig'):
        output = shared.run_command(['chkconfig', '--list'])

        for line in output:
            if "3:on" in line:
                sysv_enabled.append(line.split()[0])
    
    return sysv_enabled

def compare_listening_to_enabled(listening, enabled):
    """Return list of services the are listening but not enabled"""

    service_map = {"cupsd": "cups", "systemd-resolv": "systemd-resolved", "master": "postfix"}

    for l in listening:
        if l in service_map:
            l = service_map[l]
        if l in enabled:
            print("OK! {0} running and enabled".format(l))
        else:
            print("CHECK! {0} running but not enabled".format(l))


listening_services = get_listening_services()
systemd_enabled = get_systemd_enabled()
sysv_enabled = get_sysv_enabled()
compare_listening_to_enabled(listening_services, systemd_enabled + sysv_enabled)
