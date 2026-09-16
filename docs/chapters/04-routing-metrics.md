<span class="chapter-num">Κεφάλαιο 4</span>

# Μετρικές Δρομολόγησης

*Καλύπτει: γιατί μετράει η ποιότητα της ζεύξης, τη μετρική Expected Transmission Count (ETX) και τι μετράει, ποια διαδρομή διαλέγει, το ενεργειακό μοντέλο, τη λυμένη άσκηση του 2026, και μια σύντομη ματιά στις άλλες μετρικές. Πηγές: Διαλέξεις 4 και 5, χειρόγραφες σημειώσεις (σελίδες 15 έως 16), θέμα εξετάσεων 2026.*

Τα προηγούμενα κεφάλαια ρώτησαν *ποιος* στέλνει και *πώς* μοιράζεται το βάρος. Αυτό το κεφάλαιο ρωτά κάτι πιο βασικό: όταν ένας κόμβος έχει πολλές διαδρομές προς τον προορισμό, **ποια να διαλέξει;** Η απάντηση δεν είναι πάντα «η συντομότερη», και ο λόγος οδηγεί στη μετρική που εξετάζεται ως άσκηση: το Expected Transmission Count (ETX).

## 4.1 Γιατί Μετράει η Ποιότητα της Ζεύξης {#link-quality}

Αν οι ασύρματες ζεύξεις ήταν τέλειες, χωρίς λάθη, η επιλογή θα ήταν εύκολη: διάλεξε τη διαδρομή με τα **λιγότερα βήματα** (Διάλεξη 4, διαφάνεια 7). Λιγότερα βήματα, λιγότερες μεταδόσεις.

Στην πραγματικότητα όμως οι ζεύξεις **δεν** είναι τέλειες. Και εδώ κρύβεται μια παγίδα: μια διαδρομή με λίγα βήματα χρησιμοποιεί μεγάλες αποστάσεις ανά βήμα, και οι ζεύξεις μεγάλης απόστασης έχουν συνήθως **χαμηλή ποιότητα**, δηλαδή τα πακέτα χάνονται συχνά και πρέπει να ξανασταλούν. Ένα «σύντομο» μονοπάτι στα βήματα μπορεί έτσι να κοστίζει **περισσότερες** μεταδόσεις από ένα μονοπάτι με πιο πολλά αλλά αξιόπιστα βήματα.

Χρειαζόμαστε λοιπόν έναν τρόπο να μετράμε την ποιότητα μιας ζεύξης. Ο απλός τρόπος: κάθε φορά που ένα πακέτο παραδίδεται επιτυχώς, ο παραλήπτης στέλνει πίσω ένα σύντομο μήνυμα επιβεβαίωσης, το λεγόμενο Acknowledgement (ACK). Μετρώντας πόσο συχνά φτάνει το ACK, ξέρουμε πόσο αξιόπιστη είναι η ζεύξη (Διάλεξη 4, διαφάνεια 7).

## 4.2 Πόσες Μεταδόσεις Χρειάζεται μια Ζεύξη {#etx-metric}

Το Expected Transmission Count (ETX) βάζει αυτή την ιδέα σε νούμερο. Για μια ζεύξη ορίζει δύο πιθανότητες (Διάλεξη 4, διαφάνεια 8):

- \(d_f\) (forward): η πιθανότητα να φτάσει επιτυχώς ένα πακέτο στον παραλήπτη.
- \(d_r\) (reverse): η πιθανότητα να γυρίσει επιτυχώς το ACK στον αποστολέα.

Μια μετάδοση θεωρείται πετυχημένη μόνο αν συμβούν **και τα δύο**: φτάσει το πακέτο και γυρίσει το ACK. Αν κάθε μετάδοση είναι μια ανεξάρτητη δοκιμή τύπου «πέτυχε ή απέτυχε», τότε ο **αναμενόμενος αριθμός μεταδόσεων** ώσπου να περάσει ένα πακέτο είναι:

<div class="formula" markdown="1">
$$\text{ETX} = \frac{1}{d_f \cdot d_r}$$

<span class="label">Ο αναμενόμενος αριθμός μεταδόσεων για μία ζεύξη (Διάλεξη 4, διαφάνεια 8)</span>
</div>

Η διαίσθηση: αν μια ζεύξη περνά το πακέτο με πιθανότητα 0.5 (μαζί με το ACK), τότε χρειάζονται κατά μέσο όρο 1/0.5 = 2 προσπάθειες. Αν η πιθανότητα είναι 0.1, χρειάζονται 10. Όσο χειρότερη η ζεύξη, τόσο μεγαλύτερο το ETX.

Για μια **ολόκληρη διαδρομή**, το ETX είναι το **άθροισμα** των ETX όλων των ζεύξεών της (χειρόγραφες σημειώσεις, σελίδα 15). Η λογική δρομολόγησης είναι απλή: διάλεξε τη διαδρομή με το **μικρότερο άθροισμα ETX**, δηλαδή με τις λιγότερες συνολικά αναμενόμενες μεταδόσεις.

## 4.3 Ποια Διαδρομή Διαλέγει η Μετρική {#which-path}

Το παράδειγμα των διαφανειών δείχνει καθαρά γιατί το ETX δεν προτιμά ούτε τις πολύ σύντομες ούτε τις πολύ μακριές διαδρομές (Διάλεξη 4, διαφάνεια 9). Έχουμε τρεις διαδρομές από το A στο B. Για απλότητα, όλες οι αντίστροφες πιθανότητες είναι \(d_r = 1\), οπότε το ETX κάθε ζεύξης είναι απλώς \(1/d_f\):

<!-- etx_figures:routes -->
<figure class="steps steps--three" id="fig-4-1">
<div class="steps__grid"><div class="step"><svg viewBox="0 0 260 180" xmlns="http://www.w3.org/2000/svg" role="img"><line x1="36.5" y1="90.0" x2="220.0" y2="90.0" stroke="var(--fig-warn)" stroke-width="2" stroke-dasharray="5 4" stroke-linecap="round"/><polygon points="220.0,90.0 214.0,93.2 214.0,86.8" fill="var(--fig-warn)"/><circle cx="78.0" cy="44.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="130.0" cy="36.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="182.0" cy="44.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="130.0" cy="148.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="30.0" cy="90.0" r="7.5" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="1.8"/><rect x="220.0" y="80.0" width="20" height="20" rx="2" fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="1.8"/><circle r="3.4" fill="var(--fig-warn)" stroke="var(--fig-node)" stroke-width="1" class="fig-packet" style="offset-path: path('M 30.0 90.0 L 230.0 90.0'); offset-rotate: 0deg;"/></svg><p class="step__text"><span class="step__num">1</span><strong>Απευθείας.</strong> Μία μόνο ζεύξη, αλλά χαμηλής ποιότητας 0.1. Χρειάζονται κατά μέσο όρο 1 / 0.1 = <strong>10</strong> μεταδόσεις.</p></div><div class="step"><svg viewBox="0 0 260 180" xmlns="http://www.w3.org/2000/svg" role="img"><line x1="34.7" y1="85.5" x2="73.3" y2="48.5" stroke="var(--fig-warn)" stroke-width="1.6" stroke-linecap="round"/><polygon points="73.3,48.5 71.2,55.0 66.8,50.3" fill="var(--fig-warn)"/><line x1="84.4" y1="43.0" x2="123.6" y2="37.0" stroke="var(--fig-warn)" stroke-width="1.6" stroke-linecap="round"/><polygon points="123.6,37.0 118.1,41.1 117.2,34.7" fill="var(--fig-warn)"/><line x1="136.4" y1="37.0" x2="175.6" y2="43.0" stroke="var(--fig-warn)" stroke-width="1.6" stroke-linecap="round"/><polygon points="175.6,43.0 169.2,45.3 170.1,38.9" fill="var(--fig-warn)"/><line x1="186.7" y1="48.5" x2="222.8" y2="83.1" stroke="var(--fig-warn)" stroke-width="1.6" stroke-linecap="round"/><polygon points="222.8,83.1 216.2,81.2 220.7,76.6" fill="var(--fig-warn)"/><circle cx="78.0" cy="44.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="130.0" cy="36.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="182.0" cy="44.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="130.0" cy="148.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="30.0" cy="90.0" r="7.5" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="1.8"/><rect x="220.0" y="80.0" width="20" height="20" rx="2" fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="1.8"/><circle r="3.4" fill="var(--fig-warn)" stroke="var(--fig-node)" stroke-width="1" class="fig-packet" style="offset-path: path('M 30.0 90.0 L 78.0 44.0 L 130.0 36.0 L 182.0 44.0 L 230.0 90.0'); offset-rotate: 0deg;"/></svg><p class="step__text"><span class="step__num">2</span><strong>Μέσω C, D, E.</strong> Τέσσερις σύντομες ζεύξεις καλής ποιότητας 0.9. Συνολικά 4 × (1 / 0.9) ≈ <strong>4.44</strong> μεταδόσεις.</p></div><div class="step"><svg viewBox="0 0 260 180" xmlns="http://www.w3.org/2000/svg" role="img"><line x1="35.6" y1="93.3" x2="124.4" y2="144.7" stroke="var(--fig-ok)" stroke-width="2.6" stroke-linecap="round"/><polygon points="124.4,144.7 117.6,144.5 120.8,139.0" fill="var(--fig-ok)"/><line x1="135.6" y1="144.7" x2="221.3" y2="95.0" stroke="var(--fig-ok)" stroke-width="2.6" stroke-linecap="round"/><polygon points="221.3,95.0 217.8,100.8 214.6,95.3" fill="var(--fig-ok)"/><circle cx="78.0" cy="44.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="130.0" cy="36.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="182.0" cy="44.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="130.0" cy="148.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><circle cx="30.0" cy="90.0" r="7.5" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="1.8"/><rect x="220.0" y="80.0" width="20" height="20" rx="2" fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="1.8"/><circle r="3.4" fill="var(--fig-warn)" stroke="var(--fig-node)" stroke-width="1" class="fig-packet" style="offset-path: path('M 30.0 90.0 L 130.0 148.0 L 230.0 90.0'); offset-rotate: 0deg;"/></svg><p class="step__text"><span class="step__num">3</span><strong>Μέσω F.</strong> Δύο ζεύξεις μέτριας ποιότητας 0.8: 2 × (1 / 0.8) = <strong>2.5</strong> μεταδόσεις. Το μικρότερο άθροισμα, άρα τη διαλέγει το ETX.</p></div></div>
<div class="legend"><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><circle cx="9" cy="7" r="5.5" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="1.5"/></svg>κόμβος-πηγή</span><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><circle cx="9" cy="7" r="5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.2"/></svg>ενδιάμεσος κόμβος</span><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><rect x="3" y="1" width="12" height="12" rx="1.5" fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="1.5"/></svg>προορισμός</span><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-warn)" stroke-width="2" stroke-dasharray="5 4"/></svg>ζεύξη χαμηλής ποιότητας</span><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-warn)" stroke-width="1.8"/></svg>ζεύξη της διαδρομής</span><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-ok)" stroke-width="2.6"/></svg>η διαδρομή που διαλέγει το ETX</span><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><circle cx="9" cy="7" r="3.4" fill="var(--fig-warn)" stroke="var(--fig-node)" stroke-width="1"/></svg>πακέτο</span></div>
<figcaption>Σχήμα 4.1 · Τρεις διαδρομές από το A στο B, και ποια διαλέγει το Expected Transmission Count (ETX). Διάλεξη 4, διαφάνεια 9.</figcaption>
</figure>
<!-- /etx_figures:routes -->

Η νικήτρια είναι η μεσαία λύση, η διαδρομή μέσω F: ούτε η μία ριψοκίνδυνη ζεύξη της απευθείας διαδρομής, ούτε οι πολλές ζεύξεις της διαδρομής μέσω C, D, E. Το ETX **παίρνει τη μέση οδό** (Διάλεξη 4, διαφάνεια 10): προτιμά λίγες, αξιόπιστες ζεύξεις μέτριας απόστασης.

## 4.4 Πλεονεκτήματα και Όρια {#strengths-limits}

**Τι κερδίζει το ETX** (Διάλεξη 4, διαφάνεια 10, και χειρόγραφες σημειώσεις, σελίδα 16):

- **Λιγότερες μεταδόσεις, λιγότερη ενέργεια.** Ελαχιστοποιώντας τις αναμενόμενες μεταδόσεις, μειώνει και την ενέργεια, αφού κάθε μετάδοση κοστίζει.
- **Αντιμετωπίζει την ασυμμετρία.** Επειδή λαμβάνει υπόψη και τις δύο κατευθύνσεις (\(d_f\) και \(d_r\)), πιάνει ζεύξεις που δουλεύουν καλά προς τη μία φορά αλλά όχι προς την άλλη.
- **Ισορροπία.** Διαλέγει με βάση την πραγματική απόδοση, όχι απλώς την απόσταση.

**Πού αδυνατεί:** το ETX προϋποθέτει ότι γνωρίζουμε τις πιθανότητες \(d_f\) και \(d_r\). Αυτό είναι εφικτό σε **στατικά** δίκτυα, όπου μετρώνται περιοδικά. Σε **δυναμικά** δίκτυα, όπου οι κόμβοι κινούνται και η ποιότητα αλλάζει γρήγορα, οι μετρήσεις παλιώνουν αμέσως και το κόστος της συνεχούς παρακολούθησης γίνεται απαγορευτικό. Για τέτοιες περιπτώσεις προτείνεται μια άλλη μετρική, το Minimum Outage Route (MOR), που στηρίζεται σε αναλυτικό μοντέλο του καναλιού αντί σε μετρήσεις (Διάλεξη 4, διαφάνειες 10 και 13).

## 4.5 Το Ενεργειακό Μοντέλο {#energy-model}

Η άσκηση των εξετάσεων συνδέει το ETX με **ενέργεια**. Χρειαζόμαστε δύο κόστη ανά bit (Διάλεξη 4, διαφάνεια 11):

- \(E_c\): η ενέργεια για να λειτουργήσει το ραδιόφωνο ανά bit. Πληρώνεται **και** στη μετάδοση **και** στη λήψη (τα ηλεκτρονικά του πομποδέκτη δουλεύουν και στις δύο πλευρές).
- \(E_{tx}(d) = k \cdot d^2\): η επιπλέον ενέργεια ανά bit για να φτάσει το σήμα σε απόσταση d (ο ενισχυτής). Μεγαλώνει με το τετράγωνο της απόστασης, όπως και στα προηγούμενα κεφάλαια.

Μία **μεμονωμένη προσπάθεια** μετάδοσης ενός πακέτου b bits σε μια ζεύξη μήκους d κοστίζει, λοιπόν: \(E_c \cdot b\) στον πομπό (ραδιόφωνο) + \(E_{tx}(d) \cdot b\) στον πομπό (ενισχυτής) + \(E_c \cdot b\) στον δέκτη (ραδιόφωνο).

Εδώ αξίζει να λυθεί μια φαινομενική αντίφαση, γιατί μπερδεύει εύκολα. Στην [ενότητα 4.2](#etx-metric) είπαμε ότι μια επιτυχής παράδοση χρειάζεται **δύο ταξίδια**: να φτάσει το πακέτο *και* να γυρίσει το ACK. Γιατί λοιπόν το κόστος εδώ μετρά μόνο **ένα** ταξίδι, το πήγαινε του πακέτου;

Ο λόγος είναι ότι το ACK είναι **ελάχιστο**: λίγα bits, μπροστά στα 200 του πακέτου. Το μοντέλο αγνοεί εντελώς την ενέργειά του. Δεν χάνεται όμως από την εικόνα· απλώς μπαίνει ως **πιθανότητα, όχι ως ενέργεια**. Η πιθανότητα της επιστροφής, το \(d_r\), ζει μέσα στο ETX (θυμηθείτε, \(\text{ETX} = 1/(d_f \cdot d_r)\)): μια κακή διαδρομή επιστροφής ανεβάζει το ETX, άρα χρειάζονται περισσότερα ταξίδια **του πακέτου**, και αυτά είναι που κοστίζουν. Έτσι το δεύτερο ταξίδι επηρεάζει το **πόσες φορές** στέλνουμε, όχι το κόστος της κάθε φοράς.

Και μια δεύτερη, μικρότερη σύγχυση: το \(E_c\) εμφανίζεται δύο φορές όχι επειδή στέλνουμε δύο φορές, αλλά επειδή αυτό το **ένα** ταξίδι μοιράζεται σε **δύο κόμβους**. Πληρώνουν τα ηλεκτρονικά τους και οι δύο άκρες της ίδιας μετάδοσης: ο πομπός για να στείλει, ο δέκτης για να λάβει. Ο ενισχυτής \(E_{tx}(d)\) μπαίνει μία φορά, γιατί μόνο ο πομπός «σπρώχνει» το σήμα· ο δέκτης απλώς ακούει. Καμία ανάγκη λοιπόν για ×2.

Και επειδή χρειάζονται κατά μέσο όρο ETX προσπάθειες για να περάσει το πακέτο, πολλαπλασιάζουμε επί ETX:

<div class="formula" markdown="1">
$$E_{\text{ζεύξης}} = \text{ETX} \cdot \big(\,E_c \cdot b + E_{tx}(d) \cdot b + E_c \cdot b\,\big)$$

<span class="label">Ενέργεια για την παράδοση ενός πακέτου σε μία ζεύξη (Διάλεξη 4, διαφάνεια 12)</span>
</div>

Ας το δούμε στο παράδειγμα των διαφανειών: μια ζεύξη A → B με ETX = 1.3 και απόσταση d = 5 m, με \(E_c = 50\) nJ/bit, \(k = 1\), και πακέτο b = 100 bits (Διάλεξη 4, διαφάνειες 11 έως 12):

<div class="trace-label">Ενέργεια της ζεύξης A → B</div>
<div class="trace" markdown="1">
$$
\begin{aligned}
E_{A \to B} &= \text{ETX} \cdot \big(E_c \cdot b + E_{tx}(d) \cdot b + E_c \cdot b\big) && \\[0.7em]
            &= 1.3 \cdot \big(50 \cdot 100 + 1 \cdot 5^2 \cdot 100 + 50 \cdot 100\big) && (\text{ETX}=1.3,\ E_c=50,\ d=5,\ b=100) \\[0.7em]
            &= 1.3 \cdot \big(50 \cdot 100 + 25 \cdot 100 + 50 \cdot 100\big) && (1 \cdot 5^2 = 25) \\[0.7em]
            &= 1.3 \cdot \big(5000 + 2500 + 5000\big) && (\text{κάθε όρος} \times 100) \\[0.7em]
            &= 1.3 \cdot 12500 && (5000 + 2500 + 5000 = 12500) \\[0.7em]
            &= 16250 \text{ nJ} = 16.25\ \mu\text{J} && (1000 \text{ nJ} = 1\ \mu\text{J})
\end{aligned}
$$
</div>

!!! exam "Τι να περιμένετε στην εξέταση"

    <div class="exam-record"><a class="exam-chip is-hit" href="../../#exam-papers"><strong>6/2/2026</strong> βάση του Θέματος Δ.1</a><a class="exam-chip" href="../../#exam-papers"><strong>15/2/2025</strong> όχι</a><a class="exam-chip" href="../../#exam-papers"><strong>2/2022</strong> όχι</a></div>

    Αυτός ο τύπος είναι το εργαλείο της άσκησης. Το κλειδί είναι να θυμάστε τους **τρεις** ενεργειακούς όρους ανά προσπάθεια (ραδιόφωνο πομπού, ενισχυτής, ραδιόφωνο δέκτη) και ότι όλα πολλαπλασιάζονται επί το ETX. Η [επόμενη ενότητα](#worked-2026) λύνει το θέμα του 2026 με τα ακριβή του νούμερα.

## 4.6 Λυμένη Άσκηση: το Θέμα Δ.1 του 2026 {#worked-2026}

!!! question "Η εκφώνηση (6 Φεβρουαρίου 2026, Θέμα Δ.1, 2.5 μονάδες)"

    Δίνεται η τοπολογία A —(ETX = 4.3, 5 m)— B —(ETX = 1.5, 5 m)— C. Υποθέστε ότι η ενέργεια λειτουργίας του ραδιοφώνου ανά bit (λήψη και μετάδοση) είναι \(E_c = 40\) nJ/bit, και ότι η ενέργεια επιτυχούς μετάδοσης σε απόσταση d είναι \(E_{tx}(d) = k \cdot d^2\) nJ/bit με k = 1. Να υπολογιστεί η αναμενόμενη συνολική κατανάλωση ενέργειας του δικτύου για τη δρομολόγηση ενός πακέτου b = 200 bits από το A στο C μέσω πολυβηματικής μετάδοσης.

<!-- etx_figures:hops -->
<figure class="steps" id="fig-4-2">
<div class="step"><svg viewBox="0 0 260 180" xmlns="http://www.w3.org/2000/svg" role="img"><line x1="40.5" y1="90.0" x2="123.5" y2="90.0" stroke="var(--fig-warn)" stroke-width="2" stroke-linecap="round"/><polygon points="123.5,90.0 117.5,93.2 117.5,86.8" fill="var(--fig-warn)"/><line x1="136.5" y1="90.0" x2="216.0" y2="90.0" stroke="var(--fig-warn)" stroke-width="2" stroke-linecap="round"/><polygon points="216.0,90.0 210.0,93.2 210.0,86.8" fill="var(--fig-warn)"/><circle cx="34.0" cy="90.0" r="7.5" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="1.8"/><circle cx="130.0" cy="90.0" r="6.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.4"/><rect x="216.0" y="80.0" width="20" height="20" rx="2" fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="1.8"/><circle r="3.4" fill="var(--fig-warn)" stroke="var(--fig-node)" stroke-width="1" class="fig-packet" style="offset-path: path('M 34.0 90.0 L 130.0 90.0 L 226.0 90.0'); offset-rotate: 0deg;"/></svg><p class="step__text">Κάθε ζεύξη έχει το δικό της ETX (πόσες μεταδόσεις χρειάζονται κατά μέσο όρο) και το δικό της μήκος (πόσο κοστίζει η κάθε μετάδοση). Το συνολικό κόστος είναι το άθροισμα των δύο ζεύξεων.</p></div>
<div class="legend"><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><circle cx="9" cy="7" r="5.5" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="1.5"/></svg>κόμβος-πηγή</span><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><circle cx="9" cy="7" r="5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.2"/></svg>ενδιάμεσος κόμβος</span><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><rect x="3" y="1" width="12" height="12" rx="1.5" fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="1.5"/></svg>προορισμός</span><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-warn)" stroke-width="1.8"/></svg>ζεύξη της διαδρομής</span><span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" aria-hidden="true"><circle cx="9" cy="7" r="3.4" fill="var(--fig-warn)" stroke="var(--fig-node)" stroke-width="1"/></svg>πακέτο</span></div>
<figcaption>Σχήμα 4.2 · Η τοπολογία του Θέματος Δ.1 (2026): το πακέτο ταξιδεύει από το A στο C μέσω του B, σε δύο ζεύξεις.</figcaption>
</figure>
<!-- /etx_figures:hops -->

**Βήμα 1: Το κόστος μιας προσπάθειας σε ζεύξη 5 m.** Και οι δύο ζεύξεις έχουν το ίδιο μήκος (5 m), το ίδιο πακέτο (200 bits) και το ίδιο \(E_c\), οπότε το κόστος **μιας** προσπάθειας είναι το ίδιο και για τις δύο. Ας το υπολογίσουμε μία φορά:

<div class="trace-label">Κόστος μιας προσπάθειας σε ζεύξη 5 m</div>
<div class="trace" markdown="1">
$$
\begin{aligned}
E_{1} &= E_c \cdot b + E_{tx}(5) \cdot b + E_c \cdot b && \\[0.7em]
      &= 40 \cdot 200 + 1 \cdot 5^2 \cdot 200 + 40 \cdot 200 && (E_c=40,\ d=5,\ b=200) \\[0.7em]
      &= 40 \cdot 200 + 25 \cdot 200 + 40 \cdot 200 && (1 \cdot 5^2 = 25) \\[0.7em]
      &= 8000 + 5000 + 8000 && (\text{κάθε όρος} \times 200) \\[0.7em]
      &= 21000 \text{ nJ} && (8000 + 5000 + 8000)
\end{aligned}
$$
</div>

**Βήμα 2: Κάθε ζεύξη επί το δικό της ETX.** Η ζεύξη A → B χρειάζεται κατά μέσο όρο 4.3 προσπάθειες, η B → C μόνο 1.5:

<div class="trace" markdown="1">
$$
\begin{aligned}
E_{A \to B} &= \text{ETX}_{AB} \cdot E_1 = 4.3 \cdot 21000 = 90300 \text{ nJ} && \\[0.7em]
E_{B \to C} &= \text{ETX}_{BC} \cdot E_1 = 1.5 \cdot 21000 = 31500 \text{ nJ} &&
\end{aligned}
$$
</div>

**Βήμα 3: Άθροισμα των δύο ζεύξεων.** Η συνολική ενέργεια του δικτύου για να φτάσει το πακέτο από το A στο C:

<div class="trace" markdown="1">
$$
\begin{aligned}
E_{A \to C} &= E_{A \to B} + E_{B \to C} && \\[0.7em]
            &= 90300 + 31500 && \\[0.7em]
            &= 121800 \text{ nJ} = 121.8\ \mu\text{J} && (1000 \text{ nJ} = 1\ \mu\text{J})
\end{aligned}
$$
</div>

Η απάντηση είναι **121 800 nJ = 121.8 μJ**. Παρατηρήστε πού πάει η ενέργεια: η ζεύξη A → B κοστίζει σχεδόν τριπλάσια από τη B → C, όχι επειδή είναι πιο μακριά (ίδια απόσταση), αλλά επειδή είναι **χειρότερης ποιότητας**: το υψηλό της ETX σημαίνει ότι το πακέτο ξανα-μεταδίδεται πολλές φορές πριν περάσει.

!!! exam "Τι να περιμένετε στην εξέταση"

    <div class="exam-record"><a class="exam-chip is-hit" href="../../#exam-papers"><strong>6/2/2026</strong> Θέμα Δ.1, 2.5 μονάδες</a><a class="exam-chip" href="../../#exam-papers"><strong>15/2/2025</strong> όχι</a><a class="exam-chip" href="../../#exam-papers"><strong>2/2022</strong> όχι</a></div>

    Αυτή είναι η ίδια η άσκηση. Η δομή μιας πλήρους λύσης: (1) γράψτε τον τύπο, (2) υπολογίστε το κόστος μιας προσπάθειας σε ζεύξη 5 m (ίδιο και για τις δύο), (3) πολλαπλασιάστε το με το ETX της κάθε ζεύξης, (4) προσθέστε. Προσοχή στους **τρεις** ενεργειακούς όρους ανά προσπάθεια: το πιο συχνό λάθος είναι να ξεχαστεί το \(E_c\) της λήψης.

## 4.7 Οι Άλλες Μετρικές Δρομολόγησης {#other-metrics}

Το ETX είναι μία από πολλές μετρικές που εξετάζει η διάλεξη. Οι υπόλοιπες δεν εξετάζονται, αλλά αξίζει να ξέρετε ότι υπάρχουν, οργανωμένες σε τρεις οικογένειες (Διάλεξη 4, διαφάνεια 6):

- **Με βάση την ποιότητα ζεύξης.** Εκτός από το ETX, το Minimum Outage Route (MOR) για δυναμικά δίκτυα (ενότητα 4.4).
- **Με βάση την απόσταση.** Επιλέγουν κόμβους πιο κοντά στον προορισμό, όπως το Extremely Opportunistic Routing (ExOR), όπου δεν προαποφασίζεται ποιος θα προωθήσει, και το Local Target Protocol (LTP), ένας απλός άπληστος αλγόριθμος.
- **Πολλαπλών διαδρομών.** Χρησιμοποιούν πολλές διαδρομές για ανθεκτικότητα, όπως το Probabilistic Forwarding Protocol (PFR).

!!! extra "Εκτός ύλης"

    Η διάλεξη αναλύει τα Extremely Opportunistic Routing (ExOR), Local Target Protocol (LTP) και Probabilistic Forwarding Protocol (PFR) με αρκετή λεπτομέρεια (γεωμετρία, πιθανοτικά όρια, πειραματικές συγκρίσεις), αλλά τίποτα από αυτά δεν έχει εμφανιστεί στα θέματα εξετάσεων. Για την ύλη, το ETX και ο υπολογισμός ενέργειάς του είναι το ζητούμενο.
