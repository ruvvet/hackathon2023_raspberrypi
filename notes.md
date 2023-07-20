# Pi

https://www.makeuseof.com/tag/15-useful-commands-every-raspberry-pi-user-should-know/
sudo shutdown -h now
sudo shutdown -r now

ps -aef | grep python3 >> check script is running

### login

pw = raspberry
user = pi
host = raspberrypi

### copy/ssh

ssh raspberrypi.local

# on network via ip

arp -a >> get list of services
find `b8-27-eb...`
ssh raspberrypi@ip

scp -r Documents/Jenny-Projects/07-15-2023-hackathon/Dexter/ pi@raspberrypi.local:/home/pi

#### config/nav

sudo raspi-config >> pi configs
sudo nano /etc/wpa_suplicant/wpa_supplicant.conf >> add additional wifi
ls -a

# Python

# installing packages

sudo pip3 install <>

# picamera

raspistill -o Desktop/img.jpgpip

# Slack bot permissions

channels:join
chat:write
chat:write:customize
files:read
files:write
