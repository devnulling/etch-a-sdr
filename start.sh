#!/bin/bash
file="/home/odroid/startup"
mode=$(cat $file)

if [ $mode == "etch" ]
	then
	echo 'running etch start up'
	/bin/bash /home/odroid/start_etch.sh
fi

if [ $mode == "gqrx" ]
        then
        echo 'running gqrx start up'
	/usr/local/bin/gqrx &
	/bin/bash /home/odroid/controls.sh

fi


