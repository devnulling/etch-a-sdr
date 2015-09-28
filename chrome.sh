#!/bin/bash
sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' /home/odroid/.config/chromium/Default/Preferences
chromium-browser --incognito --disable-restore-session-state --disable-sync --app="http://localhost:7200/"
