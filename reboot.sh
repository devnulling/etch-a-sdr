#!/bin/bash
num=`cut -d ',' -f2 /home/odroid/rebootct.txt`

if [ $num -gt 4 ]
then
	echo "0" > /home/odroid/rebootct.txt
	sudo poweroff
else
	oldnum=`cut -d ',' -f2 /home/odroid/rebootct.txt`
	newnum=`expr $oldnum + 1`
	sed -i "s/$oldnum\$/$newnum/g" /home/odroid/rebootct.txt
fi
