# Glossaire complet - SDR et Radio

## A

**ADC (Analog-to-Digital Converter)** : Convertisseur analogique-numérique. Transforme un signal analogique continu en signal numérique discret avec une résolution de 8 à 24 bits et des fréquences d'échantillonnage de quelques kHz à plusieurs GHz.

**ADS-B (Automatic Dependent Surveillance-Broadcast)** : Système de surveillance automatique des avions qui diffuse en temps réel la position, l'altitude, la vitesse et l'identité des aéronefs sur 1090 MHz.

**AF (Audio Frequency)** : Fréquences audio comprises entre 20 Hz et 20 kHz, bande audible par l'oreille humaine.

**AGC (Automatic Gain Control)** : Contrôle automatique de gain. Système qui ajuste automatiquement l'amplification d'un signal pour maintenir un niveau constant.

**AIS (Automatic Identification System)** : Système d'identification automatique des navires qui transmet des informations de navigation sur les fréquences 161.975 MHz et 162.025 MHz.

**Alias** : Artefact qui apparaît quand la fréquence d'échantillonnage est inférieure au double de la fréquence maximale du signal (violation du théorème de Nyquist).

**AM (Amplitude Modulation)** : Modulation d'amplitude. La porteuse varie en amplitude selon le signal modulant.

**Antenne isotrope** : Antenne théorique parfaite rayonnant également dans toutes les directions (référence pour mesurer le gain des antennes réelles).

**APRS (Automatic Packet Reporting System)** : Système de communication numérique des radioamateurs utilisant des paquets AX.25 sur 144.39 MHz.

**ASK (Amplitude Shift Keying)** : Modulation par déplacement d'amplitude. L'amplitude de la porteuse change entre deux niveaux selon le bit transmis.

**Atténuateur** : Composant qui réduit intentionnellement la puissance d'un signal RF (exprimé en dB : -10 dB, -20 dB, etc.).

**AWGN (Additive White Gaussian Noise)** : Bruit blanc gaussien additif. Modèle de bruit le plus couramment utilisé en communications.

## B

**Bande passante (Bandwidth)** : Gamme de fréquences qu'un système peut traiter efficacement. Pour un filtre, largeur entre les fréquences de coupure à -3 dB.

**BER (Bit Error Rate)** : Taux d'erreur binaire. Probabilité qu'un bit reçu soit différent du bit transmis. Exprimé en pourcentage ou en puissance de 10.

**BPF (Band Pass Filter)** : Filtre passe-bande. Laisse passer une bande de fréquences spécifique tout en atténuant les fréquences en dehors de cette bande.

**BPSK (Binary Phase Shift Keying)** : Modulation par déplacement de phase binaire. La phase change de 0° ou 180° selon le bit (équivalent à DBPSK différentiel).

## C

**Carrier** : Porteuse. Signal haute fréquence (par exemple 100 MHz) modulé pour transporter l'information.

**CB (Citizens Band)** : Bande citoyenne. Bande radio publique autour de 27 MHz utilisée pour les communications de loisir.

**CW (Continuous Wave)** : Onde continue. Modulation utilisée en morse (télégraphie) où seule la présence/absence du signal compte.

**Cyclic prefix** : Préfixe cyclique. Extension ajoutée aux symboles OFDM pour combattre l'écho multipath (généralement 1/4 de la longueur du symbole utile).

## D

**DAC (Digital-to-Analog Converter)** : Convertisseur numérique-analogique. Transforme un signal numérique discret en signal analogique continu.

**dB (Decibel)** : Unité logarithmique pour exprimer les rapports de puissance ou d'amplitude :
- Puissance : dB = 10 × log₁₀(P₁/P₂)
- Amplitude : dB = 20 × log₁₀(A₁/A₂)

**dBm** : Décibels par rapport à 1 milliwatt. Unité de puissance absolue couramment utilisée en RF :
- 0 dBm = 1 mW
- 10 dBm = 10 mW
- 20 dBm = 100 mW
- 30 dBm = 1 W

**Demodulation** : Processus inverse de la modulation. Extraction du signal original de la porteuse modulée.

**Doppler effect** : Effet Doppler. Changement de fréquence observé quand l'émetteur et le récepteur sont en mouvement relatif : f' = f × (v ± v₀)/(v ∓ vₛ)

**DSP (Digital Signal Processing)** : Traitement numérique du signal. Ensemble des techniques mathématiques et algorithmiques appliquées aux signaux numérisés.

**DVB-T (Digital Video Broadcasting - Terrestrial)** : Télévision numérique terrestre utilisant la modulation COFDM dans les bandes UHF.

## E

**EIRP (Effective Isotropic Radiated Power)** : Puissance isotrope rayonnée effective. Puissance qu'une antenne isotrope devrait rayonner pour produire la même densité de puissance dans la direction principale.

**ERP (Effective Radiated Power)** : Puissance rayonnée effective. Puissance isotrope équivalente dans la direction de rayonnement maximal.

**Échantillonnage (Sampling)** : Conversion d'un signal continu en signal discret par prélèvement de valeurs à intervalles réguliers.

## F

**FCC (Federal Communications Commission)** : Autorité de régulation américaine des télécommunications et des fréquences radio.

**FFT (Fast Fourier Transform)** : Transformée de Fourier rapide. Algorithme efficace (O(N log N)) pour calculer la DFT d'un signal de N échantillons.

**FIR (Finite Impulse Response)** : Réponse impulsionnelle finie. Type de filtre numérique dont la réponse s'annule après un nombre fini d'échantillons.

**FM (Frequency Modulation)** : Modulation de fréquence. La fréquence de la porteuse varie selon l'amplitude du signal modulant.

**FPGA (Field Programmable Gate Array)** : Circuit programmable par l'utilisateur contenant des blocs logiques configurables et des DSP intégrés.

**FSK (Frequency Shift Keying)** : Modulation par déplacement de fréquence. La fréquence change entre deux valeurs selon le bit transmis.

**FWHM (Full Width at Half Maximum)** : Largeur à mi-hauteur. Mesure de la largeur d'une fonction (par exemple, largeur d'un lobe spectral).

## G

**Gain** : Amplification d'un signal :
- En dB pour les amplificateurs
- En dBi pour les antennes (par rapport à une antenne isotrope)
- En dBd pour les antennes (par rapport à un dipôle)

**GMSK (Gaussian Minimum Shift Keying)** : Modulation GMSK utilisée dans GSM. Version lissée de MSK pour réduire la largeur de bande occupée.

**GNSS (Global Navigation Satellite System)** : Système global de navigation par satellite (GPS, GLONASS, Galileo, BeiDou).

**GPS (Global Positioning System)** : Système de positionnement global américain utilisant 24 satellites et les fréquences L1 (1575.42 MHz) et L2 (1227.60 MHz).

**GSM (Global System for Mobile communications)** : Standard de téléphonie mobile 2G utilisant la modulation GMSK.

## H

**HackRF** : Plateforme SDR open-source émission/réception couvrant de 1 MHz à 6 GHz avec 20 MHz de bande passante instantanée.

**HF (High Frequency)** : Hautes fréquences, 3-30 MHz. Bandes utilisées pour les communications longue distance par réflexion ionosphérique.

**HPF (High Pass Filter)** : Filtre passe-haut. Atténue les basses fréquences tout en laissant passer les hautes fréquences.

## I

**I/Q (In-phase/Quadrature)** : Composantes en phase et en quadrature d'un signal complexe. Permettent de représenter complètement un signal modulé.

**IF (Intermediate Frequency)** : Fréquence intermédiaire. Fréquence sur laquelle le signal est translaté pour faciliter le traitement (généralement 10.7 MHz pour la FM).

**IIR (Infinite Impulse Response)** : Réponse impulsionnelle infinie. Type de filtre récursif dont la réponse peut théoriquement durer indéfiniment.

**IP3 (Third Order Intercept Point)** : Point d'interception du 3e ordre. Mesure de la linéarité d'un amplificateur (plus IP3 est élevé, meilleure est la linéarité).

**ISM (Industrial, Scientific and Medical)** : Bandes réservées aux applications industrielles, scientifiques et médicales (ex : 433 MHz, 2.4 GHz, 5.8 GHz).

## J

**Jamming** : Brouillage intentionnel d'un signal radio. Technique utilisée en guerre électronique pour perturber les communications adverses.

## K

**K-factor** : Facteur K. Mesure de la propagation en visibilité directe. Plus K est élevé, meilleures sont les conditions de propagation.

## L

**LNA (Low Noise Amplifier)** : Amplificateur basse bruit. Amplificateur RF optimisé pour ajouter le minimum de bruit au signal (NF < 1 dB idéalement).

**LO (Local Oscillator)** : Oscillateur local. Génère la fréquence de référence pour les mélangeurs (upconversion/downconversion).

**LPF (Low Pass Filter)** : Filtre passe-bas. Laisse passer les basses fréquences tout en atténuant les hautes fréquences.

**LTE (Long Term Evolution)** : Standard de téléphonie mobile 4G utilisant OFDM et MIMO.

## M

**MIMO (Multiple Input Multiple Output)** : Entrées/sorties multiples. Technique utilisant plusieurs antennes pour améliorer la capacité et la fiabilité.

**Mixer** : Mélangeur. Composant qui combine deux signaux pour produire des fréquences somme et différence.

**Modulation** : Processus de modification d'une porteuse haute fréquence selon le signal d'information à transmettre.

**Morse code** : Code utilisant des impulsions courtes (points = ·) et longues (traits = —) pour représenter les lettres.

## N

**NF (Noise Figure)** : Figure de bruit. Mesure de la dégradation du rapport S/N introduite par un composant :
NF = 10 × log₁₀(T_système / T₀) où T₀ = 290 K

**NOAA** : Administration nationale américaine océanique et atmosphérique. Exploite des satellites météorologiques transmettant sur 137 MHz.

**Nyquist theorem** : Théorème de Nyquist-Shannon. Pour échantillonner un signal limité en bande à B Hz, la fréquence d'échantillonnage doit être ≥ 2B.

## O

**OFDM (Orthogonal Frequency Division Multiplexing)** : Multiplexage par répartition orthogonale de fréquence. Divise le canal en multiples sous-porteuses orthogonales.

**OOK (On-Off Keying)** : Allumage/extinction. Modulation la plus simple où le signal est présent (1) ou absent (0).

**OOK (On-Off Keying)** : Modulation d'amplitude binaire (présence/absence de porteuse).

**OOK (On-Off Keying)** : Technique de modulation où l'amplitude varie entre zéro et un niveau maximum.

## P

**Phase noise** : Bruit de phase. Variation aléatoire de la phase d'un oscillateur, visible comme un élargissement des raies spectrales.

**PLL (Phase Locked Loop)** : Boucle à verrouillage de phase. Système qui synchronise un oscillateur sur une référence de fréquence.

**PM (Phase Modulation)** : Modulation de phase. La phase de la porteuse varie selon l'amplitude du signal modulant.

**Polarisation** : Orientation du champ électrique d'une onde électromagnétique (linéaire verticale/horizontale, circulaire droite/gauche).

**Preamp** : Préamplificateur. Amplificateur placé en entrée d'un système pour améliorer la sensibilité.

**PSK (Phase Shift Keying)** : Modulation par déplacement de phase. La phase change selon les symboles transmis.

**PSD (Power Spectral Density)** : Densité spectrale de puissance. Représentation de la distribution de puissance en fonction de la fréquence.

## Q

**QAM (Quadrature Amplitude Modulation)** : Modulation d'amplitude en quadrature. Combine modulation d'amplitude et de phase.

**QPSK (Quadrature Phase Shift Keying)** : Modulation PSK quadratique. 4 symboles (2 bits) avec phases 0°, 90°, 180°, 270°.

## R

**RF (Radio Frequency)** : Fréquences radio. Généralement 3 kHz à 300 GHz.

**RSSI (Received Signal Strength Indicator)** : Indicateur de force du signal reçu. Mesure la puissance du signal en dBm ou dBμV.

**RTL-SDR** : SDR basé sur le tuner RTL2832U, populaire et abordable, couvrant 24 MHz à 1.7 GHz avec 8 bits de résolution.

## S

**Sampling rate** : Fréquence d'échantillonnage. Nombre d'échantillons par seconde (exprimé en Hz ou échantillons/seconde).

**SDR (Software Defined Radio)** : Radio définie par logiciel. Système où la majorité des fonctions de traitement du signal sont réalisées par logiciel.

**SFDR (Spurious Free Dynamic Range)** : Plage dynamique sans produits parasites. Mesure de la pureté spectrale d'un ADC ou DAC.

**S/N (Signal-to-Noise ratio)** : Rapport signal/bruit. Rapport entre la puissance du signal utile et la puissance du bruit.

**SNR (Signal-to-Noise Ratio)** : Rapport signal sur bruit. Mesure de la qualité d'un signal :
SNR = 10 × log₁₀(P_signal / P_bruit)

**Spectrum analyzer** : Analyseur de spectre. Instrument qui affiche la distribution fréquentielle de la puissance d'un signal.

**SSB (Single Side Band)** : Bande latérale unique. Modulation qui ne transmet qu'une seule bande latérale pour économiser la bande passante.

**Superhétérodyne** : Architecture de récepteur utilisant plusieurs étages de mélange pour translater le signal RF vers une fréquence intermédiaire fixe.

## T

**TDMA (Time Division Multiple Access)** : Accès multiple par répartition dans le temps. Technique de partage du canal par slots temporels.

**THD (Total Harmonic Distortion)** : Distorsion harmonique totale. Mesure de la quantité de distorsion introduite par un système non-linéaire.

## U

**UHF (Ultra High Frequency)** : Ultra hautes fréquences, 300 MHz - 3 GHz.

**USRP (Universal Software Radio Peripheral)** : Plateforme SDR professionnelle d'Ettus Research, offrant haute performance et modularité.

## V

**VHF (Very High Frequency)** : Très hautes fréquences, 30-300 MHz.

**VSWR (Voltage Standing Wave Ratio)** : Rapport d'onde stationnaire. Mesure de l'adaptation d'impédance :
VSWR = (1 + |Γ|) / (1 - |Γ|) où Γ est le coefficient de réflexion

## W

**Waterfall** : Représentation temporelle du spectre. Affichage où chaque ligne horizontale représente le spectre à un instant donné.

**WFM (Wide FM)** : FM large bande utilisée pour la radio broadcast (déviation de ±75 kHz).

**WiFi** : Famille de protocoles de communication sans fil utilisant les bandes 2.4 GHz et 5 GHz.

## X

**X-tal** : Abréviation de crystal (cristal). Désigne un oscillateur à quartz pour sa stabilité fréquentielle.

## Z

**Z (Impédance)** : Impédance. Opposition d'un circuit aux courants alternatifs, exprimée en ohms complexes.

---

*Ce glossaire couvre les termes essentiels du SDR et des communications radio. Il est organisé alphabétiquement pour faciliter la recherche.*
