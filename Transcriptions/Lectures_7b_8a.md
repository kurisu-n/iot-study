# Lecture 7b - IoT protocols and open challenges

## Slide 1
Prof. Periklis Chatzimisios (pchatzimisios@ihu.gr)

## Slide 2: IoT Verticals
*   **Smart Wearables**
*   **Smart Home**
*   **Smart City**
*   **Smart Agriculture**
*   **Connected Car**
*   **Health Care**
*   **Industry Automation**
*   **Smart Energy**

## Slide 3: IoT common architecture
[Figure: Shows the architecture starting from Edge-side to Cloud-side and User-side]
*   **Edge-side:** Thing -> Radio -> Gateway -> Connectivity
*   **Cloud-side:** Ingestion & Storage -> Trigger & Alert Processing / Visualization / Devices & Firmware Mgt.
*   **User-side:** Apps

## Slide 4: Three main approaches for networking
*   **Short-range multihop**
    *   ZigBee
    *   WiFi low energy
    *   RFID
*   **Cellular**
    *   GSM
    *   LTE-A
    *   5G
*   **Low Power Wide Area Networks (LPWAN)**
    *   SIGFOX
    *   NB-IoT
    *   LoRa
[Figure: Diagrams of various network topologies including mesh, cellular base stations, and LPWAN gateways connecting to the internet]

## Slide 5: Short range multihop
*   **Pros:** Low energy consumption, Very cheap
*   **Cons:** Instability, Troublesome maintenance, High complexity of large networks

## Slide 6: Cellular-based solutions
*   **Pros:** Easy integration with rest of the world, Well-established technology, Almost ubiquitous coverage, Long range
*   **Cons:** Architectural limits, Energy efficiency, Costs

## Slide 7: LPWAN
*   **Pros:** Low power, Very long range, Low cost
*   **Cons:** Long delays, Low bitrate

## Slide 8: 5G requirements
*   10000 x more traffic
*   10-100 x more devices
*   < 1 millisecond latency
*   10 years M2M battery life
*   M2M ultra low cost
*   Flat energy
*   > 10 Gbit/s peak data rates
*   100 Mbit/s wherever needed
*   Ultra reliability

*(Source: Understanding 5G, Anritsu whitepaper, 2016)*

## Slide 9: Key Performance Indicators – ITU (1)
*   **Peak data rate:** Maximum achievable data rate under ideal conditions per user/device (in Gbit/s).
*   **User experienced data rate:** Achievable data rate that is available ubiquitously across the coverage area to a mobile user/device (in Mbit/s or Gbit/s).
*   **Latency:** The contribution by the radio network to the time from when the source sends a packet to when the destination receives it (in ms).
*   **Mobility:** Maximum speed at which a defined QoS and seamless transfer between radio nodes which may belong to different layers and/or radio access technologies (multi-layer/-RAT) can be achieved (in km/h).

## Slide 10: Key Performance Indicators – ITU (2)
*   **Connection density:** Total number of connected and/or accessible devices per unit area (per km²).
*   **Energy efficiency:** Energy efficiency has two aspects:
    *   on the network side, energy efficiency refers to the quantity of information bits transmitted to/received from users, per unit of energy consumption of the radio access network (RAN) (in bit/Joule);
    *   on the device side, energy efficiency refers to quantity of information bits per unit of energy consumption of the communication module (in bit/Joule).
*   **Spectrum efficiency:** Average data throughput per unit of spectrum resource and per cell (bit/s/Hz).
*   **Area traffic capacity:** Total traffic throughput served per geographic area (in Mbit/s/m²).

## Slide 11
*   7 Billion Devices 2014 -> Throughput but there is more .... -> 500 Billion Devices 2022

## Slide 12: Reliable Multicast
[Figure: An image of a stadium with many arrows pointing to users, demonstrating reliable multicast in a dense environment]

## Slide 13: Precision Farming/Agriculture
[Figure: Diagram showing farming ecosystem components]
*   Satellites, Drones -> Navigation, Communication, Remote sensing
*   Consultant, Dealer, Supplier, Manufacturer, Contractor -> Farm Management Information System <- Buildings, Stables
*   Wireless Connection -> Farmer

## Slide 14: Industrial Internet of Things (IIoT)
*   **Industrial Internet of Things:** When the IoT is extended for industrial applications such as manufacturing and supply chain management.
*   IIoT is an industrial application of IoT (a network connecting industrial machinery and devices) in areas such as oil and gas, transportation, mining and metals, mining, aviation, logistics, etc.
    *   Predictive Maintenance
    *   Adaptive Assembly Lines / Customized Products

## Slide 15: Characteristics of IIoT (1)
**IIoT : an application of IoT**
**IIoT key enabler for Industry 4.0**

**Requirements of Industrial Communications**
*   Guarantees → Determinism
    *   High Reliability: almost no packet loss
    *   Delay: deadlines (real time)

**Wired Industrial Networks**
*   Reliable
*   Low delay
*   High data transfer speed
*   Not flexible
*   Costly

**Wireless Sensor & Actuators Networks**
*   Unreliable
*   No deterministic delay
*   Flexible, reconfigurable
*   Cost reduction
*   Safety
*(Best effort)*

## Slide 16: Characteristics of IIoT (2)
*   Machine-to-Machine communication
*   Coexistence & Interoperability
*   Big Data

## Slide 17: Industry 4.0
[Figure: Diagram showing a cycle of Industry 4.0 components]
*   Autonomous Robots
*   Simulation
*   System Integration
*   Internet of Things
*   Cybersecurity
*   Cloud Computing
*   Additive Manufacturing
*   Augmented Reality
*   Big Data

## Slide 18: Industry 4.0 in European Union
[Figure: Map of Europe highlighting various initiatives such as Catapult, Industrie du Futur, Industria Conectada 4.0, Fabbrica Intelligente, Smart Industry, Produktion 2030, Industrie 4.0, Prumysl 4.0, iPAR4.0]

## Slide 19: Industry 4.0 in USA and China
*   USA: Industrial Internet Consortium, Manufacturing USA (National Network for Manufacturing Innovation)
*   China: internet+, Made in China 2025

## Slide 20: Industry 4.0 - Main characteristics
*   **Aware:** Smart Products are equipped with sensor technology giving access to condition information regarding the product and its environment.
*   **Connected:** Smart Products are equipped with a M2M communication device that enables interaction and data exchange with other cyber-physical systems.
*   **Intelligent:** Smart Products are equipped with computing power that enables autonomous decision-making and self-learning processes based on defined algorithms.
*   **Responsive:** Smart Products are equipped with control technology that enables autonomous product adaption based on internal or external commands.

## Slide 21: Industrial IoT - Manufacturing
[Figure: Diagram of a manufacturing plant connecting to global facility insight and customer site, emphasizing predictive maintenance and operational awareness]

## Slide 22: Industrial IoT - Predictive Maintenance (1)
**Motor vibration sensor:**
*   Built for Industrial IoT, for preventive maintenance
*   Measure vibration behavior on machinery’s motors
*   Detect anomalies and trigger alert
*   Suggest maintenance through Machine Learning
*   Energy harvesting from vibration and/or heat
*   [Figure: Placement of the sensor on a motor]

## Slide 23: Industrial IoT - Predictive Maintenance (2)
*   **Time-to-Failure:**
    *   **Months:** Predictive (based on usage and wear characteristics to predict failure)
    *   **Weeks:** Condition-monitoring (based on standard asset operation)
    *   **Days:** Preventive (based on time or operational cycles)
    *   **Failure:** Reactive (based on asset failure)
*   [Figure: Graph showing vibration sensor readings over time, from normal to "Wear evidence", "Performance decrease", "Audible Noise", "Hot to touch", and finally "Motor Fails"]

## Slide 24: An inclusive overview
*   **Diverse Vertical Applications:** Big Data Measurement, Big Data Networking, Big Data Management, Big Data Analytics, Big Data Visualization
*   **Thing Domain:** Thing/Object Domain (Physical or Virtual)
*   **Device Domain (Generate Data):** RFID Networks, Wireless Sensor Networks, Body Area Networks, Vehicular Networks -> Gateways and RFID Readers
*   **Network Domain (Collect Data):** Access Networks (Wired: xDSL, Cable, Fiber, etc. / Wireless: 3G/4G, Satellite, etc.) -> Core Networks (Software-Defined Networks, Content-Centric Networks, etc)
*   **Service Domain (Manage Data):** Services and Applications (Servers in the Cloud Providing Various Services)
*   **User Domain (Access Data):** End-users accessing Raw and Processed Data
*   **End-to-End IoT System:** Spans Edge/Fog Computing and Cloud Computing
*   **Overall:** Big Data Privacy and Security

## Slide 25: VITAL Project – Overall architecture
**National project:** Versatile Internet of Things for AgricuLture – (VITAL)
[Figure: Sensors -> IoT Gateway -> IoT Platform -> Rules System -> Alerts via SMS]

## Slide 26: VITAL Project – IoT Platform
[Figure: Platform architecture]
*   **Events** flow into a Message Broker
*   Processing split into Batch Layer and Streaming Layer
*   Data goes to Serving Layer
*   Queries and Responses interface with VITAL Platform and API
*   Connects to VITAL applications, End Customer, and Service Provider
*   Includes Management Application

## Slide 27-29: VITAL Project – Dashboard view
[Figures: Screenshots of the VITAL Dashboard showing map locations, soil moisture data, irrigation thresholds, control options, and rules engine settings]

## Slide 30: IIoT scenario: A multi-hop topology Low-power and Lossy Network (LLN)
*   **Application:** CBR traffic, converge cast
*   **Environment:** Low power, Multi-hop, Lossy links
*   [Figure: Diagram of nodes A, B, C connecting via radio links and routing links to a Sink]

## Slide 31: Lossy Links
*   **External interference**
    *   Overcrowded ISM band
    *   Co-located wireless networks
    *   Co-located high power networks (e.g., Wi-Fi)
*   **Multi-path fading effect**
    *   Reflective structures
*   **Harsh Industrial Environment**
*   **Lossy Links ->** Unreliability, Unpredictable latency

## Slide 32: MAC Layer Importance
*   **MAC Layer**
    *   Coordinating the accesses to shared wireless medium
    *   Avoiding collisions
    *   Saving Energy
        *   Deafness
        *   Idle listening
        *   Overhearing
*   **Best effort solutions (CSMA, ALOHA) -> Unsuitable for IIoT**
*   **Scheduled-based -> Deterministic Behavior**

## Slide 33: Objective
**To provide Reliable Communications for the IIoT**
*   Improve/purpose MAC mechanisms to provide
    *   High Reliability
    *   Low and Deterministic Delay
**Research methodology**
*   Real-world experiments
*   Trace based - Simulations

## Slide 34: LLN stack
*   **IEEE:**
    *   Low level protocols
    *   Save energy
    *   Reliability
*   **IETF:**
    *   IPv6 Connectivity
*   **6TiSCH:**
    *   Glue TSCH, IPv6
*   **Our Research Efforts:**
    *   Enhance Time-Slotted Channel Hopping (TSCH)
    *   Purpose a Scheduling Function for IIoT

## Slide 35: A hot research topic: Very dense networks
*   Scenarios could be residential environments with a large number of connected users (apartment buildings, residential complexes), offices and other gathering places such as stadiums and concert halls.

## Slide 36: Very dense networks (2)
*   Large number of access points and associated STAs deployed in geographical limited region.
[Figure: Diagrams of WLAN coverage areas packed with many access points and stations]

## Slide 37: Overlapping Basic Service Sets - OBSSs
**Overlapping Basic Service Set (OBSS)**
*   **Case A:** The Information Element (for the channel selection procedure) is exchanged directly between APs that are in direct range of each other
*   **Case B:** The AP can use the neighbor report capability (802.11k amendment) and can request from its associated STAs to scan the medium for neighboring APs and send back a Beacon Report

## Slide 38: IEEE 802.11ax Study Group
**For addressing the mentioned challenges**
*   IEEE 802.11 High Efficiency WLANs (HEW) Study Group (SG) to eventually develop an amendment
**Main goals of amendment**
*   Improve efficiency in dense networks and efficiency/robustness in outdoor deployments
*   Improve power efficiency
*   Enabling backward compatibility and coexistence with legacy IEEE 802.11 devices operating in the same band

## Slide 39: Spatial Reuse
**Efficient parallel utilization of spectrum resources from overlapped WLANs**
**Expected mechanisms for improving spatial reuse by IEEE 802.11ax**
*   **Coloring**
    *   A technique that can identify the packet Basic Service Set (BSS) origination and type of link (upload or download) in a WLAN
    *   We can apply different channel access rules according to coloring information
*   **Adaptive carrier sense threshold**
*   **Adaptive transmitter power**

## Slide 40: Adaptive carrier sense threshold
[Figure: Diagram of AP1 and AP2 with overlapping transmission ranges and CST adjustment]
*   CST level for IEEE 802.11 protocols is static so far
*   Reduction of the CST level reduces the SR (exposed node) while an increase results in more collisions (hidden node)

## Slide 41: Adaptive transmit power
*   Transmit power (Tx) level for IEEE 802.11 protocols is static so far
*   Unnecessary high Tx power level from stations or Access Points increases interference to adjacent overlapped WLANs and power consumption
*   Reducing the Tx power can reduce SNR and data throughput, thus, the proper adjustment is a challenge

## Slide 42: IEEE 802.11ax Task Group proposal
**Spatial reuse TG is considering the implementation of:**
*   **Dynamic Sensitivity Control (DSC)**
    *   Implements coloring and adaptive carrier sense threshold techniques
    *   Applies two different CST levels:
        *   Static for Intra_WLAN packets (CST)
        *   Dynamic for Inter_WLAN packets (Receiver Strength Signal Indication - RSSI is the reference level for adjusting OBSS threshold)

## Slide 43: Project TeamUp5G – Main focus on Small cells
**H2020 Marie Curie ITN project “TeamUp5G: A Multidisciplinary Approach to Training and Research on New RAN Techniques for 5G Ultra-Dense Mobile Networks”**
*   SCs are formed by low-power and reduced-size wireless access points that operate in licensed spectrum and are operator-managed.
*   Due to their low power transmission, SCs can potentially contribute to up to a 60% reduction of power consumption in the global communications infrastructure.
*   Role of Small Cells increases with each "G": 3G (Coverage) -> 4G (CAPEX optimization) -> 5G (Performance & Capacity)

## Slide 44: UDNs in the 5G context
**The ultra-dense networks with small-cells (SCs) are**
*   critical to fulfil the user satisfaction
*   subject of challenging requirements for the evolution to 5G - must be able to meet the requirements of very different types of applications.
*   Nowadays SC solutions have inherent technical limitations
*   Possibly the most important challenge is the demand of increasing data rates per km².

## Slide 45: UDNs in the new 5G context must be able to meet stringent requirements
*   broadband mobile access
*   the ecosystem of the Internet of Things (IoT)
*   This leads to the explosion of SCs that will require new solutions to mitigate interference and optimise the network resources

## Slide 46: Solutions for research: Dynamic Spectrum Management and Optimisation
*   Scheduling and resource allocation become essential components of wireless data systems because different users experience different fading conditions
*   Unlicensed and licensed shared spectrum offer a set of possible advantages, which can potentially lead to greater spectral efficiency than exclusive access
*   Optimization of the access through the use of shared bands and cognitive radio (CR)
*   Dynamic spectrum sharing licensed assisted access (LAA) has been adopted by 3GPP, and LAA has adopted CA as a mandatory function

## Slide 47: Energy Consumption Reduction
*   Mobile network energy consumption is very significant
*   When mixtures of macro and SCs are deployed, the potential of improving becomes even higher
*   Challenging traffic for emerging 5G applications, multi-connectivity ....
*   Further work is needed on mechanisms for energy consumption reduction in the context of “energy-challenged” scenarios such as IoT, particularly considering the increased durations of batteries

## Slide 48: Solutions for research: Dynamic Spectrum Management and Optimisation
*   The project proposes energy-aware MAC protocols with cognitive radio capabilities and optimisations
*   Energy-awareness will be studied for long-range radio technologies
*   Provision M2M traffic serving as backhaul of the network of sensors along with the own cellular traffic

## Slide 49: TeamUp5G Use cases
*   Emergency Drone
*   Predictive Maintenance
*   Multiplayer Game and Live events with VR
*   Safe Family Traveling
[Figure: Radar chart displaying requirements for these use cases across Area traffic capacity, Peak data rate, User experience data rate, Spectrum efficiency, Mobility, Latency, Connection density, and Energy efficiency]

## Slide 50: 5G / IoT challenges (summary)
*   Heterogeneity – Interoperability
*   Scalability – Big Data
*   Identification and Addressing
*   Security – Privacy – Trust
*   Miniaturization of devices
*   Energy efficiency – Greening of IoT
*   Standardization

---

# Lecture 8a - Basics of the IEEE 802.11 MAC sub-layer

## Slide 1
Next-Generation IEEE 802.11 standards
Basics of the IEEE 802.11 MAC sub-layer
Periklis Chatzimisios

## Slide 2 & 3: Contents
*   Carrier Sense Multiple Access basics
*   IEEE 802.11 architecture
*   Physical and virtual channel sensing
*   Access methods in IEEE 802.11 MAC sub-layer
*   IEEE 802.11 MAC basics

## Slide 4: Multiple access protocols
*   single shared broadcast channel
*   two or more simultaneous transmissions by nodes: interference
    *   collision if node receives two or more signals at the same time
*   **multiple access protocol**
    *   distributed algorithm that determines how nodes share channel, i.e., determine when node can transmit
    *   communication about channel sharing must use channel itself!
    *   no out-of-band channel for coordination

## Slide 5: Carrier Sense Multiple Access (CSMA)
**Simple CSMA:** listen before transmit:
*   if channel sensed idle: transmit entire frame
*   if channel sensed busy: defer transmission
*   human analogy: don’t interrupt others!

**Carrier sensing (more detailed)**
*   A prospective sender listens to (“senses”) the channel (“carrier”) before trying to transmit.
*   If the channel is idle, the sender is allowed to transmit.
*   If the channel is busy (i.e. used by another device), the sender defers transmission for a certain time period (“backoff”).
*   The backoff period is determined by one of several strategies.

## Slide 6: CSMA backoff strategies
**Non-persistent CSMA**
*   Sender draws a random waiting (backoff) time from a certain interval [t1, t2]
*   After waiting, sender senses channel again

**Persistent CSMA**
*   Sender continues to sense the channel and awaits end of current transmission
*   Sender then either sends or behaves according to a backoff strategy

**Example: p-persistent CSMA**
*   Once the channel is free, a prospective sender transmits with probability p and waits another fixed backoff period T with probability (1-p)
*   Special case: 1-persistent

## Slide 7: CSMA and collisions
**CSMA/CD:** CSMA with collision detection
*   collisions detected within short time
*   colliding transmissions aborted, reducing channel wastage
*   collision detection easy in wired, difficult with wireless
*   human analogy: the polite conversationalist
*   collisions can still occur with carrier sensing:
    *   propagation delay means two nodes may not hear each other’s just-started transmission
*   collision: entire packet transmission time wasted
    *   distance & propagation delay play role in determining collision probability

## Slide 8: Multiple access links and protocols
**Two types of “links”:**
*   **point-to-point**
    *   point-to-point link between Ethernet switch, host
    *   PPP for dial-up access
*   **broadcast (shared wire or medium)**
    *   old-school Ethernet
    *   upstream HFC in cable-based access network
    *   802.11 wireless LAN, 4G/4G, satellite

## Slide 9: Classification of MAC protocols
*   **Centralized**
    *   Dedicated network nodes (e.g. base stations) allocate channels
*   **Distributed**
    *   All network nodes “cooperate” to regulate channel access
*   **Reservation / Schedule-based**
    *   Channel is reserved for dedicated use of a device pair
    *   Collisions do not occur
*   **Random Access / Contention-based**
    *   Nodes compete for access to a shared channel in a probabilistic manner
    *   Collisions may occur and are resolved
*   **Hybrid schemes**

## Slide 10: Random access protocols
When node has packet to send:
*   transmit at full channel data rate R
*   no a priori coordination among nodes
*   two or more transmitting nodes: “collision”

random access protocol specifies:
*   how to detect collisions
*   how to recover from collisions (e.g., via delayed retransmissions)

examples of random access MAC protocols:
*   ALOHA, slotted ALOHA
*   CSMA, CSMA/CD, CSMA/CA

## Slide 12: Protocol stack of IEEE 802.11
[Figure: Diagram of Protocol Stack showing Application, Transport, Network, Data Link, and Physical layers across a Mobile Device, Access Point, Access Router, and Corresponding Host]
*   **Data Link Layer:** 802.2 LLC, 802.11 MAC
*   **Physical Layer:** 802.11 PHY

## Slide 13: Protocol stack of IEEE 802.11
*   **PHY layer:** Deals with the actual transmission and reception of radio signals, modulation, coding, and basic carrier sensing. Different 802.11 amendments (a/b/g/n/ac/ax) define various PHY characteristics.
*   **MAC sub-layer:** Manages access to the shared wireless medium, defines frame formats, handles error recovery, authentication, and association. It's the focus of architectural discussions.

## Slide 14: IEEE 802.11 MAC sub-layer overview
**Key responsibilities of the IEEE 802.11 MAC:**
*   Medium access control: Determining who gets to transmit and when.
*   Reliable data delivery: Providing mechanisms for acknowledgments, retransmissions, and fragment assembly/disassembly.
*   Frame formatting: Defining the structure of IEEE 802.11 MAC frames (management, control, data).
*   Association and authentication: Managing device connections and security.
*   Power management: Enabling devices to conserve battery life.
*   Quality of Service (QoS): Differentiating and prioritizing traffic types.

## Slide 15: IEEE 802.11 LAN architecture
*   wireless host communicates with base station
    *   base station = access point (AP)
*   **Basic Service Set (BSS),** the fundamental building block of an 802.11 network:
    *   in infrastructure mode it contains wireless hosts and an Access Point (AP) -> base station
    *   in ad hoc mode it contains hosts only
*   **Extended Service Set (ESS):**
    *   A set of connected BSSs forming a larger network

## Slide 16-21: Elements of a wireless (local area) network
*   **wireless hosts**
    *   laptop, smartphone
    *   run applications
    *   may be stationary (non-mobile) or mobile
    *   wireless does not always mean mobility
*   **base station**
    *   typically connected to wired network
    *   relay - responsible for sending packets between wired network and wireless host(s) in its “area”
    *   e.g., cell towers, IEEE 802.11 access points
*   **wireless link**
    *   typically used to connect mobile(s) to base station, also used as backbone link
    *   multiple access protocol coordinates link access
    *   various transmission rates and distances, frequency bands
*   **infrastructure mode**
    *   base station connects mobiles into wired network
    *   handoff: mobile changes base station providing connection into wired network
*   **ad hoc mode**
    *   no base stations
    *   nodes can only transmit to other nodes within link coverage
    *   nodes organize themselves into a network: route among themselves

## Slide 22: Taxonomy of wireless networks
| | single hop | multiple hops |
| :--- | :--- | :--- |
| **infrastructure (e.g., APs)** | host connects to base station (WiFi, cellular) which connects to larger Internet | host may have to relay through several wireless nodes to connect to larger Internet: mesh net |
| **no infrastructure** | no base station, no connection to larger Internet (Bluetooth, ad hoc nets) | no base station, no connection to larger Internet. May have to relay to reach other a given wireless node MANET, VANET |

## Slide 23-24: Mobility of stations
**Q1:** How mobility differentiates from simply being "wireless"?
**Answer:** Wireless implies the absence of physical cables for connection. A device can be stationary but connected wirelessly. Mobility extends this by adding the dimension of movement.

**Q2:** Why a station seems to “move” from a BSS to another one?
**Answer:** (a) A device moves out of range of its current IBSS. (b) Manual selection by the User, disconnecting from one IBSS and then manually selecting and joining a different, from the list of available networks.

## Slide 25: IEEE 802.11 association
*   arriving host: must associate with an AP
    *   scans channels, listening for beacon frames containing AP’s name (SSID) and MAC address
    *   selects AP to associate with
    *   then may perform authentication
    *   then typically run Dynamic Host Configuration Protocol (DHCP) to get IP address in AP’s subnet
*   Note:
    *   SSID (Service Set Identifier): A human-readable name (e.g., "MyHomeWi-Fi," "OfficeNetwork") associated with a BSS or ESS, allowing users to identify and connect to a network.

## Slide 26: IEEE 802.11 Access Point (AP)
*   **Access Point (AP)**
    *   A specialized STA that acts as a central hub and bridge between the wireless BSS and a wired Distribution System (typically an Ethernet network).
*   **Functionality:**
    *   Beaconing: Periodically broadcasts Beacon frames to advertise the presence and capabilities of its BSS.
    *   Association/disassociation: Manages requests from STAs to join or leave its BSS.
    *   Authentication/deauthentication: Handles security processes for STAs.
    *   Buffering: Buffers frames for power-saving STAs.
    *   Frame forwarding: Forwards frames between associated STAs and between the BSS and the DS.

## Slide 27: Characteristics of selected wireless links
[Figure: Chart mapping data rate vs. range for different protocols]
*   **Indoor (10-30m):** 802.11ax (14 Gbps), 802.11ac (3.5 Gbps), 802.11n (600 Mbps), 802.11g (54 Mbps), 802.11b (11 Mbps), Bluetooth (2 Mbps)
*   **Outdoor (50-200m):** 802.11ax, 802.11ac, 802.11n
*   **Midrange outdoor (200m-4Km):** 5G (10 Gbps), 802.11 af,ah, 4G LTE
*   **Long range outdoor (4Km-15Km):** 5G, 4G LTE

## Slide 29: Core principles of CSMA/CA in IEEE 802.11
**How CSMA/CA in IEEE 802.11 works (in principle):**
*   **Carrier sense:** A station first "listens" to the medium to determine if it is currently idle. This involves both physical and virtual carrier sense.
*   **Wait and backoff:** If the medium is busy, or after a transmission, the station waits for a specific InterFrame Space (IFS) and then enters a random backoff process. The various IFSs provide varying priority for different types of frames.
*   **Transmit:** If the medium remains idle after the backoff, the station transmits its frame.
*   **Acknowledgement (ACK):** The receiving station sends an immediate ACK frame upon successful reception.
*   **Retransmission:** If the sender does not receive an ACK, it assumes a collision or loss and retransmits the frame after another backoff.

## Slide 30: Physical carrier sensing in IEEE 802.11
**Physical carrier sensing (Clear Channel Assessment - CCA):**
*   **Mechanism:** Performed at the Physical layer (PHY). A station literally listens to the radio channel for signals.
*   **Detection methods:**
    *   Energy Detect (ED): Checks if the received signal strength (RSSI) on the channel is above a certain threshold. If so, the medium is considered busy.
    *   Preamble Detect (PD): Detects an IEEE 802.11 preamble (the start of an IEEE 802.11 frame). This is more precise as it indicates an actual IEEE 802.11 transmission, not just general noise.
    *   Limitation: Prone to the hidden station problem; a station might not hear another transmitting station, leading to collisions.

## Slide 31: Virtual carrier sensing in IEEE 802.11
**Virtual carrier sensing (Network Allocation Vector - NAV):**
*   It's a timer maintained by each station, indicating the duration for which the medium is expected to be busy. It effectively addresses the hidden station problem.
*   **Setting and utilizing NAV:**
    *   Duration/ID field: Almost all IEEE 802.11 MAC frames (data, management, control) contain a "Duration/ID" field. When a station receives any frame, it reads this field and updates its NAV if the new value is greater than its current NAV.
    *   NAV update: All stations within range hearing any frame update their NAV, effectively "reserving" the medium for the duration specified (even for stations that cannot hear the actual data transmission).
    *   For data frames and acknowledgement (ACK) frames, this field typically indicates the remaining time until the current transmission sequence (e.g., Data + ACK) is complete. For control frames (RTS/CTS) it plays a crucial role in medium reservation.
    *   Principle: A station can only transmit if both its physical carrier sense indicates the medium is idle and its NAV has counted down to zero.

## Slide 32: Virtual channel sensing in IEEE 802.11
[Figure: Timing diagram showing Station A transmitting RTS, Station B sending CTS, A sending Data, B sending ACK. Stations C and D update their NAV based on the RTS/CTS exchange and defer their transmission]

## Slide 33: Performance (throughput)
*   **Ideal situation:** If we could schedule the transmissions perfectly, such that there is neither an overlap and nor a gap between the messages, we could achieve the maximum throughput.

## Slide 34: CSMA in IEEE 802.11 (Basic Access method)
**IEEE 802.11 sender (when trying to send)**
*   Step 1: If sense channel idle for DIFS then transmit frame
*   Step 2: If sense channel busy then:
    *   2.1 Start random backoff timer, count down the backoff timer only while channel idle and freeze when busy (resumes if idle for DIFS)
    *   2.2 Transmit when timer expires
*   Step 3: If ACK received, wait for DIFS, then go to step 2.1
*   Step 4: If no ACK received, double backoff range, select time randomly from range, repeat step 2
**IEEE 802.11 receiver**
*   If frame received successfully then return ACK after SIFS interval (ACK needed due to hidden terminal problem)

## Slide 35: CSMA in IEEE 802.11
**Discussion: How CSMA really works in IEEE 802.11?**
*   **Q1:** Why does the station transmit when timer expires?
*   **Q2:** If ACK received, why do we need to wait for DIFS?
*   **Q3:** Why If no ACK received, why do we need to double backoff range, select time randomly from range and repeat step 2?

## Slide 36: Location dependent carrier sensing
*   **Hidden nodes:** A hidden node is one that is within the range of the intended destination but out of range of the sender
*   **Exposed nodes:** An exposed node is one that is within the range of the sender but out of range of the destination
*   **Capture:** This event occurs when a receiver can correctly receive a transmission from one of two (or more) simultaneous transmissions, all within its range, because the signal strength of the correctly received signal is much higher than strength of the other signals

## Slide 37: Wireless link characteristics: Hidden nodes
*   **Hidden node problem:**
    *   B, A hear each other
    *   B, C hear each other
    *   A, C can not hear each other means A, C unaware of their interference at B
*   **Attenuation also causes “hidden nodes”:**
    *   B, A hear each other
    *   B, C hear each other
    *   A, C can not hear each other interfering at B

## Slide 38: Wireless link characteristics: Exposed nodes
*   B is transmitting to A
*   C wants to transmit to D
*   C senses transmission & declines even if its transmission to D will not cause any collision to A

## Slide 39: Wireless link characteristics: Capture problem
*   If A and C transmit simultaneously to B then the signal power of C, received at B, is higher than the one from A and there is a good probability that C’s signal can be correctly decoded in the presence of A’s transmission.
*   This capture of C’s signal can improve protocol performance, but it results in unfair sharing of the channel with preference given to nodes closer to the receiver.

## Slide 40: Wireless link characteristics: multipath
*   **Multipath propagation:** radio signal reflects off objects ground, built environment, arriving at destination at slightly different times.

## Slide 41: Collision avoidance through exchange of RTS-CTS
*   **RTS/CTS mechanism**
    *   Collision for long packets is wasteful
    *   RTS (Request to Send): Request to reserve channel to send long packet w/o collisions
    *   CTS (Clear to Send): Approve RTS
    *   Optional mechanism
*   **idea: sender “reserves” channel use for data frames using small reservation packets**
    *   sender first transmits short request-to-send (RTS) packet to receiver using CSMA
    *   BS broadcasts clear-to-send CTS in response to RTS
    *   CTS heard by all nodes
        *   sender transmits data frame
        *   other stations defer transmission

## Slide 42: Collision avoidance through exchange of RTS-CTS
*   RTS‐CTS handshake used to resolve hidden terminal problem and shorten the duration of collisions
    *   RTS = Ready to Send; transmitted by sender to inform receiver of available data
    *   CTS = Clear to Send; broadcasted by receiver to inform all neighbors that channel will be occupied
    *   ACK = Acknowledgement; broadcasted by receiver to inform all neighbors that channel is free again

## Slide 43-46: Collision avoidance through exchange of RTS-CTS (Discussion)
*   **Q1: Do we have collisions with the use of RTS/CTS?**
    *   **Answer:** The RTS/CTS handshake reduces number of collisions (not avoids them completely). RTSs may still collide with each other (but they’re short), thus, collision duration is reduced.
*   **Q2: Is there any overhead that RTS/CTS adds?**
*   **Q3: The RTS/CTS frames are always transmitted using the control rate that is lower than the data rate. Do you revise your previous reply regarding overhead?**
    *   **Answer:** The RTS/CTS handshake adds significant signaling overhead, especially if data messages are short.
*   **Q4: Could you propose some ideas for the optimum use of RTS/CTS? When it is beneficial to be employed?**
    *   **Answer:** The RTS/CTS depends on the size of data frames and the frequency of collisions (potential presence of hidden stations or dense environments). Can we tell if they are hidden stations in our network? Can we find the number of stations in the network?
*   **Note:** Stations typically use an RTS Threshold parameter (configurable on APs and wireless clients). If the size of the data frame to be transmitted exceeds this threshold, the RTS/CTS handshake is initiated.

## Slide 48: Access methods in IEEE 802.11 MAC sub-layer
*   **DCF (Distributed Coordination Function)**
    *   Ad hoc and infrastructure mode
    *   Contention based distributed system
    *   Mandatory
*   **PCF (Point Coordination Function)**
    *   Infrastructure mode, optional
    *   Contention free centralized system
    *   Polling to coordinate senders, e.g. to ensure QoS
    *   For real time service

## Slide 49: Access methods in IEEE 802.11 MAC sub-layer
*   **Hybrid Coordination Function (HCF):** The QoS-aware successor, including:
    *   **Enhanced Distributed Channel Access (EDCA):** Contention-based with priorities.
    *   **HCF Controlled Channel Access (HCCA):** Centralized, scheduled access for guaranteed QoS.

## Slide 50-51: Distributed Coordination Function (DCF) - Basic Access method
[Figures: Timing diagrams demonstrating DIFS, SIFS, Contention Window, and backoff slots for the Basic Access method]

## Slide 52: Point Coordination Function (PCF)
*   PCF is an optional access method in the original IEEE 802.11 standard that operates under the control of a Point Coordinator (PC), which is typically the Access Point (AP).
*   Unlike the contention-based DCF, PCF uses a polling mechanism. The PC (AP) grants permission to stations to transmit, eliminating contention during the Contention-Free Period (CFP).
*   **Operation during CFP:**
    *   The AP begins a CFP by sending a special Beacon frame that indicates the start and duration of the CFP.
    *   During the CFP, the AP uses PIFS to gain priority over DCF stations.
    *   The AP polls stations in a round-robin fashion using CF-Poll frames.
    *   A polled station can transmit one data frame (or a combined data/ACK frame) after receiving a CF-Poll, without contention.
    *   If a polled station has no data, it sends a Null frame or CF-ACK.
    *   At the end of the CFP (or if no response to polling), the AP sends a CF-End frame to revert to DCF mode.

## Slide 53: Point Coordination Function (PCF)
[Figure: Timing diagram showing Contention Free Repetition Interval containing Contention Free Period and Contention Period, mapping CF-Poll, CF-Up Frame, CF-Down Frame, etc.]

## Slide 55: Transmission procedure
[Figure: Flowchart describing the transmission procedure (Wait for frame -> Medium idle? -> Wait IFS -> Transmit frame vs Backoff mechanisms)]

## Slide 56: Busy channel and backoff
*   A node backs off upon a busy medium as follows:
    *   The node sets a **backoff counter** to a random integer value rand from the interval [0, CW]. This interval is called **contention window**.
    *   Whenever the medium is idle for a period of Δ, the node decreases this counter by one.
    *   If the channel is busy during a period Δ, the node freezes the counter until the channel is idle again.

## Slide 57-58: Backoff procedure
*   To avoid collision, backoff stage is considered to determine the contention window (CW). A station picks up a random number in the current contention window.
*   The Binary Exponential Backoff (BEB) scheme is used as follows:
    *   CW = 2^k(CWmin+1) -1 , where k = the backoff stage (0,…K)
*   Upon success (ACK received): CW = CWmin

**Discussion: How backoff procedure works in IEEE 802.11?**
*   **Q1:** Why we double the contention window after every failed transmission?
*   **Q2:** Why do we keep constant the contention window after reaching the maximum value (CWmax)?
*   **Q3:** Why do we reset the contention window to CWmin after a successful transmission?

## Slide 59: Example of Basic Access and backoff
[Figure: Timing diagram showing station A and station B transmitting with backoff counters decrementing during idle periods]

## Slide 60: Example of RTS/CTS and backoff
[Figure: Detailed timing diagram tracking backoff counters, NAVs, RTS, CTS, DATA, and ACK across multiple stations]

## Slide 61: Fragmentation
[Figure: Timing diagram depicting fragmentation where a single data payload is broken down into Fragment 0, Fragment 1, Fragment 2, with corresponding ACKs and SIFS spacings]

## Slide 62: Retry limit
*   Stations maintain a Station Short Retry Counter (SSRC) and Long Retry Counter (SLRC).
    *   SSRC increases by one for each failed RTS frame or data frame when RTS/CTS is not utilized for this transmission.
    *   SLRC increases by one for each failed data frame when RTS/CTS is utilized for this transmission.
    *   Both counter is reset upon a successful transmission.
    *   Retry is aborted when SSRC or SLRC reach the defined retry limit. The station then proceeds with the transmission of the next frame on the queue.
*   **Question for discussion:** Why IEEE 802.11 considers a retry limit for frame transmissions?

## Slide 63-67: Example of DCF operation
[Figures: Sequential timing diagrams showing devices A, B, C, D, E attempting to transmit, backing off, deferring access, and finally successfully transmitting data over the medium]
