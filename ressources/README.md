# Ressources SDR

Ce dossier contient des ressources complémentaires pour accompagner le livre "Comprendre le SDR".

## 📂 Structure

```
ressources/
├── exemples_code/           # Exemples de code pratiques
│   ├── python/             # Scripts Python (pyrtlsdr, numpy, etc.)
│   ├── matlab/             # Scripts MATLAB (avec Communications Toolbox)
│   ├── bash/               # Scripts d'automatisation
│   └── README.md           # Guide d'utilisation des exemples
├── schemas/                # Schémas et diagrammes ASCII
│   ├── architecture_sdr.txt    # Architecture générale SDR
│   └── modulations_numeriques.txt  # Comparaison des modulations
└── configs/                # Fichiers de configuration
    └── gnuradio_config.py  # Configuration GNU Radio recommandée
```

## 🚀 Démarrage rapide

### Installation des dépendances Python

```bash
# Installation des bibliothèques requises
pip install numpy scipy matplotlib pyrtlsdr pyModeS

# Pour MATLAB: installer Communications Toolbox
```

### Test des exemples

```bash
# Scanner FM
cd exemples_code/python
python scan_fm.py

# Capture ADS-B
python adsb_capture.py --duration 30
```

### Configuration GNU Radio

```bash
# Copier la configuration recommandée
cp ressources/configs/gnuradio_config.py ~/.gnuradio/config.conf
```

## 📋 Liste des exemples

### Python

#### `scan_fm.py`
- **Description**: Scanner automatique de stations FM
- **Dépendances**: numpy, matplotlib, pyrtlsdr
- **Utilisation**: `python scan_fm.py`
- **Sortie**: Liste des stations détectées + graphique

#### `adsb_capture.py`
- **Description**: Capture et décodage de signaux ADS-B
- **Dépendances**: numpy, pandas, pyrtlsdr, pyModeS
- **Utilisation**: `python adsb_capture.py --duration 60 --output avions.csv`
- **Sortie**: Fichier CSV avec positions des avions

### MATLAB

#### `fm_demodulation.m`
- **Description**: Démonstration modulation/démodulation FM
- **Prérequis**: MATLAB + Communications Toolbox
- **Contenu**: Génération, modulation, démodulation, analyse

### Bash

#### `sdr_setup.sh`
- **Description**: Script d'installation automatique SDR sous Linux
- **Options**: `--full`, `--minimal`, `--update`, `--test`
- **Fonction**: Installation GNU Radio, drivers, applications

## 📊 Schémas disponibles

### `architecture_sdr.txt`
Diagramme ASCII montrant l'architecture complète d'un SDR :
- Antenne → Front-end RF → ADC → Traitement numérique → Logiciel → Applications
- Flux réception et émission
- Composants clés

### `modulations_numeriques.txt`
Comparaison visuelle des modulations numériques :
- ASK, FSK, PSK, QAM, OFDM
- Signaux temporels, constellations
- Tableau comparatif avantages/inconvénients

## ⚙️ Configurations

### `gnuradio_config.py`
Configuration recommandée pour GNU Radio :
- Répertoires par défaut
- Options de performance
- Thèmes et raccourcis
- Paramètres de débogage

## 📚 Ressources externes recommandées

### Documentation officielle
- [GNU Radio Tutorials](https://wiki.gnuradio.org/index.php/Tutorials)
- [RTL-SDR Documentation](https://rtl-sdr.com/)
- [HackRF Documentation](https://hackrf.readthedocs.io/)

### Communautés
- [Reddit r/RTLSDR](https://www.reddit.com/r/RTLSDR/)
- [GNU Radio Mailing List](https://lists.gnu.org/mailman/listinfo/discuss-gnuradio)
- [Discord SDR](https://discord.gg/gnuradio)

### Outils complémentaires
- [Inspectrum](https://github.com/miek/inspectrum) : Analyse spectrale avancée
- [Baudline](http://www.baudline.com/) : Analyse temps-fréquence
- [SigDigger](https://batchdrake.github.io/SigDigger/) : Analyseur universel

## 🔧 Dépannage

### Erreur "Module not found"
```bash
# Vérifier l'installation
pip list | grep pyrtlsdr

# Réinstaller si nécessaire
pip uninstall pyrtlsdr
pip install pyrtlsdr
```

### SDR non détecté
```bash
# Linux: vérifier les permissions
lsusb  # Voir si le SDR est détecté
sudo usermod -a -G plugdev $USER
# Redémarrer la session
```

### MATLAB: Toolbox manquante
- Dans MATLAB: Home → Add-ons → Get Add-ons
- Rechercher "Communications Toolbox"
- Installer et activer

## 📝 Contribution

Les ressources sont extensibles. Suggestions d'améliorations :

### Nouveaux exemples
- Scripts pour d'autres modulations (QPSK, OFDM)
- Applications spécifiques (AIS, NOAA, radio numérique)
- Interfaces graphiques (Tkinter, PyQt)

### Nouveaux schémas
- Architecture d'un récepteur superhétérodyne
- Chaîne de traitement DSP
- Diagrammes de constellations

### Nouvelles configurations
- Profils pour différents SDR (LimeSDR, USRP)
- Paramètres optimisés pour usage spécifique

## 📄 Licence

Tous les exemples et ressources sont sous licence MIT, sauf mention contraire.

---

*Ces ressources complètent le livre et fournissent des outils pratiques pour l'apprentissage du SDR.*
