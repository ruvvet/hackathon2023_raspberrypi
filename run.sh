#!/bin/bash
cd /home/pi/Dexter
python dex.py
bash -c '/usr/bin/python3 /home/pi/myscript.py > /home/pi/mylog.log 2>&1' &