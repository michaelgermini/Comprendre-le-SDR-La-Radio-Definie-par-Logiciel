# Matériel SDR conseillé selon budget

## Budget 0-50€ : Découverte

### Matériel essentiel
#### RTL-SDR v3 (~25€)
**Avantages :**
- Prix très accessible
- Qualité professionnelle
- Compatible avec tous les logiciels
- Stabilité fréquentielle (±1 ppm)

**Inconvénients :**
- Réception uniquement
- Bande passante limitée (2.4 MHz)
- 8 bits de résolution

**Où acheter :** Amazon, Banggood, AliExpress, NooElec

#### Antenne dipôle λ/2 144/430 MHz (~10€)
**Caractéristiques :**
- Couvre 2m et 70cm
- Gain ~2.15 dBi
- Polarisation verticale
- Connecteur SMA

#### Câble SMA mâle-femelle (~5€)
**Spécifications :**
- Longueur 50cm ou 1m
- Blindage correct
- Connecteurs de qualité

### Accessoires recommandés
#### Préamplificateur VHF/UHF (~15€)
- Gain 10-15 dB
- NF < 2 dB
- Alimentation 5V USB

#### Support antenne magnétique (~10€)
- Aimant puissant
- Câble 3m
- Base lourde

### Logiciels inclus
- **SDR++** : Interface moderne, gratuit
- **GQRX** : Spécialisé Linux, gratuit
- **SDR#** : Windows, gratuit

### Utilisations possibles
- Écouter radio FM/AM
- Scanner bandes VHF/UHF
- Recevoir ADS-B (avec antenne adaptée)
- Découverte protocoles simples

### Limitations
- Pas d'émission
- Performances limitées en HF
- Bande passante réduite

---

## Budget 50-150€ : Intermédiaire

### Matériel principal
#### HackRF One (~120€)
**Spécifications :**
- Fréquences : 1 MHz - 6 GHz
- Bande passante : 20 MHz
- Résolution : 8 bits
- Puissance TX : 0-15 dBm (avec ampli)

**Avantages :**
- Émission et réception
- Large couverture fréquentielle
- Communauté active
- Open hardware

**Inconvénients :**
- Consommation élevée
- Chauffement
- Drivers parfois complexes

#### Antenne discone large bande (~40€)
**Caractéristiques :**
- Couverture : 25-1300 MHz
- Gain : 0-3 dBi
- Omnidirectionnelle
- Idéale pour monitoring

### Accessoires essentiels
#### Atténuateur 20dB (~15€)
- Protection pour tests émission
- Haute puissance (10W)
- Connecteurs SMA

#### Charge dummy load 50 ohms (~20€)
- Résistance 50 ohms
- Puissance 10W
- Tests sans antenne

#### GPSDO pour stabilité (~50€)
- Référence 10 MHz stable
- Précision ±0.5 ppm
- Interface USB

### Logiciels
- **GNU Radio** : Développement avancé
- **Universal Radio Hacker** : Analyse protocoles
- **SDR++** : Interface utilisateur

### Utilisations possibles
- Émission expérimentale légale
- Analyse protocoles propriétaires
- Tests sécurité IoT
- Radioamateur (avec licence)

### Améliorations possibles
- Préamplificateur large bande (~30€)
- Filtre passe-bande (~25€)
- Batterie externe (~20€)

---

## Budget 150-400€ : Avancé

### Matériel professionnel
#### LimeSDR (~250€)
**Spécifications :**
- Fréquences : 100 kHz - 3.8 GHz
- MIMO : 2x2 canaux
- Bande passante : 30.72 MHz
- Résolution : 12 bits

**Avantages :**
- Excellent rapport qualité/prix
- Capacités MIMO
- Stabilité intégrée
- Idéal pour recherche

#### USRP B200 (~300€)
**Spécifications :**
- Fréquences : 70 MHz - 6 GHz
- Bande passante : 56 MHz
- Résolution : 12 bits
- Interface : USB 3.0

**Avantages :**
- Support UHD officiel
- Excellente stabilité
- Grande communauté
- Documentation complète

### Antennes spécialisées
#### Antenne Yagi 1090 MHz (~50€)
- Gain 10-12 dBi
- Directionnelle
- ADS-B/TCAS

#### Antenne quadrifilaire NOAA (~60€)
- Polarisation circulaire
- Gain 8-10 dBi
- Satellites LEO

### Instrumentation
#### Analyseur de spectre USB (~100€)
- Plage : 1 MHz - 6 GHz
- Résolution 1 Hz
- Interface PC

#### Wattmètre RF (~80€)
- Mesure puissance TX
- Précision ±0.1 dB
- Calibration automatique

### Utilisations avancées
- Recherche MIMO/5G
- Tests protocoles spatiaux
- Développement radio cognitive
- Mesures professionnelles

---

## Budget 400-1000€ : Expert

### Équipement laboratoire
#### USRP X310 (~800€)
**Spécifications :**
- Fréquences : DC - 6 GHz
- Bande passante : 160 MHz
- Résolution : 14 bits
- Ethernet Gigabit

**Avantages :**
- Performance maximale
- Synchronisation précise
- Modules interchangeables
- Usage professionnel

#### LimeSDR + expansion (~400€)
- MIMO 2x2 complet
- Front-end large bande
- Synchronisation GPS
- Logiciels spécialisés

### Station complète
#### Antenne rooftop (~200€)
- Multi-bandes
- Préamplificateur intégré
- Rotateur automatique
- Mât et fixation

#### Ampli puissance 10W (~150€)
- Gain 40 dB
- Linéarité excellente
- Protection contre SWR
- Refroidissement actif

### Outils de mesure
#### Générateur de signaux (~300€)
- Fréquences : 9 kHz - 6 GHz
- Modulation intégrée
- Calibration précise

#### Analyseur de réseaux (~400€)
- Mesure SWR
- Graphiques de Smith
- Calibration automatique

### Logiciels professionnels
#### MATLAB Communications Toolbox (~500€/an)
- Simulation avancée
- Analyse spectrale
- Traitement DSP

#### Keysight SystemVue (~2000€+)
- Conception système
- Simulation end-to-end
- Génération de code

---

## Budget 1000€+ : Recherche

### Équipement haute performance
#### USRP haut de gamme personnalisé
- Configurations spéciales
- Modules spécifiques
- Intégration système

#### SDR modulaires
- VRTX-2977 : SDR vectoriel
- Modules RF interchangeables
- Interfaces optiques

### Laboratoire complet
#### Chambre anéchoïque (~5000€)
- Mesures précises
- Calibration absolue
- Tests CEM

#### Instrumentation spécialisée
- Analyseur de modulation
- Testeur de BER
- Générateur de fading

### Collaborations
#### Partenariats industriels
- Accès équipement spécialisé
- Projets de recherche
- Publications conjointes

#### Centres de recherche
- Universités partenaires
- Laboratoires nationaux
- Programmes européens

---

## Recommandations par usage

### Radioamateur débutant
**Budget : 50-100€**
- RTL-SDR + antenne dual-band
- Logiciels SDR#
- Licence CEPT Novice

### Monitoring professionnel
**Budget : 200-400€**
- HackRF One + antenne discone
- Préamplificateur + filtres
- Logiciels spécialisés

### Recherche académique
**Budget : 500-1000€**
- USRP B210/X310
- Instrumentation complète
- Logiciels MATLAB/GNU Radio

### Développement commercial
**Budget : 1000€+**
- Équipement laboratoire
- Certification et conformité
- Support technique

---

## Conseils d'achat

### Qualité vs Prix
- Privilégiez la qualité pour usage sérieux
- Vérifiez compatibilité logicielle
- Lisez les retours utilisateurs

### Sources fiables
- **NooElec** : Qualité RTL-SDR
- **Great Scott Gadgets** : HackRF officiel
- **Ettus Research** : USRP officiel
- **Myriad RF** : LimeSDR officiel

### Garantie et support
- Privilégiez revendeurs avec SAV
- Communautés actives pour support
- Documentation complète

### Évolutivité
- Choisissez matériel extensible
- Interfaces standard (USB, Ethernet)
- Communauté active

---

## Évolution du matériel

### Tendances actuelles
- Intégration RF/micrologicielle
- Interfaces USB 3.0/4.0
- Synchronisation précise
- Consommation réduite

### Technologies émergentes
- SDR quantique
- IA intégrée
- Matériaux avancés
- Intégration photonique

### Préparation future
- Investir dans standards ouverts
- Formation continue
- Réseau professionnel
- Veille technologique
