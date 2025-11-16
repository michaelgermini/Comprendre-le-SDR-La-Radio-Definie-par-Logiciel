# Chapitre 2 : Fondamentaux des ondes radio

## 2.1 Les bases de l'électromagnétisme

### Les ondes électromagnétiques

Les ondes radio sont une forme d'énergie qui se propage dans l'espace sous forme d'ondes électromagnétiques. Ces ondes sont caractérisées par leur fréquence et leur longueur d'onde.

#### Propriétés fondamentales

- **Dualité onde-particule** : Les ondes électromagnétiques présentent à la fois des propriétés ondulatoires et particulaires (photons)
- **Vitesse de propagation** : c = 299 792 458 m/s dans le vide
- **Relation fréquence-longueur d'onde** : λ = c / f

### Le spectre électromagnétique

Le spectre électromagnétique s'étend des ondes radio aux rayons gamma :

| Gamme | Fréquence | Longueur d'onde | Usage |
|-------|-----------|-----------------|-------|
| Ondes radio | < 3 GHz | > 10 cm | Communications |
| Micro-ondes | 3 GHz - 300 GHz | 10 cm - 1 mm | Radar, satellites |
| Infra-rouge | 300 GHz - 400 THz | 1 mm - 750 nm | Télécommandes, chaleur |
| Lumière visible | 400 - 800 THz | 750 - 400 nm | Vision |
| Ultra-violet | 800 THz - 30 PHz | 400 - 10 nm | Stérilisation |
| Rayons X | 30 PHz - 30 EHz | 10 nm - 10 pm | Imagerie médicale |
| Rayons gamma | > 30 EHz | < 10 pm | Médecine, astrophysique |

## 2.2 Spectre radio : bandes, fréquences, allocations

### Les bandes de fréquence radio

L'Union Internationale des Télécommunications (UIT) définit plusieurs bandes de fréquences :

#### Bandes VLF (Very Low Frequency) - 3 kHz à 30 kHz
- Longueur d'onde : 100 km à 10 km
- Applications : Communication sous-marine, navigation

#### Bandes LF (Low Frequency) - 30 kHz à 300 kHz
- Longueur d'onde : 10 km à 1 km
- Applications : Radionavigation, radio maritime

#### Bandes MF (Medium Frequency) - 300 kHz à 3 MHz
- Longueur d'onde : 1 km à 100 m
- Applications : Radio AM, maritime

#### Bandes HF (High Frequency) - 3 MHz à 30 MHz
- Longueur d'onde : 100 m à 10 m
- Applications : Radio mondiale, aviation

#### Bandes VHF (Very High Frequency) - 30 MHz à 300 MHz
- Longueur d'onde : 10 m à 1 m
- Applications : FM, TV, aviation

#### Bandes UHF (Ultra High Frequency) - 300 MHz à 3 GHz
- Longueur d'onde : 1 m à 10 cm
- Applications : Télévision, GSM, GPS

#### Bandes SHF (Super High Frequency) - 3 GHz à 30 GHz
- Longueur d'onde : 10 cm à 1 cm
- Applications : Satellites, radar, WiFi

### Allocations internationales

#### Réglementation de l'UIT

L'UIT divise le monde en trois régions :
- **Région 1** : Europe, Afrique, Russie
- **Région 2** : Amériques
- **Région 3** : Asie, Australie

Chaque région a ses propres allocations de fréquences.

#### Autorisations d'usage

- **Service fixe** : Communications point-à-point
- **Service mobile** : Communications mobiles
- **Service de radiodiffusion** : Radio/TV
- **Service amateur** : Radioamateurs
- **Service satellite** : Communications spatiales

## 2.3 Modulation : AM, FM, PM

### Modulation d'amplitude (AM)

La modulation d'amplitude consiste à faire varier l'amplitude d'une porteuse selon le signal à transmettre.

#### Principe
```
Porteuse : A × cos(2πf_c t)
Signal modulé : [A + m(t)] × cos(2πf_c t)
```

Où :
- A : amplitude de la porteuse
- f_c : fréquence de la porteuse
- m(t) : signal modulant

#### Avantages et inconvénients
- **Avantages** : Simple à implémenter, bonne couverture
- **Inconvénients** : Sensible aux parasites, inefficace en puissance

### Modulation de fréquence (FM)

La modulation de fréquence fait varier la fréquence de la porteuse selon le signal à transmettre.

#### Principe
```
Porteuse : A × cos(2πf_c t + φ(t))
```

Où φ(t) est proportionnel à l'intégrale du signal modulant.

#### Avantages et inconvénients
- **Avantages** : Bonne qualité audio, résistante aux parasites
- **Inconvénients** : Bande passante plus large, complexité accrue

### Modulation de phase (PM)

La modulation de phase fait varier la phase de la porteuse selon le signal à transmettre.

#### Principe
```
Porteuse : A × cos(2πf_c t + k × m(t))
```

Où k est la constante de modulation de phase.

#### Applications
- Télécommunications numériques
- Systèmes de navigation (GPS)

## 2.4 Modulations numériques : FSK, PSK, QAM, OFDM

### Modulation par déplacement de fréquence (FSK)

#### Principe
La fréquence de la porteuse change entre deux valeurs selon le bit à transmettre :
- Bit 0 : fréquence f1
- Bit 1 : fréquence f2

#### Types
- **2-FSK** : 2 fréquences pour 1 bit
- **4-FSK** : 4 fréquences pour 2 bits

#### Applications
- Radio amateur (RTTY)
- Télécommunications lentes

### Modulation par déplacement de phase (PSK)

#### Principe
La phase de la porteuse change selon la valeur du bit :
- BPSK : 2 phases (0° et 180°)
- QPSK : 4 phases (0°, 90°, 180°, 270°)
- 8-PSK : 8 phases

#### Avantages
- Efficacité spectrale
- Résistance au bruit

#### Applications
- Satellite (DVB-S)
- WiFi (802.11)

### Modulation d'amplitude en quadrature (QAM)

#### Principe
Combinaison de modulation d'amplitude et de phase :
- 16-QAM : 16 symboles (4 bits par symbole)
- 64-QAM : 64 symboles (6 bits par symbole)
- 256-QAM : 256 symboles (8 bits par symbole)

#### Applications
- Télévision numérique terrestre (DVB-T)
- Câble (DOCSIS)
- LTE/5G

### Multiplexage par répartition orthogonale de fréquence (OFDM)

#### Principe
Division du canal en multiples sous-porteuses orthogonales :
- Chaque sous-porteuse transporte une partie des données
- Les sous-porteuses sont espacées de 1/T (T = durée du symbole)

#### Avantages
- Résistance aux échos et au fading
- Efficacité spectrale optimale

#### Applications
- WiFi (802.11a/g/n/ac/ax)
- LTE/5G
- DAB (radio numérique)

## 2.5 Antennes : principes essentiels

### Fonctionnement d'une antenne

Une antenne est un transducteur qui convertit les signaux électriques en ondes électromagnétiques (émission) et vice-versa (réception).

#### Paramètres clés

- **Longueur d'onde** : λ = c / f
- **Impédance** : Généralement 50 ou 75 ohms
- **Gain** : Puissance par rapport à une antenne isotrope
- **Directivité** : Concentration du rayonnement
- **Pola** : Orientation du champ électrique

### Types d'antennes

#### Antenne dipôle
- Longueur : λ/2
- Omnidirectional dans le plan horizontal
- Simple et efficace

#### Antenne Yagi
- Haute directivité
- Gain élevé
- Utilisée pour la réception TV/DAB

#### Antenne parabolique
- Très haute directivité
- Applications satellite
- Diamètre déterminé par la fréquence

#### Antenne hélicoïdale
- Polarisation circulaire
- Applications satellite (GPS, Iridium)

### Adaptation d'impédance

#### Pourquoi adapter ?
- Maximiser le transfert d'énergie
- Réduire les réflexions
- Améliorer l'efficacité

#### Méthodes
- Ligne quart d'onde
- Transformateur d'impédance
- Réseaux d'adaptation

### Antennes pour SDR

#### Antennes large bande
- Couvrent plusieurs bandes de fréquences
- Nécessaires pour le SDR (scanning)

#### Antennes discone
- Très large bande
- Applications professionnelles

#### Antennes log-périodiques
- Bande large avec directivité
- Applications monitoring
