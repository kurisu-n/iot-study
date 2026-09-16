<span class="chapter-num">Κεφάλαιο 1</span>

# Διάδοση Δεδομένων σε Ασύρματα Δίκτυα Αισθητήρων

*Καλύπτει: Flooding, Directed Diffusion, Omniscient Multicast, Flat vs Hierarchical Routing*

## 1.1 Το Θεμελιώδες Πρόβλημα

Φανταστείτε ένα πεδίο καλυμμένο με εκατοντάδες μικροσκοπικούς, αυτόνομους αισθητήρες που τροφοδοτούνται από μπαταρία. Ένας από αυτούς ανιχνεύει κάτι ενδιαφέρον — μια απότομη αύξηση θερμοκρασίας, μια χημική ανωμαλία, μια κίνηση. Η μέτρηση αυτή δεν έχει καμία αξία αν παραμείνει αποθηκευμένη στον κόμβο. Πρέπει να φτάσει σε ένα κέντρο ελέγχου — τον λεγόμενο <span class="key-term">sink</span> ή <span class="key-term">Base Station (BS)</span> — όπου μπορεί κάποιος να δράσει.

Το ερώτημα που κινεί ολόκληρη αυτή τη θεματική ενότητα, όπως διατυπώνεται στις διαφάνειες του μαθήματος, είναι:

> «How can sensor p, via cooperation with the rest of the sensors in the network, propagate information about event E to the control center(s)?»

Οι αισθητήρες δεν μπορούν να εκπέμψουν απευθείας στο BS — είναι συσκευές χαμηλής ισχύος με περιορισμένη εμβέλεια ραδιοεπικοινωνίας. Κάθε κόμβος επικοινωνεί μόνο με τους άμεσους γείτονές του. Τα δεδομένα πρέπει λοιπόν να μεταπηδήσουν (*hop*) από κόμβο σε κόμβο μέχρι να φτάσουν στον sink. Ο τρόπος οργάνωσης αυτών των «πηδημάτων» ονομάζεται <span class="key-term">πρωτόκολλο δρομολόγησης</span> (routing protocol), και η επιλογή πρωτοκόλλου καθορίζει πόσο θα επιβιώσει το δίκτυο, πόσο γρήγορα φτάνουν τα δεδομένα, και πόση ενέργεια σπαταλιέται στη διαδρομή.

<figure>
<svg viewBox="0 0 700 280" xmlns="http://www.w3.org/2000/svg">
  <!-- Sensor field cloud -->
  <ellipse cx="300" cy="150" rx="250" ry="120" fill="var(--fig-surface-accent)" stroke="var(--fig-accent)" stroke-width="2" stroke-dasharray="6 3"/>
  <text x="300" y="30" text-anchor="middle" font-size="13" fill="var(--fig-label)">Πεδίο Αισθητήρων (Sensor Field)</text>

  <!-- Random sensor nodes -->
  <circle cx="120" cy="130" r="6" fill="var(--fig-node)"/>
  <circle cx="170" cy="90" r="6" fill="var(--fig-node)"/>
  <circle cx="200" cy="170" r="6" fill="var(--fig-node)"/>
  <circle cx="250" cy="110" r="6" fill="var(--fig-node)"/>
  <circle cx="280" cy="200" r="6" fill="var(--fig-node)"/>
  <circle cx="310" cy="80" r="6" fill="var(--fig-node)"/>
  <circle cx="340" cy="160" r="6" fill="var(--fig-node)"/>
  <circle cx="380" cy="120" r="6" fill="var(--fig-node)"/>
  <circle cx="420" cy="180" r="6" fill="var(--fig-node)"/>
  <circle cx="450" cy="100" r="6" fill="var(--fig-node)"/>
  <circle cx="160" cy="200" r="6" fill="var(--fig-node)"/>
  <circle cx="390" cy="210" r="6" fill="var(--fig-node)"/>
  <circle cx="480" cy="150" r="6" fill="var(--fig-node)"/>

  <!-- Event node (pulsing) -->
  <circle cx="170" cy="170" r="6" fill="var(--fig-event)" class="anim-pulse"/>
  <text x="170" y="163" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--fig-event)">Event E</text>

  <!-- Path from event to sink -->
  <line x1="170" y1="170" x2="250" y2="110" stroke="var(--fig-event)" stroke-width="2.5" class="anim-flow-right" marker-end="url(#arrowRed)"/>
  <line x1="250" y1="110" x2="340" y2="160" stroke="var(--fig-event)" stroke-width="2.5" class="anim-flow-right" marker-end="url(#arrowRed)"/>
  <line x1="340" y1="160" x2="420" y2="180" stroke="var(--fig-event)" stroke-width="2.5" class="anim-flow-right" marker-end="url(#arrowRed)"/>
  <line x1="420" y1="180" x2="480" y2="150" stroke="var(--fig-event)" stroke-width="2.5" class="anim-flow-right" marker-end="url(#arrowRed)"/>

  <!-- Path nodes highlighted -->
  <circle cx="250" cy="110" r="7" fill="var(--fig-event-soft)" stroke="var(--fig-event)" stroke-width="2"/>
  <circle cx="340" cy="160" r="7" fill="var(--fig-event-soft)" stroke="var(--fig-event)" stroke-width="2"/>
  <circle cx="420" cy="180" r="7" fill="var(--fig-event-soft)" stroke="var(--fig-event)" stroke-width="2"/>

  <!-- Sink / BS -->
  <rect x="610" y="100" width="70" height="90" rx="6" fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="2"/>
  <text x="645" y="135" text-anchor="middle" font-size="11" fill="var(--fig-on-accent)" font-weight="bold">Sink</text>
  <text x="645" y="150" text-anchor="middle" font-size="10" fill="var(--fig-on-accent-soft)">(BS)</text>
  <!-- Antenna -->
  <line x1="645" y1="100" x2="645" y2="70" stroke="var(--fig-accent-deep)" stroke-width="2"/>
  <circle cx="645" cy="67" r="4" fill="var(--fig-accent-deep)"/>
  <path d="M632 76 Q645 60 658 76" stroke="var(--fig-accent-deep)" stroke-width="1.5" fill="none"/>
  <path d="M625 82 Q645 62 665 82" stroke="var(--fig-accent-deep)" stroke-width="1.5" fill="none"/>

  <!-- Link from field to sink -->
  <line x1="480" y1="150" x2="610" y2="145" stroke="var(--fig-event)" stroke-width="2.5" class="anim-flow-right" marker-end="url(#arrowRed)"/>

  <!-- Node label -->
  <text x="172" y="195" text-anchor="middle" font-size="10" fill="var(--fig-event)">κόμβος p</text>

  <!-- Arrow markers -->
  <defs>
    <marker id="arrowRed" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="var(--fig-event)"/>
    </marker>
    <marker id="arrowBlue" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="var(--fig-accent)"/>
    </marker>
    <marker id="arrowGreen" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="var(--fig-ok)"/>
    </marker>
    <marker id="arrowOrange" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="var(--fig-warn)"/>
    </marker>
  </defs>
</svg>
<figcaption>Σχήμα 1.1 — Το θεμελιώδες πρόβλημα: ο κόμβος p ανιχνεύει ένα γεγονός E και πρέπει, σε συνεργασία με τους υπόλοιπους κόμβους, να μεταφέρει την πληροφορία στο κέντρο ελέγχου (Sink/BS).</figcaption>
</figure>

Υπάρχουν δύο θεμελιωδώς διαφορετικές φιλοσοφίες αντιμετώπισης αυτού του προβλήματος:

- **Επίπεδη δρομολόγηση (flat routing):** κάθε κόμβος-αισθητήρας είναι ισότιμος — κανείς δεν αναλαμβάνει ειδικό ρόλο. Τα δεδομένα ρέουν στο δίκτυο με βάση το *περιεχόμενο* της πληροφορίας. Χαρακτηριστικό παράδειγμα: **Directed Diffusion (DD)**.
- **Ιεραρχική δρομολόγηση (hierarchical routing):** ορισμένοι κόμβοι αναλαμβάνουν ρόλους αρχηγών, οργανώνοντας τους γείτονές τους σε ομάδες (clusters). Χαρακτηριστικό παράδειγμα: **LEACH**.

Πριν εμβαθύνουμε στο Directed Diffusion, αξίζει να κατανοήσουμε την πιο απλή δυνατή προσέγγιση — και γιατί αποτυγχάνει.

## 1.2 Flooding: Η Ωμή Βία ως Σημείο Αναφοράς

Το Flooding είναι ακριβώς αυτό που υποδηλώνει το όνομά του — πλημμύρα. Όταν ένας αισθητήρας ανιχνεύει ένα γεγονός, εκπέμπει (broadcast) τα δεδομένα σε κάθε γείτονά του. Κάθε γείτονας τα αναμεταδίδει σε κάθε *δικό του* γείτονα. Η διαδικασία συνεχίζεται μέχρι κάθε κόμβος του δικτύου να έχει λάβει το μήνυμα — συμπεριλαμβανομένου του sink.

Ο μηχανισμός λειτουργεί ως εξής:

1. Ο κόμβος-πηγή ανιχνεύει ένα γεγονός και το εκπέμπει.
2. Κάθε κόμβος που λαμβάνει το μήνυμα το αναμεταδίδει **ακριβώς μία φορά**, ώστε να αποφευχθούν άπειροι βρόχοι.
3. Τελικά, το μήνυμα κατακλύζει ολόκληρο το δίκτυο.

Αν υπάρχουν $n$ πηγές και $N$ συνολικοί κόμβοι, έχουμε $nN$ μεταδόσεις. Σε ένα τετραγωνικό πλέγμα (square grid) μεγέθους $\sqrt{N} \times \sqrt{N}$, κάθε μήνυμα στέλνεται δύο φορές σε κάθε κανάλι, οπότε οι συνολικές λήψεις είναι $2n(2\sqrt{N}(\sqrt{N}-1) + 2(\sqrt{N}-1)^2)$. Το συνολικό κόστος μετάδοσης και λήψης υπολογίζεται ως:

<div class="formula" markdown="1">
$$C_f = nN + 4n(\sqrt{N} - 1)(2\sqrt{N} - 1)$$

<span class="label">Κόστος Flooding — τάξη μεγέθους: $\mathcal{O}(nN)$</span>
</div>

Αυτό το κόστος αυξάνεται **γραμμικά** με το $N$ — αν διπλασιάσουμε το μέγεθος του δικτύου, διπλασιάζουμε περίπου και τον ενεργειακό λογαριασμό. Στην πράξη, αυτό σημαίνει ότι το flooding εξαντλεί τις μπαταρίες με ανησυχητικό ρυθμό, επειδή κάθε γεγονός σπρώχνεται σε κάθε γωνιά του δικτύου ανεξάρτητα από το αν κάποιος εκεί ενδιαφέρεται.

<figure>
<svg viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg">
  <!-- Grid of nodes -->
  <g id="flood-nodes">
    <!-- Row 1 -->
    <circle cx="80"  cy="60"  r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="160" cy="60"  r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="240" cy="60"  r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="320" cy="60"  r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="400" cy="60"  r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <!-- Row 2 -->
    <circle cx="80"  cy="140" r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="160" cy="140" r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="240" cy="140" r="8" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="2"/> <!-- SOURCE -->
    <circle cx="320" cy="140" r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="400" cy="140" r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <!-- Row 3 -->
    <circle cx="80"  cy="220" r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="160" cy="220" r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="240" cy="220" r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="320" cy="220" r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="400" cy="220" r="8" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
  </g>

  <!-- Animated flood waves expanding from source (240,140) -->
  <circle cx="240" cy="140" r="0" fill="none" stroke="var(--fig-event)" stroke-width="2" opacity="0">
    <animate attributeName="r" from="0" to="140" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" from="0.7" to="0" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="240" cy="140" r="0" fill="none" stroke="var(--fig-event)" stroke-width="2" opacity="0">
    <animate attributeName="r" from="0" to="140" dur="3s" begin="1s" repeatCount="indefinite"/>
    <animate attributeName="opacity" from="0.7" to="0" dur="3s" begin="1s" repeatCount="indefinite"/>
  </circle>
  <circle cx="240" cy="140" r="0" fill="none" stroke="var(--fig-event)" stroke-width="2" opacity="0">
    <animate attributeName="r" from="0" to="140" dur="3s" begin="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" from="0.7" to="0" dur="3s" begin="2s" repeatCount="indefinite"/>
  </circle>

  <text x="240" y="135" text-anchor="middle" font-size="10" fill="var(--fig-on-accent)" font-weight="bold">SRC</text>
  <text x="240" y="270" text-anchor="middle" font-size="12" fill="var(--fig-event)" font-style="italic">Κάθε γεγονός πλημμυρίζει ολόκληρο το δίκτυο</text>
</svg>
<figcaption>Σχήμα 1.2 — Flooding: ο κόμβος-πηγή εκπέμπει ένα γεγονός και τα κύματα μεταδόσεων εξαπλώνονται σε όλους τους κόμβους, ανεξαρτήτως αν ενδιαφέρονται για τα δεδομένα. Κόστος: <span class="arithmatex">\(\mathcal{O}(nN)\)</span>.</figcaption>
</figure>

Πέρα από τη σπατάλη ενέργειας, υπάρχουν και πρακτικά προβλήματα. Όταν εκατοντάδες κόμβοι προσπαθούν να αναμεταδώσουν ταυτόχρονα, τα ραδιοσήματά τους **συγκρούονται** στο επίπεδο MAC (Media Access Control), προκαλώντας καθυστερήσεις (delays) και αναγκαστικές επαναμεταδόσεις. Επιπλέον, ακόμα και οι κόμβοι που δεν εκπέμπουν καταναλώνουν ενέργεια κρατώντας τους πομποδέκτες τους ενεργοποιημένους — φαινόμενο γνωστό ως <span class="key-term">idle listening</span>, που αποδεικνύεται εκπληκτικά δαπανηρό.

Το flooding χρησιμεύει ως **αναλυτικό σημείο αναφοράς** (baseline): αν ένα νέο πρωτόκολλο δεν μπορεί να νικήσει το flooding, κάτι έχει πάει πολύ στραβά. Κανείς όμως δεν θα το ανέπτυσσε σε πραγματικό δίκτυο αισθητήρων.

## 1.3 Directed Diffusion: Data-Centric, Demand-Driven

Το Directed Diffusion (DD), που παρουσιάστηκε από τους Intanagonwiwat, Govindan και Estrin στο 6ο Διεθνές Συνέδριο Mobile Computing and Networking (2000), ακολουθεί την αντίθετη λογική από το flooding. Αντί να σπρώχνει δεδομένα παντού ελπίζοντας ότι κάποιος τα θέλει, το DD επιτρέπει στον sink να **τραβήξει** (pull) μόνο τα δεδομένα που πραγματικά χρειάζεται.

Είναι ένα <span class="key-term">data-centric</span> πρωτόκολλο — ενδιαφέρεται για το *τι* λένε τα δεδομένα, όχι *ποιος* τα παρήγαγε. Είναι επίσης <span class="key-term">application-aware</span> (αναγνωρίζει το είδος των δεδομένων) και <span class="key-term">energy-efficient</span> (σχεδιασμένο για ενεργειακή αποδοτικότητα).

Σύμφωνα με τις διαφάνειες, τα βασικά στοιχεία (elements) του DD είναι τέσσερα: **Interest messages**, **Data messages**, **Gradients**, και **Reinforcements of gradients**. Αυτά αντιστοιχούν στις τέσσερις φάσεις λειτουργίας που επαναλαμβάνονται κυκλικά.

### Φάση 1 — Διάδοση Ενδιαφέροντος (Interest Propagation)

Ο sink κατασκευάζει ένα μήνυμα που περιγράφει το είδος δεδομένων που θέλει, εκφρασμένο ως ζεύγη ιδιότητας-τιμής (attribute-value pairs). Αυτό το μήνυμα ονομάζεται <span class="key-term">interest</span>. Ένα παράδειγμα από τις διαφάνειες:

```text
type     = wheeled vehicle       // ανίχνευση τοποθεσίας οχήματος
interval = 100 ms                // αποστολή γεγονότων κάθε 100ms
duration = 10 seconds            // για τα επόμενα 10 δευτερόλεπτα
rect     = [-100, 100, 200, 400] // από κόμβους εντός ορθογωνίου
```

Ο sink πλημμυρίζει (flood) το interest στο δίκτυο. Ναι, αυτό χρησιμοποιεί flooding — αλλά πρόκειται για **εφάπαξ κόστος εγκατάστασης**, όχι κόστος ανά γεγονός. Σημαντικό: το interest **δεν περιέχει πληροφορία για τον sink** — ο sink μαθαίνεται μόνο μέσω των gradients.

Κάθε κόμβος διατηρεί ένα <span class="key-term">interest cache</span>. Όταν ένα interest φτάσει, αποθηκεύεται τοπικά. Αν ήδη υπάρχει ίδιο interest στο cache, δημιουργείται μόνο ένα νέο gradient. Τα interests σβήνονται μόνο όταν εκπνεύσουν όλα τα σχετιζόμενα gradients.

### Φάση 2 — Δημιουργία Κλίσεων (Gradient Setup)

Καθώς το interest κυματίζει προς τα έξω από τον sink, κάθε κόμβος που το λαμβάνει δημιουργεί ένα <span class="key-term">gradient</span> — ένα βέλος που δείχνει πίσω προς τον γείτονα που του παρέδωσε το interest. Κάθε gradient αποθηκεύει δύο πληροφορίες: **data rate** (ρυθμός δεδομένων) και **duration** (διάρκεια).

Σκεφτείτε τα gradients σαν βέλη ζωγραφισμένα στο πάτωμα ενός κτιρίου, που δείχνουν όλα προς την έξοδο. Δεν μεταφέρουν δεδομένα — σημαδεύουν την κατεύθυνση που πρέπει να ακολουθήσουν τα δεδομένα όταν εμφανιστούν. Μπορούν να υπάρχουν **πολλαπλά gradients** σε κάθε κόμβο (ένα για κάθε γείτονα που προώθησε το interest), δημιουργώντας εφεδρικά μονοπάτια.

<figure>
<svg viewBox="0 0 700 500" xmlns="http://www.w3.org/2000/svg">
  <!-- PHASE 1: Interest Propagation -->
  <g class="anim-fadein-1">
    <rect x="10" y="10" width="330" height="220" rx="10" fill="var(--fig-surface-accent)" stroke="var(--fig-accent)" stroke-width="1.5"/>
    <text x="175" y="35" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--fig-accent-deep)">Φάση 1: Interest Propagation</text>

    <!-- Sink -->
    <rect x="250" y="100" width="60" height="35" rx="5" fill="var(--fig-accent)"/>
    <text x="280" y="122" text-anchor="middle" font-size="10" fill="var(--fig-on-accent)" font-weight="bold">Sink</text>

    <!-- Nodes -->
    <circle cx="60"  cy="120" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="120" cy="80"  r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="120" cy="160" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="180" cy="120" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="180" cy="180" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>

    <!-- Interest arrows (sink → outward) dashed blue -->
    <line x1="250" y1="117" x2="187" y2="120" stroke="var(--fig-accent)" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
    <line x1="180" y1="113" x2="127" y2="83"  stroke="var(--fig-accent)" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
    <line x1="180" y1="127" x2="127" y2="157" stroke="var(--fig-accent)" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
    <line x1="120" y1="87"  x2="67"  y2="115" stroke="var(--fig-accent)" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
    <line x1="120" y1="153" x2="67"  y2="125" stroke="var(--fig-accent)" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
    <line x1="180" y1="127" x2="180" y2="173" stroke="var(--fig-accent)" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>

    <text x="175" y="210" text-anchor="middle" font-size="10" fill="var(--fig-accent)">Ο Sink πλημμυρίζει interests στο δίκτυο</text>
  </g>

  <!-- PHASE 2: Gradient Setup -->
  <g class="anim-fadein-2">
    <rect x="360" y="10" width="330" height="220" rx="10" fill="var(--fig-surface-ok)" stroke="var(--fig-ok)" stroke-width="1.5"/>
    <text x="525" y="35" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--fig-ok-deep)">Φάση 2: Gradient Setup</text>

    <!-- Sink -->
    <rect x="600" y="100" width="60" height="35" rx="5" fill="var(--fig-accent)"/>
    <text x="630" y="122" text-anchor="middle" font-size="10" fill="var(--fig-on-accent)" font-weight="bold">Sink</text>

    <!-- Nodes -->
    <circle cx="410" cy="120" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="470" cy="80"  r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="470" cy="160" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="530" cy="120" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="530" cy="180" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>

    <!-- Gradient arrows (nodes → sink direction) solid green -->
    <line x1="417" y1="118" x2="463" y2="83"  stroke="var(--fig-ok)" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <line x1="417" y1="122" x2="463" y2="157" stroke="var(--fig-ok)" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <line x1="477" y1="80"  x2="523" y2="115" stroke="var(--fig-ok)" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <line x1="477" y1="157" x2="523" y2="123" stroke="var(--fig-ok)" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <line x1="537" y1="118" x2="597" y2="115" stroke="var(--fig-ok)" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <line x1="533" y1="173" x2="533" y2="127" stroke="var(--fig-ok)" stroke-width="2" marker-end="url(#arrowGreen)"/>

    <text x="525" y="210" text-anchor="middle" font-size="10" fill="var(--fig-ok)">Τα gradients δείχνουν «πίσω» προς τον Sink</text>
  </g>

  <!-- PHASE 3: Data Propagation -->
  <g class="anim-fadein-3">
    <rect x="10" y="250" width="330" height="230" rx="10" fill="var(--fig-surface-warn)" stroke="var(--fig-warn)" stroke-width="1.5"/>
    <text x="175" y="275" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--fig-warn-deep)">Φάση 3: Data Propagation</text>

    <!-- Source -->
    <circle cx="50" cy="370" r="9" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="2"/>
    <text x="50" y="395" text-anchor="middle" font-size="9" fill="var(--fig-event)" font-weight="bold">Source</text>

    <!-- Sink -->
    <rect x="270" y="340" width="50" height="30" rx="5" fill="var(--fig-accent)"/>
    <text x="295" y="360" text-anchor="middle" font-size="9" fill="var(--fig-on-accent)" font-weight="bold">Sink</text>

    <!-- Intermediate nodes -->
    <circle cx="120" cy="340" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="120" cy="400" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="190" cy="370" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="190" cy="310" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>

    <!-- Exploratory data flows (multiple paths, orange dashed) -->
    <line x1="57" y1="367" x2="113" y2="343" stroke="var(--fig-warn)" stroke-width="2" stroke-dasharray="4 3" class="anim-flow-right" marker-end="url(#arrowOrange)"/>
    <line x1="57" y1="373" x2="113" y2="397" stroke="var(--fig-warn)" stroke-width="2" stroke-dasharray="4 3" class="anim-flow-right" marker-end="url(#arrowOrange)"/>
    <line x1="127" y1="338" x2="183" y2="315" stroke="var(--fig-warn)" stroke-width="2" stroke-dasharray="4 3" class="anim-flow-right" marker-end="url(#arrowOrange)"/>
    <line x1="127" y1="342" x2="183" y2="367" stroke="var(--fig-warn)" stroke-width="2" stroke-dasharray="4 3" class="anim-flow-right" marker-end="url(#arrowOrange)"/>
    <line x1="127" y1="398" x2="183" y2="373" stroke="var(--fig-warn)" stroke-width="2" stroke-dasharray="4 3" class="anim-flow-right" marker-end="url(#arrowOrange)"/>
    <line x1="197" y1="367" x2="268" y2="355" stroke="var(--fig-warn)" stroke-width="2" stroke-dasharray="4 3" class="anim-flow-right" marker-end="url(#arrowOrange)"/>
    <line x1="195" y1="313" x2="268" y2="348" stroke="var(--fig-warn)" stroke-width="2" stroke-dasharray="4 3" class="anim-flow-right" marker-end="url(#arrowOrange)"/>

    <text x="175" y="445" text-anchor="middle" font-size="10" fill="var(--fig-warn)">Διερευνητικά δεδομένα σε χαμηλό ρυθμό</text>
    <text x="175" y="460" text-anchor="middle" font-size="10" fill="var(--fig-warn)">μέσω πολλαπλών μονοπατιών</text>
  </g>

  <!-- PHASE 4: Reinforcement -->
  <g class="anim-fadein-4">
    <rect x="360" y="250" width="330" height="230" rx="10" fill="var(--fig-surface-event)" stroke="var(--fig-event)" stroke-width="1.5"/>
    <text x="525" y="275" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--fig-event-deep)">Φάση 4: Reinforcement</text>

    <!-- Source -->
    <circle cx="400" cy="380" r="9" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="2"/>
    <text x="400" y="405" text-anchor="middle" font-size="9" fill="var(--fig-event)" font-weight="bold">Source</text>

    <!-- Sink -->
    <rect x="620" y="350" width="50" height="30" rx="5" fill="var(--fig-accent)"/>
    <text x="645" y="370" text-anchor="middle" font-size="9" fill="var(--fig-on-accent)" font-weight="bold">Sink</text>

    <!-- Intermediate nodes -->
    <circle cx="470" cy="350" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="470" cy="410" r="7" fill="var(--fig-surface-soft)" stroke="var(--fig-node-soft)" stroke-width="1.5"/>
    <circle cx="540" cy="370" r="7" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.5"/>
    <circle cx="540" cy="320" r="7" fill="var(--fig-surface-soft)" stroke="var(--fig-node-soft)" stroke-width="1.5"/>

    <!-- Faded non-reinforced paths -->
    <line x1="407" y1="383" x2="463" y2="407" stroke="var(--fig-node-soft)" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="477" y1="348" x2="533" y2="323" stroke="var(--fig-node-soft)" stroke-width="1.5" stroke-dasharray="3 3"/>

    <!-- REINFORCED PATH (thick, solid red) -->
    <line x1="407" y1="377" x2="463" y2="353" stroke="var(--fig-event)" stroke-width="4" marker-end="url(#arrowRed)">
      <animate attributeName="stroke-width" values="2;4;2" dur="2s" repeatCount="indefinite"/>
    </line>
    <line x1="477" y1="352" x2="533" y2="368" stroke="var(--fig-event)" stroke-width="4" marker-end="url(#arrowRed)">
      <animate attributeName="stroke-width" values="2;4;2" dur="2s" repeatCount="indefinite"/>
    </line>
    <line x1="547" y1="370" x2="618" y2="365" stroke="var(--fig-event)" stroke-width="4" marker-end="url(#arrowRed)">
      <animate attributeName="stroke-width" values="2;4;2" dur="2s" repeatCount="indefinite"/>
    </line>

    <text x="525" y="445" text-anchor="middle" font-size="10" fill="var(--fig-event-deep)">Ο Sink ενισχύει το ταχύτερο μονοπάτι</text>
    <text x="525" y="460" text-anchor="middle" font-size="10" fill="var(--fig-event-deep)">— τα υπόλοιπα σβήνουν σταδιακά</text>
  </g>
</svg>
<figcaption>Σχήμα 1.3 — Οι τέσσερις φάσεις του Directed Diffusion: (1) ο Sink πλημμυρίζει interests, (2) οι κόμβοι δημιουργούν gradients προς τον Sink, (3) διερευνητικά δεδομένα ρέουν σε χαμηλό ρυθμό μέσω πολλαπλών μονοπατιών, (4) ο Sink ενισχύει (reinforce) το ταχύτερο μονοπάτι.</figcaption>
</figure>

### Φάση 3 — Διάδοση Δεδομένων (Data Propagation)

Όταν ένας κόμβος-αισθητήρας ανιχνεύσει ένα γεγονός που ταιριάζει με κάποιο αποθηκευμένο interest, αρχίζει να αισθητηριάζει (sensing). Υπολογίζει τον υψηλότερο ρυθμό αποστολής (data rate) μεταξύ των gradients του και δημιουργεί δείγματα γεγονότων (event samples) σε αυτόν τον ρυθμό.

Ένα data message, σύμφωνα με τις διαφάνειες, μοιάζει κάπως έτσι:

```text
type       = wheeled vehicle     // τύπος γεγονότος
instance   = truck               // στιγμιότυπο
location   = [125, 220]          // τοποθεσία κόμβου
intensity  = 0.6                 // πλάτος σήματος
confidence = 0.85                // βαθμός εμπιστοσύνης
timestamp  = 01:20:40            // τοπικός χρόνος
```

Τα data messages αποστέλλονται ως **unicast** στους γείτονες προς τους οποίους δείχνουν τα gradients. Κάθε κόμβος διατηρεί ένα <span class="key-term">data cache</span>: αν λάβει μήνυμα χωρίς αντίστοιχο interest στο cache ή αν τα δεδομένα ήδη υπάρχουν, το μήνυμα απορρίπτεται. Αλλιώς, αποθηκεύεται και προωθείται.

### Φάση 4 — Ενίσχυση (Reinforcement)

Αρχικά, ο sink εκπέμπει interests χαμηλού ρυθμού — τα αντίστοιχα gradients ονομάζονται <span class="key-term">exploratory gradients</span>. Μόλις ο sink αρχίσει να λαμβάνει διερευνητικά δεδομένα, **ενισχύει** (reinforce) τον γείτονα που του τα παρέδωσε πρώτος, στέλνοντας ξανά το ίδιο interest αλλά με μικρότερο interval (δηλαδή υψηλότερο ρυθμό).

Η επιλογή γείτονα προς ενίσχυση βασίζεται σε **τοπικά κριτήρια** — για παράδειγμα, ενισχύεται ο γείτονας που ανέφερε πρώτος ένα νέο γεγονός. Τα αντίστοιχα gradients ονομάζονται <span class="key-term">data gradients</span> (υψηλού ρυθμού). Τα exploratory gradients στα μη-ενισχυμένα μονοπάτια σταδιακά εκπνέουν (timeout) εκτός αν ανανεωθούν.

Αυτό το σχήμα είναι **αντιδραστικό** (reactive): όποτε ένα μονοπάτι παραδίδει γεγονός ταχύτερα από τα υπόλοιπα, ενισχύεται αυτόματα. Υποστηρίζει επίσης πολλαπλούς sinks και πολλαπλές πηγές ταυτόχρονα.

### Τοπική Επισκευή και Αρνητική Ενίσχυση

Τα μονοπάτια μπορούν να υποβαθμιστούν με τον χρόνο — κόμβοι εξαντλούν τη μπαταρία τους ή αυξάνονται οι παρεμβολές. Ένας ενδιάμεσος κόμβος μπορεί να **ανιχνεύσει** αυτή την υποβάθμιση (π.χ. παρατηρώντας μειωμένο ρυθμό γεγονότων) και να εφαρμόσει <span class="key-term">τοπική επισκευή (local repair)</span> ενισχύοντας έναν εναλλακτικό γείτονα.

Η <span class="key-term">αρνητική ενίσχυση (negative reinforcement)</span> λειτουργεί στην αντίθετη κατεύθυνση: ένα interest αποστέλλεται ξανά αλλά με *χαμηλό* ρυθμό (exploratory), σηματοδοτώντας ότι αυτό το μονοπάτι δεν χρειάζεται πλέον υψηλό ρυθμό. Αν όλα τα εξερχόμενα gradients ενός κόμβου γίνουν exploratory, ο κόμβος εφαρμόζει αρνητική ενίσχυση στους γείτονές του.

### In-Network Aggregation

Η μεγάλη κομψότητα του DD βρίσκεται στη δυνατότητα <span class="key-term">in-network aggregation</span>: καθώς τα δεδομένα ρέουν κατά μήκος των gradients, οι ενδιάμεσοι κόμβοι μπορούν να συνδυάσουν μετρήσεις από πολλαπλές πηγές. Αν δύο αισθητήρες αναφέρουν πανομοιότυπα δεδομένα, ένας ενδιάμεσος κόμβος μπορεί να **καταστείλει το διπλότυπο** (duplicate suppression) και να προωθήσει μόνο ένα αντίγραφο. Η προσομοίωση δείχνει ότι χωρίς aggregation, το DD καταναλώνει **3× έως 5× περισσότερη ενέργεια**.

!!! exam "Σημείωση Εξεταστικής"

    Στο Θέμα Α.1 της εξεταστικής 2026, ζητήθηκε συνοπτική περιγραφή της λειτουργίας του DD. Τα κλειδιά: data-centric, τέσσερις φάσεις (interests → gradients → data → reinforcement), in-network aggregation, local repair.

## 1.4 Omniscient Multicast: Το Θεωρητικό Ανώτατο Όριο

Για να αξιολογηθεί σωστά το DD, η αναλυτική σύγκριση (από τις διαφάνειες 23–27) χρησιμοποιεί ένα ιδεατό πρωτόκολλο: <span class="key-term">Omniscient Multicast</span>. Δεν πρόκειται για πραγματικό πρωτόκολλο — υποθέτει ότι κάθε πηγή γνωρίζει το **shortest-path multicast tree** προς κάθε sink, και τα δεδομένα ταξιδεύουν χωρίς συγκρούσεις.

Έστω $T_i$ το δέντρο multicast με ρίζα την πηγή $i$, και $C(T_i)$ το κόστος παράδοσης δεδομένων γι' αυτό το δέντρο. Αποδεικνύεται ότι:

<div class="formula" markdown="1">
$$C(T_i) = \mathcal{O}(\sqrt{N}) \quad \text{για } m \ll \sqrt{N}$$

$$C_o = \mathcal{O}(n\sqrt{N})$$

<span class="label">Κόστος Omniscient Multicast</span>
</div>

Αξιοσημείωτο: το DD, αν και πλήρως κατανεμημένο (κανένας κόμβος δεν γνωρίζει την καθολική τοπολογία), πετυχαίνει κόστος ίδιας τάξης μεγέθους — $C_d = \mathcal{O}(n\sqrt{N})$. Μάλιστα, χάρη στο in-network aggregation, η προσομοίωση σε ns-2 δείχνει ότι **$C_d < C_o$** σε πραγματικές συνθήκες.

## 1.5 Αναλυτική Σύγκριση

Η σύγκριση βασίζεται σε τετραγωνικό πλέγμα $\sqrt{N} \times \sqrt{N}$ με $n$ πηγές και $m$ sinks. Τα αποτελέσματα προσομοίωσης (ns-2) μετρούν τρεις μετρικές: μέση ενέργεια, μέση καθυστέρηση, και delivery ratio.

| Μετρική | Flooding | Omniscient Multicast | Directed Diffusion |
|:---|:---|:---|:---|
| **Πολυπλοκότητα κόστους** | $\mathcal{O}(nN)$ | $\mathcal{O}(n\sqrt{N})$ | $\mathcal{O}(n\sqrt{N})$ |
| **Μηχανισμός** | Broadcast σε όλους | Shortest-path multicast tree | Interests, gradients, reinforcement |
| **Ενεργειακή απόδοση** | Πολύ χαμηλή | Υψηλή | **Υψηλότερη** (aggregation) |
| **Μέση καθυστέρηση** | Πολύ υψηλή (collisions) | Χαμηλή | Χαμηλή (συγκρίσιμη) |
| **Ανοχή σε σφάλματα** | Εγγενώς ανθεκτικό | Ευάλωτο (ένα δέντρο) | Ανθεκτικό (local repair) |
| **Aggregation** | Καμία | Καμία | Ναι (duplicate suppression) |

## 1.6 Πλεονεκτήματα και Περιορισμοί του DD

### Πλεονεκτήματα

- **Ενεργειακή αποδοτικότητα:** Κόστος $\mathcal{O}(n\sqrt{N})$ — τάξεις μεγέθους κάτω από flooding.
- **Ανοχή σε σφάλματα:** Η μέση ενέργεια δεν αυξάνεται σημαντικά ακόμα και με αστοχίες κόμβων. Η καθυστέρηση αυξάνεται το πολύ 20% (σύμφωνα με προσομοίωση, διαφ. 34).
- **In-network aggregation:** Μειώνει 3×–5× την ενέργεια σε σχέση με DD χωρίς aggregation.
- **Αρνητική ενίσχυση:** Χωρίς αυτή, η ενέργεια διπλασιάζεται (διαφ. 37).

### Περιορισμοί

- **Idle listening:** Αν οι πομποδέκτες καταναλώνουν σημαντική ενέργεια σε κατάσταση αναμονής, η απόδοση του DD μειώνεται δραματικά. Η ενέργεια αδράνειας κυριαρχεί σε όλα τα πρωτόκολλα (διαφ. 38).
- **MAC layer dependency:** Ο σχεδιασμός του MAC επηρεάζει σημαντικά την τελική απόδοση.

## 1.7 Επίπεδη vs Ιεραρχική Δρομολόγηση

Το DD αποτελεί παράδειγμα **επίπεδης δρομολόγησης** (flat routing) στα καλύτερά της: κανείς κόμβος δεν χρειάζεται ειδικό ρόλο, δεν απαιτείται σχηματισμός συστάδων, και το δίκτυο αυτο-οργανώνεται γύρω από τη ζήτηση δεδομένων.

Η flat δρομολόγηση έχει όμως μια **δομική αδυναμία** σε πυκνά δίκτυα με υψηλή κυκλοφορία: όλα τα gradients συγκλίνουν προς τον sink, οπότε οι κόμβοι στη γειτονιά του προωθούν την κυκλοφορία *όλων* και εξαντλούνται πρώτοι. Αυτό δημιουργεί <span class="key-term">ενεργειακές τρύπες (energy holes)</span>.

| Χαρακτηριστικό | Flat Routing (DD) | Hierarchical (LEACH) |
|:---|:---|:---|
| **Ρόλοι κόμβων** | Ισότιμοι | Cluster Heads vs Members |
| **Πολυπλοκότητα** | Σχετικά απλή | Πιο περίπλοκη (CH election, TDMA) |
| **Κόστος οργάνωσης** | Χαμηλό | Υψηλότερο (set-up phase) |
| **Επεξεργασία δεδομένων** | Aggregation στους ενδιάμεσους κόμβους | Compression από τις κεφαλές συστάδων |
| **Ενεργειακές τρύπες** | Πιθανές (κοντά στο sink) | Μετριάζονται (rotation) |

Αυτό ακριβώς είναι το πρόβλημα που σχεδιάστηκαν να λύσουν τα ιεραρχικά πρωτόκολλα — κάτι που θα εξετάσουμε στο **Κεφάλαιο 2: LEACH**.

!!! exam "Σημείωση Εξεταστικής"

    Στο Θέμα Α.2 της εξεταστικής 2026, ζητήθηκε συγκριτική αξιολόγηση DD vs EBP ως προς την κατανάλωση ενέργειας σε κάθε κόμβο και συνολικά. Το DD είναι energy-efficient αλλά δεν εγγυάται ομοιόμορφη κατανομή ενέργειας (energy balance) — αυτό ακριβώς προσφέρει το EBP.

---

*Πηγές: Lecture 2 (DD & LEACH), Lecture 3 (EBP), χειρόγραφες σημειώσεις σελ. 1–6, Θέματα 2026.*
