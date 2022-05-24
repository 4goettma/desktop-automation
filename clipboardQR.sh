#!/bin/sh
xclip -o | qr --error-correction=L --factory=pil > /tmp/qr.png && feh -F -Z /tmp/qr.png && rm /tmp/qr.png
