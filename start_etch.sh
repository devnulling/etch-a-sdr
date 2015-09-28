#!/bin/bash

screen -d -m /usr/local/bin/redis-server
printf "Redis Started";
printf "";
sleep 1;

screen -d -m /usr/local/bin/forever start /home/odroid/etch-a-node/app.js
printf "nodejs app started";
printf "";
sleep 1;

sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' /home/odroid/.config/chromium/Default/Preferences
/bin/bash /home/odroid/etch_controls.sh &

/bin/bash /home/odroid/start_chrome.sh &


