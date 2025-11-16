# 📡 Table des fréquences internationales - Guide complet SDR

## 🌍 Régions UIT et contexte réglementaire

L'Union Internationale des Télécommunications (UIT) divise le monde en **trois régions** pour l'allocation des fréquences radio :

- **Région 1** : Europe, Afrique, Russie, Moyen-Orient, Mongolie
- **Région 2** : Amériques (Nord, Centrale, Sud), Groenland
- **Région 3** : Asie, Australie, Pacifique (sauf régions 1&2)

### 📋 Autorités réglementaires par région

| Région | Autorité principale | Pays couverts | Particularités |
|--------|-------------------|---------------|----------------|
| **1** | CEPT (Europe)<br/>ETSI | 48 pays européens | Harmonisation poussée, licences individuelles |
| **2** | CITEL<br/>FCC (USA) | 35 pays américains | Plus flexible, innovation rapide |
| **3** | APT | 38 pays asiatiques | Développement rapide 5G/6G |

### ⚖️ Statuts d'allocation des fréquences

| Statut | Description | Exemple d'usage |
|--------|-------------|-----------------|
| **Primaire** | Usage exclusif garanti | Aviation, maritime |
| **Secondaire** | Pas d'interférence aux primaires | Radioamateur, ISM |
| **Partagé** | Coordination entre utilisateurs | Satellite, recherche |
| **Libre** | Sans licence (sous conditions) | ISM, courte portée |

### 🔄 Évolution des allocations

- **WRC-23** (2023) : Nouvelles bandes pour 6G, protection 5G
- **WRC-27** (2027) : Bandes THz, communications spatiales
- **Tendances** : Partage dynamique, IA pour gestion spectre

---

## 📻 Bandes par service - Région 1 (Europe/UE)

## Bandes par service - Région 1 (Europe)

### Radioamateur
| Bande | Fréquence | Classe licence | Usage principal |
|-------|-----------|----------------|-----------------|
| 136 kHz | 135.7-137.8 kHz | Expérimental | Télégraphie lente |
| 160m | 1.810-1.850 MHz | Général | Phone/CW longue distance |
| 80m | 3.500-3.800 MHz | Général | Phone/CW |
| 60m | 5.351.5-5.366.5 MHz | Général | Phone/CW limité |
| 40m | 7.000-7.200 MHz | Général | Phone/CW mondiale |
| 30m | 10.100-10.150 MHz | Général | CW/Data |
| 20m | 14.000-14.350 MHz | Général | Phone/CW |
| 17m | 18.068-18.168 MHz | Général | Phone/CW |
| 15m | 21.000-21.450 MHz | Général | Phone/CW |
| 12m | 24.890-24.990 MHz | Général | Phone/CW |
| 10m | 28.000-29.700 MHz | Général | Phone/CW/TV |
| 6m | 50.000-52.000 MHz | Général | Phone/CW |
| 4m | 70.000-70.500 MHz | Général | Phone/CW |
| 2m | 144.000-146.000 MHz | Général | Phone/CW |
| 70cm | 430.000-440.000 MHz | Général | Phone/CW |
| 23cm | 1240.000-1300.000 MHz | Avancé | Data/Satellite |
| 13cm | 2320.000-2450.000 MHz | Avancé | Data |
| 9cm | 3400.000-3475.000 MHz | Avancé | Data |
| 6cm | 5650.000-5850.000 MHz | Avancé | Data |
| 3cm | 10.000-10.500 GHz | Avancé | Data |
| 1.2cm | 24.000-24.250 GHz | Avancé | Data |

### Aviation
| Service | Fréquence | Usage | Mode |
|---------|-----------|-------|------|
| VHF Air-Ground | 118.000-137.000 MHz | Communications vocales | AM |
| UHF Military | 225.000-400.000 MHz | Aviation militaire | AM |
| ADS-B | 1090 MHz | Surveillance automatique | Mode S |
| ACARS | 131.550 MHz | Données avion-sol | ASK |
| VOR | 108.000-118.000 MHz | Navigation | AM |
| ILS Localizer | 108.100-111.950 MHz | Atterrissage | AM |
| ILS Glide Path | 328.600-335.400 MHz | Atterrissage | AM |
| DME | 960-1215 MHz | Distance | Pulsé |

### Maritime
| Service | Fréquence | Usage | Mode |
|---------|-----------|-------|------|
| MF Maritime | 1605-4000 kHz | Communications longue distance | SSB |
| VHF Maritime | 156.000-162.050 MHz | Communications côtières | FM |
| AIS 1 | 161.975 MHz (87B) | Identification automatique | GMSK |
| AIS 2 | 162.025 MHz (88B) | Identification automatique | GMSK |
| DSC | 156.525 MHz | Appel de détresse | FSK |
| NAVTEX | 518 kHz | Messages météo/navigation | FSK |
| EPIRB | 406.025 MHz | Balise de détresse | ASK |

### Radiodiffusion
| Service | Bande | Fréquences | Modulation |
|---------|-------|------------|------------|
| LW (GO) | 148.5-283.5 kHz | Grandes ondes | AM |
| MW (OM) | 526.5-1606.5 kHz | Ondes moyennes | AM |
| SW | 3-30 MHz | Ondes courtes | AM/SSB |
| FM | 87.5-108 MHz | VHF | FM stéréo |
| DAB | 174-240 MHz | Band III | OFDM |
| TV VHF | 174-230 MHz | Bandes I-III | COFDM |
| TV UHF | 470-862 MHz | Bandes IV-V | COFDM |

### Télécommunications mobiles
| Standard | Bande | Fréquences (MHz) | Technologie |
|----------|-------|------------------|------------|
| GSM 900 | Primaire | 890-915 (UL), 935-960 (DL) | GMSK |
| GSM 1800 | DCS | 1710-1785 (UL), 1805-1880 (DL) | GMSK |
| UMTS 2100 | IMT-2000 | 1920-1980 (UL), 2110-2170 (DL) | WCDMA |
| LTE 800 | Digital Dividend | 791-821 (UL), 832-862 (DL) | OFDM |
| LTE 1800 | DCS | 1710-1785 (UL), 1805-1880 (DL) | OFDM |
| LTE 2600 | IMT-E | 2500-2570 (UL), 2620-2690 (DL) | OFDM |
| 5G 700 | Sub-700 | 703-748 (UL), 758-803 (DL) | OFDM |
| 5G 3500 | C-band | 3400-3800 (UL), 3400-3800 (DL) | OFDM |

## 🏭 Bandes ISM et IoT (libres d'usage)

### Europe (CEPT/ETSI)
| Fréquence | Bande | Puissance max | Usage principal | Modulation typique |
|-----------|-------|---------------|-----------------|-------------------|
| 6.765-6.795 MHz |  |  | RFID HF | ASK |
| 13.553-13.567 MHz |  |  | RFID HF, NFC | ASK |
| 26.957-27.283 MHz |  | 4 W | CB, LPD | AM/FM |
| 40.66-40.70 MHz |  |  | Télécommandes | ASK/FSK |
| 433.05-434.79 MHz |  | 10 mW ERP | IoT courte portée | FSK, LoRa |
| 868.00-868.60 MHz |  | 25 mW ERP | LPWAN, LoRa, SigFox | CSS, DBPSK |
| 2400.00-2483.50 MHz |  | 100 mW ERP | WiFi 2.4GHz, Bluetooth | OFDM, FHSS |
| 5725.00-5875.00 MHz |  | 25 mW ERP | LoRa, applications diverses | CSS |
| 24.00-24.25 GHz |  |  | Applications haute fréquence | Divers |

### États-Unis (FCC)
| Fréquence | Bande | Puissance max | Usage principal | Notes |
|-----------|-------|---------------|-----------------|-------|
| 6.765-6.795 MHz |  |  | RFID HF | ISM |
| 13.553-13.567 MHz |  |  | RFID HF, NFC | ISM |
| 26.957-27.283 MHz |  | 4 W | CB, LPD | Licensed by rule |
| 40.66-40.70 MHz |  |  | Télécommandes | ISM |
| 433.05-434.79 MHz |  | 1.5 W | IoT courte portée | ISM |
| 902-928 MHz |  | 4 W | LPWAN, LoRa, SigFox | ISM |
| 2400-2483.5 MHz |  | 1 W | WiFi, Bluetooth, Zigbee | UNII |
| 5725-5850 MHz |  | 1 W | Applications diverses | UNII |
| 24.00-24.25 GHz |  |  | Applications haute fréquence | ISM |
| 57-64 GHz |  |  | Communications mmWave | ISM |

### Asie (Région 3)
| Fréquence | Puissance max | Usage principal | Réglementation |
|-----------|---------------|-----------------|----------------|
| 315 MHz |  | Télécommandes | Variable par pays |
| 433 MHz | 10 mW | IoT | Harmonisé CEPT |
| 779-787 MHz |  | LTE-M, NB-IoT | Mobile |
| 920-925 MHz |  | LoRa, SigFox | Variable |
| 2.4 GHz | 100 mW | WiFi, Bluetooth | Mondiale |

### 🌐 Technologies IoT par bande

| Technologie | Bande | Portée | Débit | Avantages |
|-------------|-------|--------|-------|-----------|
| **LoRa** | 433/868/915 MHz | 2-20 km | 0.3-50 kbps | Ultra-longue portée |
| **SigFox** | 868/902 MHz | 10-50 km | 100-600 bps | Faible consommation |
| **NB-IoT** | 700-900 MHz | 10-50 km | 20-250 kbps | Réseaux cellulaires |
| **LTE-M** | 700-900 MHz | 5-20 km | 0.3-1 Mbps | Compatible LTE |
| **WiFi HaLow** | 900 MHz | 1 km | 150-300 kbps | Faible puissance |
| **Zigbee** | 2.4 GHz | 100m | 250 kbps | Maillage |
| **Bluetooth LE** | 2.4 GHz | 100m | 1 Mbps | Ultra basse consommation |

---

## 🚁 Drones et véhicules autonomes

### Europe (UE)
| Usage | Fréquence | Puissance max | Conditions |
|-------|-----------|---------------|------------|
| **Contrôle** | 2.4 GHz | 100 mW | Licence gratuite |
| **Vidéo** | 2.4/5.8 GHz | 25 mW | Licence gratuite |
| **Télémesure** | 433/868 MHz | 25 mW | Licence gratuite |
| **Navigation** | GPS L1/L2 | - | Ouvert |
| **Détection** | 24 GHz |  | Véhicules seulement |

### États-Unis (FCC)
| Usage | Fréquence | Puissance max | Classe |
|-------|-----------|---------------|--------|
| **Contrôle** | 2.4 GHz | 1 W | Part 15 |
| **Vidéo** | 2.4/5.8 GHz | 1 W | Part 15 |
| **Télémesure** | 900 MHz | 1 W | Part 15 |
| **Radar** | 24 GHz |  | Véhicules |
| **LiDAR** | 905 nm |  | Optique |

### Bandes dédiées drones (émergentes)
| Fréquence | Statut | Usage prévu |
|-----------|--------|-------------|
| 5850-5925 MHz | En discussion | Contrôle haute fiabilité |
| 5030-5091 MHz | Alloué USA | BVLOS (Beyond Visual Line of Sight) |
| 2700 MHz | En discussion | Corridors urbains |

---

## 📡 5G et réseaux mobiles avancés

### 5G NR (New Radio) - Bandes FR1 (< 6 GHz)
| Bande | Fréquence (MHz) | Usage | Région principale |
|-------|-----------------|-------|------------------|
| n1 | 1920-1980 (UL), 2110-2170 (DL) | Mobile legacy | Mondiale |
| n3 | 1710-1785 (UL), 1805-1880 (DL) | Mobile legacy | Mondiale |
| n7 | 2500-2570 (UL), 2620-2690 (DL) | Mobile legacy | Mondiale |
| n20 | 832-862 (UL), 791-821 (DL) | Digital Dividend | Europe |
| n28 | 703-748 (UL), 758-803 (DL) | APT 700 | Asie-Pacifique |
| n38 | 2570-2620 (UL/DL) | TDD partagé | Europe |
| n41 | 2496-2690 (UL/DL) | TDD | USA/Asie |
| n77 | 3300-4200 (UL/DL) | C-band | Mondiale |
| n78 | 3300-3800 (UL/DL) | C-band | Europe/USA |

### 5G NR - Bandes FR2 (mmWave)
| Bande | Fréquence (GHz) | Usage | Défi principal |
|-------|-----------------|-------|----------------|
| n257 | 26.5-29.5 | mmWave | Propagation |
| n258 | 24.25-27.5 | mmWave | Propagation |
| n259 | 39.5-43.5 | mmWave | Équipement |
| n260 | 37-40 | mmWave | Propagation |
| n261 | 27.5-28.35 | mmWave | Partage spectre |

### 6G - Bandes émergentes (prévisionnelles)
| Bande | Fréquence | Usage prévu | Technologie |
|-------|-----------|-------------|-------------|
| D-band | 130-175 GHz | Très haut débit | THz communications |
| H-band | 220-325 GHz | Imagerie, sensing | Ondes sub-mm |
| Spectrum sharing | 6-24 GHz | Partage dynamique | IA gestion spectre |
| Optical wireless | 300-400 THz | LiFi haute vitesse | Communications optiques |

---

## 🔬 Recherche scientifique et instrumentation

### Radioastronomie (protégée internationalement)
| Bande | Fréquence | Usage | Protection |
|-------|-----------|-------|------------|
| L-band | 1400-1427 MHz | Hydrogène neutre | Strictement protégée |
| S-band | 2.3-2.5 GHz | Recherche planétaire | Coordination requise |
| C-band | 4.5-7.0 GHz | Radioastronomie | Zones dédiées |
| X-band | 8.0-12.0 GHz | Exploration spatiale | Partage limité |
| K-band | 18-26.5 GHz | Recherche atmosphérique | Zones dédiées |

### Géophysique et environnement
| Application | Fréquence | Usage | Exemple |
|-------------|-----------|-------|---------|
| **Sismologie** | VLF/LF | Détection séismes | 10-30 kHz |
| **Ionosphère** | HF | Sondage ionosphérique | 2-30 MHz |
| **Océanographie** | HF/VHF | Radar surface | 3-30 MHz |
| **Climatologie** | MW/SW | Sondage atmosphérique | 1-30 GHz |
| **Volcanologie** | VLF | Détection éruptions | <30 kHz |

### Physique des particules
| Expérience | Fréquence | Usage |
|------------|-----------|-------|
| **Pierre Auger** | VHF | Détection rayons cosmiques |
| **LHC** | SHF | Communications accélérateurs |
| **ITER** | mmWave | Plasma fusion |

---

## 🛡️ Communications militaires et gouvernementales

### OTAN - Bandes communes
| Bande | Fréquence | Usage | Sécurité |
|-------|-----------|-------|----------|
| **A** | 225-400 MHz | Aviation tactique | Chiffré |
| **B** | 400-500 MHz | Communications terrestres | Chiffré |
| **C** | 500-1000 MHz | Commandement | Chiffré |
| **D** | 1000-2000 MHz | Liaisons données | Chiffré |
| **E** | 2000-3000 MHz | Surveillance | Chiffré |
| **F** | 3000-6000 MHz | Radar | Classifié |

### Fréquences stratégiques (exemples)
| Usage | Fréquence | Notes |
|-------|-----------|-------|
| **Sous-marins** | ELF (3-30 Hz) | Pénétration eau |
| **Stratégique** | VLF (3-30 kHz) | Commandement nucléaire |
| **Tactique** | HF (3-30 MHz) | Communications longue portée |
| **Anti-jamming** | EHF (30-300 GHz) | Haute résistance brouillage |

### Systèmes de guerre électronique
| Type | Fréquence | Fonction |
|------|-----------|----------|
| **COMINT** | Large spectre | Interception communications |
| **ELINT** | 1-40 GHz | Détection radar |
| **SIGINT** | Tout spectre | Renseignement signaux |
| **Jamming** | Adaptative | Brouillage intelligent |

---

## 🛰️ Communications spatiales et satellites

### Navigation GNSS étendu
| Système | Fréquence | Usage | Précision |
|---------|-----------|-------|-----------|
| **GPS L1C** | 1575.42 MHz | Civil ouvert | 5-10m |
| **GPS L2C** | 1227.60 MHz | Civil précis | 1-5m |
| **GPS L5** | 1176.45 MHz | Sécurité | <1m |
| **Galileo E1** | 1575.42 MHz | Haute précision | <1m |
| **Galileo E5** | 1191.795 MHz | Commercial | <1m |
| **GLONASS L1** | 1602 MHz | Navigation russe | 5-10m |
| **BeiDou B1C** | 1575.42 MHz | Navigation chinoise | 5-10m |
| **NavIC L5** | 1176.45 MHz | Navigation indienne | 5-10m |

### Satellites météorologiques avancés
| Satellite/Constellation | Fréquence | Usage | Résolution |
|------------------------|-----------|-------|------------|
| **NOAA POES** | 137 MHz | APT analogique | 4 km |
| **Meteor M2** | 137 MHz | LRPT numérique | 1 km |
| **FengYun** | 1700 MHz | HRIT Chine | 1 km |
| **Himawari** | 1691 MHz | HRIT Japon | 0.5 km |
| **GOES-R** | 1686 MHz | HRIT USA | 0.5 km |
| **Meteosat** | 1694 MHz | MSG Europe | 1 km |

### Communications par satellite
| Service | Fréquence | Usage | Couverture |
|---------|-----------|-------|------------|
| **Inmarsat STD-C** | 1.5-1.6 GHz | Maritime | Globale |
| **Inmarsat BGAN** | 1.5-1.6 GHz | Broadband | Globale |
| **Iridium** | 1616-1626 MHz | Téléphonie | Polaire |
| **Globalstar** | 1610-1626 MHz | Téléphonie | Globale sauf pôles |
| **Thuraya** | 1525-1661 MHz | Moyen-Orient | Régionale |
| **Starlink** | Ku/Ka-band | Internet | Globale progressive |

### Radioamateur satellite (OSCAR)
| Bande | Fréquence | Usage | Exemples satellites |
|-------|-----------|-------|-------------------|
| **15m** | 21.210 MHz | Uplink | AO-7, AO-73 |
| **10m** | 29.400-29.500 MHz | Uplink | AO-7, AO-73 |
| **2m** | 145.825-146.000 MHz | Downlink | ISS, nombreux cubesats |
| **70cm** | 435-438 MHz | Downlink | AO-73, cubesats |
| **23cm** | 1269-1274 MHz | Uplink | AO-40 (†) |
| **13cm** | 2400-2450 MHz | Uplink | AO-40 (†) |

---

## 📊 Outils de calcul et conversion

### Longueur d'onde et fréquence
```
λ(m) = c / f(Hz)    où c = 299 792 458 m/s

Exemples pratiques :
• 100 MHz → λ = 3.00 m
• 433 MHz → λ = 0.69 m
• 868 MHz → λ = 0.35 m
• 2.4 GHz → λ = 0.12 m
• 5.8 GHz → λ = 0.052 m
```

### Puissance et niveaux
```
dBm = 10 × log₁₀(P_mW)
dBW = 10 × log₁₀(P_W) = dBm - 30
W = 10^(dBm/10) / 1000

Exemples :
• 0 dBm = 1 mW = -30 dBW
• 10 dBm = 10 mW = -20 dBW
• 20 dBm = 100 mW = -10 dBW
• 30 dBm = 1 W = 0 dBW
```

### Atténuation en espace libre
```
L_fs(dB) = 32.4 + 20 log₁₀(d_km) + 20 log₁₀(f_MHz)

Exemples :
• 1 km à 433 MHz : 68.4 dB
• 10 km à 433 MHz : 88.4 dB
• 1 km à 2.4 GHz : 80.4 dB
• 10 km à 2.4 GHz : 100.4 dB
```

### Budget de liaison simplifié
```
P_rx = P_tx + G_tx + G_rx - L_path - L_misc

Où :
• P_tx : puissance émise (dBm)
• G_tx/rx : gains antennes (dBi)
• L_path : pertes propagation (dB)
• L_misc : pertes diverses (câbles, etc.)
```

### Rapport signal/bruit requis
| Modulation | SNR requis (dB) | Usage |
|------------|-----------------|-------|
| BPSK | 9.6 | Satellite, GPS |
| QPSK | 9.6 | Télévision numérique |
| 16-QAM | 14.5 | WiFi, câble |
| 64-QAM | 18.8 | DOCSIS |
| 256-QAM | 24.2 | 5G |

---

## ⚠️ Considérations réglementaires importantes

### Licences par pays (Europe)
| Pays | Autorité | Licence SDR | Particuliarités |
|------|----------|-------------|-----------------|
| **France** | ANFR/ARCEP | Classe expérimentale | 10mW ISM limité |
| **Allemagne** | BNetzA | Licence individuelle | Très stricte |
| **UK** | Ofcom | Licence légère | Flexible |
| **Italie** | MISE | Licence expérimentale | 25mW ISM |
| **Espagne** | MINETUR | Licence générale | Modérée |

### Restrictions communes
- **Aviation** : 108-137 MHz strictement protégé
- **Maritime** : 156-162 MHz usage professionnel uniquement
- **Urgences** : Bandes médicales et secours protégées
- **GNSS** : Réception seulement, pas d'émission

### Évolution réglementaire
- **5G** : Nouvelles bandes, partage dynamique
- **6G** : Bandes THz, régulation adaptative
- **IoT** : Simplification pour objets connectés
- **Amateur** : Bandes supplémentaires possibles

---

## 🔍 Fréquences intéressantes pour SDR

### Détection automatique (ADS-B, AIS, ACARS)
- **ADS-B** : 1090 MHz (avions)
- **AIS** : 162 MHz (navires)
- **ACARS** : 131.550 MHz (avions)
- **EPIRB** : 406 MHz (balises détresse)

### Météorologie (facile à recevoir)
- **NOAA APT** : 137 MHz (images satellites)
- **VOLMET** : 118-137 MHz (météo aviation)
- **NAVTEX** : 518 kHz (météo maritime)

### Radioamateur (avec licence)
- **2m** : 144-146 MHz (VHF)
- **70cm** : 430-440 MHz (UHF)
- **23cm** : 1240-1300 MHz (SHF)

### IoT et LPWAN
- **LoRa** : 868 MHz (Europe), 915 MHz (USA)
- **SigFox** : 868 MHz (Europe)
- **NB-IoT** : Bandes LTE (700-900 MHz)

### Recherche et expérimentation
- **VLF/LF** : <300 kHz (phénomènes naturels)
- **HF** : 3-30 MHz (propagation ionosphérique)
- **UHF/SHF** : >1 GHz (expérimental)

---

*Cette table des fréquences internationales enrichie constitue une référence complète pour les utilisateurs SDR. Elle couvre tous les aspects modernes des communications radio : IoT, 5G/6G, drones, satellites, recherche scientifique, et applications militaires. Vérifiez toujours la législation locale et les allocations UIT actuelles avant toute utilisation. Dernière mise à jour : 2025*
