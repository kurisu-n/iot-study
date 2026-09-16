# IoT Exam 2026 — Transcription & Coverage Analysis

> Εξέταση Μαθήματος: **Διαδίκτυο των Πραγμάτων**  
> Ημ/νία: 6 Φεβρουαρίου 2026 — Διάρκεια: 2 ώρες  
> Διδάσκων: Κωνσταντίνος Μάριος Αγγελόπουλος  
> Τα θέματα επιστρέφονται με το γραπτό.

---

## ΘΕΜΑ Α

### A.1 (1 μονάδα)
Περιγράψτε συνοπτικά, με απλούς όρους, πώς λειτουργεί το πρωτόκολλο Directed Diffusion στα ασύρματα δίκτυα αισθητήρων.

### A.2 (1,5 μονάδες)
Σε συνέχεια του προηγούμενου ερωτήματος, γράψτε μία συγκριτική αξιολόγηση του πρωτοκόλλου Directed Diffusion με το Energy Balance Protocol (EBP). Με βάση το κάθε πρωτόκολλο, πώς αναμένουμε να εξελιχθεί ένα ασύρματο δίκτυο αισθητήρων στον χρόνο ως προς την κατανάλωση ενέργειας σε κάθε κόμβο αλλά και συνολικά ως δίκτυο;

---

## ΘΕΜΑ Β

### B.1 (2,5 μονάδες)
Εξετάστε ένα ασύρματο δίκτυο αισθητήρων που αποτελείται από ασύρματους κόμβους-αισθητήρες (sensor motes). Υποθέστε ότι το δίκτυο χρησιμοποιεί το πρωτόκολλο δρομολόγησης LEACH, ρυθμισμένο να λειτουργεί σε περιόδους (eras) των **7 γύρων (rounds)**, με το **14% των κόμβων** να λειτουργούν ως αρχηγοί συστάδων (cluster-heads) σε κάθε γύρο. Να περιγράψετε και να παρουσιάσετε πώς λειτουργεί ο αλγόριθμος εκλογής των αρχηγών συστάδων για μία περίοδο (era).

---

## ΘΕΜΑ Γ

### Γ.1 (0,5 μονάδες)
Γράψτε μία συγκριτική αξιολόγηση του πρωτοκόλλου WiFi με το πρωτόκολλο LoRaWAN.

### Γ.2 (1 μονάδα)
Περιγράψτε τα βασικά δομικά στοιχεία της αρχιτεκτονικής ενός δικτύου LoRaWAN και αναφέρετε το τυπικό εύρος των ρυθμών μετάδοσης δεδομένων (data rates) που υποστηρίζει το πρωτόκολλο.

### Γ.3 (1 μονάδα)
Εξηγήστε τη σχέση μεταξύ του Spreading Factor, της εμβέλειας (communication range) και του ρυθμού μετάδοσης (data rate). Τι συμβαίνει στην κατανάλωση ενέργειας της συσκευής όταν αυξάνεται ο SF;

---

## ΘΕΜΑ Δ

### Δ.1 (2,5 μονάδες)

```
   (A) ——ETX=4.3, 5m——> (B) ——ETX=1.5, 5m——> (C)
```

Δεδομένης της παραπάνω τοπολογίας δικτύου, υποθέστε ότι:
1. Η ενέργεια που απαιτείται για τη λειτουργία της μονάδας ραδιοεπικοινωνίας για κάθε bit (τόσο για τη λήψη όσο και για τη μετάδοση) είναι **Ec = 40 [nJ/bit]**.
2. Η ενέργεια που απαιτείται για την επιτυχή μετάδοση ενός μηνύματος σε απόσταση (d) είναι **ETX(d) = k·d² [nJ/bit]**, όπου **(k = 1)**.

Να υπολογιστεί η αναμενόμενη συνολική κατανάλωση ενέργειας του δικτύου για τη δρομολόγηση ενός πακέτου μήκους **b = 200 [bits]** από τον κόμβο A στον κόμβο C μέσω πολυβηματικής (multi-hop) μετάδοσης.

---

# Coverage Analysis: Raw Notes vs 2026 Exam

## Summary

| Θέμα | Τύπος | Covered by Raw Notes? | Verdict |
|:---|:---|:---|:---|
| **A.1** DD overview | Theory (short) | ✅ **Fully covered** (Pages 1–6) | Ready |
| **A.2** DD vs EBP comparison | Theory (comparative) | ⚠️ **Partially covered** | Gap — no direct DD↔EBP comparison |
| **B.1** LEACH CH election with numbers | **Exercise** (calculation) | ✅ **Fully covered** (Pages 10–11) | Ready — but need to practice with P=14%, 1/P=7 |
| **Γ.1** WiFi vs LoRaWAN | Theory (short) | ❌ **Not covered** | Gap — LoRaWAN not in raw notes |
| **Γ.2** LoRaWAN architecture + data rates | Theory | ❌ **Not covered** | Gap — LoRaWAN not in raw notes |
| **Γ.3** Spreading Factor / range / data rate | Theory + reasoning | ❌ **Not covered** | Gap — LoRaWAN not in raw notes |
| **Δ.1** ETX multi-hop energy calculation | **Exercise** (calculation) | ✅ **Fully covered** (Pages 15–16) | Ready — same pattern, different numbers |

## Detailed Gap Analysis

### ✅ Well Covered (5/10 marks — Θέμα Α.1 + Β.1 + Δ.1)

**Θέμα A.1 — Direct Diffusion (1 μονάδα):**
The raw notes cover DD comprehensively: the 4-step cycle (interests → gradients → data propagation → reinforcement), advantages (in-network aggregation, fault tolerance), and limitations (idle listening, MAC dependency). This is a slam dunk.

**Θέμα B.1 — LEACH CH Election (2.5 μονάδες):**
The raw notes have the T(n) formula with full explanation of P, r, G, and the exclusion/probability-increase/reset cycle. The exam gives **P = 14% = 0.14** and **1/P = ~7 rounds = 1 era**. You need to:
- Show T(n) values increasing across rounds 0–6
- Show how G shrinks each round
- Demonstrate that after 7 rounds, all nodes served as CH at least once

The notes have the conceptual framework; you just need to practice plugging in P=0.14.

**Θέμα Δ.1 — ETX Multi-hop Energy (2.5 μονάδες):**
The raw notes have a *solved single-hop ETX exercise* with the exact same energy model. The exam extends this to **two hops** (A→B→C). You need to:
- Calculate E(A→B) using ETX=4.3, d=5m
- Calculate E(B→C) using ETX=1.5, d=5m
- Sum them for total network energy

Same formula, just applied twice and summed. The notes nail this pattern.

---

### ⚠️ Partially Covered (1.5 marks — Θέμα A.2)

**Θέμα A.2 — DD vs EBP Comparison (1.5 μονάδες):**
The raw notes cover DD and EBP *separately* but don't do a direct comparison. You'd need to synthesize:
- DD: flat, data-centric, reduces transmissions via aggregation but doesn't explicitly balance energy
- EBP: hierarchical, ring-based CH probability, explicitly balances energy depletion across nodes
- DD → energy-efficient but hotspots possible near sink; EBP → uniform depletion, maximizes network lifetime

The material is there, but you'd need to connect the dots yourself.

---

### ❌ Not Covered (2.5 marks — Θέμα Γ)

**Θέμα Γ — LoRaWAN (all 3 sub-questions, 2.5 μονάδες total):**
The raw notes have **zero content on LoRaWAN, WiFi comparison, Spreading Factor, or LPWAN architecture**. This material is likely in:
- **Lecture 6a** (MSc IoT - LPWANs - RPL - Architectures)
- **Lecture 7a/7b** (IoT topics / IoT protocols)
- **Lecture 8a/8b** (IEEE 802.11 / WiFi standards)

This is the biggest gap and needs to be filled from the lecture PDFs.

---

## Exam Weight Breakdown

```
Exercises (need math):     5.0 / 10 marks  (50%)  ← Θέμα Β.1 + Δ.1
Theory (short answers):    5.0 / 10 marks  (50%)  ← Θέμα Α + Γ

Covered by raw notes:      6.0 / 10 marks  (60%)
Gaps to fill from lectures: 4.0 / 10 marks (40%)  ← mainly LoRaWAN + DD↔EBP synthesis
```

## Priority for Next Steps

1. **HIGH** — Transcribe Lecture 6a (LPWANs/RPL) → covers LoRaWAN architecture, data rates, SF
2. **HIGH** — Transcribe Lecture 8a/8b (802.11/WiFi) → covers WiFi for comparison
3. **MEDIUM** — Practice LEACH T(n) calculation with P=0.14, 7 rounds
4. **MEDIUM** — Practice ETX multi-hop calculation with the exact exam numbers
5. **LOW** — Build DD vs EBP comparison notes (synthesis from existing material)
