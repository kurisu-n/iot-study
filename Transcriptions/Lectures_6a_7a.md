# Lecture 6a - MSc IoT - LPWANs - RPL - Architectures

**Professor:** Marios Angelopoulos
**Department:** Department of Computer Engineering & Electronic Systems, International Hellenic University

## Evolution of Internet
* **First wave:** Computers => Telephony Nets => Satellites => Cellular Nets
* **Second wave:** Humans (Social networks) – Dynamic content generation
* **Next wave:** Machines / "Things" – Devices use the Internet infrastructure

### Typical Computer Networks vs IoT and Sensor Networks
* **Typical Computer Networks:** End-nodes are powerful devices, connections are reliable and persistent, more or less static architectures.
* **IoT and Sensor Networks:** End-nodes are highly-constrained devices, connections are unreliable and ephemeral, significantly higher numbers of devices, new protocol stacks introduced (interoperability and standardization issues).

## IoT Elements and Environments
* **Devices:** tags, sensors, wearables, etc.
* **Machines:** home appliances, robots, vehicles, etc.
* **Environments:** smart buildings, smart campus, smart city, smart economy, etc.

## Wireless Communication Technologies
* **Short Range / PAN:** Bluetooth, Bluetooth SMART, Thread, ZigBee, WiFi.
* **LPWAN:** M-Bus, Weightless, LoRa, 6LoWPAN, Sigfox.
* **Cellular / WAN:** GSM, UMTS, 4G LTE-M, 4G LTE-NB-IoT, 5G.

## Protocols

### PHY and MAC Layers
* **IEEE802.15.4:** Protocol specifying the physical and access layers for low-rate wireless personal area networks (LR-WPANs). Supports both sub-GHz and 2.4GHz. Low-rate RF communication ranging from 20Kbps up to 250Kbps.
* **ZigBee:** IEEE802.15.4-based specification for small, low-power digital radios. 250Kbps data rate; 10-100 metres (line-of-sight). A suite of several high-level protocols for Personal Area Networks.

### MAC and Networking Layers
* **6LoWPAN:** IPv6 over Low power Wireless Personal Area Networks. Adaptation layer protocol that enables IPv6 to run on 802.15.4 networks. Defines encapsulation and header compression mechanisms. Developed by IETF (RFC 6282).
* **IPv6:** Latest version of the Internet Protocol, providing vast address space.

## The RPL Protocol
* **RPL:** Routing Protocol for Low-power and Lossy Networks. Set of IPv6-based solutions defined by IETF.

### Terminology
* **DAG:** Directed Acyclic Graph. A directed graph having the property that all edges are oriented such that no cycles exist.
* **DAG root:** A node within the DAG that has no outgoing edge.
* **Rank:** A scalar indicating the depth of a node (position in DAG).
* **RPLInstanceID:** A unique identifier within a network.
* **Objective Function (OF):** Defines how routing metrics, optimization objectives, and related functions are used to compute Rank.

### Metrics
* **Node Residual Energy:** `EE = Power_now / Power_max * 100`
* **ETX:**
  `PRR(p) = Number of received packets / Number of sent packets`
  `ETX = 1 / (PRR_down * PRR_up)`

### Control Messages
* **DIO:** DODAG Information Object
* **DAO:** Destination Advertisement Object
* **DIS:** DODAG Information Solicitation

### DAG Construction
1. LBR-1 (Root) multicasts RA-DIO.
2. Nodes receive and process RA-DIO. They consider link metrics (e.g., ETX) and optimization objectives to join the DAG.
3. Nodes add LBR-1 as a DAG parent and calculate their depth/rank.
4. The process cascades as nodes multicast their own RA-DIOs, allowing deeper nodes to join and optimize their routes.
* **Other Mechanisms:** MP2P (Multiple Points to Point), P2MP (Point to Multiple Points), Loop removal.

## LPWAN Technologies
* Wireless communication technologies balancing the trade-off between communication range and power consumption.
* **Characteristics:** Low frequency (sub-GHz) => long range (Kms). Low bitrate => low duty cycle => low power consumption. Typically non-IP networks.
* **Spectra:** Licensed (e.g., NB-IoT) and unlicensed (e.g., LoRaWAN, Sigfox).

### LoRaWAN
* **LoRa Alliance:** Wide Area Network protocol for IoT. PHY & MAC layer protocol designed for large-scale public networks.
* **Data rates:** 0.3Kbps – 50Kbps; Communication range up to few Kms.
* **Architecture:** Multicast; messages from devices are received by multiple APs (Gateways) and forwarded to a Network Server and Application Server.

#### LoRaWAN Network Stack
* Uses LoRa as the underlying radio modulation.
* **3 Classes of Devices:**
  * **Class A (Baseline):** Battery powered, bi-directional comm (low power consumption, high latency).
  * **Class B:** Battery powered, bi-directional comm., extra receive windows (high power consumption, low latency).
  * **Class C (Continuous):** Mains-powered devices, no latency.

#### Signal Modulation
* **LoRa:** Proprietary modulation technique (owned by Semtech).
* **Spread spectrum technology:** Chirp modulation (CSS).
* **Duty Cycle:** In Europe (868MHz and 433MHz), a 1% duty cycle is imposed.
* **Spread Factor (SF):** Tunable parameter trading data rate for range and robustness. Affects time on air.
  `Ts = (2^SF) / BW`
  * Example: SF12, BW 125 kHz => Ts ≈ 32.8 ms

### Sigfox
* Proprietary LPWAN technology and infrastructure.
* **Ultra narrowband:** sub-GHz frequencies; 140 uplink msg/day and 4 downlink msg/day.
* **Architecture:** 1-hop star topology.

### NB-IoT (Narrow-Band IoT)
* Standard specifications developed by 3GPP.
* Focuses on indoor coverage, low cost, long battery life, and high connection density.
* Uses a subset of the LTE standard: OFDM modulation for downlink, SC-FDMA for uplink.

## Protocols - Transport Layer
* **CoAP (Constrained Application Protocol):** Designed for resource-constrained devices. Brings RESTful architectures to IoT (HTTP of IoT). Uses GET, POST, PUT. IETF RFC 7959.
* **MQTT (Message Queue Telemetry Transport):** Publish-subscribe-based lightweight messaging protocol on top of TCP/IP. Publisher generates messages to "topics", Broker distributes them to Subscribers. OASIS MQTTv3.1.1.

## IoT and 5G
* 5G refers to an ecosystem of technologies employing mmWave frequencies (24GHz, 60GHz).
* **MEC-enabled 5G Architecture:** Multi-access Edge Computing (MEC), Network Function Virtualisation (NFV), BaseBand Unit (BBU), Remote Radio Heads (RRH).


---


# Lecture 7a - IoT Topics

**Professor:** Periklis Chatzimisios
**Affiliation:** International Hellenic University (IHU)

## The Exciting World of IoT
* **Internet of Things (IoT):** Complex and heterogeneous resources and networks.
* **Things Connecting to Things:** e.g., smart cars, routers, petrol stations communicating.
* **People Connecting to Things:** e.g., ECG sensors, motion sensors communicating with cloud services.

## Industrial Internet of Things (IIoT)
* IoT extended for industrial applications such as manufacturing and supply chain management.
* Used in oil and gas, transportation, mining, aviation, logistics.
* **Applications:** Predictive Maintenance, Adaptive Assembly Lines / Customized Products.
* **Characteristics:** Machine-to-Machine communication, Coexistence & Interoperability, Big Data.
* **Industry 4.0:** The Smart Factory, autonomous systems, IoT, machine learning (4th Industrial Revolution).

## IoT Verticals
* Smart Wearables, Smart Home, Smart City, Smart Agriculture.
* Connected Car, Health Care, Industry Automation, Smart Energy.

### Smart Cities
* **Smart parking:** Monitoring parking spaces.
* **Structural Health:** Monitoring vibrations in buildings/bridges.
* **Traffic Congestion:** Monitoring vehicles/pedestrians to optimize routes.
* **Smart lighting:** Weather adaptive street lights.
* **Waste management:** Optimizing trash collection routes based on container levels.
* **Smart roads:** Intelligent highways with warning messages.

## Networking Approaches
1. **Short-range multihop:** ZigBee, WiFi low energy, RFID.
2. **Cellular:** GSM, LTE-A, 5G.
3. **Low Power Wide Area Networks (LPWAN):** SIGFOX, NB-IoT, LoRa.

## 5G Requirements and Use Cases
* **Requirements (2020+):** 10000x more traffic, 10-100x more devices, 1 millisecond latency, 10 years M2M battery life, Flat energy, 10 Gbit/s peak data rates, Ultra reliability.
* **Use Cases:**
  * **eMBB / xMBB:** Enhanced / extreme mobile broadband.
  * **mMTC:** Massive machine type communications.
  * **URLLC / uMTC:** Ultra reliable & low latency communications.

### Tactile Internet
* Critical control of remote devices, media everywhere, smart vehicles.
* **Goal of 1ms latency:** $\Sigma$ = 0.3ms (Terminal) + $\Sigma$ = 0.2ms (Air Interface) + $\Sigma$ = 0.5ms (Base Station & Compute).

### The 5G World
* **Technologies & Concepts:** Network Slicing, SDN (Software Defined Networking), NFV (Network Function Virtualization), Mobile Edge Cloud, Network Coding, Machine Learning.

## 5G / IoT Challenges
* Heterogeneity – Interoperability
* Scalability – Big Data
* Identification and Addressing
* Security – Privacy – Trust
* Miniaturization of devices
* Energy efficiency – Greening of IoT
* Standardization
