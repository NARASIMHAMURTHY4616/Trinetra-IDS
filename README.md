# 🔱 Trinetra IDS

Trinetra IDS is a modular Network Intrusion Detection System (IDS) designed to capture, analyze, and inspect network traffic in real time. Built with extensibility in mind, Trinetra provides a foundation for protocol analysis, threat detection, alert generation, and future AI-assisted security analytics.

Inspired by **Trinetra (The Three Eyes)**, the project aims to observe network activity, detect suspicious behavior, and provide actionable security visibility.
Trinetra IDS observes, analyzes, and reveals hidden threats within network traffic.
---

## 🚀 Features

- Real-time packet capture using Scapy
- IPv4 and IPv6 support
- TCP, UDP, ICMP, and DNS traffic analysis
- Source and destination IP tracking
- Service and port identification
- DNS query extraction
- Protocol-based traffic classification
- Modular detection engine
- Rule-based analysis architecture
- Alert generation framework
- Dashboard-ready packet storage
- Extensible design for ML and AI integration

---

## 📊 Packet Information Collected

For every captured packet:

- Packet ID
- Timestamp
- IP Version (IPv4 / IPv6)
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

## 🏗️ Architecture

```text
Network Traffic
        │
        ▼
Capture Layer
(net_sniffer.py)
        │
        ▼
Analysis Engine
(engine.py)
        │
        ▼
Protocol Routers
        │
 ┌──────┼──────┐
 ▼      ▼      ▼
TCP    UDP    ICMP
Rules  Rules  Rules
        │
        ▼
Alert Generation
        │
        ▼
Alert Database
        │
        ▼
Dashboard / Reports
```

---

## 📂 Project Structure

```text
Trinetra-IDS/
│
├── capture/
│   └── net_sniffer.py
│
├── config/
│   └── rules.json
│
├── database/
│   └── alerts.db
│
├── rules/
│   ├── tcp.py
│   ├── udp.py
│   ├── icmp.py
│   └── unknown.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── dashboard.html
│
├── engine.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- Scapy
- SQLite
- Flask (Planned Dashboard Integration)
- HTML
- CSS
- JavaScript
- Threading

---

## 🔍 Current Capabilities

### Network Packet Capture

Captures and processes network packets in real time.

### Protocol Analysis

Currently supports:

- TCP
- UDP
- ICMP
- DNS

### Service Detection

| Port | Service |
|--------|---------|
| 21 | FTP |
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |

### Packet Routing Engine

Routes packets to protocol-specific analysis modules for efficient inspection.

---

## 🗺️ Development Roadmap

### Phase 1 – Core IDS Engine

- [x] Packet Capture Engine
- [x] Packet Analysis Engine
- [x] IPv4 Support
- [x] IPv6 Support
- [x] Protocol Routing
- [x] Modular Rule System
- [ ] Alert Database Integration
- [ ] Dashboard Integration

### Phase 2 – Detection Rules

- [ ] SSH Activity Detection
- [ ] SYN Scan Detection
- [ ] Port Scan Detection
- [ ] ICMP Sweep Detection
- [ ] DNS Anomaly Detection
- [ ] Alert Severity Classification

### Phase 3 – Advanced Security Analytics

- [ ] Threat Intelligence Integration
- [ ] IOC Detection
- [ ] MITRE ATT&CK Mapping
- [ ] Automated Incident Reports
- [ ] Risk Scoring Engine

### Phase 4 – Trinetra-X Integration

Integration with Netra-X:

- Python Source Code Analysis
- Malicious Script Detection
- Security Risk Assessment
- Unified Security Dashboard

---

## 🎯 Vision

Trinetra aims to evolve from a packet monitoring solution into a complete cybersecurity platform capable of:

- Detecting network threats
- Generating security alerts
- Assisting incident response
- Integrating AI/ML-driven threat analysis
- Providing unified visibility across network and code security domains

---

## 👥 Contributors

### 🔐 Narasimha Balla
Cybersecurity Engineer • Project Lead • Detection Engine Development

### 💻 Anusha Ganisetti
Frontend Developer • UI/UX Design • Dashboard Development

### 🤖 ML Contributor
Machine Learning Integration • Traffic Analytics • Threat Classification

---

## ⚠️ Disclaimer

This project is intended solely for educational, research, and authorized security monitoring purposes. Users are responsible for ensuring compliance with applicable laws, regulations, and organizational policies.

---

## ⭐ Support

If you find this project useful, consider starring the repository and contributing to its development.
