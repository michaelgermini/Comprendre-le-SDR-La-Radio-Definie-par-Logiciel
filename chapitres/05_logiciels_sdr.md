# Chapitre 5 : Logiciels pour SDR

## 5.1 SDR++

### Présentation

SDR++ est un analyseur de spectre et récepteur SDR multiplateforme moderne.

#### Historique
- Fork de SDR# (Windows only)
- Développement actif depuis 2019
- Support multiplateforme (Windows/Linux/macOS)

### Fonctionnalités principales

#### Interface utilisateur
- Interface moderne et intuitive
- Thèmes personnalisables
- Support haute résolution

#### Fonctionnalités RF
- Analyse spectrale temps réel
- Waterfall display
- Démodulateurs intégrés (AM/FM/SSB)
- Enregistrement audio/vidéo

### Compatibilité matérielle

#### SDR supportés
- RTL-SDR
- HackRF
- LimeSDR
- USRP (via UHD)
- Airspy
- SDRplay

#### Drivers
- Support natif des drivers
- Configuration automatique
- Gestion des périphériques multiples

### Modules et plugins

#### Modules de base
- **Source** : Interface avec le SDR
- **Radio** : Démodulation audio
- **Recorder** : Enregistrement
- **Frequency Manager** : Gestion des fréquences

#### Modules avancés
- **Network** : Streaming réseau
- **Audio** : Traitement audio
- **DSP** : Filtres numériques
- **Morse Decoder** : Décodage morse

## 5.2 GQRX

### Présentation

GQRX est un récepteur SDR open-source pour Linux, inspiré de SDR#.

#### Philosophie
- Logiciel libre et gratuit
- Interface simple et efficace
- Intégration parfaite avec Linux

### Fonctionnalités

#### Interface
- Interface GTK+ native
- Contrôles intuitifs
- Affichage spectre/waterfall

#### Démodulateurs
- AM, FM, SSB, CW
- Démodulateur numérique (APCO25, DMR)
- Squelch automatique
- Filtrage audio

### Configuration avancée

#### Réglages DSP
- Filtrage numérique
- Correction AGC
- Égalisation audio

#### Enregistrement
- Enregistrement IQ
- Enregistrement audio
- Streaming UDP

## 5.3 GNU Radio (flowgraphs)

### Présentation

GNU Radio est le framework de référence pour le SDR, offrant une programmation par blocs graphiques.

#### Architecture
- Programmation par blocs (flowgraphs)
- Bibliothèque extensive de blocs
- Support Python/C++

### Interface graphique : GNU Radio Companion (GRC)

#### Création de flowgraphs
- Interface drag & drop
- Connexion de blocs
- Génération automatique de code

#### Blocs disponibles

##### Sources
- **osmocom Source** : Interface RTL-SDR/HackRF
- **USRP Source** : Interface USRP
- **File Source** : Lecture fichiers IQ
- **Signal Source** : Génération de signaux

##### Traitement
- **FFT** : Transformée de Fourier
- **Filter** : Filtres FIR/IIR
- **Mixer** : Mixage fréquence
- **Demod** : Démodulateurs

##### Sinks
- **Audio Sink** : Sortie audio
- **File Sink** : Enregistrement
- **UDP Sink** : Streaming réseau
- **QT GUI** : Interfaces graphiques

### Programmation avancée

#### Python integration
```python
#!/usr/bin/env python3

import numpy as np
from gnuradio import gr, analog, blocks

class my_top_block(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "My SDR Flowgraph")

        # Création des blocs
        self.source = osmocom.source(args="numchan=1")
        self.demod = analog.am_demod_cf(
            channel_rate=250000,
            audio_decim=1,
            audio_pass=5000,
            audio_stop=5500,
        )
        self.sink = audio.sink(48000, "", True)

        # Connexion des blocs
        self.connect(self.source, self.demod, self.sink)
```

#### Applications typiques

##### Récepteur FM simple
- Source RTL-SDR
- Filtre passe-bande
- Démodulateur FM
- Sortie audio

##### Analyse spectrale
- Source SDR
- FFT
- Affichage spectre
- Waterfall

##### Émetteur de test
- Génération signal
- Modulation
- Source HackRF/USRP

## 5.4 CubicSDR

### Présentation

CubicSDR est un récepteur SDR multiplateforme avec interface 3D.

#### Caractéristiques uniques
- Interface 3D innovante
- Support bookmarking
- Démarrage rapide

### Fonctionnalités

#### Interface 3D
- Visualisation spectrale 3D
- Navigation intuitive
- Gestion des signaux actifs

#### Fonctionnalités RF
- Démodulateurs multiples
- Enregistrement IQ/audio
- Streaming réseau

## 5.5 Universal Radio Hacker

### Présentation

URH (Universal Radio Hacker) est spécialisé dans l'analyse et la rétro-ingénierie de protocoles radio.

#### Usage principal
- Analyse de signaux inconnus
- Rétro-ingénierie de protocoles propriétaires
- Sniffing de télécommandes

### Fonctionnalités

#### Analyse de signaux
- Capture temps réel
- Analyse modulation
- Détection automatique de protocoles

#### Outils de rétro-ingénierie
- **Ask modulation** : Analyse ASK
- **FSK demodulation** : Analyse FSK
- **PSK analysis** : Analyse PSK

#### Génération de signaux
- Replay de signaux capturés
- Génération de protocoles personnalisés
- Test de vulnérabilités

### Applications pratiques

#### Sécurité IoT
- Analyse télécommandes 433/868 MHz
- Hacking de serrures connectées
- Test de sécurité domotique

#### Radio amateur
- Analyse de protocoles APRS
- Décodage de modes numériques
- Développement de nouveaux modes

## 5.6 OpenWebRX

### Présentation

OpenWebRX transforme votre SDR en récepteur radio accessible via navigateur web.

#### Architecture
- Serveur SDR local
- Interface web responsive
- Streaming audio temps réel

### Fonctionnalités

#### Interface web
- Contrôles complets
- Spectre et waterfall
- Démodulateurs intégrés

#### Streaming
- Audio en direct
- Contrôle à distance
- Multi-utilisateurs

### Installation et configuration

#### Prérequis
- SDR compatible (RTL-SDR, HackRF)
- Serveur Linux
- Python 3

#### Configuration
```bash
# Installation
git clone https://github.com/jketterl/openwebrx.git
cd openwebrx
./openwebrx.py --help

# Configuration
nano config_webrx.py
```

#### Usage
- Accès via http://localhost:8073
- Configuration via interface web
- Personnalisation des démodulateurs

## 5.7 Logiciels spécialisés (ADS-B, AIS, NOAA…)

### Logiciels ADS-B

#### Dump1090
- Décodeur ADS-B open-source
- Interface web intégrée
- Compatible RTL-SDR

#### Caractéristiques
- Détection avions en temps réel
- Base de données FlightRadar24
- Cartographie intégrée

### Logiciels AIS

#### AIS Dispatcher
- Décodeur AIS maritime
- Compatible RTL-SDR
- Interface cartographique

#### Applications
- Suivi trafic maritime
- Sécurité navigation
- Recherche environnementale

### Logiciels météo (NOAA)

#### WxToImg
- Décodeur images NOAA
- Correction képlerienne
- Interface graphique

#### Caractéristiques
- Réception APT
- Géolocalisation
- Correction atmosphérique

### Autres logiciels spécialisés

#### Radioastronomie
- **GNU Radio** : Analyse signaux astronomiques
- **SETI tools** : Recherche signaux extraterrestres

#### Télécommunications
- **gr-gsm** : Analyse GSM
- **gr-lte** : Analyse LTE
- **gr-ieee802-11** : Analyse WiFi

#### Militaire/Professionnel
- **srsLTE** : Suite LTE complète
- **OpenBTS** : Station de base GSM
- **Osmocom** : Suite télécom open-source

### Comparatif des logiciels

| Logiciel | Usage principal | Interface | Multiplateforme | Niveau |
|----------|----------------|-----------|-----------------|--------|
| SDR++ | Analyse générale | Graphique | ✅ | Débutant |
| GQRX | Réception | Graphique | Linux | Intermédiaire |
| GNU Radio | Développement | Graphique/Code | ✅ | Avancé |
| CubicSDR | Analyse 3D | Graphique | ✅ | Intermédiaire |
| URH | Rétro-ingénierie | Graphique | ✅ | Intermédiaire |
| OpenWebRX | Streaming web | Web | ✅ | Débutant |
| Dump1090 | ADS-B | Console/Web | ✅ | Intermédiaire |

### Choix du logiciel

#### Pour débuter
- **SDR++** : Interface moderne, facile
- **GQRX** : Simple et efficace
- **OpenWebRX** : Accès web

#### Pour développement
- **GNU Radio** : Framework complet
- **Python + bibliothèques** : Personnalisation

#### Pour analyse spécialisée
- **URH** : Rétro-ingénierie
- **Logiciels dédiés** : ADS-B, AIS, etc.

#### Pour usage avancé
- **GNU Radio + Python** : Tout est possible
- **UHD + C++** : Performance maximale
