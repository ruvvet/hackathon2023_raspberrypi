# Pi

https://www.makeuseof.com/tag/15-useful-commands-every-raspberry-pi-user-should-know/
sudo shutdown -h now
sudo shutdown -r now

sudo reboot

ps -aef | grep python3 >> check script is running
ps- ef for all running processes
sudo killall python3 >> to kill all python scripts

### login

pw = raspberry
user = pi
host = raspberrypi

# get ip
hostname -I

### copy/ssh

ssh raspberrypi.local

# on network via ip

arp -a >> get list of services
find `b8-27-eb...`
iq: ssh pi@192.168.128.228 // 192.168.128.228
home: 192.168.86.115

scp -r Documents/Jenny-Projects/07-15-2023-hackathon/Dexter/ pi@raspberrypi.local:/home/pi

#### config/nav

sudo raspi-config >> pi configs
sudo nano /etc/wpa_suplicant/wpa_supplicant.conf >> add additional wifi
ls -a

# Python

# installing packages

sudo pip3 install <>

# picamera

raspistill -o Desktop/img.jpg

# Slack bot permissions

channels:join
chat:write
chat:write:customize
files:read
files:write

# open cv stuff

pip install numpy - <linux>sudo apt-get install python3-numpy
pip install matplotlib - <linux> sudo apt-get install python3-matplotlib
pip install opencv-python

refs
**https://core-electronics.com.au/guides/object-identify-raspberry-pi/
**https://cocodataset.org/#download
https://medium.com/swlh/dog-breed-classifier-a900d4cc95be
https://towardsdatascience.com/a-dog-detector-and-breed-classifier-4feb99e1f852

https://medium.com/@divyanshuDeveloper/a-simple-animal-classifier-from-scratch-using-keras-61ef0edfcb1f


sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get autoremove -y && sudo apt-get autoclean -y

sudo pip3 -v install opencv-contrib-python --no-cache-dir
sudo pip3 install numpy==1.19.3 --upgrade
sudo pip3 -v install opencv-contrib-python==4.5.3.56 --no-cache-dir
<<opencv-contrib-python==4.5.3.56>>

uninstall - python3-opencv
python3-numpy
python3-matplotlib

sudo pip3 cache purge
dpkg-query -l '*numpy*'
sudo apt autoremove

usr/local/lib/python3.9

python3 -m pip freeze