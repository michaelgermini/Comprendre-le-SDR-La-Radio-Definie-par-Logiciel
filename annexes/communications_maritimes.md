# ⚓ Annexe : Communications Maritimes MF/VHF

## Introduction aux Communications Maritimes

Les communications maritimes sont essentielles à la sécurité et à l'efficacité de la navigation mondiale. Elles utilisent principalement deux bandes : MF (Moyenne Fréquence) et VHF (Très Haute Fréquence), chacune adaptée à des usages spécifiques.

### Importance stratégique
- **Sécurité** : Sauvetage, urgences, coordination
- **Navigation** : Informations météo, trafic maritime
- **Commerce** : Coordination logistique portuaire
- **Pêche** : Gestion des zones de pêche
- **Tourisme** : Communications plaisance

---

## 📻 Bande MF Maritime (1605-4000 kHz)

### Caractéristiques techniques
| Paramètre | Valeur | Explication |
|-----------|--------|-------------|
| **Fréquence** | 1605-4000 kHz | Bande marine internationale |
| **Longueur d'onde** | 187-75 mètres | Propagation par onde de sol/ciel |
| **Modulation** | SSB (Single Side Band) | Économie spectrale, longue portée |
| **Largeur de bande** | 3 kHz par canal | Bande étroite pour SSB |
| **Puissance** | 100-1000 W | Forte puissance pour longue portée |

### Canaux MF standardisés

#### Canaux de détresse et sécurité
| Canal | Fréquence | Usage | Portée |
|-------|-----------|-------|--------|
| **2182 kHz** | 2182.0 kHz | Détresse internationale | Globale |
| **2174.5 kHz** | 2174.5 kHz | Appel de détresse | 500-1000 km |
| **2187.5 kHz** | 2187.5 kHz | Sécurité maritime | Régionale |

#### Canaux de travail
| Canal | Fréquence | Usage | Région |
|-------|-----------|-------|--------|
| **2003 kHz** | 2003.0 kHz | Navigation nord-atlantique | Atlantique Nord |
| **2045 kHz** | 2045.0 kHz | Navigation pacifique | Pacifique |
| **2065 kHz** | 2065.0 kHz | Navigation indien | Océan Indien |
| **2183 kHz** | 2183.0 kHz | Trafic commercial | Internationale |
| **2191 kHz** | 2191.0 kHz | Coordination portuaire | Côtière |

### Propagation MF
- **Onde de sol** : 0-50 km, fiable, peu d'atténuation
- **Onde de ciel** : 50-2000 km, réflexion ionosphère
- **Portée** : Jusqu'à 3000 km de jour, plus la nuit
- **Fiabilité** : Bonne, moins affectée que VHF par le temps

### Équipements MF
- **Transceiver SSB** : Icom M700Pro, Sailor RT2048
- **Antenne** : Fil long (15-25m), verticale ou inclinée
- **Alimentation** : 12/24V DC, forte consommation
- **Prix** : 2000-5000€ pour équipement professionnel

---

## 📡 Bande VHF Maritime (156.000-162.050 MHz)

### Caractéristiques techniques
| Paramètre | Valeur | Explication |
|-----------|--------|-------------|
| **Fréquence** | 156.000-162.050 MHz | Bande marine VHF |
| **Longueur d'onde** | 1.92-1.86 mètres | Propagation en visibilité |
| **Modulation** | FM (Frequency Modulation) | Qualité audio, simplex |
| **Largeur de bande** | 25 kHz par canal | Canaux étroits |
| **Puissance** | 1-25 W | Puissance adaptée à la portée |

### Canaux VHF standardisés

#### Canaux d'urgence et sécurité
| Canal | Fréquence | Usage | Priorité |
|-------|-----------|-------|----------|
| **16** | 156.800 MHz | Appel de détresse | **MAXIMUM** |
| **70** | 156.525 MHz | Appel de détresse numérique (DSC) | **MAXIMUM** |
| **06** | 156.300 MHz | Communications de secours | Haute |

#### Canaux de navigation et trafic
| Canal | Fréquence | Usage | Type |
|-------|-----------|-------|------|
| **08** | 156.400 MHz | Navigation nord-atlantique | International |
| **10** | 156.500 MHz | Navigation | International |
| **12** | 156.600 MHz | Navigation pacifique | International |
| **14** | 156.700 MHz | Navigation | International |
| **72** | 156.625 MHz | Navigation | International |

#### Canaux portuaires et locaux
| Canal | Fréquence | Usage | Exemple |
|-------|-----------|-------|---------|
| **01** | 156.050 MHz | Trafic portuaire | Rotterdam, Anvers |
| **02** | 156.100 MHz | Trafic portuaire | Hambourg, Brême |
| **03** | 156.150 MHz | Trafic portuaire | Londres, Southampton |
| **04** | 156.200 MHz | Trafic portuaire | Marseille, Barcelone |
| **05** | 156.250 MHz | Trafic portuaire | Dunkerque, Calais |

#### Canaux plaisance et pêche
| Canal | Fréquence | Usage | Région |
|-------|-----------|-------|---------|
| **09** | 156.450 MHz | Communications plaisance | Internationale |
| **17** | 156.850 MHz | Communications plaisance | Internationale |
| **19** | 156.950 MHz | Communications plaisance | Internationale |
| **22** | 157.100 MHz | Communications plaisance | Internationale |
| **23** | 157.150 MHz | Communications plaisance | Internationale |

### Propagation VHF
- **Ligne de vue** : Portée 20-50 km depuis hauteur d'antenne
- **Influence météo** : Pluie, brouillard réduisent la portée
- **Réflexion** : Sur l'eau, peut étendre légèrement la portée
- **Interférences** : Moins affectée par l'activité solaire que MF

### Équipements VHF
- **Transceiver fixe** : Icom IC-M510, Standard Horizon GX2100
- **Transceiver portable** : Icom IC-M93D, Yaesu FTA550
- **Antenne** : Quart d'onde (λ/4 ≈ 16cm) verticale
- **Prix** : 200-1000€ pour équipements marins certifiés

---

## 🔧 Réception avec SDR

### Configuration SDR pour MF Maritime

#### Matériel requis
- **SDR** : RTL-SDR v3 ou équivalent (couverture <30 MHz)
- **Antenne** : Fil long (10-20m) ou antenne active MF
- **Filtre** : Passe-bas <4 MHz pour éviter aliasing
- **Amplificateur** : Préampli MF faible bruit (optionnel)

#### Configuration GNU Radio
```python
# Paramètres MF Maritime
mf_config = {
    'center_freq': 2182e3,  # 2182 kHz
    'sample_rate': 12e3,    # 12 kHz (supérieur à 2x bande)
    'bandwidth': 3e3,       # 3 kHz par canal
    'modulation': 'SSB',    # Single Side Band
    'gain': 40,             # Gain élevé pour signaux faibles
}
```

#### Flowgraph typique
```
RTL-SDR Source → Low Pass Filter → SSB Demodulator → Audio Sink
```

### Configuration SDR pour VHF Maritime

#### Matériel requis
- **SDR** : RTL-SDR ou HackRF (couverture VHF)
- **Antenne** : Antenne VHF marine (λ/4 verticale)
- **Filtre** : Passe-bande 156-162 MHz
- **Préampli** : LNA VHF (optionnel)

#### Configuration GNU Radio
```python
# Paramètres VHF Maritime
vhf_config = {
    'center_freq': 156.8e6,  # 156.8 MHz (canal 16)
    'sample_rate': 2e6,      # 2 MHz
    'bandwidth': 25e3,       # 25 kHz par canal
    'modulation': 'FM',      # Narrow FM
    'gain': 30,              # Gain adapté
}
```

#### Flowgraph typique
```
RTL-SDR Source → Band Pass Filter → FM Demodulator → Audio Sink
```

---

## 📡 Protocoles et Signaux

### DSC (Digital Selective Calling)
- **Fréquence** : 156.525 MHz (VHF), 2187.5 kHz (MF)
- **Modulation** : FSK (VHF), SSB (MF)
- **Usage** : Appel automatique de détresse
- **Format** : Messages numériques structurés

### NAVTEX (Navigational Text)
- **Fréquence** : 518 kHz (international)
- **Modulation** : FSK 100 bauds
- **Usage** : Messages météo et navigation
- **Portée** : 200-400 km

### AIS (Automatic Identification System)
- **Fréquence** : 161.975/162.025 MHz
- **Modulation** : GMSK
- **Usage** : Identification et suivi des navires
- **Portée** : 20-50 km

---

## 🆘 Procédures d'urgence

### Signal de détresse MF/VHF
- **Voix** : "MAYDAY MAYDAY MAYDAY"
- **Canal** : 16 VHF (156.8 MHz)
- **DSC** : Code automatique d'urgence
- **EPIRB** : Balise de localisation 406 MHz

### Coordination des secours
- **MRCC** : Maritime Rescue Coordination Centre
- **RCC** : Rescue Coordination Centre
- **SAR** : Search And Rescue operations
- **Procedures** : Défines par l'IMO (International Maritime Organization)

---

## 📊 Applications Pratiques pour SDRistes

### Surveillance maritime
- **Trafic commercial** : Suivi des mouvements portuaires
- **Pêche illégale** : Détection activités suspectes
- **Sécurité** : Monitoring des appels de détresse
- **Navigation** : Apprentissage procédures maritimes

### Recherche et éducation
- **Propagation** : Étude des ondes MF/VHF
- **Météo** : Réception bulletins NAVTEX
- **Techniques** : Apprentissage modulation SSB/FM
- **Réseaux** : Exploration protocoles maritimes

### Projets SDR spécifiques

#### Récepteur NAVTEX
```python
# Configuration NAVTEX 518 kHz
navtex_config = {
    'frequency': 518e3,
    'modulation': 'FSK',
    'baudrate': 100,
    'shift': 170,  # Hz
    'filter': 'narrow',  # 300 Hz bandwidth
}
```

#### Décodeur DSC
```python
# Configuration DSC VHF
dsc_config = {
    'frequency': 156.525e6,
    'modulation': 'FSK',
    'symbol_rate': 1200,  # bauds
    'format': 'DSC',      # Digital Selective Calling
}
```

---

## ⚖️ Réglementations Maritimes

### Organisations internationales
- **IMO** : International Maritime Organization
- **ITU** : Union Internationale des Télécommunications
- **IHO** : International Hydrographic Organization

### Certificats requis
- **SRC** : Short Range Certificate (VHF obligatoire)
- **LRC** : Long Range Certificate (MF/SSB)
- **GMDSS** : Global Maritime Distress Safety System
- **ROC** : Radio Operator's Certificate

### Règles d'usage
- **Licence** : Obligatoire pour émission
- **Canal 16** : Écoute permanente sur VHF
- **Puissance** : Limitée selon taille du navire
- **Maintenance** : Contrôles périodiques obligatoires

---

## 🛠️ Équipements et Coûts

### Pour récepteur SDR maritime
| Composant | Prix approximatif | Usage |
|-----------|-------------------|-------|
| **RTL-SDR v3** | 25€ | Réception VHF |
| **Antenne VHF marine** | 30€ | Canal 16 et trafic |
| **Antenne MF longue** | 50€ | Réception MF longue distance |
| **Préampli VHF** | 25€ | Amélioration sensibilité |
| **Logiciel SDR** | Gratuit | GNU Radio, SDR++ |

### Stations complètes
| Type | Prix | Usage |
|------|------|-------|
| **VHF portable marin** | 200-400€ | Plaisance, petit commerce |
| **VHF fixe marin** | 400-800€ | Navigation commerciale |
| **MF/SSB marin** | 1000-3000€ | Navigation hauturière |
| **GMDSS complet** | 5000-15000€ | Navires commerciaux |

---

## 🌊 Cas d'usage avancés

### Recherche océanographique
- **Balises** : Suivi courants marins
- **Bouées** : Mesures météorologiques
- **Sous-marins** : Communications ELF/VLF
- **Gliders** : Véhicules autonomes

### Environnement marin
- **Pollution** : Détection déversements
- **Sauvetage** : Coordination opérations SAR
- **Pêche** : Gestion zones protégées
- **Tourisme** : Sécurité plaisance

### Défense et sécurité
- **Garde-côtes** : Surveillance maritime
- **Douanes** : Contrôle frontières maritimes
- **Police** : Lutte contre trafic
- **Militaire** : Communications tactiques

---

## 🔗 Ressources et Communautés

### Associations maritimes
- **SSB Net** : Réseau quotidien MF
- **Maritime Mobile Service** : Service officiel
- **Cruising Club** : Communauté plaisance

### Logiciels spécialisés
- **YADD (Yet Another DSC Decoder)** : Décodage DSC
- **NAVTEX decoder** : Logiciel NAVTEX
- **AIS dispatcher** : Suivi trafic maritime

### Forums SDR maritimes
- **Reddit r/RTLSDR** : Projets maritimes
- **BoatUS** : Communauté navigation USA
- **RYA** : Royal Yachting Association UK

---

## 📚 Références Techniques

### Standards IMO
- **SOLAS** : Safety of Life at Sea
- **GMDSS** : Global Maritime Distress System
- **ITU-R M.1084** : Caractéristiques stations VHF
- **ITU-R M.493** : Caractéristiques stations MF

### Publications
- **IALA Guidelines** : Aides navigation
- **USCG Communications** : Manuel garde-côtes
- **Radio Navigational Aids** : Publication Admiralty

---

## 🎯 Recommandations pour SDRistes

### Débutants
1. Commencer par VHF canal 16 (facile à recevoir)
2. Acquérir antenne VHF marine appropriée
3. Écouter procédures de sécurité
4. Participer à des exercices radio

### Intermédiaires
1. Explorer MF maritime (2182 kHz)
2. Développer décodeur NAVTEX
3. Étudier protocoles DSC
4. Participer à réseaux SSB

### Avancés
1. Créer station SDR complète
2. Développer logiciels décodage
3. Contribuer à projets open-source
4. Collaborer avec communautés maritimes

---

*Cette annexe couvre les aspects essentiels des communications maritimes pour utilisateurs SDR. Respectez toujours les réglementations internationales et locales.*

**⚓ Sécurité en mer avant tout !** 🛟🚢
