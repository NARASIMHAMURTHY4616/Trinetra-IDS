def analyze_icmp(packet):

    print("[ICMP]", packet["src_ip"], "->", packet["dst_ip"])
