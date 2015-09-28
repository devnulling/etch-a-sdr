#!/bin/bash
file="/home/odroid/startup"
mode=$(cat $file)

if [ $mode == "etch" ]
	then
	/usr/bin/screen -d -m /usr/bin/python /home/odroid/etch-a-node/controls.py
fi

