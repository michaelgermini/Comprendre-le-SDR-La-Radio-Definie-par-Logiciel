# Sommaire complet - Comprendre le SDR

## 📖 Table des matières détaillée

### Chapitre 1 : Introduction au SDR
- 1.1 Qu'est-ce que le SDR ?
- 1.2 Brève histoire de la radio jusqu'au SDR
- 1.3 Les avantages de la radio définie par logiciel
- 1.4 Les principaux cas d'usage du SDR aujourd'hui

### Chapitre 2 : Fondamentaux des ondes radio
- 2.1 Les bases de l'électromagnétisme
- 2.2 Spectre radio : bandes, fréquences, allocations
- 2.3 Modulation : AM, FM, PM
- 2.4 Modulations numériques : FSK, PSK, QAM, OFDM
- 2.5 Antennes : principes essentiels

### Chapitre 3 : Architecture d'un SDR
- 3.1 Les différents blocs d'un récepteur traditionnel
- 3.2 Passage à une radio définie par logiciel
- 3.3 Le rôle du convertisseur analogique/numérique (ADC)
- 3.4 Filtrage numérique et DSP
- 3.5 Montée et descente en fréquence (mixers logiciels)

### Chapitre 4 : Le matériel SDR
- 4.1 RTL-SDR : le SDR low-cost
- 4.2 HackRF One : émission/réception
- 4.3 LimeSDR : précision et MIMO
- 4.4 USRP : le standard professionnel
- 4.5 Comparatif complet des plateformes
- 4.6 Accessoires : antennes, LNAs, filtres, pré-amplis, câbles

### Chapitre 5 : Logiciels pour SDR
- 5.1 SDR++
- 5.2 GQRX
- 5.3 GNU Radio (flowgraphs)
- 5.4 CubicSDR
- 5.5 Universal Radio Hacker
- 5.6 OpenWebRX
- 5.7 Logiciels spécialisés (ADS-B, AIS, NOAA…)

### Chapitre 6 : Projets pratiques - Réception
- 6.1 Écouter la FM avec RTL-SDR
- 6.2 Scanner les fréquences locales
- 6.3 Suivre les avions : ADS-B (1090 MHz)
- 6.4 Suivre les navires : AIS (162 MHz)
- 6.5 Recevoir les satellites météo NOAA
- 6.6 Décoder les radios amateurs APRS
- 6.7 Sniffer des signaux inconnus (URH)

### Chapitre 7 : Projets pratiques - Émission (légale uniquement)
- 7.1 Premiers pas en émission avec HackRF/LimeSDR
- 7.2 Générer un signal FM
- 7.3 Comprendre la puissance, émission, atténuateurs
- 7.4 Transmettre un signal numérique simple
- 7.5 Créer un réseau radio local expérimental
- 7.6 Précautions légales et limites

### Chapitre 8 : DSP (Traitement numérique du signal)
- 8.1 Échantillonnage et fréquence de Nyquist
- 8.2 Filtres (FIR, IIR)
- 8.3 FFT et analyse spectrale
- 8.4 Décodage des modulations numériques
- 8.5 Corrélation et synchronisation
- 8.6 Analyse d'un signal bruité

### Chapitre 9 : Sécurité & Radiohacking
- 9.1 Introduction au radiohacking éthique
- 9.2 Sniffer une télécommande 433 MHz
- 9.3 Décryptage de protocoles propriétaires
- 9.4 Attaques par relecture (replay attack)
- 9.5 Limites éthiques et légales (exemples concrets)

### Chapitre 10 : SDR et l'avenir des communications
- 10.1 Radio cognitive
- 10.2 5G / 6G et réseaux dynamiques
- 10.3 Satellites et constellations SDR
- 10.4 SDR dans l'aéronautique et la défense
- 10.5 Vers une radio totalement virtuelle

### Chapitre 11 : Annexes
- 11.1 Glossaire complet
- 11.2 Table des fréquences internationales
- 11.3 Matériel conseillé selon budget
- 11.4 Flows GNU Radio prêts à l'emploi
- 11.5 Ressources & communautés SDR

## 📂 Structure des fichiers

```
📘 Livre SDR/
├── README.md                          # Présentation générale
├── SOMMAIRE.md                        # Ce fichier
├── chapitres/                         # Chapitres principaux
│   ├── 01_introduction_sdr.md
│   ├── 02_fondamentaux_ondes_radio.md
│   ├── 03_architecture_sdr.md
│   ├── 04_materiel_sdr.md
│   ├── 05_logiciels_sdr.md
│   ├── 06_projets_pratiques_reception.md
│   ├── 07_projets_pratiques_emission.md
│   ├── 08_dsp_traitement_numerique_signal.md
│   ├── 09_securite_radiohacking.md
│   ├── 10_sdr_avenir_communications.md
│   └── 11_annexes.md
├── annexes/                           # Ressources supplémentaires (futur)
└── ressources/                        # Images, schémas, exemples (futur)
```

## 📊 Statistiques du livre

- **11 chapitres** principaux
- **49 sous-chapitres** détaillés
- **Environ 15 000 mots** de contenu technique
- **Couverture complète** : théorie, pratique, projets, sécurité
- **Langue** : Français technique
- **Style** : Pédagogique et scientifique

## 🎯 Public cible

- **Débutants** : Chapitres 1-2, projets simples
- **Intermédiaires** : Chapitres 3-5, projets avancés
- **Avancés** : Chapitres 6-8, DSP, sécurité
- **Experts** : Chapitres 9-10, recherche, avenir

## 🔧 Prérequis recommandés

### Connaissances
- Électronique de base
- Programmation (Python recommandé)
- Mathématiques (algèbre, analyse)

### Matériel minimum
- Ordinateur avec USB
- RTL-SDR (20-30€)
- Antenne adaptée

## 📚 Utilisation du livre

### Lecture linéaire
1. Commencer par l'introduction (chapitre 1)
2. Acquérir les bases théoriques (chapitres 2-3)
3. Choisir son matériel (chapitre 4)
4. Installer les logiciels (chapitre 5)
5. Pratiquer avec les projets (chapitres 6-7)
6. Approfondir DSP (chapitre 8)
7. Explorer sécurité (chapitre 9)
8. Découvrir l'avenir (chapitre 10)
9. Consulter les annexes au besoin

### Lecture thématique
- **Pratique uniquement** : Chapitres 6-7 + annexes
- **Théorie uniquement** : Chapitres 1-3 + 8
- **Sécurité** : Chapitres 9 + annexes légales
- **Matériel** : Chapitres 4 + 11.3

## 🤝 Contribution

Ce livre est un travail évolutif. Contributions bienvenues :

- **Corrections** : Fautes, erreurs techniques
- **Améliorations** : Clarté, exemples supplémentaires
- **Mises à jour** : Nouveaux matériels, standards
- **Traductions** : Versions dans d'autres langues

## 📄 Licence

Creative Commons BY-SA 4.0

- **BY** : Attribution obligatoire
- **SA** : Partage dans les mêmes conditions
- **4.0** : Version internationale récente

## 🙏 Remerciements

- Communauté RTL-SDR et GNU Radio
- Auteurs des outils open-source
- Radioamateurs et chercheurs
- Lecteurs et contributeurs

---

*Ce sommaire sera mis à jour avec l'évolution du livre. Dernière mise à jour : Novembre 2025*
