# Internet of Things: Data propagation algorithms III

*Note: Lectures 4 and 5 were identical files, so this transcription covers both.*

**Dr. Constantinos Marios Angelopoulos**
mangelopoulos@ihu.gr
MSc in Web Intelligence
INTERNATIONAL HELLENIC UNIVERSITY

## Previously on WSAN ...
(Slide 2)

## The problem
(Slide 3)
"How can sensor p, via cooperation with the rest of the sensors in the network, propagate information about event E to the control center(s)?"
[Figure: A sensor network showing a sensor field with sensor nodes, a control center, and a multi-hop path from a source node to the sink]

## Directed Diffusion
(Slide 4)
* Data-centric protocol
* Can handle low dynamics
[Figure: Directed diffusion showing a Source, Event, Gradients, and Sink]

## LEACH
(Slide 5)
* Scalable, energy efficient protocol employing randomization
[Figure: Two scatter plots showing clusters and cluster heads in a sensor network]

## Next, on Internet of Things...
(Slide 6)
A. Link quality based methods
* ETX metric*
* Minimum Outage Rate (MOR)*
B. Link distance based methods
* Routing with relay diversity (ExOR)*
* Greedy, local neighbour selection (LTP)
C. Multipath routing
* Braided paths (GRAd, GRAB)
* Probabilistic forwarding (PFR)

*Protocols we will focus on

## A. Link Quality Methods
(Slide 7)
* **Main goal:** Providing robustness by selecting routes that *minimize end-to-end re-transmissions or failure probabilities*.
* **Motivation:** If wireless links were (ideally) error-free, then a shortest hop-count path could be chosen. Such paths however require long distance links, which in realistic settings are likely to be error-prone. Thus, the link quality should be taken into account (via simple ACK signals for each successfully delivered packet).

## A1. The ETX metric
(Slide 8)
* Let d_f be the **packet reception rate** (probability of successful delivery) over a link in the forward direction, and d_r the **probability that the corresponding ACK is received** in the reverse direction.
* Assuming each packet transmission can be abstracted as a Bernoulli trial, **the expected number of re-transmissions** required for successful delivery of a packet on this link is:
  ETX = 1 / (d_f d_r)
* This metric for a single link can then be incorporated into any routing protocol, so that chosen end-to-end paths **minimize the sum of ETX over all links on the path**, i.e. the total expected number of transmissions on the path.

## ETX routing - example
(Slide 9)
[Figure: A graph showing nodes A, B, C, D, E, F with forward link probabilities d_AC=0.9, d_CD=0.9, d_DE=0.9, d_EB=0.9, d_AB=0.1, d_AF=0.8, d_FB=0.8]
* This example shows 3 routes from A to B, with the forward probabilities on each link (for simplicity, all reverse probabilities are taken d_r = 1).
* The direct A-B transmission would require an expected number of 10 re-transmissions.
* The path via C,D,E would require 4(1/0.9) ≃ 4.44 re-transmissions (1.1 per link) on average.
* The A-F-B path would require 2(1/0.8) ≃ 2.5 re-transmissions (1.25 per link) on average.
  => the ETX-minimizing path is A-F-B.

## ETX routing - discussion
(Slide 10)
* As demonstrated in the example, ETX *neither favours* long paths with many short-distance, high-quality links, *nor very short paths* with a few long-distance, low-quality links. It actually takes an *"in-between"* approach.
* **ETX advantages:** It minimizes the number of transmissions required, as well as it improves energy efficiency. Also, it directly addresses the potential link asymmetries, by taking into account packet delivery probabilities in both directions.
* **ETX limitation:** *It assumes knowledge* of the d_r, d_f packet reception probabilities. In quite static networks these values may be periodically obtained via link monitoring, however in dynamic networks the obtained values may become obsolete very soon and the link monitoring overhead may be prohibitively high.

## ETX - Example 2
(Slide 11)
[Figure: Node A to Node B with ETX=1.3 and d = 5 [m]]
Assuming that:
* The energy required to operate the radio module for each bit (both for receiving and transmitting) is E_c = 50[nJ/bit];
* The energy required to successfully transmit a message over distance d is E_tx(d) = k \cdot d^2 [nJ/bit], where k = 1;
Calculate:
The expected overall network energy consumption for routing one packet of length b = 100[bits] from A to B.

## ETX - Example 2
(Slide 12)
[Figure: Node A to Node B with ETX=1.3 and d = 5 [m]]
Assumptions:
* E_c = 50[nJ/bit];
* E_tx(d) = k \cdot d^2 [nJ/bit], where k = 1;
* b = 100[bits].
Answer:
E_{A->B} = 1.3 \cdot (E_c \cdot b + E_tx(5) \cdot b + E_c \cdot b)
= 1.3 \cdot (50[nJ/bit] \cdot 100[bit] + 5^2 [nJ/bit] \cdot 100[bit] + 50[nJ/bit] \cdot 100[bit])
= 16,250 nJ = 16.25 \mu J

## A2. The Minimum Outage Route (MOR) Metric (I)
(Slide 13)
* Under *high dynamics* (mobile nodes, mobile objects) the link quality fluctuates very rapidly and *ETX is not feasible*. In such cases, *analytic models* of link quality can be used. They explicitly model the wireless channel as having multi-path fading with Rayleigh statistics (fluctuations over time).
* Let d be the distance between transmitter and receiver, h the path-loss exponent, SNR the signal-to-noise ratio without fading, f the fading state of the channel. Then, the *instantaneous* capacity of the channel is:
  C = \log (1 + (|f|^2 / d^h) SNR)

## A2. The Minimum Outage Route (MOR) Metric (II)
(Slide 14)
* The *outage probability* P_out is defined as the probability that the instantaneous channel capacity falls below the transmission rate R. It is shown that:
  P_out = 1 - \exp(-d^h / (\mu SNR*))
where \mu = E[|f|^2] is the mean of the Rayleigh fading and SNR* a normalized SNR.

## A2. The Minimum Outage Route (MOR) Metric (III)
(Slide 15)
* Then, end-to-end reliability of a route is defined as the probability that *none of the intermediate links suffers outage*, and the most reliable route between two nodes is one *that minimizes the following path metric:*
  \sum_i d_i^h
where d_i is the distance of the i-th hop in the path. The metric d^h for each link is called the minimum outage route (MOR) metric.
* The MOR approach does not require collection of link quality metrics like ETX, neither ACK messages are used. However, *its practicality is limited by the basic abstraction that the channel fading follows a certain distribution* (the Rayleigh distribution).

## B. Link Distance Methods
(Slide 16)
* In general, nodes closer *to the data destination* are chosen/favoured.
* The relay diversity is provided by the fact that wireless transmissions are *broadcast to multiple* nodes.

## B1. Routing With Relay Diversity
(Slide 17)
[Figure: (a) traditional routing where A->B->C, and (b) routing with relay diversity where A->B->C and A->C directly]
* In traditional routing, the reliability of the AC path depends on whether both AB and BC transmissions have been successful.
* However, if C *is also allowed to accept packets directly* from A, then the reliability can be further increased without much additional energy cost.
* Allowing such 2-hop packet reception, in the high SNR regime, *the end-to-end outage probability decays as* (SNR)^{-2}. When nodes within L hops can communicate with each other with high SNR, this probability can become as small as (SNR)^{-L}.
* A weakness of this method is that it requires *a larger number of receivers to be actively overhearing* each message, which may incur a *radio energy penalty*.

## Extremely Opportunistic Routing (ExOR) (I)
(Slide 18)
* **Main idea:** the identity of the node which will eventually forward a packet, *is not predetermined before the packet is transmitted*. Instead, the method tends to ensure that *the node closest to the destination receiving a given packet will forward the packet further*.
[Figure: A multi-hop topology showing A->C, D, E->B with probabilities, and a priority queue for candidate receivers (B, D, E, C)]
* The protocol has *three stages*:
  1. **Priority ordering:** At each step, the transmitter includes in the packet a schedule with the priority order of candidate receivers that should forward the packet.

## Extremely Opportunistic Routing (ExOR) (II)
(Slide 19)
2. **Transmission acknowledgements:** A MAC scheme is used so that each candidate receiver sends the ID of the highest-priority successful recipient known to it. All nodes listen to all ACKs, so they *distributively* determine *which node, among those who received the packet successfully, has the highest priority*.
3. **Forwarding decision:** After listening to all ACKs, the nodes that have not heard of any IDs with priorities greater than their own will transmit.
* Features of the ExOR protocol
  * Nodes *further away from the current node* (yet closer to the destination) are less likely to successfully receive the packet, but, whenever they receive it, they are favoured to act as forwarders!
  * This *tends to make good progress* towards the data destination, without many transmissions and delays.
  * As with relay diversity, ExOR ***requires a larger number of receivers*** to be active. Also, the priority evaluation necessitates some inter-node packet delivery ratios to be tracked and maintained.

## B2. Greedy, Local Neighbour Selection (LTP)
(Slide 20)
Network nodes are called "particles".
a) Each particle has *two communication modes*: a *broadcast* (radio) *beacon mode* and a *directed point-to-point* transmission mode (unicast mode).
b) Each particle may alternate between a **sleeping** and an **awake** mode. During sleeping periods particles cease any communication.
c) Particles *do not move*.
d) The particles are spread in a two-dimensional area (plane).

## LTP model continued
(Slide 21)
e) A *receiving wall* W is a *line* in the plane. The wall represents the control center.
f) Each particle is *aware of the direction* toward W.
g) *No geolocation* abilities assumed
**Definitions:** Let d (in numbers of particles /m^2) be the **density** of the cloud.
Let R be the maximum (beacon/laser) **transmission range** of each particle.

## The Local Target Protocol (LTP)
(Slide 22)
Let d(p_i, p_j) the (vertical) distance of p_i, p_j and d(p_i, W) the (vertical) distance of p_i from W. Let **info(E)** the info to be propagated. Each p' receiving info(E) does the following:
* **Search Phase:** It uses a low energy broadcast of a beacon (angle a above and below the vertical line) to *discover* a particle closer to W (i.e. a p'' where d(p'', W) < d(p', W)).
* **Direct Transmission Phase:** If found, p' *sends* info(E) to p'' via a unicast transmission.
* **Backtrack Phase:** If repetitions of the search phase *fail* to discover a particle nearer to W, then p' sends info(E) *to the particle it received the information from*.

## Example of the Search Phase / Example of a Transmission
(Slide 23)
[Figure: Example of Search Phase showing a beacon circle with an angle towards the wall W]
[Figure: Example of a Transmission showing nodes p0, p1, p2, p3 advancing towards W with various angles a0, a1, a2]

## Efficiency
(Slide 24)
**Definitions:** Let h_opt the *(optimal)* number of "hops" (**vertical to W** transmissions) needed to reach W, if particles always exist in pair-wise distances R towards W.
Let h the *actual* number of hops (transmissions) taken to reach W. The **"hops" efficiency** of the data propagation protocol is the ratio
  C_h = h / h_opt
where h_opt = \lceil d(p, W) / R \rceil

## Why studying h, C_h?
(Slide 25)
When a particle p "looks around" for a particle as close to W as possible to pass information, it may not get any particle in the perfect direction (on the line vertical to W passing from p), mainly because:
a) There might never have been any particles in that direction.
b) Particles of sufficient remaining battery power may not be available.
c) Particles available may temporarily "sleep" to save energy.

## Summary evaluation of LTP
(Slide 26)
* local, simple, greedy protocol
* no global structure (set of paths) maintained
* good for dense networks
* performance drops in sparse / faulty networks

## C1. Multipath Routing
(Slide 27)
* multiple routes are used, towards increasing robustness
* the routes can be *disjoint* or *partially disjoint*
* "Braided multipath routing":
  * There is a primary path that is used for routing.
  * Several alternative paths are maintained for use in case of a failure in the primary path.
  * "*Braided*" path: node disjointedness between alternative paths is not a strict requirement. Rather, for each node on the primary path, the method requires the existence of an alternative path from the source to the sink *that does not contain that node*, but which may otherwise overlap with the other nodes on the main path.
  * Compared to disjoint paths, the braided path is more suitable for *isolated failures*, while disjoint paths are more appropriate for pattern *(geographically correlated)* failures.

## Gradient Cost Routing (GRAd)
(Slide 28)
* All nodes in the network maintain an estimated **cost to the sink** (such as the number of hops needed to reach it).
* When a packet is transmitted, it includes a field with the cost **"paid"** already in the current data propagation. Also, a **remaining value** field is maintained, acting as a TTL (time-to-live) field for that packet.
* Any receiver that receives this packet forwards the packet **iff its own cost to the sink is smaller than the remaining value of the packet**. Before forwarding, the "cost paid" field is increased by one and the remaining value field is decreased by one.
* GRAd actually **allows multiple** nodes to **forward the same message**, so it essentially performs *a limited directed flooding* towards the sink and provides significant robustness but at the cost of a larger overhead.

## Gradient Broadcast Routing (GRAB)
(Slide 29)
* It enhances GRAd by **incorporating a tunable energy-robustness trade-off** through the use of credits.
* Similarly to GRAd, GRAB maintains a cost field at each node. Additionally, the packets travel from a source to the sink with a **credit value** that is decreased at each step depending on the hop cost.
* **Credit-sharing mechanism:** Earlier hops receive a larger share of the total credit in a packet, while the later nodes receive a smaller share. Intermediate nodes with greater credit can spend a larger budget sending the packet to a larger set of forwarding neighbours. This way, paths *spread out initially* while eventually the *diverse paths converge to the sink* efficiently.
[Figure: Shows paths spreading from Source and converging towards Sink]

## C2. The Probabilistic Forwarding Protocol (PFR)
(Slide 30)
We assume that each node (particle) has the following abilities:
i) It can estimate **the direction of a received transmission** (e.g. via the technology of direction-sensing antennae).
ii) It can estimate **the distance** from a nearby particle that did the transmission (e.g. via estimation of the attenuation of the received signal).
iii) It knows the **direction towards the sink S**. This can be implemented during a set-up phase, where the sink broadcasts information about itself to all particles.
iv) All particles have a common **coordinates system**.
Note that *GPS information is not needed* for this protocol. Also, there is no need to know the global structure of the network.

## Propagation Protocol Properties
(Slide 31)
* **Correctness.** Protocol \Pi must guarantee that *data arrives to the sink* S, given that the network is operational.
* **Robustness.** Protocol \Pi must guarantee that data arrives at enough points in a small interval around S, in cases where part of the network has become inoperative.
* **Efficiency.** Protocol \Pi should have a *small ratio* of the number k of *activated* particles over the total number N of particles r = k/N. Thus r is an energy efficiency metric of \Pi.

## The basic idea of PFR
(Slide 32)
PFR *probabilistically favours* transmissions toward the sink within a *thin zone* of particles around the line connecting the particle sensing the event E and the sink.
[Figure: Shows a grid of particles, Event E, Sink S, and a thin zone of solid dot particles that participate in the forwarding path]

## The Forwarding Probability
(Slide 33)
Data is propagated with a suitably chosen *probability p*, while it is not propagated with probability 1 - p.
To *favour near-optimal transmissions* we choose
P_fwd = \phi / \pi
[Figure: Shows an angle \phi_1, \phi_2 from nodes p1, p2 relative to the line ES]

## The two phases of PFR
(Slide 34)
**Phase 1: The "Front" Creation Phase.** Initially a *sufficiently large "front" of particles* is built (by using a limited, in terms of rounds, flooding), to guarantee the survivability of the data propagation process. Each particle having received the data, *deterministically broadcasts* them toward the sink.

**Phase 2: The Probabilistic Forwarding Phase.**
Each particle p receiving info(\epsilon), broadcasts it to all its neighbours with *probability* P_fwd (or it does not propagate any data with probability 1 - P_fwd) defined as follows:
P_fwd = 
  1 if \phi >= \phi_threshold = 134^\circ
  \phi / \pi otherwise

## The Correctness of PFR
(Slide 35)
**Lemma**
PFR *always succeeds* in sending the information from E to S when the whole network is operational.

In the proof, geometry is used (i.e. we *cover* the network area by unit squares and show that there are always particles "*close enough*" *to the optimal line*, i.e. with \phi > 134^\circ, that deterministically broadcast).

## The Energy Efficiency of PFR
(Slide 36)
* Consider particles that are active but *as far as possible* from ES
[Figure: Showing an area L_Q of active particles around the line ES with distance w]
The particles inside the L_Q Area
* w is *approximated* with the following random walk
[Figure: Random walk in x and y coordinates]

## The Energy Efficiency of PFR
(Slide 37)
By using stochastic dominance by a continuous time "discouraged arrivals" birth-death process, the following is proved:
**Theorem**
The energy efficiency of the PFR protocol is \Theta( (n_0 / n)^2 ) where n_0 = |ES| and the total number of particles in the network is N = n^2.
For n_0 = o(n), this is o(1).

## The Robustness of PFR
(Slide 38)
Particles *very near the ES line* are considered.
Consider the case when *some* of these particles (at angles > 134^\circ) are *not operating*.
The probability that none of them transmits is *very small*.
Authors show:
**Lemma**
PFR manages to propagate the crucial data across lines parallel to ES, and of constant distance, with *fixed* nonzero probability.

## Experimental Comparison of LTP and PFR
(Slide 39)
* C++
* 2D geometry data types of LEDA
* a variety of sensor fields in a 100m \times 100m square area:
  * we drop randomly n \in [100, 3000] particles (i.e. 0.01 <= d <= 0.3)
  * fixed radio range R = 5m
  * search angle a = 90^\circ
* each experiment was repeated for more than 5000 times to get good average results

## LTP - The impact of angle \alpha
(Slide 40)
* \alpha -> 0 => C_h -> 1
* C_h initially decreases very fast, while having a limiting behavior for \alpha <= 40
[Figure: Line chart "Ideal Hops Efficiency for angles \alpha \in [5, 90]", showing Hops Efficiency vs Maximum Angle. "Local Target" and "Min-Two Targets" lines shown.]

## LTP - The impact of sampling several targets
(Slide 41)
* # targets \uparrow => C_h -> 1
* 4 targets => already very close to optimal
[Figure: Line chart "Ideal Hops Efficiency for different number of targets", showing Hops Efficiency vs Min-# Targets.]

## LTP - Failure rate
(Slide 42)
* A variety of sensor fields: (n \in [100, 5000], 0.01 <= d <= 0.5, 100m \times 100m square, R = 5m)
* for d <= 0.1 both protocols almost always backtrack
* for d >= 0.2 the failure rate drops very fast to 0.
[Figure: Line chart "Failure rate for density d \in [0.01, 0.5] and \alpha = 90", showing Failure Rate vs Particle Density.]

## Ratio of activated particles over density
(Slide 43)
[Figure: Line chart showing Ratio of Active Particles over Total Particles (r) vs Particle Density (d) for PFR, LTPe, LTPa, LTPr]
* PFR behaves very well (r <= 0.3) for low densities (d <= 0.07)
* PFR's energy dissipation increases with density
* LTP performs best in dense networks

## Backtracks over density
(Slide 44)
[Figure: Line chart showing Number of Hops to reach Sink vs Particle Density (d) for PFR, LTPe, LTPa, LTPr]
* For very low densities (i.e. d <= 0.12), LTP backtracks a lot.
* As density increases, the number of backtracks of LTP reduces fast and almost reaches zero.

## Success Rate over Network Size
(Slide 45)
[Figure: Line chart showing Success Rate vs Network Size for PFR 0.05, PFR 0.8, H-TEEN 0.05, H-TEEN 0.8]
* For small networks, 0.85 <= P_s <= 1.
* For large networks, success rate drops:
  * For SW-PFR P_s -> 0.7.
  * For H-TEEN P_s -> 0.8 for I_s = 0.05, and P_s -> 0.3 for I_s = 0.8.

## Success Rate over Injection Rate
(Slide 46)
[Figure: Line chart showing Success Rate vs Event Rate for PFR 500x500, PFR 1500x1500, H-TEEN 500x500, H-TEEN 1500x1500]
I_s \in [0.05, 0.8]
* For large networks the success rate of H-TEEN drops significantly when I_s increases.
* SW-PFR seems to be less affected by changes in I_s.

## Average Energy over Time
(Slide 47)
[Figure: Line chart showing Average Energy per Particle (J) vs Simulation Rounds for PFR 500x500, PFR 1000x1000, H-TEEN 500x500, H-TEEN 1000x1000]
* For small network size, H-TEEN is more energy efficient.
* For large network size, the energy consumption of H-TEEN increases dramatically.
* The energy consumption of SW-PFR is almost identical in both cases.

## Number of Alive Particles over Time
(Slide 48)
[Figure: Line chart showing Alive Particles vs Simulation Rounds for PFR 500x500, PFR 1000x1000, H-TEEN 500x500, H-TEEN 1000x1000]
* For small network size SW-PFR "drains" particles rapidly.
* For large network size H-TEEN "drains" particles rapidly.

## Conclusions
(Slide 49)
* SW-PFR behaves quite well for all network sizes and injection rates.
* SW-PFR tends to strain the particles which lie close to the sink more.
* H-TEEN behaves very well on small network size and low injection rate settings, while it is "expensive" on large network areas and high injection rate.

## The End
(Slide 50)
Questions?
