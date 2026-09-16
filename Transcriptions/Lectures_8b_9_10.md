# Transcriptions: Lectures 8b, 9, 10

## Lecture 8b - Introduction to IEEE 802.11 standards
### Slide 1
Next-Generation
IEEE 802.11 standards
Introduction to the IEEE 802.11 standards
Periklis Chatzimisios

### Slide 2
Department of Information and Electronic Engineering
International Hellenic University
Introduction to IEEE 802.11
Contents
* Introduction on Wi-Fi
* Traffic volumes and use cases of Wi-Fi
* History and evolution of Wi-Fi
* Standardization process

### Slide 3
Department of Information and Electronic Engineering
International Hellenic University
Introduction to IEEE 802.11
Contents
* Introduction on Wi-Fi
* Traffic volumes and use cases of Wi-Fi
* History and evolution of Wi-Fi
* Standardization process

### Slide 4
Department of Information and Electronic Engineering
International Hellenic University
Introduction on Wi-Fi
(Global) value of Wi-Fi
(Sep 2020) USA Internet Demand Still High
+73% Average devices active online at home during working hours (vs. Jan-2020) 1
+40% Average household broadband usage per month (YOY vs. Sep-2019)2
+31% Peak upstream (videoconferencing) broadband traffic (vs.Mar 2020) 3
USA Internet Connectivity’s Importance Will Continue to Increase
+84% of USA businesses will increase WFH capacity post pandemic5
$186B ($2T) USA CARES Act funding available for telehealth & education remote learning6
Wi-Fi’s Role Is Rapidly Growing Globally
51% of 2022 IP traffic is from Wi-Fi devices4
59% of 2022 mobile data offloaded to Wi-Fi4
Wi-Fi Products Leverage the Latest Technologies to Support Evolving User Needs
Wi-Fi 6 Today: 3x faster speeds7, 75% lower latency8, 4x device capacity9
Wi-Fi 6E ~2021: Broad gigabit speed enabling, Reduced interference, Improved responsiveness
Wi-Fi 7 ~2024: Nearly 5x faster speeds10, Ultra-low latency, Enhanced reliability

### Slide 5
Department of Information and Electronic Engineering
International Hellenic University
Introduction on Wi-Fi
(Global) value of Wi-Fi
Global Value of Wi-Fi11
11Wi-Fi Alliance® and Telecom Advisory Services for Wi-Fi Alliance®, 2024 (https://www.wi-fi.org/discover-wi-fi/value-wi-fi)
Wi-Fi by the numbers11
[Figure: Diagram of economic value and shipments of Wi-Fi]

### Slide 6
Department of Information and Electronic Engineering
International Hellenic University
Introduction on Wi-Fi
Cellular vs. Wi-Fi
Mobile cellular networks:
* Licensed spectrum allocated to a single operator
* Interference is under control via cell planning and radio resource management
[Figure: Cellular network with interference under control]
Wi-Fi networks:
* Unlicensed spectrum (ISM bands), anyone can deploy a Wi-Fi network
* Subject to uncontrolled interference
* Packet collisions avoided via Distributed Coordination Function (DCF), comprising:
  * CSMA/CA + binary exponential backoff
  * Physical carrier sensing
  * Virtual carrier sensing: RTS/CTS, NAV, IFS
  * Auto repeat request (ARQ)
[Figure: Wi-Fi network with uncontrolled interference]
Source: “Where Wi-Fi meets Ultra-High Reliability”, IEEE Meditcom, 2024.

### Slide 7
Department of Information and Electronic Engineering
International Hellenic University
Introduction on Wi-Fi
Wi-Fi generations
[Figure: Infographic showing Wi-Fi 4, 5, 6, and 7 specifications]
Source: “Wi-Fi Sensing: Use Cases, Standard Technologies, and Ecosystem Enablement”, Intel, 2024.

### Slide 8
Department of Information and Electronic Engineering
International Hellenic University
Introduction on Wi-Fi
IEEE 802.11 standard evolution
[Figure: Diagram of IEEE 802.11 standard evolution from 1997 to 2023 with icons for devices]
Source: “Wi-Fi 7”, Huawei, 2025.

### Slide 9
Department of Information and Electronic Engineering
International Hellenic University
Introduction on Wi-Fi
History and future of Wi-Fi
[Figure: The HISTORY and FUTURE of Wi-Fi infographic by Rohde & Schwarz]

### Slide 10
Department of Information and Electronic Engineering
International Hellenic University
Introduction on Wi-Fi
Ongoing standardization
[Figure: Timeline of Ongoing standardization showing UHR, Wi-Fi 7, and Wi-Fi 8]
Source: “Where Wi-Fi meets Ultra-High Reliability”, IEEE Meditcom, 2024.

### Slide 11
Department of Information and Electronic Engineering
International Hellenic University
Introduction to IEEE 802.11
Contents
* Introduction on Wi-Fi
* Traffic volumes and use cases of Wi-Fi
* History and evolution of Wi-Fi
* Standardization process

### Slide 12
Department of Information and Electronic Engineering
International Hellenic University
Traffic volumes and use cases of Wi-Fi
Use cases from the past (how many years ago?)
[Figure: Diagram of a router connecting to multiple devices like PC, Smartphone, Cameras, TVs, NAS]

### Slide 13
Department of Information and Electronic Engineering
International Hellenic University
Traffic volumes and use cases of Wi-Fi
Use cases from the past (how many years ago?)
[Figure: Images of instant wireless sync, wireless display, cordless computing, internet access]

### Slide 14
Department of Information and Electronic Engineering
International Hellenic University
Traffic volumes and use cases of Wi-Fi
Internet of Things (IoT) architecture
[Figure: IoT architecture showing Thing, Gateway, Connectivity, Cloud-side, User-side Apps]

### Slide 15
Department of Information and Electronic Engineering
International Hellenic University
Traffic volumes and use cases of Wi-Fi
Verticals
Source: Keysight Technologies
Smart Wearables, Smart Home, Smart City, Smart Agriculture
Connected Car, Health Care, Industry Automation, Smart Energy

### Slide 16
Department of Information and Electronic Engineering
International Hellenic University
Traffic volumes and use cases of Wi-Fi
Very dense environments
[Figure: Diagram showing WLAN coverage area with overlapping ranges]

### Slide 17
Department of Information and Electronic Engineering
International Hellenic University
Traffic volumes and use cases of Wi-Fi
Vehicle-to-everything (V2X)
[Figure: Images of V2X connectivity in urban and highway environments]

### Slide 18
Department of Information and Electronic Engineering
International Hellenic University
Traffic volumes and use cases of Wi-Fi
Moving to 2030
Source: “Wi-Fi Sensing: Use Cases, Standard Technologies, and Ecosystem Enablement”, Intel, 2024.
[Figure: The Wireless World in 2030 infographic]

### Slide 19
Department of Information and Electronic Engineering
International Hellenic University
Traffic volumes and use cases of Wi-Fi
Smart farm
* A single AP covered the multi-acre farm, including multiple greenhouses and a small shop.
[Figure: Photos and heatmaps of Green House Coverage and Whole Farm Coverage]
Source: “IEEE 802.11 Standards development enables innovation and productivity enhancements to build economic value”, IEEE 802, 2024.

### Slide 20
Department of Information and Electronic Engineering
International Hellenic University
Traffic volumes and use cases of Wi-Fi
Smart industrial complex
* Two AP are able to cover the entire 1 km by 300m industrial site, with multiple high-bay workshops and large heavy equipment moving around the site.
[Figure: Photos and heatmap of a smart industrial complex]
Source: “IEEE 802.11 Standards development enables innovation and productivity enhancements to build economic value”, IEEE 802, 2024.

### Slide 21
Department of Information and Electronic Engineering
International Hellenic University
Industrial environments
Traffic volumes and use cases of Wi-Fi
[Figure: Images of robotic arms in industrial environments]

### Slide 22
Department of Information and Electronic Engineering
International Hellenic University
Introduction to IEEE 802.11
Contents
* Introduction on Wi-Fi
* Traffic volumes and use cases of Wi-Fi
* History and evolution of Wi-Fi
* Standardization process

### Slide 23
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
The IEEE 802.11 Working Group is one of the most active WGs in 802
IEEE 802.11 WG Voting Members: 600+
[Figure: Diagram of IEEE 802 LMSC structure and OSI Reference Model]
Source: “IEEE 802.11 Overview and Amendments under development”, IEEE 802, 2025.

### Slide 24
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
Development of the IEEE 802.11 Standard is ongoing since 1997
[Figure: Timeline from 1997 to 2024 showing IEEE 802.11 standards]
Source: “IEEE 802.11 Overview and Amendments under development”, IEEE 802, 2025.

### Slide 25
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
Completed standards
IEEE 802.11-2020 Revision project
Includes the following amendments:
* IEEE 802.11ah – Operating in license-exempt bands below 1 GHz (excl. TV bands)
* IEEE 802.11ai – Fast initial link set-up
* IEEE 802.11aj – Enable 802.11ad operation in the Chinese 59-64 GHz frequency band.
* IEEE 802.11ak – General Link
* IEEE 802.11aq – Pre-association Service Discovery
Source: “IEEE 802.11 Overview and Completed Amendments”, IEEE 802, 2025.

### Slide 26
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11ah defines OFDM PHY and MAC operating in license-exempt bands below 1 GHz (excl. TV bands)
Define OFDM PHY and MAC operating in license-exempt bands below 1 GHz (excl. TV bands)
* Extended range
* Power efficiency
* Large number of devices
Potential applications
* Internet of everything (IoT)
* Smart Grid
* Healthcare
* Smart Appliances
* Wearable consumer electronics
[Figure: Diagram of healthcare monitoring]

### Slide 27
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11ai defines fast initial link set-up methods
This amendment defines mechanisms that provide IEEE 802.11 networks with fast initial link set-up methods which do not degrade the security currently offered by Robust Security Network Association (RSNA) already defined in IEEE 802.11.
The project’s primary need came from an environment where mobile users are constantly entering and leaving the coverage area of an existing extended service set (ESS).
* scale with a high number of users simultaneously entering an ESS
* minimize the time spent within the initial link set-up phase
* securely provide initial authentication.
[Figure: Images of people in urban and transit environments]

### Slide 28
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11aj defines modifications to 802.11ad to enable operation in the Chinese 59-64 GHz frequency band
This amendment defines modifications to the IEEE P802.11ad Physical (PHY) layer and the Medium Access Control (MAC) layer to enable operation in the Chinese 59-64 GHz frequency band.
The amendment maintains backward compatibility with 802.11ad when it operates in the 59-64 GHz frequency band.
The amendment also defines modifications to the PHY and MAC layers to enable the operation in the Chinese 45 GHz frequency band. The amendment maintains the 802.11 user experience.

### Slide 29
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11ak enables an 802.11 connection to be used as a through link in a general network
This amendment enables an 802.11 connection to be used as a through link in a general network, not just as a connection to an end station at the edge of a network.
Fully general mixed 802.11 and wired plug and play in the home.
Data Center top-of-rack to top-of-rack connections for overflow traffic.
Industrial and Enterprise network use.

### Slide 30
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11aq enables the delivery of pre-association Service Discovery information
A typical use case is printer discovery in a hotel.
Pre-association protocol designed to discover services on a WLAN.
[Figure: Diagram showing discovery of different printers]

### Slide 31
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
Completed standards
IEEE Std 802.11-2024 Revision project
Includes the following amendments:
* IEEE Std 802.11ax-2021 – Increased throughput & efficiency in 2.4, 5 (and 6) GHz bands
* IEEE Std 802.11ay-2021 – Support for 20 Gbps in 60 GHz band
* IEEE Std 802.11az-2022 – 2nd generation positioning features
* IEEE Std 802.11ba-2021 – Wake up radio. Low power IoT applications
* IEEE Std 802.11bb-2023 – Light Communications
* IEEE Std 802.11bc-2023 – Enhanced Broadcast Service
* IEEE Std 802.11bd-2022 – Enhancements for Next Generation V2X
* IEEE Std 802.11be-2024 – Enhancements for extremely high throughput (EHT)
* IEEE Std 802.11bh-2024 – Operation with Randomized and Changing MAC Addresses
Source: “IEEE 802.11 Overview and Completed Amendments”, IEEE 802, 2025.

### Slide 32
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11ax is focused on improving performance in dense environments
Existing 802.11 WLAN systems serve dense deployments. IEEE 802.11ax further improves performance of WLAN deployments in dense scenarios:
* Targeting at least 4x improvement in the per-STA throughput compared to 802.11n and 802.11ac.
* Improved efficiency through spatial (MU MIMO) and frequency (OFDMA) multiplexing.
Dense scenarios are characterized by large number of access points and large number of associated STAs deployed in geographical limited region (e.g. a stadium or an airport).
[Figure: Image of a crowded stadium/airport]

### Slide 33
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11ay is defining next generation 60 GHz: increased throughput and range
20Gbps+ rates are defined
License-Exempt bands above 45 Gbps
Completion in 2020
Use Cases:
* Ultra-Short Range
* 8K UHD - Smart Home
* AR/VR and wearables
* Data Center Inter Rack connectivity
* Video / Mass-Data distribution
* Mobile Offloading and MBO
* Mobile Fronthauling
* Wireless Backhauling (w. multi-hop)
* Office Docking
* Fixed Wireless
Key additions:
* SU/ MU MIMO, up to 8 spatial streams
* Channel bonding
* Channel aggregation
* Non-uniform constellation modulation
* Advanced power saving features

### Slide 34
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11az Next Generation Positioning
The P802.11az project Next Generation Positioning extends accurate IEEE Std 802.11-2016 Fine Timing Measurement capabilities:
* Accurate indoor Navigation (sub 1m and into the <0.1m domain).
* Enables self-locating networks for easy, fast and cost efficient WLAN deployment for navigation and 6GHz AFC operation.
* Secured (authenticated and private) positioning – open my car with my smartphone, position aware services (money withdrawal).
* Unlock computer with a wearable device, adapt TV content to audience presence.
* Location based link adaptation for home usages (connect to best AP).
* Navigate in extremely dense environments (stadium/airport scenarios).
[Figure: Images of AR navigation, smart watch, smart home, and crowded airport]

### Slide 35
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11ba improves energy efficiency of stations and maintains low latency
802.11 radio needs to wake up periodically to receive data within a latency requirement → high power consumption of 802.11 station
[Figure: Diagram comparing short sleep interval vs long sleep interval with AP buffers data]

### Slide 36
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11bb Light Communications
Ability to re-use existing HT, VHT and HE PHY/MAC.
Use Cases:
* Industrial wireless applications
* Medical environments
* Enterprise
* Home
* Backhaul
* Vehicle to Vehicle Communication
* Underwater Communication
* Gas Pipeline Communication
Key additions:
* Uplink and downlink operations in 800 nm to 1000 nm band
* Minimum single-link throughput of 10 Mb/s
* Interoperability among solid state light sources with different modulation bandwidths.

### Slide 37
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11bc is defining Enhanced Broadcast Services
Enhanced Broadcast Services (eBCS) defines broadcast service enhancements within an 802.11-based network.
Client end devices broadcast information to an AP, e.g. in an IoT environment, to other STAs so that any of the receiving APs act as an access node to the Internet.
Broadcast Downlink
* Provides enhanced Broadcast Services (eBCS) of data (e.g. videos) to a large number of densely located STAs.
* These STAs may be associated, or un-associated with the AP or may be low-cost STAs that are receive only.

### Slide 38
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11bd defines an evolution of 802.11p for Vehicle to Anything (V2X)
IEEE 802.11p is largely based on 802.11a.
IEEE 802.11bd defines MAC/PHY enhancements from 802.11n, ac, ax, to provide a backwards compatible next generation V2X protocol.
* Higher Throughput
* Longer Range
* Support for Positioning
* Backward Compatibility
[Figure: Puzzle pieces showing Longer Range, Higher Throughput, Backwards Compatibility, Positioning]

### Slide 39
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11bd: Next Generation V2X Use Cases
5.9 GHz band mainly, and optionally 60 GHz
V2X Use Cases:
* Suport all defined DSRC/802.11p use cases, including Basic safety message (safety, range, backward compatibility, fairness)
* Sensor sharing (throughput)
* Multi-channel operation (safety channel + other channels)
* Infrastructure applications (throughput)
* Vehicular positioning & location (LoS and NLoS positioning accuracy)
* Automated driving assistance (safety, throughput)
* Aerial vehicle IT application (video)
* Train to train (high speed)
* Vehicle to train (high speed, long range)
Key additions (comparing to 802.11p):
* Higher throughput (2x)
* Longer range
* Support for positioning
* Backward compatibility with 11p

### Slide 40
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11be Extremely High Throughput amendment builds on 802.11ax, including 6GHz support
Extremely High Throughput (EHT)
Operation in 2.4 GHz, 5 GHz, and 6 GHz bands
Higher throughout – Project goal of at least 30 Gbps; expect 40+Gbps with 320MHz channels, 4096 QAM
Support for low latency communications
Use Cases:
* Home, enterprise, industrial, IoT
* Outdoor
* AR/VR, wireless gaming
* 4K and 8K video streaming
* Remote office
* Cloud/edge computing
* Video calling and conferencing

### Slide 41
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
Market demands and new technology drive IEEE 802.11 innovation
Demand for throughput
* Continuing exponential demand for throughput (802.11be and 802.11bn)
* Most (50-80%, depending on the country) of the world’s mobile data is carried on 802.11 (Wi-Fi) devices
New usage models / features
* Dense deployments (802.11be), Indoor Location (802.11az, 802.11bk),
* Automotive (802.11bd, AUTO)
* WLAN Sensing (802.11bf)
Technical capabilities
* Millimetric (42-71 GHz) radios (802.11bq)
Changes to regulation
* 6 GHz (802.11be)
* Coexistence and radio performance rules (e.g., ETSI BRAN, ITU-R)

### Slide 42
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
IEEE 802.11 standards pipeline (January 2025)
[Figure: Diagram of IEEE 802.11 standards pipeline]
Source: “IEEE 802.11 Overview and Amendments under development”, IEEE 802, 2025.

### Slide 43
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
New IEEE 802.11 radio technologies
Under development to meet expanding market needs and leverage new technologies
802.11bf – WLAN Sensing
802.11bi – Enhanced Data Privacy
802.11bk – 320 MHz Positioning
802.11bn – Ultra High Reliability
802.11bp – Ambient Power for IOT
802.11bq – Integrated Milli Metric Wave
ELC – Enhanced Light Communication Study Group
AUTO – Automotive Topic Interest Group
AI / ML – Artificial Intelligence / Machine Learning Group

### Slide 44
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
Wi-Fi standard evolution: 802.11bn is now under development
[Table: Wi-Fi standard evolution]
Source: “IEEE 802.11 Overview and Amendments under development”, IEEE 802, 2025.

### Slide 45
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
IEEE 802.11bn: Ultra High Reliability (UHR)
Expected to be the basis for Wi-Fi 8
Expected improvements:
* Reduce tail latency
* Reduce roaming latency by taking advantage of multi-link features
* Allow access on secondary channel while primary channel is busy
* AP power save
* Security enhancements, e.g., control frame protection
* Extend range by reducing sensitivity gap between client and AP
* Multi-AP coordination
[Figure: Diagram showing Longer Range, Higher Throughput, Backwards Compatibility, Positioning]

### Slide 46
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11bf Sensing
IEEE 802.11bf is developing a protocol for environmental sensing
Measurements that can be used to monitor environmental conditions and changes (e.g., people movement, number of people present, room occupancy)
Built on sounding (beamforming) waveforms
WLAN sensing uses PHY and MAC features of IEEE 802.11 stations to obtain measurements that may be useful to estimate features of objects in an area of interest.
* Features = Range, velocity, angular, motion, presence or proximity, gesture, etc.
* Objects = Human, animal, etc.
* Area of interest = Room, car, enterprise, etc.
[Figure: Diagram of home monitoring]

### Slide 47
Department of Information and Electronic Engineering
International Hellenic University
History and evolution of Wi-Fi
802.11bf Sensing
Use cases:
1. Smart home
2. Presence and proximity detection
3. Gesture recognition
4. Gaming control
5. Vital signs / Liveness
6. Location in store
7. Audio with user tracking (Follow-me sound)
8. Sneeze sensing
[Figure: Images illustrating the use cases]

### Slide 48
Department of Information and Electronic Engineering
International Hellenic University
Introduction to IEEE 802.11
Contents
* Introduction on Wi-Fi
* Traffic volumes and use cases of Wi-Fi
* History and evolution of Wi-Fi
* Standardization process

### Slide 49
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
What standards are (in a wide sense)
The most general definition for a «standard» may be
«a widely agreed way of doing something» .....
.... where, depending on the specific area of application, “doing something” may be replaced by, e.g., “designing a product”, “building a process”, “implementing a procedure” or “delivering a service”.
«Standard» (i.e. agreed and common) ways of doing things bring lot of benefits; our technological world without «standards» simply would not work (or, at least, it would be harder to make it work)
Source: “Understanding ICT Standardization: Principles and Practice”, ETSI, 2021

### Slide 50
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
What standards are? (various definitions)
Standards are published documents that establish specifications and procedures designed to maximize the reliability of the materials, products, methods, and/or services people use every day. Standards address a range of issues, including but not limited to various protocols to help maximize product functionality and compatibility, facilitate interoperability and support consumer safety and public health. (definition by IEEE Standards Association, IEEE-SA)
Standard is a document, established by consensus and approved by a recognized body, that provides, for common and repeated use, rules, guidelines or characteristics for activities or their results, aimed at the achievement of the optimum degree of order in a given context. (derived from ISO/IEC Guide 2:1996, definition 3.2)
Standards are produced by a variety of organizations, including scientific and professional associations, industry and trade organizations and governments.

### Slide 51
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Why Standards?
* Interoperability: The paramount benefit. Standards ensure that products, systems, and services from different manufacturers can communicate and function together seamlessly (e.g., charging your phone with any USB-C charger, connecting to any Wi-Fi network).
* Market efficiency: Reduces market fragmentation and creates larger, more predictable markets, benefiting both producers and consumers (more choice, lower prices).
* Innovation catalyst: Provides a stable base layer, allowing companies to focus their innovation efforts on value-added features and applications built upon common standards.
* Quality and reliability: Standards often include performance metrics, testing procedures, and best practices, leading to higher quality and more reliable products and services.
* Safety and health: Many standards directly address safety requirements, environmental impacts, and ergonomic considerations, protecting users and the environment.
* Facilitating trade: International standards remove technical barriers, simplifying global trade and commerce.

### Slide 52
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Different types of standards
According to the development process (standardization)
De facto standards, or standards in actuality, are adopted widely by an industry and its customers. These standards arise when a critical mass simply likes them well enough to collectively use them.
De jure standards are produced by devoted organizations, called Standards Development Organizations (SDOs). SDOs are organizations whose purpose is to develop standards and that put in place formal well-defined procedures to guarantee a fair development process.
[Figure: Logos of various SDOs]

### Slide 53
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
What are SDOs?
An SDO is an organization whose primary activities include developing, coordinating, promulgating, revising, amending, or interpreting voluntary consensus standards.
* Purpose: SDOs bring together diverse stakeholders – including industry experts, academics, government officials, regulators, and consumer representatives – to collaborate on technical specifications.
* Voluntary consensus: The standards developed are typically voluntary, meaning their adoption is not legally mandated (though they may be incorporated into regulations). They are also "consensus-based," signifying general agreement among participants.
SDOs are crucial for:
* Ensuring interoperability between different products and systems.
* Fostering innovation by providing stable technical foundations.
* Promoting market growth and reducing technical barriers to trade.
* Enhancing safety, quality, and environmental sustainability.

### Slide 54
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
What standards are NOT & classification of SDOs
Standards are NOT regulations
* While conformity with standards is voluntary, regulations are compulsory
Standards are NOT a set of thorough design rules
* Standards are aimed at defining a minimum set of requirements for an item (product, service, process, etc.) in order to make it meet certain well-defined objectives
Standards are voluntary NOT compulsory
Standardization landscape includes multiple SDOs that may differ in:
* Geographical coverage
* Technical scope of activities (as per each SDO’s statute)
* Level of recognition from regulatory or political organizations

### Slide 55
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Standards in everyday life
[Figure: Diagrams of standards in everyday life and various SDOs]
Source: “Understanding ICT Standardization: Principles and Practice”, ETSI, 2021

### Slide 56
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Classification of SDOs
International SDOs
* These have members worldwide, which sometimes also include national or regional standard bodies, and their deliverables have worldwide coverage.
Regional SDOs
* These have members (industries, academia and national SDOs) from countries that usually share, or are interested in promoting common practices and regulations.
National SDOs
* National SDOs operate at the single country level and issue country-specific standards; they often collaborate with International and Regional SDOs.
[Figure: Logos of various SDOs]

### Slide 57
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Classification of SDOs - Examples of scope of activities
[Table: SDOs and their scope of activity]
Source: “Understanding ICT Standardization: Principles and Practice”, ETSI, 2021

### Slide 58
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Core principles of standardization by SDOs
While specific procedures vary, most reputable SDOs adhere to common principles:
* Consensus: Decisions are based on general agreement among participants, ensuring that no single interest group can dominate. It implies reconciliation of conflicting arguments.
* Openness: The process is transparent, and all interested and qualified parties are eligible to participate, ensuring a broad range of perspectives.
* Due process: A formal, documented procedure is followed at every stage, providing fairness, transparency, and a path for appeals.
* Technical merit: Standards must be technically sound, relevant to market needs, and technologically feasible.
* Global relevance: Standards should aim for worldwide applicability and not create unnecessary trade barriers.
* Intellectual Property Rights (IPR) policy: Fair, reasonable, and non-discriminatory (FRAND/RAND) licensing of essential patents is typically required.

### Slide 59
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
The role of IEEE in standardization
* IEEE (Institute of Electrical and Electronics Engineers) is the world's largest technical professional organization dedicated to advancing technology for the benefit of humanity. It has over 400,000 members in over 160 countries.
* Role in standardization: IEEE is a leading developer of international standards in a broad range of industries, particularly in electronics, power, computing, and communications.
* Impact: IEEE standards are fundamental to the operation of countless technologies, from Wi-Fi and Ethernet to power grids and medical devices, enabling interoperability and driving innovation globally.
* IEEE Standards Association (IEEE-SA) is the organizational unit within IEEE responsible for managing the standardization process. It is composed of individual members and corporate organizations from around the world.

### Slide 60
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
The standards development lifecycle
IEEE Comm. Society Standards Development Board (IEEE COM/SDB) *
* Sponsors standards in communications & networking
[Figure: Diagram of standards development process]
Source: “IEEE-SA quick reference guide standards development process” and https://standards.ieee.org/about/policies/bylaws/ (IEEE-SA Standards Board)

### Slide 61
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Process flow
[Figure: Diagram showing Process flow from Idea to Publish Standard]
It is a very long and complicated process!

### Slide 62
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Getting Started
The idea or concept needs to be well defined and accepted for standardization
The Standard is developed under the guidance of a sponsor (e.g., IEEE COM/SDB)
[Figure: Diagram showing getting started process]

### Slide 63
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Project authorization
A potential working group or study group gathers to work on the Project Authorization Request (PAR), up to six months before a PAR needs to be submitted.
With the support of the sponsor, submit a PAR to IEEE-SA Standards Board (SASB) for an approval to start the project.
PAR is reviewed by New Standards Committee (NesCom)* and based on its recommendation, IEEE-SA Standards Board (SASB) approves/disapproves the project.
[Figure: Diagram showing project authorization process]

### Slide 64
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Draft development
Working group (WG)* is created/maintained under policies and procedures (P&P) of the sponsoring committee (e.g., IEEE P1955 Standard for 6G Empowering Robotics: Use Case Scenarios, Requirements, Architectural Impact, and Technical Assumptions).
WG officers are designated to start the development of the standard. Write drafts of the standard.
Submit finalized draft Mandatory Editorial Coordination (MEC) to ensure conformance with IEEE requirements.
[Figure: Diagram showing draft development process]

### Slide 65
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Sponsor balloting
A ballot group is formed using an electronic balloting system called myProject . Composition of that balloting group cannot change when the ballot is initiated.
A sponsor ballot is initiated with the draft, to be reviewed, commented, and voted by the ballot group.
* Needs 75% return response rate from the ballot group, and
* Needs 75% affirmative(approved) votes
WG reviews all the approved and disapproved votes with comments submitted by the ballot group. Make a reasonable attempt to resolve all negative votes
[Figure: Diagram showing sponsor balloting process]

### Slide 66
Department of Information and Electronic Engineering
International Hellenic University
Standardization process
Approval process to publication
Submit the final draft standard to Standard Review Committee (RevCom).
RevCom reviews the submitted documents/materials, and makes a recommendation to IEEE-SA Standards Board for an approval of the draft standard.
IEEE-SA Standards Board reviews the recommendation and approve the draft standard.
Publish Standard.
Complimentary copies sent to the WG.
[Figure: Diagram showing approval process to publication]

### Slide 67
Department of Information and Electronic Engineering
International Hellenic University
Thank you very much for the careful listening!
Questions?
[Figure: Photo of children writing formulas on a blackboard]

## Lecture 9 - WPT models and algorithms
### Slide 1
Models and algorithms for Wireless Power Transfer in Ad-Hoc Networks and the IoT
Prof. Constantinos Marios Angelopoulos
International Hellenic University
MSc Web Intelligent Systems
Internet of Things

### Slide 2
Wireless Power Transfer
A Wireless Power Transfer system consists of:
* chargers which transmit power wirelessly
* receivers which harvest the energy from the chargers
Envisioned by Tesla, is now becoming a game-changing technology1
More reliable and controllable than ambient energy harvesting (solar, light, wind, etc.)
1A. Kurs, A. Karalis, R. Moffatt, J. D. Joannopoulos, P. Fisher and M. Soljacic, Wireless power transfer via strongly coupled magnetic resonances, Science, vol. 317, pp. 83, 2007.

### Slide 3
Two Enabling Technologies
* Radio frequency(RF): low charging efficiency, only support low-power devices, charging distance up to few meters (0,13% efficiency).
* Resonant magnetic coupling: high charging efficiency, supports high-power equipment (e.g. electrical vehicles), charging distance <= 1 m (91 - 93% efficiency).
[Figure: Electromagnetic radiation products by Powercast Corp.]
[Figure: Resonant magnetic coupling by WiTricity for electrical vehicule charging]

### Slide 4
An Emerging Paradigm
WPT has evolved into:
* a subject of rapid technological progress
* a very active research topic
* a domain of emerging practical development and commercial application
Specialized journals, conferences and first books have appeared.
Wireless Power Consortium - Cooperation of Asian, European, and American companies in diverse industries. Working towards the global standardization charging technology (Qi standard).
Alliance for Wireless Power - Independently operated organization composed of global wireless power and technology industry leaders (Rezense standard).
Commercial products utilizing wireless power transfer are already available in the market.

### Slide 5
Commercial products
[Figure: Webpage of DanForce wireless charger]

### Slide 6
Commercial products
[Figure: News article about Apple iPhone wireless charging]

### Slide 7
Commercial products
[Figure: News article about Sony patenting technology for wireless power transfer between devices]

### Slide 8
WPT Start-ups
[Figure: News article about Nikola Labs landing investment for wireless power]

### Slide 9
WPT Start-ups
[Figure: News article about Wireless Power Market surging in 2017]

### Slide 10
WPT Start-ups
[Figure: News article about Wireless Charging Market Products netting revenues]

### Slide 11
Scope of this talk
* Via the prism of Wireless Sensor Networks, we will initially discuss the paradigm shift that WPT represents in ad-hoc networks from an algorithmic perspective.
* We will discuss heuristics that high-light the underlying issues in static and dynamic settings.
* We will review recent results in terms of
  * formal charging models
  * WPT specific concepts and phenomena
  * key optimization problems

### Slide 12
Wireless Sensor Networks (WSN)
The paradigm:
* Tiny, highly constrained autonomous devices with wireless capabilities
* Self-organized into an ad-hoc network to carry out a sensing task
[Figure: Diagram of sensor nodes in a sensor field routing data to a Control Center]

### Slide 13
Flat routing
All nodes in the network have similar role regarding the routing of data. No special nodes are used.
Example: Directed Diffusion2
2Chalermek Intanagonwiwat, Ramesh Govindan, Deborah Estrin: Directed diffusion: a scalable and robust communication paradigm for sensor networks. MOBICOM 2000: 56-67
[Figure: Diagram showing flat routing]

### Slide 14
Hierarchical routing
Special nodes assume greater responsibility regarding routing of data than most nodes inside the network. Super nodes – cluster heads.
Example: LEACH3
3- Wendi Rabiner Heinzelman, Anantha Chandrakasan, Hari Balakrishnan: Energy-Efficient Communication Protocol for Wireless Microsensor Networks. HICSS 2000
[Figure: Diagram showing hierarchical routing with cluster heads]

### Slide 15
Energy is the Big Issue
Flat and Hierarchical routing are two fundamental routing paradigms. Other paradigms also exist (e.g. for obstacle avoidance) but energy is The Issue.
[Figure: Multi-hop Transmissions]
[Figure: Direct Transmissions]
Network evolution over time. Sink in the far North.

### Slide 16
The Energy Balance Protocol
Intuition: To avoid premature network disconnection, all nodes should dissipate energy at the same rate independently of their position4.
The protocol combines two transmission types:
* Short transmissions to the next sector with probability P_i
* Long direct transmissions to the Sink with probability 1 - P_i
* The closer to the Sink, the more likely to send directly to the Sink
It is proven that EBP maximises the flow and the lifetime of the network. The best we can do in terms of algorithms!
4Charilaos Efthymiou, Sotiris E. Nikoletseas, José D. P. Rolim: Energy Balanced Data Propagation in Wireless Sensor Networks. IPDPS 2004
[Figure: Diagram of Energy Balance Protocol]

### Slide 17
Constantinos Marios Angelopoulos, Sotiris E. Nikoletseas, Theofanis P. Raptis:
Wireless energy transfer in sensor networks with adaptive, limited knowledge protocols. Computer Networks 70: 113-141 (2014)

### Slide 18
The WPT paradigm
A new network paradigm
A Wireless Rechargeable Sensor Network consists of
* a set of sensor motes: that are deployed over an area of interest; the network area
* a Sink: a special node of the network towards which sensory data are routed
* a Mobile Charger: a mobile entity, with significant energy reserves, that can recharge the sensor motes via wireless energy transfer

### Slide 19
The WPT paradigm
Wireless Rechargeable Sensor Networks (WRSNs) enable:
* the highly constrained resource of energy to be managed in great detail and more efficiently
* the energy management to be performed passively by sensors, with no computational and communication overhead
* the energy management to be studied and designed independently of the underlying routing protocol

### Slide 20
The WPT paradigm.
Remarks
* The wireless recharge problem in WSNs may look similar to other problems (e.g. data collection via mobile sinks)
* However, it admits special features and new trade-offs that necessitate a direct approach
* For instance, what is the amount of energy each mote should receive?
* Note that charger optimisation problems are (inherently) computationally hard (see NP-completeness of the Charger Dispatch Decision Problem - CDDP)5
5Constantinos Marios Angelopoulos, Sotiris E. Nikoletseas, Theofanis P. Raptis, Christoforos Raptopoulos, Filippos Vasilakis: Efficient energy management in wireless rechargeable sensor networks. MSWiM 2012: 309-316

### Slide 21
Research Questions
We identify and try to optimize the following trade-offs:
* How should the total available energy of the network be split between sensors and the Mobile Charger?
* Given that the energy the Mobile Charger may deliver to the motes is finite, should each sensor be fully or partially charged?
* What trajectory should the MC follow in order to charge the sensors?
We seek to achieve significant performance gains over the no-recharge case.

### Slide 22
The Charger Dispatch Decision Problem
Non-formal description: Given a set of sensors S, deployed over an area A, that generate and propagate data to a Sink, and a Mobile Charger M;
The CDDP is to determine whether there is a feasible schedule for M to visit the sensors so that no message is lost due to insufficient energy.
Theorem: CDDP is NP-complete. Proof: Reduction from Geometric–TSP.

### Slide 23
Heuristic Traversal Strategies
* Global knowledge strategy: The MC prioritizes motes based on distance and residual energy.
* Random walk strategy: The MC chooses the next mote u.a.r. among the neighbours of the current mote.
* Space-filling strategy (the spiral): Covers the entire network / avoids overlaps.
* Move along the diameter strategy: Quickly changes sub-regions.
[Figure: Spiral strategy]
[Figure: Move along the diameter strategy]

### Slide 24
The Adaptive Strategy
* The Charger follows concentric trajectories.
* Using limited information, locally available, it is able to identify areas of high energy depletion.
* The radius of the trajectory adapts to the energy depletion rates of each sub-region.
[Figure: Adaptive Strategy trajectory]
Criticality of node v_i at time t:
c_i(t) = f_i(t) * p_i(t)
, where f_i(t): normalised traffic flow at v_i and p_i(t): normalised energy consumption at v_i. The protocol implicitly adapts to the underlying routing protocol.

### Slide 25
Performance Evaluation
[Figure: Performance Evaluation visual]
* Significant performance gains achieved by introducing the charger.
* By using locally available network information the protocol achieves similar performance to the powerful global knowledge strategy.

### Slide 26
Constantinos Marios Angelopoulos, Julia Buwaya, Orestis Evangelatos, Jose D. P. Rolim:
Traversal Strategies for Wireless Power Transfer in Mobile Ad-Hoc Networks.
18th ACM International Conference on Modeling, Analysis and Simulation of Wireless and Mobile Systems , MSWiM 2015: 31-40

### Slide 27
The Problem
Definition
The Problem:
In an ad-hoc network where agents are randomly and dynamically moving inside an area of interest, what traversal strategy should a Mobile Charger (MC) follow in order to efficiently recharge them.

### Slide 28
The Mobility Model
* The traversal speed of each agent is modelled as a Poisson random variable
* We consider two mobility models:
  * Random Walk Mobility Model: Each A_i performs an independent blind random walk -> uniform agent distributions
  * extended Random Walk Mobility Model: Each A_i performs a biased random walk towards some hotspots -> heterogeneous agent distributions (concept of social attractivity)
[Figure: (a) Snapshot of a homogeneous agent distribution]
[Figure: (b) Snapshot of a heterogeneous agent distribution]

### Slide 29
The Energy Model
* All agents are considered identical.
* The amount of dissipated energy for a given time interval is modelled as a Poisson random variable.
Charging Model:
* We consider that MC employs inductive charging and transmits energy omni-directionally -> one-to-many charging model.
* For energy transmission we consider the Friis formula and the RF-to-DC energy conversion efficiency
* We assume that the energy reserves of MC are practically inexhaustible

### Slide 30
Towards an Efficient Heuristic
The Charger Traversal Decision Problem (CTDP) is to determine whether there is a feasible schedule for MC to visit points in OMEGA such that no agent "dies" at any time.
Theorem: The CTDP is NP-complete.
Proof outline: Reduction from the Charger Dispatch Decision Problem - CDDP6 (reduced from the Geometric Travelling Salesman Problem)
6Efficient energy management in wireless rechargeable sensor networks Constantinos Marios Angelopoulos, Sotiris E. Nikoletseas, Theofanis P. Raptis, Christoforos Raptopoulos, Filippos Vasilakis 15th ACM International Conference on Modeling, Analysis and Simulation of Wireless and Mobile Systems, Paphos, Cyprus, (MSWiM 2012).

### Slide 31
The Weighting Function
The MC needs a way to prioritize the agents for charging. We identify the following network aspects:
* the energy need E^{need}_i := E_{max} - E_i (with E_i indicating residual energy) of each agent A_i
* the mean energy dissipation rate \lambda_i of each agent A_i
* the mobility level M^i_{x(i)} of each agent A_i
* the euclidean distance d_i of each agent A_i from the MC

### Slide 32
The Weighting Function
Definition (The Weighting Function)
W : A -> R^+_0; W_i |-> ( (E^{need}_i)^\alpha (\lambda_i)^\beta ) / ( (M^i_{x(i)})^\gamma (d_i)^\delta ) (1)
where E^{need}_i := (E_{max} - E_i) / E_{max} * 100; \lambda_i := \lambda_i / \lambda_{max} * 100; M^i_{x(i)} := M^i_{x(i)} / M_{max} * 100; d_i := d_i / d_{max} * 100
* We use normalized values due to different units and scales of each parameter
* Nominator and denominator are defined based on the desired monotonicity of W
* Exponents are positive integers that help fine tune the importance of each parameter

### Slide 33
The Global Knowledge ILP Strategy - GK-ILP
Definition (The Global Knowledge ILP)
max_{x,y,\beta_i,d_i} \sum_i W_i \beta_i (2a)
d_i >= |x_i - x| \forall i (2b)
d_i >= |y_i - y| \forall i (2c)
R_{low} + (1 - \beta_i) * M >= d_i \forall i (2d)
\beta_i \in {0, 1} \forall i (2e)
i: the indice of agent A_i \in A; W_i: the weight of A_i \in A
\beta_i: binary decision variable
d_i: the distance of A_i from the MC (x, y)
x_i, y_i: the position of A_i and M a large constant

### Slide 34
Other Strategies
* The Global Knowledge Tessellation Strategy: Area OMEGA is virtually tessellated into tiles; the Charger optimizes its trajectory according to the cumulative weight of each tile.
* The Space-filling Strategy: The Charger systematically sweeps OMEGA in a deterministic way. Requires some network knowledge
* The Random Walk Strategy: The Charger performs a random walk in OMEGA. Zero-knowledge, randomized traversal strategy.

### Slide 35
The Reactive Local Knowledge Strategy
Local knowledge traversal strategy that exploits local information collected distributively.
Agents assume an active role by collecting local network information periodically:
* Current coordinates (x_i, y_i)
* Total energy needed by one-hop neighbours (E^{need}_i)
* Average energy dissipation rate of neighbourhood (\lambda_i)
* Average mobility level of neighbourhood (M^i_{x(i)})

### Slide 36
The Reactive Local Knowledge Strategy -RLK
From this collected information each agent computes a weight via a slightly modified weighting function (distance to MC is missing)
W_i : W_i |-> ( E^{need}_i \lambda_i ) / M^i_{x(i)} (3)
This info along with the local coordinates are stored and carried during the agent’s network traversal in the form of tuples.
Tuples age over time and are updated with information of higher quality, when found.
The MC gains a “blurred” view of the network status in the near past and adjusts its traversal

### Slide 37
The Reactive Local Knowledge Strategy -RLK
Some remarks:
* The protocol introduces some communication overhead but this is limited and local.
* Information regarding critical areas are carried for more time and thus further in the network.
* The protocol is distributed and therefore scalable and applicable in realistic settings.
Performance Evaluation:
* In homogeneous settings cheap naive strategies, such as Random Walks, demonstrate good performance
* In heterogeneous settings introducing a small network overhead in a sophisticated way drastically increases performance

### Slide 38
S. Nikoletseas, T. Raptis, C. Raptopoulos. Low Radiation Efficient Wireless Energy Transfer in Wireless Distributed Systems, in ICDCS 2015.
Also in the Journal of Computer Networks (COMNET 2017).

### Slide 39
The Scalar Charging Model
* Authors define a novel charging model that takes into account real hardware restrictions:
  * finite initial charger energy supplies (it can transfer restricted energy)
  * finite node battery capacity (it can store restricted energy)
  => non-linear constraints (time multiplies power) that radically change the complexity of the considered computational problems
  => authors focus on useful energy received (not just power rate)
Charging: A node v \in P harvests energy from a charger u \in M with charging rate given by
P_{v,u}(t) = { (\alpha r_u^2) / (\beta + dist(v,u))^2, if E^{(t)}_u, C^{(t)}_v > 0, dist(v, u) <= r_u; 0, otherwise }
\alpha and \beta are known positive constants determined by the environment and hardware.

### Slide 40
Charging Model contin’d
Energy: The harvested energy by the nodes is additive. Therefore, the total energy that node v gets within the time interval [0,T] is
H_v(T) = \sum_{u \in M} \int_0^T P_{v,u}(t) dt
EMR: The electromagnetic radiation (EMR) at a point x is proportional to the additive power received at that point. In particular, for any x \in A, the EMR at time t on x is given by
R_x(t) = \gamma \sum_{u \in M} P_{x,u}(T)
where \gamma is a constant that depends on the environment.

### Slide 41
The Low Radiation Efficient Charging (LREC) Problem
Authors define the following:
* Let M a set of chargers and P be a set of nodes in an area A. Suppose that
(i) each charger u \in M initially has available energy E^{(0)}_u
(ii) each node v \in P has initial energy storage capacity C^{(0)}_v
* Assign to each charger u \in M a radius r_u, so that
(a) the total usable energy given to the nodes of the network is maximized
(b) the electromagnetic radiation at any point of A is at most \rho.
The problem is proven to be NP-hard (the problem is relaxed and an ILP formulation is provided).
Authors, also provide interesting insights in fundamental properties of the problem; e.g. by introducing the power constraint, affects the monotonicity of the objective function.

### Slide 42
Power Maximization in the Vector Model
I. Katsidimas, S. Nikoletseas, T. Raptis and C. Raptopoulos. Efficient Algorithms for Power Maximization in the Vector Model for Wireless Energy Transfer, in ICDCN 2017.
Also in the Journal of Pervasive and Mobile Computing (PMC), 2017.

### Slide 43
Limitations of the scalar model
* Friis model (widely used):
P_r = P_t * G_t * G_r * (\lambda / 4\pi R)^2
where G_t, G_r antenna gains, \lambda the wavelength and R the distance.
* It is a scalar (1-dimensional) model, assuming received energy is additive.
* A gross model, unable to explain detailed phenomena in real applications with many nodes.
* Still, in case of one charger or few remote chargers, it is valid. When "micro management" is needed in the presence of several nearby chargers, then it is not sufficient.

### Slide 44
A need for more precise models
* Multiple nearby transmitters introduce complex interference among waves.
* This leads to interesting constructive and destructive combinations of waves.
* This complex process necessitates the introduction of vector (2-dimensional) models, providing us with more detailed and realistic modelling abstractions.

### Slide 45
The vector model 1/2
* The electric field created by an energy transmitter (charger) C, operating at full capacity, at a receiver R at distance d = dist(C, R) is given by7
E(C, R) = \sqrt{ (Z_0 * G_C * P_C) / (4 * \pi d^2) } * e^{-j 2\pi / \lambda d}
where Z_0 a constant for wave-impedance, G_C the antenna gain, P_C the transmitted power and \lambda the wavelength.
* This gives rise to a 2-dimensional vector:
E(C, R) = \beta * (1/d) * e^{-j 2\pi / \lambda d} = \beta * (1/d) * [ \cos( (2\pi / \lambda) d ) \\ \sin( (2\pi / \lambda) d ) ]
where \beta constant depends on hardware and environment.
7M. Y. Naderi, K. R. Chowdhury, S. Basagni, Wireless sensor networks with RF energy harvesting: Energy models and analysis, in WCNC 2015

### Slide 46
The vector model 2/2
* The total electric field at a receiver R created by a family of energy transmitters C is the superposition (vector-sum) of their individual electric fields, that is
E(C, R) = \sum_{C \in C} E(C, R)
.
* Furthermore, the total available power at the receiver R is given by
P(C, R) = \gamma * ||E(C, R)||^2
where ||.|| denotes the length (2-norm) of the vector and \gamma constant that depends on hardware.

### Slide 47
Interesting Phenomena - how two nearby points can differ a lot
[Figure: Line with points C1, R, R', C2]
* P(C_1, R) = P(C_2, R) = 1 (only 1 transmitter operational).
* P(C_1, C_2, R) = (1 + 1)^2 (both operational => superadditive power since C_1, C_2 are equidistant and vectors have same direction).
* P(C_1, C_2, R') = (8/15)^2 ~ 0.28 < min P(C_1, R'), P(C_2, R') = (4/5)^2 ~ 0.64 (cancellation effect at a nearby point).

### Slide 48
Interesting Phenomena - the full curves
[Figure: Plot of Power vs Position showing curves for both operational, only (0,0), only (2,0), sum of chargers]
* Local maxima indicate points of superadditive power.
* Local minima occur at points of cancellation.
* Note: It is highly non-trivial to derive a closed formula for the points of maximum/minimum power. So we have to examine a whole space of system configurations and evaluate power received.

### Slide 49
Two optimization problems
Definition (MAX-POWER)
Given a family of chargers C and family of receivers R, find a configuration for the chargers that maximizes the total power to R. That is, find x* such that
x* \in arg \max_{x \in [0,1]^C} P(C(x), R)
where P(C(x), R) = \sum_{R \in R} P(C(x), R)
Definition (MAX-kMIN-GUARANTEE)
Given a family of chargers C and a family of receivers R, find a configuration for the chargers that maximizes the minimum cumulative power among all subsets of R of size k. That is, find x* such that
x* \in arg \max_{x \in [0,1]^C} \min_{A \in (R \\ k)} P(C(x), A)
where P(C(x), A = \sum_{R \in A} P(C(x), R).

### Slide 50
Until next time!

## Lecture 10 - LEC - Mobility in IoT 2025-26
### Slide 1
Internet of Things
Mobility in IoT
Prof. Constantinos Marios Angelopoulos
mangelopoulos@ihu.gr
MSc in Web Intelligence
INTERNATIONAL HELLENIC UNIVERSITY

### Slide 2
Overview
* Sink Mobility Protocols
* Adaptive Sink Trajectories
* Sink & Sensor Mobility

### Slide 3
Limitations of Static Sink(s)
* Computation and communication (energy) overhead on the sensors
* Low Scalability
* Uneven load distribution among the sensors
* Bypassing obstacles requires a lot of resources
* Dynamic networks have significant reconfiguration cost

### Slide 4
Mobility: Main Idea
Advances in technology and new applications suggest that sensors may be mobile.
* Wildlife monitoring
* Monitoring in urban environments
* Drones - UxVs
Introducing mobility shifted the burden from the sensor nodes to the sink
Main Idea:
* Sink has significant and easily replenished energy reserves.
* The sink can move inside the sensor network area, in close proximity to the sensors.
* By travelling in the whole network area, sink collects all the available data.

### Slide 5
Mobility: New Challenges
Sink mobility in WSNs presents many new challenges
* Sink must cover the whole network
* Incurs longer delivery delays
* Bad scalability when network area increases
* Routing and localization problems become more difficult

### Slide 6
Mobility: Advantages
* Sparse, disconnected and irregular networks can be better handled
* The mobile sink can bypass obstacles
* Better load distribution
* Scales well with respect to number of sensors
* Reduces communication distance
* Reduces energy consumption on the sensors => System lifetime increases
* Reduces adversarial overhearing => Enhances security

### Slide 7
Early Works on WSNs with Mobility
1. J. Luo and J.-P. Hubaux. "Joint Mobility and Routing for Lifetime Elongation in Wireless Sensor Networks." In 24th IEEE INFOCOM, 2005. (optimal movement)
2. D. Jea, A. Somasundara, and M. Srivastava. "Multiple controlled mobile elements (data mules) for data collection in sensor networks". (deterministic movement) In DCOSS 2005.
3. D. Goldenberg, J. Lin, A. Morse, B. Rosen, and Y. Yang: "Towards mobility as a network control primitive." In MobiHoc 2004. (optimal placement)

### Slide 8
J. Luo and J.-P. Hubaux
Joint Mobility and Routing for Lifetime Elongation in Wireless Sensor Networks
The main idea is that a mobile entity can help remove "hot spot" areas, reduce energy consumption and better equalize the load among the sensors.
* sensors are uniformly distributed in a circle of radius R
  * strongly connected network
  * full coverage
* sensors generate data at a constant rate \lambda
* shortest path routing assumed
The authors propose an analytical model for calculating the load on each sensor.

### Slide 9
J. Luo and J.-P. Hubaux
Results:
* the optimal movement trajectory is a circle along the periphery of the network
* optimum routing switches between shortest path and trajectory based routing
* arbitrary motion can reduce maximum load by 3 times
* joint mobility and routing can increase lifetime by 500%
[Figure: a) Static sink and b) Mobile sink exact load 3D plots]

### Slide 10
D. Jea, A. Somasundara, and M. Srivastava
Multiple controlled mobile elements (data mules) for data collection in sensor networks
The main idea is that multiple mobile sinks can be used to fully cover the sensor network.
* Sinks move deterministically
  * linear parallel trajectories
  * all nodes are within one hop from at least one and no more than two sinks
  * nodes that can communicate with two sinks are called shareable
* All data is transmitted over one hop.
* Data throughput is maximized by equalizing the load among the sinks.
[Figure: Example regions and data mules assignment]

### Slide 11
D. Jea, A. Somasundara, and M. Srivastava
Three load balancing protocols
* First Come First Serve: Shareable nodes associate to the first sink they listen
* Equal share: Shareable nodes are equally shared between the two sinks
* Load balanced: Shareable nodes are assigned according to the total load of each sink
[Figure: Graph of Average # of packets per node per round vs Data Mule ID]

### Slide 12
Goldenberg et al
Towards mobility as a network control primitive
* Nodes can move
  * controlled movement
  * localization is available
* Optimize routing paths wrt energy
* Examine constrained vs unconstrained movement
The authors prove that the optimal arrangement of nodes is along a straight line in equally spaced positions.
[Figure: Example tree structures of unconstrained and constrained movement]

### Slide 13
Goldenberg et al
* Initially a lot of energy is spent for optimizing the path
* Optimizing paths saves significant amounts of energy in the long term
* Unconstrained movement spends more energy on movement but saves more energy in the long term
[Figure: a) unconstrained and b) constrained Total Power Used vs Total Bits Sent]

### Slide 14
Simple Sink Mobility
Athanasios Kinalis, Sotiris E. Nikoletseas, Dimitra Patroumpa, José D. P. Rolim: Biased sink mobility with adaptive stop times for low latency data collection in sensor networks. Information Fusion 15: 56-63 (2014)
* One of the first approaches to sink mobility, particularly with randomized techniques
* Authors assume a very weak model i.e. limited or no network knowledge, no coordination of sensors
* Authors present several combinations of mobility strategies and data collection techniques, achieving trade-offs mainly between energy consumption and latency
* The protocols significantly reduce energy dissipation and maximize the success rate; however latency increases

### Slide 15
The Model
* A number of n ultra-small homogeneous sensor devices are spread in an area D x D
  * random uniform deployment
  * "clustered" deployment: p_n "pockets" i.e. regions in the network area with high particle density d_p
* Sensor devices do not move
[Figure: Network Model diagrams]

### Slide 16
P1: Random Walk with Passive Data Collection
* S performs random walk: M_{random} selects a random direction and a random distance
* S periodically broadcasts beacons
* Sensors cache the recorded data
* When sensor hears a beacon starts to transmit the cached data
* Very low communication overhead on sensors
* Requires very little network knowledge

### Slide 17
P2: Partial Random Walk with Limited Multihop Collection
* S partitions the rectangular network area in j x j square regions
* Each region is represented by a vertex in an overlay graph G_o(V, E) stored locally on the S
* M_{graph}: S moves from v_i \in V to another region v_j adjacent to v_i selected randomly and uniformly
* S periodically broadcasts beacons with a hop counter h_c and a ttl
* Beacons form minimum hop propagation trees ttl hops deep
[Figure: Overlay graph diagram]

### Slide 18
P3: Biased Random Walk with Passive Collection
* S partitions the rectangular network area in j x j square regions
* S constructs locally an overlay graph G_o(V, E)
* Each region is associated with a visit counter c_v and a density counter d_v
* Each time S visits a region, it updates the counters
  * c_v = c_v + 1
  * d_v = d_v + # unseen before sensors
* M_{bias}: moves from the center of one region to the center of another adjacent region
* The next region is selected with "biased" probability p_v

### Slide 19
P3: Biased Random Walk with Passive Collection (cont.)
Frequency of visits
* c_{neigh}(u) = \sum_v c_v for all v : (u, v) \in E.
* p(f)_v = (1 - c_v / c_{neigh}(u)) / (deg_u - 1)
* Favours less frequently visited areas
Local Density
* d_{neigh}(u) = \sum_v d_v for all v : (u, v) \in E
* p(d)_v = (1 + d_v / d_{neigh}(u)) / (deg_u + 1)
* Dense areas are favoured
Weighted Combination
p_v = \alpha * p(f)_v + \beta * p(d)_v
where \alpha >= 0, \beta >= 0 and \alpha + \beta = 1.

### Slide 20
P3: Biased Random Walk with Passive Collection (cont.)
* Sensors transmit the data when they receive a beacon
* Low communication overhead on the sensors
* Frequency bias increases fairness
* Density bias better copes with irregular node deployment

### Slide 21
P4: Deterministic Walk with Multihop Collection
* S follows a static path of length l
* M_{circle}: moves on a circle of radius r = l / 2\pi
* M_{line}: moves back and forth on a line segment of length l
* S transmits beacons that form unlimited minimum hop propagation trees
* Sensors store their hop distance h_d from the sink
  * if h_d > 0 propagate data to the next hop
  * if h_d = 0 propagate data to the sink or cache if sink not present
* Significant communication overhead on the sensors

### Slide 22
Findings Overview
All protocols achieve high success rate and low energy consumption at the cost of increased latency.
* P1 – Random Walk with Passive Data Collection
  * Increasing mobility speed improves performance significantly
  * Unaffected by network topology
* P2 – Partial Random Walk with Limited Multihop Collection
  * Increasing the size of the data collection area significantly reduces delay but also reduces success rate
* P3 – Biased Random Walk with Passive Collection
  * Frequency biased movement \simeq 100% success rate, low energy consumption and low delay
  * Density biased movement can improve performance in very dense areas
* P4 – Deterministic Walk with Multihop Collection
  * Protocol performance is greatly affected by l
  * Circular paths are slightly better than linear paths

### Slide 23
Constantinos - Marios Angelopoulos, Sotiris Nikoletseas, Dimitra Patroumpa, and Jose Rolim.
Coverage-Adaptive Random Walks for Fast Sensory Data Collection
ADHOC-NOW 2010 - Edmonton, Canada

### Slide 24
Random Walks in WSNs
Random walks can serve as fully local, very simple strategies for sink motion, reduce energy dissipation a lot but increasing latency.
To achieve satisfactory energy-latency trade-offs the sink walks can be made adaptive, depending on local network parameters such as density and/or history of past visits in each network region.

### Slide 25
The Network Model
* Planar area
* Sensors deployment is random uniform over the network area
* All sensors have sensory data to deliver
* No data is generated during the network traversal (focus on data collection)
* Visited nodes are distinguished by lack of data.

### Slide 26
The Sink
* During the network initialization, a graph formation phase is executed by the sink
* The network area is partitioned in j x j equal square regions, called cells.
* A virtual lattice graph G_o = G(V, E) is created which is overlaid over the network area.
* When the sink is located at the center of a cell, it can communicate with every sensor node within the cell area.

### Slide 27
Blind Random Walk 1/2
* The most simple and straightforward of all.
* Each move is stochastically independent from all previous ones
* The sink selects its next position with the same probability for each one of the four coordinate directions.

### Slide 28
Blind Random Walk 2/2
* Very robust solution
* Probabilistically guarantees that eventually all the cells of the network will be visited
* All data will be collected
However, in some network structures it may become inefficient, mostly with respect to latency.

### Slide 29
Random Walks with Memory 1/2
Extends the Blind Random Walk. Uses some (constant) memory of past visits.
* The sink maintains a First-in-First-out (FIFO) list M
* M contains the last K cells visited during the random walk.
* The next hop is chosen uniformly among the neighbours of the cell that are not in the memory list M

### Slide 30
Random Walks with Memory 2/2
Trade-off: The use of memory eliminates loops in random walks, but it may also lead to a deadlock.
* If K = 0, the random walks become blind and can have loops but no deadlocks.
* For complete memory, the random walks can only have deadlocks and no loops.
* When the size of M is 0 <= K <= n - 1, random walks can have both loops and deadlocks.

### Slide 31
Random Walk with Inertia 1/2
* Four directions: North, South, East and West
* Each one is assigned a probability.
* the probability distribution on each step of the walk changes adaptively to the nodes' discovery
The following principle is followed:
Reinforce the direction where newly discovered sensors were found and weaken the directions where already visited sensors have been identified.

### Slide 32
Random Walk with Inertia 2/2
p_c: current direction probability at time t is:
p_c^{t+1} = { p_c^t + \delta, if new nodes discovered; p_c^t - \delta, if no new nodes discovered }
while each one of the probabilities towards the rest three directions (p_r: rest direction probabilities) are:
p_r^{t+1} = { p_r^t - \delta/3, if new nodes discovered; p_r^t + \delta/3, if no new nodes discovered }

### Slide 33
Visualization of the Inertia Walk
[Figure: Series of snapshots showing the visualization of the Inertia Walk]

### Slide 34
Explore-and-Go Random Walk
The sink motion consists of two types of motion:
* moving on a straight line
* arbitrarily changing direction
The sink chooses between them via a bias factor \beta.
F_{motion} = { move straight, with probability \beta; change direction, with probability 1 - \beta }
where, \beta = { 0.1, when new nodes were discovered; 0.9, when no new nodes were discovered }

### Slide 35
Visualization of Explore-n'-Go
[Figure: Series of snapshots showing the visualization of Explore-n'-Go]

### Slide 36
Inertia vs Explore-n'-Go
Similarities
* Require zero knowledge of network area
* Require zero knowledge of sensor distribution.
* Have light-weight requirements in terms of memory and computational power
One main difference:
* Inertia walk performs network coverage by drawing big straight lines.
* Explore-n'-Go performs a more systematic network coverage, by sequentially visiting network subregions.

### Slide 37
Curly Random Walk 1/3
Intuition:
* start by visiting a confined subregion
* gradually allow the sink to perform a motion of higher degree of freedom
* eventually, the sink will cover the entire network area.
To achieve this, initially the sink performs frequent narrow left-turns, which gradually get wider.

### Slide 38
Curly Random Walk 2/3
This type of motion can be modelled as a series of successive straight S and left-turn L moves.
SLSSLSSSLSSSSL...
Obviously, the probability distribution of left turns is the geometric distribution.
* probability mass function P^i = (1 - p_L)^i p_L
* p_L: probability of left turn
* i the number of successive straight moves before the next left turn.
* For a fixed i, p_L^i = 1 / (i + 1).

### Slide 39
Curly Walk 3/3
[Figure: An example of network traversal following Curly Random Walk in a 50 x 50 network area. (snapshots after 500, 2 * 10^3 and 2 * 10^4 hops.)]

### Slide 40
Cover Time
[Figure: Bar chart of Cover Time (Hops) for various Random Walks]

### Slide 41
A New Metric: Proximity Variation
[Figure: Plot of Average Minimum Distance from Sink vs Hops for different random walks]
The mean value (over all cells) of the smallest distance from the sink for all the cells.
PV = (\sum_{i=1}^n \min(dist(i))) / n

### Slide 42
Angelopoulos Constantinos Marios, Nikoletseas Sotiris
Aggregated Sensory Data Collection by Mobility-based Topology Ranks
IEEE GLOBECOM 2009

### Slide 43
The Problem
In a WSN with full mobility scheme, where both sensors and sink move dynamically, how can the sink efficiently collect data from sensors?

### Slide 44
The Problem
[Figure: Diagram showing a moving Pocket of sensors and a Sink]

### Slide 45
The Sensor Model
Both the sensors and the sink are assumed to be mobile and equipped with (relative) localization hardware
* a DxD plane network area
* n total number of sensors deployed
* d is the density of sensors in that area (sensors/m^2)
* Sensor devices are equipped with a set of hardware monitors that can measure environmental conditions of interest.
* also, fixed transmission range R, general purpose storage memory of small constant size

### Slide 46
Modelling Dynamic Sensory Mobility
[Figure: State machines for Transitions between slow mobility roles, medium mobility level, medium mobility with fast bursts, and fast mobility]

### Slide 47
Our Approach
* Sensors are moving inside the network area, independently of each other.
* Each sensor periodically measures the number of its neighbours and stores a tuple.
* Each tuple consists of: the number of neighbours, a timestamp, the current position
Based on tuples, the sink is going to exploit general topological information.

### Slide 48
Our Approach II
Each tuple is assigned a value via the ranking function
R = d^2_{local} / (\Delta P \Delta T)
where:
* d is the number of neighbours.
* \Delta P the distance between position where d was measured and current position.
* \Delta T the time interval when d was measured and current time.

### Slide 49
Our Approach II
Each tuple is assigned a value via the ranking function
R = d^2_{local} / (\Delta P \Delta T)
* Only one tuple is stored each time.
* A new tuple replaces stored one in sensor memory, iff it is asigned a higher value.
* When a sensor reaches the radio range of the sink, along with the sensory data, the stored tuple is also sent.
* The sink chooses to move towards the direction corresponding to the highest ranking collected tuple.

### Slide 50
The Aggregation Process
The sink initially traverses the network area at random direction. For a short period of time it collects tuples. Tuples A,B corresponding to positions relatively close are aggregated into C, based on an angle_{thresh}
* C_{d_{local}} = A_{d_{local}} + B_{d_{local}}
* C_P = (A_P * A_{d_{local}} + B_P * B_{d_{local}}) / (A_{d_{local}} + B_{d_{local}})
* C_T = (A_T * A_{d_{local}} + B_T * B_{d_{local}}) / (A_{d_{local}} + B_{d_{local}})
[Figure: Diagram of aggregation process]

### Slide 51
Protocols we compare with
* Blind Random Walk: In this scenario the sink is simply moving according to a random walk process and serves any sensors that it may reach.
* Optimized Deterministic: The sink sweeps the entire area in a way that no overlaps occur.
  [Figure: Diagram of Optimized Deterministic sweep]
* Our Protocol without Aggregation Process
In order to inspect the impact of the process

### Slide 52
Performance Findings
[Figure: Bar chart of Latency (sec) vs Number of nodes]
[Figure: Bar chart of Success Rate % vs Number of nodes]
[Figure: Bar chart of Energy (Joules) vs Number of Nodes]
* Latency improves up to 8 times
* Better success rate, from 93% to 98%
* Slightly (10%) more energy dissemination
* Improvements also in homogeneous placement

### Slide 53
Thank you.
