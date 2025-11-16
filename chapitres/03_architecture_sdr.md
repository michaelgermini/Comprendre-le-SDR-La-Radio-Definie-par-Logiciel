# Chapitre 3 : Architecture d'un SDR

## 3.1 Les différents blocs d'un récepteur traditionnel

### Architecture d'un récepteur superhétérodyne

Le récepteur radio traditionnel utilise une architecture superhétérodyne depuis les années 1920.

#### Étages principaux

1. **Antenne** : Capture le signal radio
2. **Filtre d'entrée** : Sélection préliminaire des fréquences
3. **Étage RF (Radio Frequency)** : Amplification et filtrage haute fréquence
4. **Méilleur (Mixer)** : Translation en fréquence intermédiaire
5. **Filtre IF (Intermediate Frequency)** : Sélection du canal
6. **Détecteur** : Extraction du signal audio/vidéo
7. **Étage AF (Audio Frequency)** : Amplification audio

#### Oscillator local

L'oscillateur local génère une fréquence fixe ou variable :
- **Oscillateur à quartz** pour stabilité
- **Synthétiseur de fréquence** pour agilité
- **VCO (Voltage Controlled Oscillator)** pour modulation FM

### Limites de l'architecture traditionnelle

#### Complexité matérielle
- Multiples étages analogiques
- Composants spécialisés pour chaque bande
- Difficulté d'intégration

#### Rigidité
- Fréquences fixes
- Modulation fixe par récepteur
- Mise à jour matérielle coûteuse

#### Performances limitées
- Dérives thermiques
- Tolérances de composants
- Bruit et distorsions cumulés

## 3.2 Passage à une radio définie par logiciel

### Révolution conceptuelle

Le SDR remplace les composants analogiques spécialisés par des processeurs programmables.

#### Évolution des architectures

1. **SDR hybride** : Mélange analogique/numérique
2. **SDR direct** : Conversion directe analogique-numérique
3. **SDR full-software** : Tout en numérique

### Avantages de l'approche logicielle

#### Flexibilité
- Reprogrammation instantanée
- Adaptation aux nouveaux standards
- Personnalisation selon usage

#### Performance
- Précision numérique
- Algorithmes avancés
- Correction d'erreurs en temps réel

#### Évolutivité
- Mises à jour logicielles
- Ajout de fonctionnalités
- Intégration de nouveaux protocoles

## 3.3 Le rôle du convertisseur analogique/numérique (ADC)

### Fonctionnement de l'ADC

L'ADC transforme un signal analogique continu en signal numérique discret.

#### Paramètres clés

- **Résolution** : Nombre de bits (8, 12, 14, 16 bits typiques)
- **Fréquence d'échantillonnage** : f_s ≥ 2 × f_max (théorème de Nyquist)
- ** Bande passante** : Fréquence maximale convertible
- **Rapport signal/bruit (SNR)** : Qualité de conversion

### Types d'ADC pour SDR

#### ADC flash
- Très rapide
- Haute consommation
- Utilisé dans les SDR haute performance

#### ADC pipeline
- Bon compromis vitesse/précision
- Utilisé dans les SDR grand public

#### ADC sigma-delta
- Haute résolution
- Bonne linéarité
- Utilisé pour applications audio

### Considérations pratiques

#### Échantillonnage en quadrature
- Capture I (In-phase) et Q (Quadrature)
- Préservation de la phase
- Reconstruction complète du signal

#### Calibration
- Correction des erreurs de gain
- Compensation des non-linéarités
- Calibration automatique

## 3.4 Filtrage numérique et DSP

### Traitement numérique du signal (DSP)

Le DSP applique des algorithmes mathématiques aux signaux numérisés.

#### Opérations de base

- **Filtrage** : Suppression des fréquences indésirables
- **Mixage** : Changement de fréquence
- **Amplification** : Ajustement des niveaux
- **Modulation/Démodulation** : Encodage/décodage des données

### Types de filtres numériques

#### Filtres FIR (Finite Impulse Response)
- Réponse impulsionnelle finie
- Phase linéaire
- Stabilité garantie

#### Filtres IIR (Infinite Impulse Response)
- Réponse impulsionnelle infinie
- Plus efficaces
- Risque d'instabilité

### Architecture DSP moderne

#### Processeurs dédiés
- DSP Texas Instruments
- FPGA Xilinx/Altera
- GPU pour calculs parallèles

#### Chaîne de traitement SDR

1. **Correction IQ** : Équilibrage des voies I/Q
2. **Filtrage passe-bas** : Limitation de bande
3. **Décimation** : Réduction du taux d'échantillonnage
4. **Mixage numérique** : Translation en fréquence
5. **Filtrage canal** : Sélection du signal désiré
6. **Démodulation** : Extraction des données

## 3.5 Montée et descente en fréquence (mixers logiciels)

### Principe du mixage

Le mixage combine deux signaux pour produire des fréquences somme et différence.

#### Mixage analogique traditionnel
```
Signal RF × Oscillateur local = (f_RF + f_LO) + (f_RF - f_LO)
```

#### Mixage numérique
Utilisation de la multiplication complexe :
```
z[n] = x[n] × e^(j2πf_LO n / f_s)
```

### Implémentation logicielle

#### Mixer numérique direct
- Multiplication par sinus/cosinus
- Calcul intensif
- Précision parfaite

#### Mixer par cordic
- Algorithme efficace
- Calcul de rotations
- Utilisé dans les FPGA

### Applications du mixage en SDR

#### Réception
- Translation du signal RF vers fréquence base
- Sélection de canaux spécifiques
- Analyse spectrale

#### Émission
- Translation du signal base vers fréquence RF
- Génération de signaux modulés
- Synthèse de fréquences

### Considérations de performance

#### Fréquence d'échantillonnage
- Doit respecter le théorème de Nyquist
- f_s ≥ 2 × (f_signal + bande/2)

#### Précision numérique
- Quantization noise
- Overflow handling
- Rounding errors

#### Temps réel
- Latence minimale
- Débit de calcul suffisant
- Optimisation des algorithmes
