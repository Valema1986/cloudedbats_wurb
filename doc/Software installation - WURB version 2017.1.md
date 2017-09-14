# Software installation - WURB version 2017.1
 
This guide describes how to install the CloudedBats-WURB, Wireless Ultrasonic Recorder for Bats, on a Raspberry Pi 3 B, or 2 B. The user of this guide should be familiar with the Linux operating system and the Raspberry Pi computer. If not, please contact me to get a link to an already prepared disk image file for download. 
 
### Download Raspbian Jessie Light.
Jessie Light is based on Debian Jessie, and it is very similar to Ubuntu when running it in a terminal window.
 
Download page:
 
    https://www.raspberrypi.org/downloads/raspbian/
 
Follow the instructions and install the Jessie Light image file (.img) on a Micro-SD card.
 
### SSH - activate
 
It is possible to connect a monitor/TV via HDMI and keyboard/mouse via USB and perform the installation. Personally I prefer to use ssh from a terminal window on another computer in the same local network, and the guide describes that alternative.
 
For security reasons ssh is disabled by default. The easiest way to enable it is to connect the Micro-SD card to a computer and create an empty file named 'ssh'. More info here: https://www.raspberrypi.org/documentation/remote-access/ssh/
 
Move the Micro-SD card to the Raspberry Pi and start it. Connect an Ethernet cable  to connect the Raspberry Pi to your local network. 
 
Start a terminal window on a computer in the local network. ('raspberrypi.local' works on Mac, I don't know if it is working on Windows.)   
 
    ssh pi@raspberrypi.local
    (password: raspberry)
 
### Change password.
 
    passwd     
 
(For example, change password to 'cloudedbats'.)
 
### Basic Raspberry Pi configuration
 
    sudo raspi-config 
 
Change these parts:
 
- Hostname: wurb1 (for example)
- Localisation Options - Change Timezone: Europe - Stockholm  (for example)
- Advanced Options - Expand Filesystem
 
### Reboot and login again with the new host name
 
    sudo reboot
 
    (wait until rebooted)
 
    ssh pi@wurb1.local
    pw: cloudedbats
 
### Upgrade Raspbian Jessie Light
 
    sudo apt-get update
    sudo apt-get upgrade
 
### Set up WiFi (optional)
 
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
 
Add these lines. Note: Must be 'tab', not spaces, for indentation.
 
    network={
    	ssid="<open-network-name>"
    	key_mgmt=NONE
    	priority=70
    }
    network={
    	ssid="<closed-network-name>"
    	psk="<closed-network-password>"
    	priority=80
    }
 
### Install software packages. 
 
    sudo apt-get install git portaudio19-dev gpsd gpsd-clients usbmount
 
    sudo apt-get install python3 python3-pip python3-numpy python3-scipy python3-all-dev python3-rpi.gpio
 
    sudo pip3 install pyaudio gps3 python-dateutil pyusb pytz
 
### Config GPS
 
    sudo nano /etc/default/gpsd 
 
Set these values:
 
    START_DAEMON="true"
    USBAUTO="true"
    DEVICES="/dev/ttyUSB0"
    GPSD_OPTIONS="-n"
    GPSD_SOCKET="/var/run/gpsd.sock"
 
### Config usbmount for automatic handling of USB memory/disk.
 
    sudo nano /etc/usbmount/usbmount.conf
 
Modify to these values:
 
    MOUNTOPTIONS="noexec,nodev,noatime,nodiratime"
    FS_MOUNTOPTIONS="-fstype=vfat,uid=pi,gid=pi,dmask=0000,fmask=0111"
 
### Special rules for Pettersson m500 (windows version).
 
Add a new file called "pettersson_m500_batmic.rules".
 
    cd /etc/udev/rules.d/
    sudo nano /etc/udev/rules.d/pettersson_m500_batmic.rules
 
Add this line to the file:
 
    SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", MODE="0664", GROUP="pi"
 
### Install the CloudedBats WURB software
 
    cd /home/pi
    mkdir cloudedbats
    cd cloudedbats/
    
    git clone https://github.com/cloudedbats/cloudedbats_wurb.git .
 
### Automatic start for  the WURB software at startup
 
    sudo nano /etc/rc.local
 
Add this before "exit 0":
 
    # CloudedBats.
    sudo -u pi python3 /home/pi/cloudedbats/cloudedbats_wurb/wurb_raspberry_pi/control_raspberrypi_by_gpio.py &
    sudo -u pi python3 /home/pi/cloudedbats/cloudedbats_wurb/wurb_main.py &
 
### Finished
 
    sudo shutdown -h now
 
### Connect pheripherals.
 
- Disconnect power.
 
- Connect USB memory or disk.
- Connect GPS (optional, but recommended).
- Connect ultrasonic microphone.
- Connect computer mouse (optional).
- Connect switches for Raspberry Pi and Rec. control.
 
- Connect power.
 
### Login and test
 
    ssh pi@wurb1.local
    pw: cloudedbats
 
### Test GPS.
 
    cgps -s
 
### Check log files.
 
    cat /home/pi/cloudedbats/cloudedbats_wurb/wurb_log_files/wurb_log.txt
    cat /home/pi/cloudedbats/cloudedbats_wurb/wurb_log_files/raspberry_pi_gpio_control_log.txt
 