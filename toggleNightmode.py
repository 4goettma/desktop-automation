#!/usr/bin/env python3
import os, subprocess

flag = "/tmp/i3wmNightmode"

def toggle():
    if not os.path.exists(flag):
        with open(flag, "w") as file:
            file.write(subprocess.check_output(['xbacklight']).decode().replace('\n',''))
        #with open('/proc/acpi/ibm/kbdlight','w') as file:
        #        file.write("0")
        subprocess.call(['xbacklight','-set','0.01'])
        subprocess.call(['redshift','-r','-P','-O','1000'])
    else:
        subprocess.call(['redshift','-x'])
        with open(flag, "r") as file:
            subprocess.call(['xbacklight','-set',file.read()])
        #with open('/proc/acpi/ibm/kbdlight','w') as file:
        #    file.write("1")
        os.remove(flag)

toggle()
