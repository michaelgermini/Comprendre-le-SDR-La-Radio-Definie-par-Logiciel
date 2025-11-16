# Chapitre 4 : Le matériel SDR

## 4.1 RTL-SDR : le SDR low-cost

### Présentation

Le RTL-SDR est probablement le SDR le plus populaire au monde grâce à son prix très accessible.

#### Historique
- Basé sur le tuner RTL2832U + R820T
- Initialement conçu pour la réception DVB-T
- Découvert en 2010 par des hackers
- Popularisé par le blog rtl-sdr.com

### Caractéristiques techniques

#### Gamme de fréquence
- **Réception** : 24 MHz à 1.7 GHz (selon modèle)
- **Échantillonnage** : 8 bits
- **Bande passante** : 2.4 MHz maximum
- **Interface** : USB 2.0

#### Performances
- **Sensibilité** : -120 dBm (variable)
- **SNR** : 40-50 dB
- **Stabilité** : ±1 ppm (avec GPSDO optionnel)
- **Consommation** : < 300 mA

### Modèles disponibles

#### RTL-SDR v3
- Chip R820T2
- TCXO intégré (±1 ppm)
- Filtre passe-bas amélioré
- Blindage RF

#### RTL-SDR v4
- Chip R860
- Gamme étendue (100 kHz - 1.7 GHz)
- Sensibilité améliorée
- Filtrage avancé

### Applications typiques

#### Réception FM/AM
- Radio FM stéréo
- Radio AM/MW
- Radio aviation (VHF)

#### Télécommunications
- GSM monitoring (attention légal)
- Tetra/police
- Radio amateur

#### Signaux satellites
- NOAA APT
- Meteor M2
- ISS transmissions

## 4.2 HackRF One : émission/réception

### Présentation

Le HackRF One est un SDR full-duplex conçu pour les radioamateurs et chercheurs.

#### Philosophie
- Open-source hardware
- Communauté active
- Émission légale (respect réglementations)

### Caractéristiques techniques

#### Gamme de fréquence
- **Réception/Émission** : 1 MHz à 6 GHz
- **Échantillonnage** : 8 bits (extensible à 16 bits)
- **Bande passante** : 20 MHz
- **Interface** : USB 3.0

#### Performances
- **Sensibilité RX** : -110 dBm
- **Puissance TX** : 0-15 dBm (avec ampli externe)
- **SNR** : > 40 dB
- **Stabilité** : ±20 ppm (améliorable avec GPSDO)

### Architecture matérielle

#### FPGA Lattice
- Traitement temps réel
- Interface USB 3.0
- Contrôle des périphériques

#### Convertisseurs RF
- ADC/DAC Maxim MAX5864
- Large bande passante
- Bonne linéarité

### Applications

#### Radio amateur
- Transmission sur bandes amateurs
- Tests de protocoles
- Mesures RF

#### Recherche
- Développement de nouveaux standards
- Tests de sécurité
- Prototypage

#### Éducation
- Enseignement des communications
- Expérimentation RF
- Projets étudiants

## 4.3 LimeSDR : précision et MIMO

### Présentation

Le LimeSDR est un SDR professionnel offrant des capacités MIMO (Multiple Input Multiple Output).

#### Fabricant
- Myriad-RF (maintenant Lime Microsystems)
- Design open-source
- Support communautaire

### Caractéristiques techniques

#### Gamme de fréquence
- **Réception/Émission** : 100 kHz à 3.8 GHz
- **Échantillonnage** : 12 bits
- **Bande passante** : 30.72 MHz
- **Canaux** : 2x2 MIMO

#### Performances
- **Sensibilité RX** : -110 dBm
- **Puissance TX** : -30 à +10 dBm
- **SNR** : > 50 dB
- **Stabilité** : ±0.5 ppm

### Capacités MIMO

#### 2x2 MIMO
- Deux antennes RX et TX indépendantes
- Applications beamforming
- Tests 5G/LTE avancés

#### Synchronisation
- Horloge commune
- Phase cohérente
- Mesures précises

### Applications avancées

#### Recherche 5G
- Tests de modulation massive MIMO
- Beamforming algorithmique
- Channel sounding

#### Radar
- Systèmes radar expérimentaux
- Détection et localisation
- Imagerie RF

#### Communications spatiales
- SDR satellite
- Radio définie logicielle spatiale
- Tests de constellations

## 4.4 USRP : le standard professionnel

### Présentation

L'Universal Software Radio Peripheral (USRP) est la référence professionnelle en SDR.

#### Fabricant
- Ettus Research (National Instruments)
- Standard de facto
- Support commercial

### Caractéristiques techniques

#### Gamme étendue
- **USRP B200/B210** : 70 MHz - 6 GHz
- **USRP X300/X310** : DC - 6 GHz
- **USRP N210** : DC - 6 GHz avec GPSDO

#### Performances élevées
- **Échantillonnage** : 14-16 bits
- **Bande passante** : 56 MHz (B200) à 160 MHz (X310)
- **Stabilité** : ±0.01 ppm avec GPSDO
- **Synchronisation** : OctoClock pour réseaux

### Écosystème

#### Logiciels supportés
- GNU Radio natif
- UHD (USRP Hardware Driver)
- MATLAB/Simulink
- LabVIEW

#### Accessoires
- GPSDO pour stabilité
- Amplificateurs externes
- Filtres spécialisés

### Applications professionnelles

#### Recherche académique
- Communications sans fil
- Traitement du signal
- Réseaux ad hoc

#### Industrie
- Tests de conformité
- Développement de standards
- Mesures RF

#### Défense
- Systèmes de guerre électronique
- Communications tactiques
- Surveillance

## 4.5 Comparatif complet des plateformes

### Critères de comparaison

#### Prix
- **RTL-SDR** : 20-50€
- **HackRF One** : 300-400€
- **LimeSDR** : 250-350€
- **USRP B200** : 700-1000€
- **USRP X310** : 3000-5000€

#### Performances RF

| Critère | RTL-SDR | HackRF | LimeSDR | USRP B200 | USRP X310 |
|---------|---------|--------|---------|-----------|-----------|
| Fréquence min | 24 MHz | 1 MHz | 100 kHz | 70 MHz | DC |
| Fréquence max | 1.7 GHz | 6 GHz | 3.8 GHz | 6 GHz | 6 GHz |
| Bande passante | 2.4 MHz | 20 MHz | 30 MHz | 56 MHz | 160 MHz |
| Résolution ADC | 8 bits | 8 bits | 12 bits | 12 bits | 14 bits |
| Stabilité | ±20 ppm | ±20 ppm | ±0.5 ppm | ±2.5 ppm | ±0.005 ppm |

#### Fonctionnalités

| Fonction | RTL-SDR | HackRF | LimeSDR | USRP B200 | USRP X310 |
|----------|---------|--------|---------|-----------|-----------|
| Émission | ❌ | ✅ | ✅ | ✅ | ✅ |
| MIMO | ❌ | ❌ | ✅ (2x2) | ❌ | ✅ (optionnel) |
| GPSDO | Optionnel | Optionnel | Intégré | Optionnel | Optionnel |
| Synchronisation | ❌ | ❌ | ✅ | ✅ | ✅ |
| API stable | ⚠️ | ✅ | ✅ | ✅ | ✅ |

### Choix selon usage

#### Débutant/RX seulement
- **RTL-SDR v3/v4** : Parfait pour découvrir

#### Radio amateur/émission
- **HackRF One** : Bon rapport qualité/prix

#### Recherche MIMO/5G
- **LimeSDR** : Spécialisé MIMO

#### Professionnel/laboratoire
- **USRP B200/X310** : Haute performance

#### Budget limité
- **RTL-SDR** : Découverte
- **HackRF One** : Émission abordable

## 4.6 Accessoires : antennes, LNAs, filtres, pré-amplis, câbles

### Antennes

#### Antennes omnidirectionnelles
- **Antenne dipôle** : λ/2, couverture 360°
- **Antenne discone** : Large bande, monitoring
- **Antenne col de cygne** : Portable, large bande

#### Antennes directives
- **Antenne Yagi** : Haute directivité, faible bruit
- **Antenne parabolique** : Très directive, satellites
- **Antenne log-périodique** : Bande large, directivité

#### Antennes spécialisées
- **Antenne GPS** : Réception GPS actif/passif
- **Antenne 433 MHz** : Objets connectés
- **Antenne 868 MHz** : Lora/SigFox

### Amplificateurs (LNAs)

#### Low Noise Amplifier
- **Gain** : 10-30 dB
- **NF (Noise Figure)** : < 1 dB idéalement
- **IP3** : Point d'interception 3e ordre

#### Types
- **LNA large bande** : 50 MHz - 6 GHz
- **LNA narrow band** : Bande spécifique
- **LNA GPS** : 1575 MHz, NF < 1 dB

### Filtres

#### Filtres passe-bande
- **Filtre VHF** : 118-137 MHz (aviation)
- **Filtre UHF** : 400-470 MHz (PMR)
- **Filtre GPS** : 1575 MHz ± 10 MHz

#### Filtres passe-bas
- **Filtre harmoniques** : Suppression harmoniques TX
- **Filtre anti-aliasing** : Avant ADC

#### Filtres notch
- **Filtre pager** : Suppression signaux pager
- **Filtre GSM** : Réduction interférences GSM

### Pré-amplificateurs et atténuateurs

#### Pré-amplificateurs
- **Préampli VHF/UHF** : Gain 10-20 dB
- **Préampli satellite** : LNA + filtre

#### Atténuateurs
- **Atténuateur fixe** : 10/20/30 dB
- **Atténuateur variable** : Ajustable 0-30 dB
- **Atténuateur SMA** : Haute puissance

### Câbles et connecteurs

#### Types de câbles
- **RG-58** : Usage général, pertes élevées
- **RG-174** : Portable, flexible
- **LMR-400** : Basse perte, extérieur

#### Connecteurs
- **SMA** : Standard SDR
- **BNC** : Instrumentation
- **N-type** : Haute puissance
- **F-type** : TV/satellite

### Accessoires avancés

#### Sources de référence
- **GPSDO** : Référence 10 MHz stable
- **Rubidium** : Haute stabilité (±0.001 ppm)

#### Mesure
- **Analyseur de spectre** : Visualisation spectre
- **Wattmètre RF** : Mesure puissance
- **Générateur de signaux** : Tests et calibration

#### Alimentation
- **Alimentation stabilisée** : 5V/3A pour SDR
- **Batterie externe** : Usage mobile
- **UPS** : Continuité en cas de coupure
