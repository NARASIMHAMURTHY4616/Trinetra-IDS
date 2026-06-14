

# 🔱 Trinetra IDS

Trinetra IDS is a real-time Network Intrusion Detection System (IDS) designed to monitor network traffic, analyze packets, detect suspicious activities, and generate actionable security alerts.

Inspired by the concept of **Trinetra (The Three Eyes)**, the project aims to provide visibility into network communications and help identify potential security threats in real time.

---

## 🚀 Features

- Real-time packet capture using Scapy
- TCP, UDP, ICMP, and DNS traffic analysis
- Source and destination IP tracking
- Port and service identification
- DNS query extraction
- Protocol statistics generation
- Packet metadata collection
- Live packet monitoring dashboard support
- Export-ready packet storage
- Modular architecture for future IDS enhancements

---

## 📊 Captured Information

For each packet, Trinetra IDS extracts:

- Timestamp
- Source IP Address
- Destination IP Address
- Protocol
- Source Port
- Destination Port
- Service Type
- TCP Flags
- DNS Queries
- Packet Length
- Packet Summary

---

## 🏗️ Project Architecture

```text
Network Traffic
        │
        ▼
Packet Capture Engine
        │
        ▼
Packet Analyzer
        │
        ▼
Packet Storage
        │
        ├── UI Packet Buffer
        └── Export Packet Storage
```

---

## 📂 Project Structure

```text
trinetra-ids/
│
├── prototype.py
├── dashboard/
├── detection/
├── alerts/
├── database/
├── reports/
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- Scapy
- Streamlit
- Threading
- Collections
- Datetime

---

## 🔍 Current Capabilities

### Packet Capture

Captures packets in real time and processes them for analysis.

### Protocol Detection

Supports:

- TCP
- UDP
- ICMP
- DNS

### Service Identification

Recognizes common services:

| Port | Service |
|--------|---------|
| 80 | HTTP |
| 443 | HTTPS |
| 53 | DNS |
| 22 | SSH |
| 21 | FTP |

---

## 📈 Future Roadmap

### Trinetra IDS v0.2

- Port Scan Detection
- SSH Brute Force Detection
- DNS Tunneling Detection
- Alert Management System
- Threat Intelligence Integration

### Trinetra IDS v1.0

- Real-time Dashboard
- MITRE ATT&CK Mapping
- Incident Reporting
- Risk Scoring Engine
- IOC Detection

### Trinetra-X

Future integration with Netra-X to provide:

- Automated Python file analysis
- Suspicious file detection
- Security risk assessment
- Unified threat visibility

---

## 🎯 Project Goal

The goal of Trinetra IDS is to evolve from a packet monitoring tool into a complete intrusion detection platform capable of identifying network threats and providing actionable security insights.

---

## ⚠️ Disclaimer

This project is intended for educational, research, and authorized security monitoring purposes only. Users are responsible for complying with applicable laws and regulations.

---

## 👨‍💻 Author

Narasimha Balla

Cybersecurity Enthusiast | Python Developer | Security Researcher

---

## ⭐ Support

If you find this project useful, consider giving it a star on GitHub.