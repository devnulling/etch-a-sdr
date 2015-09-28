#!/bin/bash
echo "starting chrome"
/bin/bash /home/odroid/chrome.sh &
echo "Sleeping for 15 seconds"
sleep 15
/usr/bin/python /home/odroid/etch_start.py &
echo "Running fullscreen and mouse clear"
