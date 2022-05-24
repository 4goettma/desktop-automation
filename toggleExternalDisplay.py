#!/usr/bin/env python3

import subprocess
output = str(subprocess.run(['xrandr'], capture_output=True).stdout,'utf-8')
subprocess.run(['feh','--bg-scale','~/.wallpaper_black.jpg'])
if ('HDMI2 disconnected 1920x1080+0+0 (' in output): # kein Kabel angeschlossen, Display   aktiviert --> ext. Display deaktivieren
    subprocess.run(['xrandr','--output','HDMI2','--off'])
elif ('HDMI2 disconnected (' in output):             # kein Kabel angeschlossen, Display deaktiviert --> Fehlermeldung anzeigen
    subprocess.run(['notify-send','HDMI2 not connected'])
elif ('HDMI2 connected (' in output):                # Kabel angeschlossen,      Display deaktiviert --> ext. Display aktivieren
    subprocess.run(['xrandr','--output','HDMI2','--mode','1920x1080','--set','Broadcast RGB','Full','--output','eDP1','--mode','1366x768','--pos','277x1080','--primary'])
elif ('HDMI2 connected 1920x1080+0+0 (' in output):  # Kabel angeschlossen,      Display   aktiviert --> ext. Display deaktivieren
    subprocess.run(['xrandr','--output','HDMI2','--off'])
subprocess.run(['feh','--bg-scale','~/.wallpaper.jpg'])