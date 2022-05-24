#!/usr/bin/env python3

import subprocess
output = str(subprocess.run(['setxkbmap','-query'], capture_output=True).stdout,'utf-8')
if ('layout:     de\nvariant:    nodeadkeys\n' in output): # bisher DE nodeadkeys
    subprocess.run(['setxkbmap','de'])
    subprocess.run(['notify-send','layout switched to german'])
else:
    subprocess.run(['setxkbmap','de','nodeadkeys'])
    subprocess.run(['notify-send','layout switched to german (no dead keys)'])