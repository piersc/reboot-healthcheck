# reboot-healthcheck

Run some checks to see if a server will reboot into the same state its in now. Checks:

- Current mounts against fstab
- Running SysV and systemd services against start up config
- If Tmux or Screen sessions are running


```
$ sudo ./reboot-healthcheck.py 
[  OK  ]: /dev/mapper/ubuntu--vg-root / in fstab 
[  OK  ]: /dev/sda2 /boot in fstab 
[  OK  ]: /dev/sda1 /boot/efi in fstab 
[ WARN ]: vpnagentd running but not enabled 
[  OK  ]: systemd-resolved running and enabled 
[  OK  ]: cups running and enabled 

Ran these modules:
- mounts 1.0
- services 1.0
- sessions 1.0
```
