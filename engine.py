# engine.py

from rules.tcp import analyze_tcp
from rules.udp import analyze_udp
from rules.icmp import analyze_icmp
from rules.unknown import analyze_unknown


def analyze(packet):

    protocol = packet["protocol"]

    if protocol == "TCP":
        analyze_tcp(packet)

    elif protocol == "UDP":
        analyze_udp(packet)

    elif protocol == "ICMP":
        analyze_icmp(packet)

    else:
        analyze_unknown(packet)
