#!/bin/bash
file="/home/odroid/startup"
mode=$(cat $file)
if [ $mode == "gqrx" ]
	then
	sleep 5
	DISPLAY=:0; /usr/bin/python /home/odroid/gqrx_start.py
fi

