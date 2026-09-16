# Transcriptions: Data Propagation Algorithms

## Lecture 2: Data Propagation Algorithms I (Directed Diffusion & LEACH)

### Slide 1:
**Internet of Things**
Lecture 1: Data Propagation Algorithms
Prof. Constantinos Marios Angelopoulos
mangelopoulos@ihu.gr
MSc in Web Intelligence

### Slide 2: The problem
“How can sensor p, via cooperation with the rest of the sensors in the network, propagate information about event E to the control center(s)?”

[Figure: A sensor field showing sensor nodes as circles inside a cloud-like shape. An event is detected by a node, and a path of interconnected nodes (black circles connected by arrows) propagates this information to the Control Center antenna.]

### Slide 3: Lecture Overview
A Detailed presentation of Directed Diffusion
B Detailed presentation of LEACH

### Slide 4: Flat vs Hierarchical Routing
* **Flat Routing:** All nodes in the network have similar role regarding the routing of data. No special nodes are used.
  - Example: Directed Diffusion
* **Hierarchical Routing:** Special nodes assume greater responsibility regarding routing of data than most nodes inside the network. Super nodes – cluster heads.
  - Example: LEACH

### Slide 5: A. Directed Diffusion
C. Intanagonwiwat, R. Govindan, D. Estrin
“Directed Diffusion: A Scalable and Robust Communication Paradigm for Sensor Networks”
6th Annual International Conference on Mobile Computing and Networking, 2000

### Slide 6: Introduction
Sensor networks require coordination in order to perform distributed event sensing.

Directed diffusion is a
* data-centric
* application aware
* energy efficient
coordination paradigm for delivering sensed data.

### Slide 7: Introduction
Challenges for directed diffusion:
* **Scalability:** The protocol should maintain correctness when the network scales a)in diameter; b)in number of nodes; c)in data volume
* **Energy efficiency:** The protocol should be kind in energy consumption so as to guarantee good network lifetime
* **Robustness / Fault tolerance:** The protocol should cope well with dynamics (at least to some degree)
* **Efficient routing:** In terms of a) number of nodes involved in propagating a single message; b)time delay; c)successful delivery rate.

### Slide 8: Directed Diffusion
Directed diffusion elements:
* Interest messages
* Data messages
* Gradients
* Reinforcements of gradients

### Slide 9: Interests and tasks
* An interest contains the description of a sensing task.
* Task descriptions are identified e.g. by a list of attribute-value pairs.
* The description specifies an interest for data matching the attributes.

Example of an interest:
```text
type = wheeled vehicle      // detect vehicle location
interval = 100 ms           // send events every 100 ms
duration = 10 seconds       // for the next 10 seconds
rect = [-100, 100, 200, 400] // from nodes within rectangle
```

### Slide 10: Interests - What happens at the Sink
Interests are injected into the network at some (possibly arbitrary) node, the sink. The sink diffuses the interests through the sensor network.
* For each interest a task is generated.
* For each active task the sink generates an exploratory interest message.

```text
type = wheeled vehicle
interval = 0.1s
rect = [-100, 100, 200, 400]
timestamp = 01:20:40
expiresAt = 01:30:40
```

Note that:
* An interest is periodically refreshed by the sink.
* Interests do not contain information about the sink.
* Interests can be aggregated e.g. interests with identical types and completely overlapping rect attributes.

### Slide 11: Interests - What happens at the Nodes
Every node maintains an interest cache.
Upon interest reception a new entry is created in the cache.
This includes:
* A timestamp that stores the timestamp of the last received matching interest.
* A gradient entry, up to one per neighbor, is created. Each gradient stores:
  * Data rate.
  * Duration.

Note that:
* If an interest already exists in cache only a new gradient is created for this interest.
* An interest is erased from cache only when every gradient has expired.

### Slide 12: Gradients
Gradients are formed by local interaction of neighboring nodes.
Neighboring nodes establish a gradient towards each other.
Gradients store a value and a direction.
Gradients facilitate ”pulling down” data towards the sink.

[Figure: Gradient establishment when flooding an interest. A network graph showing a Source and a Sink. Red arrows (gradients) point from all nodes towards the Source.]

### Slide 13: Data propagation
A sensor that receives an interest it can serve, begins sensing.
As soon as a matching event is detected:
* The node computes the highest requested event rate among it’s gradients.
* The node generates event samples at this rate.

```text
type = wheeled vehicle      // type of vehicle
instance = truck            // instance of this type
location = [125, 220]       // node location
intensity = 0.6             // signal amplitude measure
confidence = 0.85           // confidence in the match
timestamp = 01:20:40        // local event generation time
```

* Data messages are unicasted individually to the relevant neighbors (neighbors where gradients point to).

### Slide 14: Data propagation
Every node maintains a data cache.
A node receives a data message.
* If the data message doesn’t have a matching interest or data exists in cache, the message is dropped.
* Otherwise, the message is added to the data cache and is forwarded.

To forward a message:
* A node determines the data rate of received events by examining it’s data cache.
* If the requested data rate on all gradients is greater or equal to the rate of incoming events, the message is forwarded.
* If some gradients have lower data rate then the data is down-converted to the appropriate rate.

### Slide 15: Reinforcement for Path Establishment and Truncation
1. The sink initially repeatedly diffuses an interest for a low-rate event notification, the generated messages are called exploratory messages.
2. The gradients created by exploratory messages are called exploratory gradients and have low data rate.
3. As soon as a matching event is detected, exploratory events are generated and routed back to the sink.
4. After the sink receives those exploratory events, it reinforces one particular neighbor in order to “draw down” real data.
5. The gradients setup for receiving high quality tracking events are called data gradients.

### Slide 16: Path Establishment Using Positive Reinforcement
To reinforce a neighbor, the sink re-sends the original interest message with a smaller interval (higher rate).

```text
type = wheeled vehicle
interval = 10ms
rect = [-100, 100, 200, 400]
timestamp = 01:22:35
expiresAt = 01:30:40
```

Upon reception of this message a node updates the corresponding gradient to match the requested data rate.
If the requested data rate is higher than the rate of incoming events, the node reinforces one of it’s neighbors.

### Slide 17: Path Establishment Using Positive Reinforcement
The selection of a neighbour for reinforcement is based on local criteria e.g. the neighbour that reported first a new event is reinforced.
The data cache is used to determine which criteria are fulfilled.

[Figure: Gradient reinforcement. A network graph showing a thickened red path (reinforced path) established from the Source to the Sink.]

### Slide 18: Reinforcement for Path Establishment and Truncation
The above scheme is reactive to changes; whenever one path delivers an event faster than others, it is reinforced.
This scheme supports the existence of multiple sinks and multiple sources in the network.

[Figure: Two network graphs illustrating reinforcement for multiple sources and sinks. The left graph shows an Event and a Source 'A' sending data to Sink 'C' with paths reinforcing. The right graph shows a Source sending data to a Sink X.]

### Slide 19: Local Repair for Failed Paths
Paths may degrade over time.
A node can detect path degradation i.e. by noticing reduced event rates.
Intermediate nodes on a path can apply the reinforcement rules and repair the path.

[Figure: A network graph showing a path from Source to Sink with an intermediate node 'C' circumventing a failed link to repair the path.]

### Slide 20: Negative Reinforcement
A mechanism for truncating paths is required.
* Gradients timeout unless they are explicitly reinforced.
* Negative reinforcement of a path.

Negative reinforcement is achieved by sending an interest with exploratory data rate.
If all outgoing gradients of a node are exploratory the node negatively reinforces it’s neighbours.
Negative reinforcement is applied when certain criteria are met e.g. a gradient doesn’t deliver any new messages for an amount of time.

### Slide 21: Loop removal
Loops don’t deliver new events.
Some loops can’t be broken.

[Figure: Two graphs showing removable and unremovable loops in data propagation paths.]

### Slide 22: Direct Diffusion - Overview
[Figure: Three graphs side-by-side: (a) Interest propagation showing dashed arrows from Sink to Source, (b) Initial gradients set up showing red arrows pointing towards Source, (c) Data delivery along reinforced path showing a solid black path from Source to Sink.]

### Slide 23: Analytic Evaluation
Let n sources and m sinks in a square grid topology of size √N × √N.
Let dn (dm) the number of hops between two adjacent sources (sinks).
Measure the total cost of transmission and reception of one event from each source to all sinks.
* Flooding
* Omniscient Multicast
  * Uses minimum height multicast trees
* Directed diffusion

### Slide 24: Topology
[Figure: Example of a square grid topology with 5 Sources on the left and 3 Sinks on the right, connected by a grid of nodes.]

### Slide 25: Flooding
Every event is broadcasted to all nodes in the network.
Each node broadcasts an event only once, nN transmissions.

On each channel each message is sent twice,
2n(2√N(√N − 1) + 2(√N − 1)²) receptions.

Cf = nN + 4n(√N − 1)(2√N − 1)

The order of Cf is O(nN).

### Slide 26: Omniscient Multicast
Each source transmits events along a shortest-path multicast tree.
Let Ti the tree with root source i, let C(Ti) the data delivery cost for tree Ti.

Trees overlap but each message is transmitted once and received once on each tree edge. The cost of messages transmitted on a tree can be expressed as the cost of the tree T1

It is proven that C(Ti) is in the order of O(√N) for m ≪ √N.
The cost of omniscient multicast Co is in the order of O(n√N)

### Slide 27: Directed diffusion
Assume that established paths match the shortest-path multicast trees.

If all sources send identical location estimates diffusion can perform application level duplicate suppression.

Trees overlap but each message is transmitted only once and received only once on each tree edge.

Similar to Co, Cd is in the order of O(n√N) for m ≪ √N.

### Slide 28: Simulation
Flooding, Omniscient Multicast and Directed Diffusion were simulated on ns-2.
Metrics:
* Average dissipated energy.
* Average delay.
* Distinct-event delivery ratio.

### Slide 29: Comparison - Data Delivery Cost
Cf is several orders of magnitude higher than Co and Cd
Although Co and Cd are in the same order of magnitude, Co > Cd

[Figure: Line graph comparing Data Delivery Cost per distinct data unit against network size. Diffusion shows lower cost than Omniscient Multicast.]

### Slide 30: Average dissipated energy
* Omniscient multicast dissipates significant less energy than flooding since events are delivered along a single path.
* Directed diffusion outperforms omniscient multicast as in-network aggregation suppresses duplicate messages.

[Figure: Line graph comparing Average Dissipated Energy for Diffusion, Omniscient Multicast, and Flooding. Flooding is highest, followed by Omniscient Multicast, with Diffusion being the lowest.]

### Slide 31: Average delay
* Flooding is remarkably slower due to collisions in the MAC layer.
* Directed diffusion performs comparably to omniscient multicast.

[Figure: Line graph comparing Average delay for Diffusion, Omniscient Multicast, and Flooding. Flooding has the highest delay, while Diffusion and Omniscient Multicast have lower, similar delays.]

### Slide 32: Impact of dynamics on DD
Assumptions:
* Node failures occur randomly in the network.
* Half of node failures occur on nodes on the shortest path trees.
* Sources send different location estimates.

### Slide 33: Average dissipated energy
* Average dissipated energy doesn’t increase significantly.
* Instead an improvement is observed in some cases.
* Negative reinforcement rules allow a number of high quality paths.

[Figure: Line graph comparing Average dissipated energy against network size under varying node failure percentages. Energy doesn't increase significantly.]

### Slide 34: Average delay
* Average delay increases but no more than 20%.

[Figure: Line graph comparing Average delay against network size under varying node failure percentages. Delay increases but no more than 20%.]

### Slide 35: Event delivery ratio
* Event delivery ratio reduces proportionally to node failure percentage.

[Figure: Line graph comparing Distinct Event Delivery Ratio against network size under varying node failure percentages. Delivery ratio reduces proportionally to node failure.]

### Slide 36: Impact of Data Aggregation
* Without aggregation, diffusion dissipates 3 (for larger networks) to 5 times (small network sizes) more energy.
* Longer (higher latency) alternative paths form in large networks, which are pruned by negative reinforcement.

[Figure: Line graph comparing Average dissipated energy with and without suppression. Without suppression dissipates significantly more energy.]

### Slide 37: Impact of Negative reinforcement
* Without negative reinforcement 2 times more energy is dissipated.

[Figure: Line graph comparing Average dissipated energy with and without negative reinforcement. Without negative reinforcement dissipates roughly 2 times more energy.]

### Slide 38: Impact of Radio Model
* Radios that consume high energy amounts when in the idle state, affect diffusion.
* Idle time dominates the performance of all schemes.

[Figure: Line graph comparing Average dissipated energy under a different radio model, showing all schemes performing similarly due to idle time domination.]

### Slide 39: Conclusions about Directed Diffusion
* Directed diffusion has the potential for significant energy efficiency.
* Diffusion mechanisms are stable under the range of network dynamics considered.
* The sensor radio MAC layer design affects directed diffusion significantly.

### Slide 40: B. LEACH (Low Energy Adaptive Clustering Hierarchy)
W.R. Heinzelman, A. Chandrakasan & H. Balakrishnan
“Energy-Efficient Communication Protocol for Wireless Microsensor Networks”
33rd Hawaii International Conference on System Sciences, HICCS-2000

### Slide 41: Main features of LEACH
What is LEACH?
* cluster-based protocol that minimizes energy dissipation in sensor network.
* key features:
  - localized coordination and control for cluster set-up and orientation.
  - randomized rotation of the cluster “base station” or “cluster heads” and the corresponding clusters.
  - local compression to reduce global communication.

### Slide 42: Intuitive description of LEACH
How does LEACH work:
* Network is partitioned in clusters.
* Each cluster has one cluster-head.
* Each non cluster-node sends data to the head of the cluster it belongs.
* Cluster-heads gather the sent data, compress them and send them to the base-station directly.

### Slide 43: Dynamic Clusters
[Figure: Two scatter plots showing dynamic partitioning of nodes into clusters with cluster heads, represented as Voronoi-like regions.]

### Slide 44: Operation of LEACH
* LEACH operates in rounds.
* Each round in LEACH consists of phases.
  * Advertisement Phase.
  * Cluster Set-Up Phase.
  * Steady Phase.

### Slide 45: Advertisement Phase (1/3)
Election: Node n decides with probability T(n) to elect itself cluster-head

T(n) = P / (1 - P * (r mod 1/P)) if n ∈ G
0 otherwise

P: the desired percentage of cluster heads.
r: the current round.
G: the set of nodes that have not been cluster-heads in the last 1/P rounds.

[Figure: Scatter plot of randomly distributed sensor nodes.]

### Slides 46 - 52: Example
Assume that n = 100 and P = 20% ⇒ on the average, the network will have 20 cluster heads.
* r=0;G=100 −→ T(n) = 0.2 / (1 - 0.2(0 mod 1/0.2)) = 0.2 ⇒ 0.2 × 100 = 20 CHs
* r=1;G=80 −→ T(n) = 0.2 / (1 - 0.2(1 mod 1/0.2)) = 1/4 ⇒ 0.25 × 80 = 20 CHs
* r=2;G=60 −→ T(n) = 0.2 / (1 - 0.2(2 mod 1/0.2)) = 1/3 ⇒ 1/3 × 60 = 20 CHs
* r=3;G=40 −→ T(n) = 0.2 / (1 - 0.2(3 mod 1/0.2)) = 1/2 ⇒ 0.5 × 40 = 20 CHs
* r=4;G=20 −→ T(n) = 0.2 / (1 - 0.2(4 mod 1/0.2)) = 1 ⇒ 1 × 20 = 20 CHs

What happens when r=5 ?

### Slide 53: Advertisement Phase (2/3)
On every round we want on the average the same number of cluster-heads in the network, i.e. N · P (N: number of nodes).
On first round we have NP cluster-heads.
On second round we have N(1 − P)P1 cluster-heads.

N(1 − P)P1 = N · P ⇒ P1 = P / (1 − P) = T(n)

For third round we have N(1 − P)(1 − P1)P2 cluster-heads.

N(1 − P)(1 − P1)P2 = N · P ⇒
P2 = P / (1 + P · P1 − (P + P1)) = 1 / (1 − 2P) = T(n)

By induction, we get T(n)

### Slide 54: Advertisement Phase (3/3)
Cluster-Head-Advertisement:
* Each cluster-head broadcasts an advertisement message to the rest of the nodes using CSMA-MAC protocol.
* Non cluster-head nodes hear the advertisements of all cluster-head nodes.
* Each non-cluster head node decides which cluster head to join on some local criteria; e.g. by choosing the one that has the strongest signal.

### Slide 55: Cluster Set-Up Phase
* Each cluster head is informed of the members of its cluster.
* The cluster head creates a TDMA schedule
* Cluster-head broadcasts the schedule back to the cluster members.

### Slide 56: Steady Phase
* Non cluster-heads
  * Sense the environment.
  * Send their data to the cluster head during their transmission time.
* Cluster-heads
  * Receive data from non cluster-head nodes.
  * Compress the data they have received.
  * Send their data to the base station.

The Duration of steady phase is “a priori” determined.

### Slide 57: Multiple Clusters
PROBLEM
Transmissions in one cluster can degrade communications in nearby clusters.

[Figure: Venn-diagram-like circles representing overlapping transmission ranges of nearby clusters, with nodes A, B, C.]

SOLUTION
Cluster-head chooses randomly from a list of spreading codes and informs all the members of its cluster.

### Slide 58: Hierarchical Clustering Extensions
* Non cluster-heads communicate with their cluster-heads
* Cluster-heads communicate with super-cluster-heads
* And so on . . .

Advantages: Saves a lot of energy for larger networks, more realistic
Disadvantages: More complicated implementation, latency

### Slide 59: Experimental Evaluation of LEACH
We are given a network of 100 nodes.
In the area:

[Figure: Scatter plot of 100 nodes with the base station placed at coordinates (0, 100).]

The base station is placed at (0, 100).

### Slide 60: Experimental Evaluation of LEACH
There is a comparative study between:
* Minimum-Energy-Transmission.
* Direct Transmission.
* LEACH.

The evaluation measures:
* Dead Nodes’ Distribution.
* Total Energy Dissipation.
* System Life-time.

### Slide 61: Distribution of dead nodes (1/3)
Minimum-Energy-Transmission

[Figure: Scatter plot showing Distribution of dead nodes for Minimum-Energy-Transmission. Dead nodes (hollow circles) are concentrated closer to the sink.]

* After 180 rounds nodes closer to the sink die faster!

### Slide 62: Distribution of dead nodes(2/3)
Direct-Transmission

[Figure: Scatter plot showing Distribution of dead nodes for Direct-Transmission. Dead nodes (hollow circles) are concentrated further from the sink.]

* After 180 rounds nodes further to the sink die faster!

### Slide 63: Distribution of dead nodes(3/3)

[Figure: Scatter plot showing Distribution of dead nodes for LEACH. Dead nodes are distributed in a uniform manner.]

LEACH

* After 1200 rounds nodes die in uniform manner.

### Slide 64: Total energy dissipation - network diameter
[Figure: Line graph comparing Total energy dissipated vs Network diameter for Direct, MTE, and LEACH. LEACH has the lowest energy dissipation.]

* LEACH reduces 7x to 8x compared to Direct-Transmission.
* LEACH reduces 4x to 8x compared to Minimum-Energy-Transmission.

### Slide 65: System Lifetime (1/2)
[Figure: Line graph showing Number of sensors still alive over Time steps for Direct, MTE, Static Clus, and LEACH. LEACH maintains alive nodes much longer.]

* LEACH more than doubles the useful system lifetime.
* It takes 8-times longer for the first node to die in LEACH.
* It takes 3-times longer for the last node to die in LEACH.

### Slide 66: System Lifetime (2/2)
[Figure: Table comparing Round first node dies and Round last node dies for various protocols and energies.]
Table data representation:
Energy (J/node): 0.25
Protocol -> Round first node dies -> Round last node dies
Direct -> 55 -> 117
MTE -> 5 -> 221
Static Clustering -> 41 -> 67
LEACH -> 394 -> 665

Energy (J/node): 0.5
Protocol -> Round first node dies -> Round last node dies
Direct -> 109 -> 234
MTE -> 8 -> 429
Static Clustering -> 80 -> 110
LEACH -> 932 -> 1312

Energy (J/node): 1
Protocol -> Round first node dies -> Round last node dies
Direct -> 217 -> 468
MTE -> 15 -> 843
Static Clustering -> 106 -> 240
LEACH -> 1848 -> 2608

### Slide 67: Conclusions about LEACH
LEACH is a cluster-based routing protocol.
* Minimizes energy dissipation through compression techniques in cluster-level.
* Distributes the load to all the nodes at different times.

In experimental evaluation
* LEACH reduces communication energy as much as 8x compared to DT or MTE.
* In LEACH the first node death occurs over 8 times later compared DT or MTE.
* In LEACH the last node death occurs over 3 times later compared to DT or MTE.

### Slide 68: Criticism – Variations & Improvements
* Unrealistic radio assumptions (cluster-heads must transmit directly to gateways)
* No real-life implementation
* No good for reactive applications (vs. proactive ones)
* TEEN, PEGASIS, examples of variations improving on latency and realism
* Other protocols use more hierarchical levels or/and multihop routing between cluster-heads.

### Slide 69: Thank You!
Questions?


---


## Lecture 3: Energy Balance Protocols

### Slide 1:
**Internet of Things**
Energy Balance Protocols
Prof. Constantinos Marios Angelopoulos
mangelopoulos@ihu.gr
MSc in Web Intelligence

### Slide 2: A “canonical” problem: Local Event Detection and Data Propagation
A single sensor, p, senses a local event E. The general propagation problem is the following:
“How can sensor p, via cooperation with the rest of the sensors in the network, propagate information about event E to the control center?”

[Figure: A sensor field showing sensor nodes. An event is detected and propagated either hop-by-hop through intermediate nodes or via a direct transmission to the Control Center.]

### Slide 3: Representative data propagation protocols
* **Directed Diffusion (DD):** a tree-structure protocol (suitable for low dynamics)
* **LEACH:** clustering and probabilistic approach (suitable for small area networks)
* **Local Target Protocol (LTP):** greedy, single-path optimization (best for dense networks)
* **Probabilistic Forwarding Protocol (PFR):** redundant optimized transmissions (good efficiency / fault-tolerance trade-offs, best for sparse networks)
* **Energy Balance Protocol (EBP):** guaranteeing same per sensor energy (prolongs network life-time)

### Slide 4: The Energy Balance Protocol (EBP)
All protocols tend to “strain” some specific nodes in the network.

[Figure: Two scatter plots of a network. The left shows overused nodes closer to the sink in a hop-by-hop scheme. The right shows overused distant nodes in a direct transmission scheme.]

* In a hop-by-hop scheme the nodes closer to the sink tend to be overused.
* In a direct transmission scheme the distant nodes tend to be overused.

### Slide 5: Research Question
“How can we achieve equal energy dissipation per node in order to prolong the network lifetime by avoiding early network disconnection?”

### Slide 6: A Probabilistic Solution
* Direct transmission cost is much larger than that of one-hop transmission and exhausts distant nodes.
* One-hop transmissions are cheap but tend to overuse nodes that lie closer to the sink.

Solution: “Each node chooses randomly whether to propagate the event one-hop closer to the sink or to transmit it directly to the sink”.

The goal is to “balance” the two types of transmissions and achieve equal average energy dissipation per sensor.

### Slide 7: The EBP Protocol (I)
* Network Partition:
  * Partition the network into n sectors, “slices", of width R (the transmission range).

[Figure: A network partitioned into concentric sectors or "slices" radiating outwards, with width R.]

### Slide 8: The EBP Protocol (II)
* Data Propagation:
  Each node in sector i propagates its messages according to the following rule:
  - Propagate the message to sector i − 1 with probability pi.
  - Propagate the message directly to the sink with probability 1 − pi.

The choice of pi is made such that the average per sensor energy dissipation is the same for all sensors in the network.

### Slide 9: An Instance of the Execution
There is a message on node i.

[Figure: A diagram showing a node 'i' sending a message hop-by-hop to node 'i-1' with probability p_i (cost-hop), or directly to the 'Sink' with probability 1 - p_i (i^2 cost-hop).]

### Slide 10: Balanced Average per Sensor Energy Dissipation
* Si: the area size of sector i.
* Ei: the total energy dissipated in sector i.
* Sensor nodes are spread uniformly at random in the network area. We want:

E[Ei] / Si = E[Ej] / Sj   ∀i, j ∈ {1, . . . n}

### Slide 11: The Model & Assumptions
The events occur in random uniform positions in the network.
Let ϵij a random variable that measures the dissipated energy by sector i, so as to handle message j.

ϵij =
{
  cR²       with probability pi
  c(iR)²    with probability 1 − pi
}

Clearly,
E[ϵij] = pi cR² + (1 − pi)c(iR)² ⇒
E[ϵij] = [i² − pi(i² − 1)]cR²

### Slide 12: Computation of pi (message handling)
* Let hi the number of messages that were handled by sector i.
* Let fi the number of messages that were forwarded to sector i.
* Let gi the number of messages that were generated in sector i.

Clearly:
hi = fi + gi

By linearity of expectation:
E[hi] = E[fi] + E[gi]

### Slide 13: Computation of pi
Lemma
The following relationship holds:
E[fi] = pi+1 E[hi+1] = pi+1 · (E[fi+1] + E[gi+1])

Clearly:
pi+1 = E[fi] / (E[fi+1] + E[gi+1])

The Energy Balance Property:
E[ Σ(k=1 to hi) ϵik / Si ] = E[ Σ(k=1 to hj) ϵjk / Sj ]   ∀i, j ∈ {1, . . . n}

### Slide 14: A recurrence relation for pi
a(i + 1)E[fi+1] − (d(i) + a(i))E[fi] + d(i − 1)E[fi−1] = a(i)E[gi] − a(i + 1)E[gi+1]

where
a(i) = i² / (2i − 1)
d(i) = ((i + 1)² − 1) / (2i + 1)

Initial conditions:
E[fn] = 0   E[f0] = n

### Slide 15: Computation of pi
Structure of the rest of the solution.
* First we transform the recurrence into a simpler recurrence with only two successive terms (whose coefficient is 1).
* Having solved the latter recurrency, we solve the initial one.
* Having computed the values of E[fi] for i = 1, . . . , n, we compute the exact values of probabilities pi.

### Slide 16: The exact solution
- The solution:

E[fi] = - Σ(k=1 to n-i) [ Π(j=k to n-i+1) a(n - j) / Π(j=k to n-i) d(n - j) ] · ( Σ(j=1 to n-k) (a(j)E[gj] - a(j+1)E[gj+1]) + a(1) · E[f1] )

where
Π(i) (from i-1) a(i) = 1

- Easily computed in a repetitive manner
- Thus we can calculate pi’s:
pi+1 = E[fi] / (E[fi+1] + E[gi+1])

### Slide 17: A closed approximate form for pi
If E[fi] ≃ E[fi−1] then

pi = 1 − (3x) / ((i + 1)(i − 1))    for 3 ≤ i ≤ n

p2 = x and can be set to 1/2

E[fi] ≃ E[fi−1] is realistic because:
* Si ≃ Si−1
* pi ≃ pi−1.

### Slide 18: Comments on pi
- when i is large, pi is large, i.e. when far away from the sink it is better to move hop-by-hop, to avoid spending too much energy.
- when i becomes small, pi is small, i.e. when we approach the sink it is better to transmit directly in order to bypass the critical region (and since energy consumption is small).

### Slide 19: Lifespan Maximization
[Figure: Sliced network showing different communication hops, including single hops and direct-to-sink transmissions jumping over intermediate slices.]

The algorithm balances energy consumption:
- Slicing of the network
- Generalized data propagation algorithm, allows to jump over bottle-neck nodes

Note: do hops to “intermediate” slices help?

### Slide 20: Lifespan Maximization
[Figure: Sliced network highlighting a mixed data propagation algorithm where nodes choose between hop-by-hop and direct-to-sink transmissions.]

Main Theoretical Result
Lifespan is maximized by a mixed data propagation algorithm

Application
This is used to propose a distributed optimal data propagation algorithm

- mixed propagation: only single hops and direct to sink transmissions
- mixed strategies beat every other possible strategy (wrt. lifespan)

### Slide 21: Model
1. Energy cost:
Sending a message from slice i to j costs (i − j)²E/msg
2. fi,j is the message rate from slice i slice to slice j msg/t

Table:
sink | 1 | 2 | 3 | 4
--- | --- | --- | --- | ---
sink | 0 | 1 | 4 | 9 | 16
1 | 1 | 0 | 1 | 4 | 9
2 | 4 | 1 | 0 | 1 | 4
3 | 9 | 4 | 1 | 0 | 1
4 | 16 | 9 | 4 | 1 | 0

[Figure: Sliced network diagram illustrating message rates between different slices and the sink.]

### Slide 22: Model
1. Energy cost:
Sending a message from slice i to j costs (i − j)²E/msg
2. fi,j is the message rate from slice i slice to slice j msg/t

Table:
sink | 1 | 2 | 3 | 4
--- | --- | --- | --- | ---
sink | f0,0 | f0,1 | f0,2 | f0,3 | f0,4
1 | f1,0 | f1,1 | f1,2 | f1,3 | f1,4
2 | f2,0 | f2,1 | f2,2 | f2,3 | f2,4
3 | f3,0 | f3,1 | f3,2 | f3,3 | f3,4
4 | f4,0 | f4,1 | f4,2 | f4,3 | f4,4

[Figure: Sliced network diagram illustrating message rates with specific variable names like f(4,0), f(4,1), etc.]

### Slide 23: Generalized-flow maximization
Problem
Given a WSN: Maximize the generalized network flow
* Given the detection rates f0,i := gi
* Given the available energy: bi

LP to maximize the generalized-flow:
Maximize T in:
1. f0,i = Tgi (Detection rates)
2. Σ(j=0 to N) fi,j(i − j)² ≤ bi (Energy constraint)
3. Σ(j=0 to N) fi,j = Σ(j=0 to N) fj,i (Flow equations)

- gi: event generation rates (i.e. data injected at i)
- maximize time T ⇒ lifespan maximization

[Figure: Sliced network diagram alongside a Linear Programming formulation to maximize generalized-flow.]

### Slide 24: Mixed-flow maximization
Problem
Given a WSN: Maximize the mixed network flow
* Given the detection rates f0,i := gi
* Given the available energy: bi

LP to maximize the mixed-flow:
Maximize T in:
1. f0,i = Tgi (Detection rates)
2. Σ(j=0 to N) fi,j(i − j)² ≤ bi (Energy constraint)
3. Σ(j=0 to N) fi,j = Σ(j=0 to N) fj,i (Flow equations)
4. fi,j = 0 if j ∉ {0, i − 1} (mixed flow constraint)

[Figure: Sliced network diagram alongside an LP formulation to maximize mixed-flow with an added mixed flow constraint.]

### Slide 25: Mixed-flow maximization
Problem
Given a WSN: Maximize the mixed network flow
* Given the detection rates f0,i := gi
* Given the available energy: bi

LP to maximize the mixed-flow:
Maximize T in:
1. f0,i = Tgi (Detection rates)
2. Σ(j=0 to N) fi,j(i − j)² ≤ bi (Energy constraint)
3. Σ(j=0 to N) fi,j = Σ(j=0 to N) fj,i (Flow equations)
4. fi,j = 0 if j ∉ {0, i − 1} (mixed flow constraint)

(4) guarantess no hops to “intermediate” slices
(3) guarantees flow preservation

[Figure: Similar to previous slide, emphasizing flow preservation and no intermediate hops.]

### Slide 26: Mixed-flows are optimal
Result
If there exists an NRG-balanced mixed flow
1. it maximizes the mixed-flow
2. it maximizes the generalized-flow

Application
We can maximize the generalized-flow problem using:
* a mixed-flow
* a local property (energy-balance)

### Slide 27: A distributed algorithm
Definition
Inputs
1. Each node has a potential potential(n) ≃ EnergySpent(n)
2. Each node knows its list of neighbours Vn
3. Each node knows the potential of its neighbours

Algorithm Propagate Data
* Find m: the lowest potential neighbour
* If potential(m) < potential(self ) then send data to m
* Else send data directly to the sink

### Slide 28: A distributed algorithm
Illustration

[Figure: Two 3D illustrations of a distributed algorithm's potential landscape. Nodes follow the gradient, occasionally jumping over bottlenecks (peaks) to reach the sink.]

### Slide 29: A distributed algorithm
Illustration

Remark
* The algorithm produces a mixed flow
* The algorithm balances energy

[Figure: Same 3D illustration of the potential landscape.]

### Slide 30: Simulations
* Scatter nodes randomly over a region
* Events are generated randomly
* Data is propagated according to the algorithm

### Slide 31: First Simulation
* 1000 sensors randomly dispersed over a 10m disc
* Sink at the center of the disc
* Potential function potential(n) = Energy(n)

### Slide 32: First Simulation
Network flow
Messages received by sink / max{nodes}(EnergySpent)

F: the flow of the algorithm
U: maximum possible flow (offline, computed by an LP)
L: maximum possible flow without direct transmissions

[Figure: Line graph showing the network flow performance over time. The algorithm's flow approaches the maximum possible flow U computed offline.]

### Slide 33: First Simulation
Remarks
* Close to optimal
* Distributed and on-line!

[Figure: Same line graph emphasizing that the performance is close to optimal, distributed, and online.]

### Slide 34: First Simulation
- off-line ideal flow U balances the energy load
- the online algorithm performs very well

[Figure: A line graph of flow performance over time, alongside a scatter plot comparing energy for offline and online mixed algorithms vs sensor radius.]

### Slide 35: Second Simulation
* 600 sensors randomly dispersed over 2 intersecting 30° sector graphs of 10m diameter with one sink at the narrow end of each sector
* events can be reported to either sink

[Figure: Scatter plot showing a network dispersed over 2 intersecting 30-degree sector graphs with sinks at the narrow ends.]

### Slide 36: Summary
1. Proved that optimal solution belongs to a subset of realistic data propagation algorithms: a mixed strategy which is energy balanced
2. Propose a distributed algorithm based on theoretical results
3. Show that the algorithm is efficient (Markov chain context and simulations)

### Slide 37: References
- C. Efthymiou, S. Nikoletseas, J. Rolim: “Energy balanced data propagation in wireless sensor networks”, in Wireless Networks (WINET) Journal, 12(6): 691-707 (2006). Also, in Proc. 4th International Workshop on Algorithms for Wireless, Mobile, Ad-Hoc and Sensor Networks (WMAN ’04), IPDPS 2004.
- P. Leone, S. Nikoletseas and J. Rolim, “An Adaptive Blind Algorithm for Energy Balanced Data Propagation in Wireless Sensor Networks”, in the IEEE International Conference on Distributed Computing in Sensor Networks (DCOSS), LNCS, Springer Verlag, Volume 3267, pp. 35-48, 2005.
- S. Nikoletseas, I. Chatzigiannakis, A. Antoniou, C. Efthymiou, A. Kinalis and G. Mylonas, “Energy Efficient Protocols for Sensing Multiple Events in Smart Dust Networks”. In Proc. 37th Annual ACM/IEEE Simulation Symposium (ANSS’04), IEEE Computer Society Press, pp. 15 .24, 2004.
- O. Powell, P. Leone, J. Rolim, “Energy optimal data propagation in wireless sensor networks”, J. Parallel Distrib. Comput. (JPDC), 67(3): 302-317 (2007).
- A. Jarry, P. Leone, O. Powell, J. Rolim, “An Optimal Data Propagation Algorithm for Maximizing the Lifespan of Sensor Networks”, in the proceedings of DCOSS 2006.
