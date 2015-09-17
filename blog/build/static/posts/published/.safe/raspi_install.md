<!-- #short_title#Installing and Configuring Raspbian Linux# -->
<h1><a href="">Installing and Configuring <span class="highlight-red">Raspbian Linux</span> on a <span class="aux-color-yellow">Raspberry Pi</span> Model B</a></h1>

<span class="meta-info">posted by <a href="aboutme">Alex</a> at 12:39pm on Mon, Aug 9th, 2014</span>

### Preamble

In this tutorial, I’m going to show you how to install and configure a Raspberry Pi model B running the Raspbian Linux distribution. The goal is to get your pi ready for an as of yet undetermined but fun purpose. By the end of this you should have an SSH-accessible system configured with a static IP for your home LAN network.  

In follow-up posts, I’ll demonstrate a few practical uses I’ve found for it, such as a samba share, a web server, a webcam, a server for a python network game, and I'll share some system administration tips as well.

I'll show GUI options when appropriate but the command-line is going to be the main focus here.  

## What You Need

+ A raspberry Pi model with a 5V microUSB power supply <a href="#raspi_b"><i class="fa fa-camera-retro"></i></a>

+ An extra Ethernet cable <i class="fa fa-camera-retro"></i>

+ A Wifi Router and Internet Access <i class="fa fa-camera-retro"></i>

+ An SD card or a microSD card and a microUSB adapter that is 4GB or larger in size.  If you are going to purchase one, do some research on quality, not all SD cards yield good results. <i class="fa fa-camera-retro"></i>

+ An SD card reader (if you have a MacBook, iMac or Mac Mini, it may be built into your computer) <i class="fa fa-camera-retro"></i>

+ A Mac on which you have administrative privileges, preferably one with data that other people don't depend on or hold dear <i class="fa fa-camera-retro"></i>

## Formatting the SD Card

Before you insert the SD card, open the Terminal (tip: Cmd spacebar type ‘Termi…’ hit Enter)

Type `diskutil list` and note the device output. If no other disks are attached at this time, you will likely see just the `/dev/disk0` device and its partitions, `/dev/disk0s1`, `/dev/disk0s2`, etc.  These are the BSD device labels.

After we insert the SD card, `diskutil list` should reveal an additional mounted device, most likely at `/dev/disk1`. You want to make sure you reformat this disk, which is why we taking a safer route and comparing the output list before and after we insert the card. If you reverse the source and destination of the copy utility we will use, you will erase the data on your hard drive.

Insert the SD card into a card reader or into your Mac.

Type `diskutil list` again.

Note the newly added disk’s device name.  For me, it was `/dev/disk1`.

Understand the difference between `/dev/disk1` and `/dev/disk1s0` or `/dev/disk1s1`, etc.  The first describes the physical device, the latter examples refer to the logical partitions on that device. We will be writing a group of filesystems that comprise the Raspbian OS to the new `/dev/disk1` device.

Open Disk Utility.

You should see your disk in the left pane. Mine says 7.86GB Apple SDXC Reader.

Find the erase Tab and change the format to MS-DOS(FAT).

Name your disk, e.g. RASPI.

Hit Erase.

Unmount the disk but don’t eject it.  You can do this with the terminal command 

	sudo diskutil unmount /dev/disk1

## Getting and Preparing the Raspberry Pi Operating System Image

Download the latest Raspbian image from the Raspberry Pi website in either 
<a class="article-link" href="http://downloads.raspberrypi.org/raspbian_latest">ZIP format</a> or as
<a class="article-link" href="http://downloads.raspberrypi.org/raspbian_latest.torrent">a torrent</a>.

If you downloaded a ZIP file, unzip it. If you torrented it, you most likely got an IMG file.

I’m assuming the unzipped Raspbian .img file is located in your `~/Downloads` folder, aka `/Users/<USERNAME>/Downloads`, but if it is in a different location, adjust the upcoming `dd` commands to reflect that.

Recall the device name of the SD card that you recently reformatted. In my case, it is `/dev/disk1`.  You will write the Raspbian image to this device with the BSD utility, `dd`. `dd` is a low-level block copying utility that comes in extremely handy in Unix/BSD-related tasks, but it is nick-named ‘disk destroyer’ for a reason.  Be careful to get the source (designated by `if`, the input file) and destination (designated by `of`, the output file) file paths correct.

We want to use dd in this way:

	dd  if=<RPI IMAGE FILE> of=<DESTINATION DEVICE> bs=<block size>

This command copied the raspbian image to the FAT32-formatted SD device named ‘RASPI’ on my Mac.  It took me just under 35 minutes for the image writing process to complete.

	sudo dd if=~/Downloads/2014-09-09-wheezy-raspbian.img of=/dev/disk1 bs=1m


## Getting a Read on the Progress of `dd`

`dd` doesn’t give you any visible indication of its progress, but you can figure this out yourself by pressing `CTRL T` in the terminal where the dd copy is presently working.  `CTRL T` sends the `dd` process a `SIGINFO` signal that will return cpu load information to the console, as well as a read on how many bytes have been transferred by `dd` and the duration in seconds of the copy thus far.

The output is something like this:

	309329920 bytes transferred in 195.748521 secs ( 1580241 bytes/sec)

With a little math, we can get the progress so far: 

bytes copied / disk image size = % done

309,329,920 / 3,100,000,000 or roughly 1 % done.

	user@host:~ $ du -sh ~/Downloads/2014-09-09-wheezy-raspbian.img
	3.1G	/data/ISO/2014-09-09-wheezy-raspbian.img

disk image size = 3.1 GB

progress = .31GB/3.1GB = .1 = 10% done

## Network Setup

Now that your raspberry pi is properly imaged, connect it to an ethernet port on your wifi router.

Connect the micro-usb power source and plug it in. You should see a red light that indicates power.  Soon after you should see a few other lights (yellow and green), that indicate that the system is booting and that the network connection is active.

If this doesn’t happen for you, you can look at the light labels on the board and troubleshoot accordingly.  They are as follows:

**ACT** — SD Card Access

**PWR(RED)** - The device is powered

**FDX** - Full Duplex mode is enabled

**LNK** -  The Ethernet LINK is present

**100** - a 100MBit connection is active 


If all has gone well, the raspberry pi should have booted up and received an ip address from your wifi router.
You can find the raspberry pi with the Terminal application in a few ways:

### Method 1: Find it through your Wi-Fi Router

Log into the admin panel of your wifi router and look for connected devices.  It may reveal the hostname and IP address of the pi.  It showed mine as hostname raspberrypi with the IP address 192.168.1.10.  However, if your wireless router's firmware is old, it software may not show you this information.  

### Method 2: Use nmap for MAC/BSD

Download and install nmap for mac, run `sudo nmap -sP 192.168.0.0/24` from your Mac Terminal.


### Method 3: Brute Force

If you can’t or don’t want to download any extra tools and you’re on your own network, you can try a brute-force approach by pinging all of the possible IP addresses on your network once, and with a brief timeout setting. This is how you’d do it in bash:

	for i in {1..254}; do ping -c1 -t1 192.168.1.$i; done | grep -B 1 " 0.0% packet loss"

This will ping every ip address on your network once and wait a second before moving on, regardless of the result.  We are looking for a ping that results in %0.0 packet loss, and getting that line of text plus the previous line, where I know the IP address is usually output.

It should reveal the IP address of any system that respond to ping, but not the hostname.  But if you have only a handful of devices connected to your router, then the process of elimination shouldn't be too hard.

If you think you've found the pi's address, you can cancel the for loop by typing CTRL \ into the terminal.  This sends a SIGQUIT signal to the bash process running the loop.

Note: this method is permissable on your private network, but I don’t recommend doing it on a monitored network where such activity might be flagged as suspicious.
 
If you’ve found the IP address of the pi, then type `ssh pi@raspberrypi`. You will likely see a message that says:

    - `‘The authenticity of the host ‘xxx.xxx.xxx.xxx’ can’t be established. Are you sure you want to continue connecting (yes/no)?’.`


Type ‘yes’ and enter ‘raspberry’ as the password.

If you end up at a command prompt that says ‘pi@raspberrypi’, then congratulations! You got your pi online! 

… but we have more to do. :]


## Resetting the Password

Type `sudo raspi-config` and select item #2, "Change User Password"

Enter your new password twice.

Try logging out and then back in.  Your new password should work with the user `pi`, and you shouldn’t see the previous message regarding the questionable authenticity of this system's RSA key.

## Updating Current Packages

Run `sudo apt-get update` and wait a bit

## Leaving the Pi on DHCP (the default)

Setting a static IP allows you to know the address of the PI at boot time, but it requires a little work.  If you don't want to set up a static IP on your WIFI network, you can avoid the tedious process of looking for the pi each time by creating a boot script that pings your router when the PI starts up.  What this does is tell the router about its IP address, which gets passed to you when you run `arp -a ` on Linux/BSD/MAC system that is connected the router.  From there, you can deduce the proper IP.  For obvious reasons, a static IP is probably a better route, as your WIFI router's lease may expire and the IP may change.

You can create a boot script called `pingrouter` on the Pi by creating a file called `/etc/init.d/pingrouter` with the following lines:

	#!/bin/bash
	# This command will unconditionally run at boot
	ping -c1 192.168.1.1

Then run these commands:

	user@host:~ $ sudo chmod 755 /etc/init.d/pingrouter 
	user@host:~ $ sudo update-rc.d pingrouter defaults

## Assigning the System a Static IP

It is better to understand the IP address `192.168.1.10` as consisting of two addresses, a network address and a host address.  The network address identifies the internet that the host is on, e.g.,  `192.168.1`.  The host address indicates *which* host on that network, e.g.  `10`.

To assign the pi a static IP so that it boots with the same IP address each time, we need to figure out 5 things:

  - The DHCP range of the WIFI router

  - The Netmask

  - The Network Address

  - The Broadcast Address

  - The Gateway Address

In a terminal, run `ifconfig`.  This lists your network devices and the IP address information obtained by them.  Not all will have an IP address, so we need to look for an `inet` entry.  

This is the output of `ifconfig` on my system from my private LAN:

	en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
		options=27<RXCSUM,TXCSUM,VLAN_MTU,TSO4>
		ether 34:15:9e:13:0c:4e 
		nd6 options=1<PERFORMNUD>
		media: autoselect
		status: inactive
	en1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
		ether f8:1e:df:e4:e3:3e 
		inet6 fe80::fa1e:dfff:fee4:e33e%en1 prefixlen 64 scopeid 0x5 
		inet 192.168.1.6 netmask 0xffffff00 broadcast 192.168.1.255
		nd6 options=1<PERFORMNUD>
		media: autoselect
		status: active
	fw0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 4078
		lladdr 34:15:9e:ff:fe:13:0c:4e 
		nd6 options=1<PERFORMNUD>
		media: autoselect <full-duplex>
		status: inactive
	p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
		ether 0a:1e:df:e4:e3:3e 
		media: autoselect
		status: inactive

Notice that the `en1` device has an `inet` address.  We'll use this section to determine the necessary addresses for the pi's static IP.

### Netmask

The output for `en1` indicates (in hexidecimal) that the Netmask is `0xffffff00`, which is `255.255.255.0` in dotted decimal, the IP address notation you are probably most familiar with. The Netmask tells you where in the ip address the network address ends and the IP address space begins. A network with the netmask `255.255.255.0` reserves the first 3 dot-separated numbers for representation of the network. The last number, excluding 3 special addresses, indicates the total possible host addresses on that network, so 256-3, or 253.

What We Have So Far (**Netmask**)

	DHCP RANGE:  
	The Network Address: 
	The Gateway Address: 
	The Netmask: 255.255.255.0


Network Address: the netmask `255.255.255.0` indicates a network address of 3 'octets' in length. The Network address is simply the first 3 octets of the inet address you found in the `ifconfig` output, with a 0 as the last octet.


What We Have So Far (**Netmask** and **Network Address**)

	DHCP RANGE:
	The Network Address: 192.168.1.0
	The Gateway Address:
	The Netmask: 255.255.255.0
 

Gateway: since we know the Network Address now, the gateway is simply the second possible address in ascending order, so `192.168.1.1`.  This Gateway is also your WIFI router's address.

What We Have So Far (**Network Address**, **Gateway Address** and **Netmask**)

	DHCP RANGE:
	The Network Address: 192.168.1.0
	The Gateway Address: 192.168.1.0
	The Netmask: 255.255.255.0

## Your Router's DHCP range

When we set a static IP, we don't want it to conflict with an address reserved for automatic/dynamic assignment, which the WIFI router takes care of.  We need to log into our WIFI router's administration panel and find the DHCP range.  Since I have no idea what your WIFI router model is, I can only advise that you look for the DHCP range settings in the LAN Administration in your WIFI Admin panel, or look that information up in the manual for your router (can probably be found online if it's at least somewhat recent).  My WIFI router reserves addressess `192.168.1.2` through `192.168.1.100` for DHCP addresses.  This means that anything from `192.168.1.101` through `192.168.1.254` is technicially available, assuming I configured any other static IP devices on this network.


What We Have So Far (**Network Address**, **Gateway Address** and **Netmask**, **Broadcast Address** and **DHCP range**)

	DHCP RANGE: 192.168.1.2 thru 192.168.1.100
	The Network Address: 192.168.1.0
	The Gateway Address: 192.168.1.1
	Broadcast Address 192.168.1.255
	The Netmask: 255.255.255.0

We have all of the relevant information to configure a static IP. Let's edit our network settings file,  `/etc/network/interfaces` to give the pi a fixed IP address . 

But first, let’s back that up that so  we can modify it while keeping the original in tact. In a Terminal window, run 
	
	sudo cp /etc/network/interfaces /etc/network/interfaces.orig

Now lets modify the contents of `/etc/network/interfaces`. The default file looks like this:

	auto lo

	iface lo inet loopback
	iface eth0 inet dhcp

	allow-hotplug wlan0
	iface wlan0 inet manual
	wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
	iface default inet dhcp

We need to change it to this (note the arrows, which do not actually go in the file)

	bash
	allow-hotplug wlan0
	iface wlan0 inet manual
	wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
	iface default inet static <--

	address 192.168.1.10
	--> gateway 192.168.1.1
	--> netmask 255.255.255.0
	--> network 192.168.1.0
	--> broadcast 192.168.1.255

	allow-hotplug wlan0
	iface wlan0 inet manual
	wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
	iface default inet dhcp

## Starting and restarting network services

This part should be completed soon.

## Expanding the root partition

We wrote a 2.9GB root filesystem to the SD card, but that means whatever space is left on the card isn’t presently usable. For me, that’s about 5GB of space.  Fortunately, the Raspbian Image developers have provided us with a convenient ‘Expand Filesystem’ option in the same `raspi-config` panel we just used to set our password.


Type `sudo raspi-config` again

choose option #1

It should say, “Root partition has been resized … ”. Hit OK, choose Finish at the bottom, and say yes to the reboot option.  Since we’ve already set a static ip for the pi, rebooting won’t mean we have to go looking for the ip again.

All Rights Reserved Alex Ramsdell © 2015
