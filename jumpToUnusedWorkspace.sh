#!/bin/sh

# credits: https://www.reddit.com/r/i3wm/comments/ond028/script_to_open_new_unused_workspace/h5ulpka/
i3-msg workspace $(echo $(seq 1 99) $(i3-msg -t get_workspaces | sed 's/},{/\n/g' | awk -F, '{print $3}' | awk -F: '{print $2}' | sed "s/\"//g" | sort -n) | tr ' ' '\n' | sort -n | uniq -u | head -n 1)