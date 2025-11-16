# Chapitre 6 : Projets pratiques – Réception

## 6.1 Écouter la FM avec RTL-SDR

### Prérequis matériel
- RTL-SDR (v3 ou v4 recommandé)
- Antenne FM (dipôle λ/2 ou antenne TV)
- Câble SMA
- Ordinateur avec SDR++

### Installation du logiciel

#### Windows
```bash
# Télécharger SDR++ depuis https://github.com/AlexandreRouma/SDRPlusPlus
# Extraire et lancer SDRPlusPlus.exe
```

#### Linux
```bash
sudo apt update
sudo apt install librtlsdr-dev libfftw3-dev libglfw3-dev libglew-dev libvolk2-dev
git clone https://github.com/AlexandreRouma/SDRPlusPlus.git
cd SDRPlusPlus
mkdir build && cd build
cmake ..
make -j$(nproc)
sudo make install
```

### Configuration de base

#### Démarrage de SDR++
1. Lancer SDR++
2. Sélectionner "RTL-SDR Source" dans la liste des sources
3. Cliquer sur "Play" pour démarrer la réception

#### Réglages initiaux
- **Fréquence centrale** : 100 MHz (milieu de la bande FM)
- **Gain** : Automatique ou manuel (30-40 dB)
- **Mode** : FM (WFM pour wide FM)
- **Filtre** : 200 kHz de bande passante

### Recherche de stations FM

#### Méthode manuelle
1. Régler la fréquence centrale sur 88-108 MHz
2. Observer le spectre pour identifier les pics de signal
3. Ajuster la fréquence pour centrer sur un pic
4. Régler la bande passante à 200 kHz
5. Ajuster le volume et le squelch

#### Scan automatique
- Utiliser la fonction "Frequency Scanner" de SDR++
- Définir la plage 87.5-108 MHz
- Lancer le scan pour détecter automatiquement les stations

### Optimisation de la réception

#### Position de l'antenne
- Placer l'antenne près d'une fenêtre
- Orienter pour maximiser le signal
- Éviter les interférences (micro-ondes, WiFi)

#### Réduction du bruit
- Utiliser un filtre passe-bande FM si disponible
- Ajuster le gain pour éviter la saturation
- Utiliser un préamplificateur si signal faible

### Dépannage courant

#### Pas de signal
- Vérifier la connexion USB
- Tester avec une antenne différente
- Vérifier la fréquence (FM = 87.5-108 MHz)

#### Bruit excessif
- Réduire le gain
- Améliorer l'antenne
- Éloigner les sources d'interférence

## 6.2 Scanner les fréquences locales

### Préparation du matériel

#### Antennes adaptées
- **Antenne discone** : Large bande (25-1300 MHz)
- **Antenne col de cygne** : Portable, large bande
- **Antenne VHF/UHF** : Spécialisée

#### Configuration SDR++
- Source : RTL-SDR
- Fréquence : 100 MHz centrale
- Gain : 30 dB
- Mode : AM/FM selon la bande

### Exploration des bandes

#### Bande FM (87.5-108 MHz)
- Stations de radio commerciales
- Radio locale, régionale, nationale
- Identifications : RDS (Radio Data System)

#### Bande AM (530-1600 kHz)
- Radio AM/MW (moyenne onde)
- Stations internationales
- Trafic maritime (2182 kHz)

#### Bande VHF aviation (118-137 MHz)
- Communications air-sol
- Contrôle aérien
- Fréquences d'urgence (121.5 MHz)

#### Bande PMR (146-174 MHz)
- Services d'urgence
- Taxi, ambulances
- Communications municipales

#### Bande UHF (430-440 MHz)
- Radio amateur (70 cm)
- Liaison vidéo drone
- Communications data

### Techniques de scan

#### Scan manuel
1. Régler fréquence centrale
2. Observer le spectre
3. Identifier les signaux actifs
4. Démoduler selon le type

#### Scan automatique avec script

```python
#!/usr/bin/env python3
import time
from rtlsdr import RtlSdr

sdr = RtlSdr()

# Configuration
sdr.sample_rate = 2.4e6  # 2.4 MHz
sdr.center_freq = 100e6  # 100 MHz
sdr.gain = 30

# Fonction de scan
def scan_band(start_freq, end_freq, step):
    freq = start_freq
    while freq <= end_freq:
        sdr.center_freq = freq
        samples = sdr.read_samples(256*1024)
        power = sum(abs(s)**2 for s in samples) / len(samples)
        if power > threshold:  # Seuil à définir
            print(f"Signal détecté à {freq/1e6:.1f} MHz")
        freq += step

# Scan FM
scan_band(87.5e6, 108e6, 0.1e6)
```

### Analyse des signaux découverts

#### Identification des modulations
- **AM** : Enveloppe détectable
- **FM** : Bande occupée large
- **SSB** : Bande étroite, asymétrique

#### Mesure des caractéristiques
- Largeur de bande
- Puissance relative
- Stabilité de fréquence

### Applications pratiques

#### Monitoring environnemental
- Surveillance des communications d'urgence
- Détection d'interférences
- Étude de la propagation

#### Recherche radioamateur
- Écoute des bandes amateurs
- Identification des modes (SSB, CW, numérique)
- Participation aux nets

## 6.3 Suivre les avions : ADS-B (1090 MHz)

### Principe de l'ADS-B

L'ADS-B (Automatic Dependent Surveillance-Broadcast) est un système de surveillance automatique qui permet aux avions de diffuser leur position, altitude, vitesse et identité.

#### Fréquences utilisées
- **1090 MHz** : Fréquence principale ADS-B
- **Mode S** : Interrogation/réponse 1030/1090 MHz

#### Format des messages
- **Position** : Latitude, longitude, altitude
- **Vitesse** : Ground speed, heading
- **Identité** : Code OACI (24 bits)
- **Statut** : Squawk code, emergency status

### Configuration matérielle

#### Antenne adaptée
- **Antenne 1090 MHz** : Colinéaire verticale
- **Gain** : 3-6 dBi
- **Polarisation** : Verticale

#### SDR configuration
- Fréquence centrale : 1090 MHz
- Bande passante : 2 MHz
- Gain : 40-50 dB

### Logiciels ADS-B

#### Dump1090

##### Installation Linux
```bash
sudo apt update
sudo apt install git build-essential librtlsdr-dev pkg-config
git clone https://github.com/antirez/dump1090.git
cd dump1090
make
```

##### Utilisation
```bash
# Mode interactif avec carte
./dump1090 --interactive --lat 48.8566 --lon 2.3522

# Mode serveur web
./dump1090 --net --net-http-port 8080
```

#### Interface web
Accéder à http://localhost:8080 pour voir :
- Carte des avions en temps réel
- Liste des vols avec détails
- Statistiques de réception

### Analyse des données

#### Informations extraites
- **Callsign** : Indicatif du vol (AF123)
- **ICAO** : Adresse hexadécimale unique
- **Position GPS** : Latitude/longitude précise
- **Altitude** : En pieds au-dessus du niveau de la mer
- **Vitesse** : En nœuds
- **Route** : Cap magnétique

#### Visualisation avancée

##### Avec Virtual Radar Server
- Logiciel Windows multiplateforme
- Base de données complète des avions
- Cartes détaillées
- Historique des vols

##### Intégration avec FlightRadar24
- Upload des données vers FR24
- Contribution à la communauté
- Accès aux données mondiales

### Optimisation de la réception

#### Position de l'antenne
- Hauteur maximale possible
- Vue dégagée sur l'horizon
- Éloignement des obstacles

#### Réduction des interférences
- Filtre passe-bande 1090 MHz
- Préamplificateur basse bruit
- Position éloignée des émetteurs WiFi

#### Amélioration de la portée
- Antenne directive vers les couloirs aériens
- Réseau d'antennes diversifiées
- Collaboration avec d'autres récepteurs

### Applications pratiques

#### Aviation générale
- Suivi des vols locaux
- Apprentissage du trafic aérien
- Sécurité aérienne

#### Recherche
- Étude des flux aériens
- Analyse des routes
- Statistiques de trafic

## 6.4 Suivre les navires : AIS (162 MHz)

### Principe de l'AIS

L'AIS (Automatic Identification System) est un système automatique d'identification des navires qui permet l'échange d'informations de navigation entre bateaux et stations terrestres.

#### Fréquences AIS
- **Canal A** : 161.975 MHz (87B)
- **Canal B** : 162.025 MHz (88B)
- **Fréquences alternatives** : 161.525/162.025 MHz

#### Types de messages
- **Message 1/2/3** : Position, cap, vitesse
- **Message 5** : Données statiques (nom, dimensions)
- **Message 18** : Position classe B
- **Message 24** : Données statiques classe B

### Configuration

#### Antenne VHF maritime
- **Antenne quart d'onde** : λ/4 à 162 MHz
- **Gain** : 0-3 dBi
- **Montage** : Vertical, hauteur > 5m si possible

#### SDR setup
- Fréquence : 162 MHz
- Bande passante : 25 kHz par canal
- Modulation : GMSK (Gaussian Minimum Shift Keying)

### Logiciels AIS

#### AIS Dispatcher

##### Installation
```bash
# Via package manager ou compilation
sudo apt install ais-dispatcher
# ou
git clone https://github.com/bcl/aisdispatcher.git
cd aisdispatcher
make
```

##### Configuration
```bash
# Fichier de configuration
[device]
type=rtlsdr
gain=40
center_frequency=162000000
sample_rate=2400000

[receiver]
message_timeout=10
```

#### OpenCPN
- Logiciel de navigation open-source
- Intégration AIS native
- Cartes marines

### Analyse des données AIS

#### Informations transmises
- **MMSI** : Identifiant unique du navire (9 chiffres)
- **Nom du navire** : Jusqu'à 20 caractères
- **Position GPS** : Latitude/longitude
- **Cap et vitesse** : COG/SOG
- **Dimensions** : Longueur, largeur, tirant d'eau
- **Type de navire** : Cargo, passager, pêche, etc.

#### Visualisation

##### Cartes intégrées
- Affichage des navires en temps réel
- Routes de navigation
- Zones de sécurité

##### Données statistiques
- Trafic par zone
- Types de navires
- Routes commerciales

### Optimisation

#### Amélioration de la réception
- Antenne extérieure haute
- Préamplificateur VHF
- Filtre passe-bande AIS

#### Gestion des collisions
- Synchronisation sur les deux canaux
- Déduplication des messages
- Validation des données

### Applications

#### Sécurité maritime
- Surveillance du trafic côtier
- Détection d'anomalies
- Assistance aux secours

#### Recherche environnementale
- Étude des routes maritimes
- Impact sur la biodiversité
- Surveillance de la pollution

## 6.5 Recevoir les satellites météo NOAA

### Principe des satellites NOAA

Les satellites NOAA (National Oceanic and Atmospheric Administration) diffusent des images météorologiques en temps réel via la bande VHF.

#### Satellites actifs
- **NOAA 15** : 137.62 MHz (decommissioned)
- **NOAA 18** : 137.9125 MHz
- **NOAA 19** : 137.1 MHz

#### Transmission APT (Automatic Picture Transmission)
- Modulation : AM
- Bande passante : 34 kHz
- Résolution : 4 lignes par seconde
- Format : 2 canaux (visible/IR)

### Configuration matérielle

#### Antenne satellite
- **Antenne QFH** (Quadrifilar Helix) : Spécialisée satellites LEO
- **Antenne turnstile** : Plus simple à réaliser
- **Antenne Yagi 137 MHz** : Directive

#### SDR configuration
- Fréquence : Selon le satellite (137.1-137.9125 MHz)
- Bande passante : 40 kHz
- Modulation : AM (USB pour APT)

### Logiciels de réception

#### WxToImg

##### Installation
```bash
# Télécharger depuis http://www.wxtoimg.com/
# Version Linux disponible
sudo apt install wxtoimg
```

##### Configuration
1. Sélectionner le satellite
2. Entrer les coordonnées GPS
3. Configurer l'audio (RTL-SDR via sox)

#### Orbitron
- Logiciel de prédiction d'orbites
- Calcul automatique des passages
- Intégration avec WxToImg

### Réception pratique

#### Préparation du passage
1. Vérifier les horaires avec Heavens-Above
2. Orienter l'antenne vers l'azimut du satellite
3. Ajuster l'élévation selon le temps

#### Enregistrement
```bash
# Avec rtl_fm
rtl_fm -f 137.1M -s 40k -g 50 -p 0 - | sox -t raw -r 40k -e s -b 16 -c 1 - -t wav noaa19.wav
```

#### Traitement de l'image
- **Calibration** : Ajustement des niveaux
- **Projection** : Correction géographique
- **Amélioration** : Contraste, couleurs

### Analyse des images

#### Canaux disponibles
- **Canal A (visible)** : Images jour/nuit
- **Canal B (IR)** : Températures, nuages
- **Canal mixte** : Combinaison visible/IR

#### Applications météo
- Détection de fronts
- Identification des types de nuages
- Mesure des températures de surface

### Optimisation

#### Amélioration du signal
- Préamplificateur VHF basse bruit
- Filtre passe-bande étroit
- Position antenne optimale

#### Correction képlerienne
- Prédiction précise des orbites
- Compensation Doppler
- Calcul automatique de l'élévation

## 6.6 Décoder les radios amateurs APRS

### Principe de l'APRS

L'APRS (Automatic Packet Reporting System) est un système de communication numérique utilisé par les radioamateurs pour transmettre des données de position, météo, et messages texte.

#### Fréquence principale
- **144.39 MHz** (bande 2m)
- Modulation : AFSK (Audio Frequency Shift Keying)
- Débit : 1200 bps
- Format : AX.25 packets

### Configuration

#### Antenne VHF
- Antenne λ/2 verticale 144 MHz
- Gain : 0-6 dBi
- Polarisation verticale

#### SDR setup
- Fréquence : 144.39 MHz
- Bande : 25 kHz
- Modulation : FM
- Démodulation audio pour décodage logiciel

### Logiciels APRS

#### Dire Wolf

##### Installation Linux
```bash
sudo apt install direwolf
# ou compilation
git clone https://github.com/wb2osz/direwolf.git
cd direwolf
make
sudo make install
```

##### Configuration
```bash
# direwolf.conf
ACHANNELS 1
CHANNEL 0
MYCALL [votre indicatif]
MODEM 1200
```

##### Utilisation
```bash
# Avec audio depuis RTL-SDR
rtl_fm -f 144.39M -s 24k -g 40 - | direwolf -c direwolf.conf -r 24000 -
```

#### APRS.fi
- Plateforme web pour visualisation
- Cartes en temps réel
- Base de données historique

### Analyse des données APRS

#### Types de paquets
- **Position** : Latitude/longueur, altitude
- **Météo** : Température, pression, vent
- **Statut** : Messages texte libres
- **Télémesure** : Données de capteurs

#### Format des messages
```
[Indicatif]>APRS,TCPIP*,qAC,[gateway]:@[heure]z[latitude]/[longitude][symbole][commentaire]
```

#### Symboles APRS
- **/** : Position fixe
- **\** : Position mobile
- **>** : Objet
- **_** : Station météo

### Applications pratiques

#### Tracking GPS
- Positionnement en temps réel
- Suivi de véhicules/ballons
- Géocaching

#### Météo amateur
- Réseau de stations météo
- Données locales précises
- Alertes météo

#### Communication d'urgence
- Messages d'urgence
- Coordination des secours
- Communication en cas de blackout

## 6.7 Sniffer des signaux inconnus (URH)

### Principe de l'analyse de signaux

L'analyse de signaux inconnus nécessite une approche méthodique pour identifier la modulation, le protocole et le contenu des transmissions.

### Préparation

#### Matériel
- SDR large bande (HackRF ou LimeSDR recommandé)
- Antenne large bande
- Préamplificateur si nécessaire

#### Logiciel : Universal Radio Hacker (URH)

##### Installation
```bash
pip install urh
# ou
git clone https://github.com/jopohl/urh.git
cd urh
pip install .
```

### Méthodologie d'analyse

#### Étape 1 : Capture du signal
1. Lancer URH
2. Configurer la source SDR
3. Régler la fréquence approximative
4. Capturer des échantillons

#### Étape 2 : Analyse spectrale
- Observer la forme du spectre
- Mesurer la largeur de bande
- Identifier le type de modulation

#### Étape 3 : Analyse temporelle
- Examiner le signal dans le domaine temps
- Détecter les patterns périodiques
- Mesurer les durées d'impulsions

#### Étape 4 : Démodulation
- Tester différentes modulations
- ASK, FSK, PSK selon le spectre
- Ajuster les paramètres

### Types de signaux courants

#### Télécommandes 433 MHz
- Modulation : ASK/OOK
- Débit : 1000-5000 bps
- Longueur : Variable (24-48 bits)

#### Capteurs IoT (868 MHz)
- Modulation : FSK/GFSK
- Protocoles : LoRa, SigFox
- Codage : Manchester, NRZ

#### Radio amateur numérique
- Modes : FT8, WSPR, JS8Call
- Modulation : FSK multi-tones
- Synchronisation : Horloge précise

### Outils d'analyse URH

#### Analyseur de modulation
- Détection automatique du type
- Paramètres optimaux
- Visualisation des constellations

#### Décodeur de protocoles
- Bibliothèque de protocoles connus
- Éditeur de protocoles personnalisés
- Export des données

#### Générateur de signaux
- Replay des signaux capturés
- Modification des paramètres
- Test de vulnérabilités

### Applications pratiques

#### Sécurité IoT
- Analyse de dispositifs connectés
- Détection de failles
- Développement de contre-mesures

#### Rétro-ingénierie
- Compréhension de protocoles propriétaires
- Développement d'interfaces compatibles
- Intégration de systèmes existants

#### Recherche spectrale
- Cartographie des émissions locales
- Détection d'interférences
- Étude de l'occupation spectrale
