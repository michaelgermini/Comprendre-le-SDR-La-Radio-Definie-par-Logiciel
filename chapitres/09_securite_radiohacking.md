# Chapitre 9 : Sécurité & Radiohacking

## 9.1 Introduction au radiohacking éthique

### Définition du radiohacking

Le radiohacking désigne l'ensemble des techniques permettant d'analyser, comprendre et interagir avec des systèmes de communication radio, dans un contexte éthique et légal.

#### Aspects positifs
- **Sécurité offensive** : Test de vulnérabilités
- **Recherche** : Compréhension des protocoles
- **Éducation** : Apprentissage des communications
- **Défense** : Protection contre les attaques

#### Démarche éthique
- **Consentement** : Ne tester que ses propres systèmes
- **Légalité** : Respect strict de la réglementation
- **Responsabilité** : Ne pas nuire aux autres
- **Transparence** : Partage des connaissances

### Cadre légal international

#### États-Unis (FCC)
- **Communications légales** : Analyse de ses propres signaux
- **Interdiction** : Décryptage de communications chiffrées
- **Exception** : Recherche approuvée par la FCC

#### Union Européenne
- **Directive RED** : Équipements conformes uniquement
- **Réglementation nationale** : Licence obligatoire pour analyse
- **RGPD** : Protection des données personnelles

#### France (ARCEP)
- **Licence expérimentale** : Classe B pour tests
- **Brouillage interdit** : Même pour test
- **Déclaration** : Matériel professionnel

### Bonnes pratiques éthiques

#### Code de conduite
1. **Ne pas interférer** : Écouter uniquement
2. **Signaler les vulnérabilités** : De manière responsable
3. **Éduquer** : Partager les connaissances
4. **Respecter la vie privée** : Pas d'écoute indiscrète

#### Outils de conformité
- **Filtrage géographique** : Limiter aux signaux locaux
- **Masquage** : Protection des informations sensibles
- **Journalisation** : Traçabilité des actions

## 9.2 Sniffer une télécommande 433 MHz

### Protocoles de télécommandes

Les télécommandes 433 MHz utilisent généralement des protocoles simples et non chiffrés.

#### Types courants
- **Fixe** : Code toujours identique
- **Rolling code** : Code change à chaque transmission
- **Manchester** : Codage temporel
- **OOK/ASK** : Modulation d'amplitude

### Analyse avec Universal Radio Hacker (URH)

#### Capture du signal

##### Configuration
```bash
# Lancement URH
urh

# Configuration de la source
- Device: RTL-SDR
- Frequency: 433.92 MHz (bande ISM)
- Sample Rate: 1 MHz
- Gain: 30 dB
```

##### Capture
1. **Enregistrement** : Appuyer sur la télécommande pendant la capture
2. **Visualisation** : Observer la forme du signal
3. **Nettoyage** : Supprimer le bruit

#### Analyse du protocole

##### Identification de la modulation
- **OOK** : Présence/absence de signal
- **ASK** : Variation d'amplitude
- **FSK** : Variation de fréquence

##### Détection du codage
```python
# Analyse automatique URH
# 1. Click "Interpret" -> "Auto detect modulation"
# 2. Sélectionner le type détecté
# 3. Ajuster les paramètres
```

##### Extraction des bits
- **Seuillage** : Conversion analogique → numérique
- **Manchester decoding** : Si applicable
- **Validation** : Vérifier la répétabilité

### Reproduction du signal

#### Avec URH
```python
# Après analyse
# 1. Sélectionner "Analysis" -> "Bitstring"
# 2. Copier la séquence de bits
# 3. "Replay" -> "Send signal"
# 4. Ajuster la puissance et la fréquence
```

#### Test de fonctionnement
- **Distance** : Tester à différentes portées
- **Angle** : Vérifier l'orientation
- **Interférences** : En présence d'autres signaux

### Applications légitimes

#### Domotique personnelle
- **Test de sécurité** : Vérification de ses propres appareils
- **Dépannage** : Diagnostic de pannes
- **Amélioration** : Développement de nouvelles fonctionnalités

#### Éducation
- **Compréhension** : Apprentissage des protocoles simples
- **Formation** : Enseignement des modulations de base
- **Projets étudiants** : Réalisation de systèmes IoT

## 9.3 Décryptage de protocoles propriétaires

### Analyse de protocoles inconnus

#### Méthodologie systématique

##### Étape 1 : Capture
- **Multiples transmissions** : Différentes commandes
- **Conditions variables** : Distance, orientation, environnement
- **Haute qualité** : SNR élevé, faible bruit

##### Étape 2 : Analyse temporelle
- **Durée des impulsions** : Mesure précise
- **Périodes** : Identification des patterns
- **Répétitions** : Nombre de retransmissions

##### Étape 3 : Analyse fréquentielle
- **Largeur de bande** : Détermination de la modulation
- **Fréquences utilisées** : Porteuse et déviation
- **Pureté spectrale** : Recherche d'harmoniques

##### Étape 4 : Démodulation
```python
# Exemple de démodulation OOK
def demodulate_ook(signal, threshold):
    # Seuillage
    binary = (np.abs(signal) > threshold).astype(int)

    # Suppression des répétitions
    # (logique de déduplication)

    return binary

# Application
demodulated = demodulate_ook(captured_signal, adaptive_threshold)
```

### Techniques de décryptage

#### Analyse statistique
- **Fréquence des bits** : Recherche de patterns
- **Entropie** : Mesure du caractère aléatoire
- **Corrélations** : Détection de redondances

#### Attaque par clair connu
- **Connaissance partielle** : Si quelques bits sont connus
- **Test de toutes les clés** : Pour clés courtes
- **Analyse différentielle** : Comparaison de transmissions

#### Exemple concret : Protocole PT2262
```python
# Décodage PT2262 (télécommandes courantes)
def decode_pt2262(bitstream):
    # Synchronisation
    sync_pattern = [1,1,1,1,0,0,0,0] * 2

    # Recherche du préambule
    preamble_pos = find_pattern(bitstream, sync_pattern)

    if preamble_pos is not None:
        # Extraction des données
        data_start = preamble_pos + len(sync_pattern)
        data_bits = bitstream[data_start:data_start+24]  # 24 bits typiques

        # Conversion adresse/données
        address = data_bits[:16]  # 16 bits adresse
        data = data_bits[16:]     # 8 bits données

        return address, data
    return None, None
```

### Outils avancés

#### GNU Radio pour analyse
```python
# Flowgraph d'analyse personnalisée
# 1. Source SDR
# 2. Filtre passe-bande
# 3. Démodulateur adapté
# 4. Analyse statistique
# 5. Visualisation
```

#### Scripts Python spécialisés
```python
import numpy as np
from scipy import signal

def analyze_protocol(signal, fs):
    # Analyse spectrale
    freqs, psd = signal.welch(signal, fs, nperseg=1024)

    # Détection de modulation
    modulation = detect_modulation(psd, freqs)

    # Analyse temporelle
    peaks, _ = signal.find_peaks(np.abs(signal), height=0.5)

    # Calcul des intervalles
    intervals = np.diff(peaks) / fs * 1e6  # en µs

    return {
        'modulation': modulation,
        'bit_rate': estimate_bitrate(intervals),
        'protocol_type': classify_protocol(intervals)
    }
```

### Limites éthiques et légales

#### Propriété intellectuelle
- **Brevets** : Respect des droits
- **Logiciels propriétaires** : Pas de rétro-ingénierie commerciale
- **Standards ouverts** : Préférence aux protocoles documentés

#### Sécurité des systèmes
- **Ne pas compromettre** : Éviter les attaques sur des systèmes critiques
- **Signalement responsable** : Contacter les fabricants pour les vulnérabilités
- **Confidentialité** : Protection des données interceptées

## 9.4 Attaques par relecture (replay attack)

### Principe de l'attaque

Une attaque par relecture consiste à enregistrer une transmission légitime puis la retransmettre pour reproduire l'action originale.

#### Scénario typique
1. **Capture** : Enregistrement du signal de télécommande
2. **Stockage** : Sauvegarde du signal numérique
3. **Rejeu** : Retransmission à l'identique

### Implémentation technique

#### Capture et stockage
```python
# Avec GNU Radio ou URH
def capture_signal(filename, duration=1.0):
    # Configuration SDR
    sdr = RtlSdr()
    sdr.center_freq = 433.92e6
    sdr.sample_rate = 1e6
    sdr.gain = 40

    # Capture
    samples = sdr.read_samples(int(duration * sdr.sample_rate))

    # Sauvegarde
    np.save(filename, samples)

    sdr.close()
    return samples

# Utilisation
capture_signal('garage_door.npy', 2.0)
```

#### Retransmission
```python
# Avec HackRF
def replay_signal(filename, frequency=433.92e6, gain=30):
    # Chargement
    samples = np.load(filename)

    # Configuration HackRF
    # (Utilisation de GNU Radio flowgraph ou osmocom)

    # Transmission
    # osmosdr_sink -> samples -> fréquence cible
```

#### Améliorations
- **Timing précis** : Synchronisation temporelle
- **Correction de fréquence** : Adaptation à la dérive
- **Amplification** : Puissance suffisante

### Contre-mesures

#### Protocoles rolling code
- **Code changeant** : Nouvel identifiant à chaque transmission
- **Synchronisation** : État partagé entre émetteur/récepteur
- **Fenêtre temporelle** : Expiration des codes

#### Exemple : Keeloq
```python
# Simulation simplifiée Keeloq
def keeloq_encrypt(data, key, counter):
    # Fonction de hachage non-linéaire
    def nlfsr_step(state):
        bit = (state[0] ^ state[16] ^ state[19] ^ state[21] ^ state[23])
        return (state[1:] + [bit], bit)

    # Chiffrement
    encrypted = 0
    for i in range(32):
        state, bit = nlfsr_step(key)
        key = state
        encrypted |= bit << i

    return encrypted ^ data ^ counter
```

#### Authentification forte
- **Chiffrement symétrique** : AES, 3DES
- **Challenge-response** : Défis aléatoires
- **Certificats** : Authentification publique

### Applications éthiques

#### Test de sécurité
- **Audit de ses systèmes** : Vérification des vulnérabilités
- **Formation** : Démonstration des risques
- **Recherche** : Développement de meilleures sécurités

#### Dépannage
- **Capture d'urgence** : Sauvegarde de codes importants
- **Test de redondance** : Vérification des backups
- **Diagnostic** : Analyse de pannes

## 9.5 Limites éthiques et légales (exemples concrets)

### Cas d'école : IoT non sécurisé

#### Scénario
Un système domotique utilise des télécommandes 433 MHz non chiffrées pour contrôler l'ouverture des portes.

#### Analyse éthique
- **Vulnérabilité évidente** : Signaux non protégés
- **Impact potentiel** : Accès physique non autorisé
- **Responsabilité** : Fabricant vs utilisateur

#### Réponse appropriée
1. **Notification privée** : Contacter le fabricant
2. **Documentation** : Publier l'analyse (sans exploitation)
3. **Solutions alternatives** : Recommander des produits sécurisés

### Exemple : Radio amateur

#### Contexte
Interception de communications radioamateur en morse ou voix.

#### Aspects légaux
- **Légal en France** : Communications radioamateur publiques
- **Interdiction** : Enregistrement sans consentement
- **Exception** : Usage éducatif ou de recherche

#### Considérations éthiques
- **Respect de la vie privée** : Même si public, intimité
- **Non-interférence** : Ne pas perturber les communications
- **Usage éducatif** : Apprentissage des techniques

### Cas concret : ADS-B

#### Situation
Capture de données ADS-B pour tracking aérien.

#### Aspects positifs
- **Sécurité aérienne** : Amélioration de la surveillance
- **Transparence** : Données publiques par nature
- **Recherche** : Études de trafic

#### Risques potentiels
- **Vie privée** : Suivi individuel d'avions privés
- **Sécurité** : Localisation de personnalités
- **Abus** : Utilisation malveillante des données

### Réseaux de téléphonie mobile

#### GSM non chiffré
- **A5/0** : Chiffrement nul dans certains pays
- **Interception légale** : Autorisée sous conditions
- **Éthique** : Respect de la vie privée absolue

#### Actions recommandées
- **Ne pas intercepter** : Même si techniquement possible
- **Sensibilisation** : Promouvoir le chiffrement
- **Recherche académique** : Sur des signaux simulés

### Protocoles militaires

#### Interdiction absolue
- **Sécurité nationale** : Communications classifiées
- **Risques juridiques** : Sanctions sévères
- **Éthique** : Non-interférence avec la défense

#### Recherche autorisée
- **Signaux ouverts** : Bandes non-classifiées
- **Collaboration** : Avec autorités compétentes
- **Simulation** : Modèles mathématiques sans interception réelle

### Bonnes pratiques de conformité

#### Documentation
- **Journal d'activité** : Enregistrement des analyses
- **Justification** : Raison de chaque capture
- **Conservation limitée** : Suppression après usage

#### Transparence
- **Licence visible** : Affichage de numéro de licence
- **Publication responsable** : Partage sans exploitation
- **Communauté** : Discussion dans forums appropriés

#### Développement personnel
- **Formation continue** : Mise à jour des connaissances légales
- **Certification** : Obtention de qualifications reconnues
- **Réseau** : Contacts avec professionnels éthiques

### Recommandations finales

#### Pour débutants
1. **Commencer légalement** : Obtenir les licences nécessaires
2. **Tester sur soi** : Ses propres systèmes uniquement
3. **Apprendre l'éthique** : Comprendre les implications
4. **Rejoindre une communauté** : Échange avec professionnels

#### Pour chercheurs
1. **Publier éthiquement** : Sans compromettre la sécurité
2. **Collaborer** : Avec industriels et régulateurs
3. **Éduquer** : Former la nouvelle génération
4. **Innover** : Développer des solutions sécurisées

#### Pour professionnels
1. **Conformité stricte** : Respect de toutes les réglementations
2. **Audit régulier** : Vérification des pratiques
3. **Formation équipe** : Sensibilisation continue
4. **Contribution société** : Amélioration globale de la sécurité

Le radiohacking éthique est un domaine passionnant qui contribue à améliorer la sécurité globale des systèmes de communication, à condition de rester dans un cadre strictement légal et responsable.
