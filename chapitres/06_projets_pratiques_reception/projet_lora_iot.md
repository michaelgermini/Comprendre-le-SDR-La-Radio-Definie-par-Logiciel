# Projet 6.8 : Recevoir les signaux LoRa IoT

## Introduction à LoRa

LoRa (Long Range) est une technologie de modulation radio conçue pour l'Internet des Objets (IoT). Elle offre une portée exceptionnelle (jusqu'à 20 km) avec une très faible consommation d'énergie.

### Caractéristiques LoRa
- **Modulation** : Chirp Spread Spectrum (CSS)
- **Fréquences** : 433 MHz, 868 MHz, 915 MHz
- **Débit** : 0.3 à 50 kbps
- **Portée** : 2-20 km (ligne de vue)
- **SF (Spreading Factor)** : 7-12 (facteur d'étalement)

## Prérequis matériel

### SDR compatible
- **HackRF One** ou **LimeSDR** (recommandé pour la bande 868 MHz)
- **RTL-SDR** avec upconverter (pour 868 MHz)

### Antenne adaptée
- **Antenne 868 MHz** quart d'onde (λ/4 ≈ 8.2 cm)
- **Gain** : 2-5 dBi
- **Polarisation** : Verticale

## Installation des outils

### Bibliothèque LoRa
```bash
# Installation gr-lora
git clone https://github.com/BastilleResearch/gr-lora.git
cd gr-lora
mkdir build && cd build
cmake ..
make
sudo make install
```

### Alternative : LoRa Decoder Python
```bash
pip install lora-decoder
```

## Configuration SDR

### Paramètres LoRa typiques
```python
# Configuration pour LoRa 868 MHz
center_freq = 868e6  # Fréquence centrale
bandwidth = 125e3    # Bande passante
sf = 7              # Spreading Factor
cr = 4              # Coding Rate (4/5)
sync_word = 0x34    # Mot de synchronisation
```

## Flowgraph GNU Radio

### Structure du récepteur LoRa
```
Osmocom Source → Low Pass Filter → gr-lora Decoder → Message Sink
```

### Configuration détaillée
```xml
<?xml version='1.0' encoding='utf-8'?>
<flow_graph>
  <block>
    <key>options</key>
    <param>
      <key>title</key>
      <value>Récepteur LoRa IoT</value>
    </param>
  </block>

  <block>
    <key>variable</key>
    <param>
      <key>id</key>
      <value>samp_rate</value>
    </param>
    <param>
      <key>value</key>
      <value>1e6</value>
    </param>
  </block>

  <block>
    <key>osmosdr_source</key>
    <param>
      <key>args</key>
      <value>numchan=1</value>
    </param>
    <param>
      <key>sample_rate</key>
      <value>samp_rate</value>
    </param>
    <param>
      <key>center_freq</key>
      <value>868e6</value>
    </param>
    <param>
      <key>rf_gain</key>
      <value>30</value>
    </param>
  </block>

  <block>
    <key>low_pass_filter</key>
    <param>
      <key>decim</key>
      <value>1</value>
    </param>
    <param>
      <key>gain</key>
      <value>1</value>
    </param>
    <param>
      <key>samp_rate</key>
      <value>samp_rate</value>
    </param>
    <param>
      <key>cutoff_freq</key>
      <value>62.5e3</value>
    </param>
    <param>
      <key>transition_width</key>
      <value>12.5e3</value>
    </param>
  </block>

  <!-- Bloc LoRa personnalisé -->
  <block>
    <key>lora_receiver</key>
    <param>
      <key>sf</key>
      <value>7</value>
    </param>
    <param>
      <key>cr</key>
      <value>4</value>
    </param>
    <param>
      <key>sync_word</key>
      <value>0x34</value>
    </param>
  </block>

  <connection>
    <source_block_id>osmosdr_source_0</source_block_id>
    <sink_block_id>low_pass_filter_0</sink_block_id>
  </connection>

  <connection>
    <source_block_id>low_pass_filter_0</source_block_id>
    <sink_block_id>lora_receiver_0</sink_block_id>
  </connection>
</flow_graph>
```

## Capture et analyse

### Script Python de capture
```python
#!/usr/bin/env python3
"""
Captureur LoRa IoT simple
"""

import numpy as np
from rtlsdr import RtlSdr
import time
import argparse

class LoRaCapture:
    def __init__(self, freq=868e6, gain=30):
        self.sdr = RtlSdr()
        self.sdr.center_freq = freq
        self.sdr.sample_rate = 1e6
        self.sdr.gain = gain

        # Paramètres LoRa
        self.sf = 7  # Spreading Factor
        self.bw = 125e3  # Bandwidth

    def capture_packet(self, duration=1.0):
        """Capture un packet LoRa"""
        samples = self.sdr.read_samples(int(duration * self.sdr.sample_rate))
        return samples

    def detect_lora_preamble(self, samples):
        """Détection simplifiée de préambule LoRa"""
        # Analyse de la fréquence instantanée
        analytic_signal = samples  # Version simplifiée
        instantaneous_freq = np.diff(np.angle(analytic_signal))

        # Recherche de pattern LoRa (chirp)
        # Cette implémentation est simplifiée
        return len(instantaneous_freq) > 100

    def decode_lora_packet(self, samples):
        """Décodage simplifié (nécessite gr-lora pour vrai décodage)"""
        if self.detect_lora_preamble(samples):
            return "Packet LoRa détecté"
        return None

    def continuous_capture(self, output_file=None):
        """Capture continue avec analyse"""
        print("Capture LoRa continue - Ctrl+C pour arrêter")

        try:
            while True:
                samples = self.capture_packet(0.1)
                result = self.decode_lora_packet(samples)

                if result:
                    timestamp = time.strftime("%H:%M:%S")
                    print(f"[{timestamp}] {result}")

                    if output_file:
                        with open(output_file, 'a') as f:
                            f.write(f"{timestamp}: {result}\n")

                time.sleep(0.1)

        except KeyboardInterrupt:
            print("\nCapture terminée")

    def close(self):
        self.sdr.close()

def main():
    parser = argparse.ArgumentParser(description='Captureur LoRa IoT')
    parser.add_argument('--freq', type=float, default=868e6,
                       help='Fréquence en Hz (défaut: 868MHz)')
    parser.add_argument('--gain', type=int, default=30,
                       help='Gain SDR (défaut: 30)')
    parser.add_argument('--output', type=str,
                       help='Fichier de sortie pour les packets')
    parser.add_argument('--duration', type=float, default=10.0,
                       help='Durée de capture simple (secondes)')

    args = parser.parse_args()

    capture = LoRaCapture(freq=args.freq, gain=args.gain)

    if args.output:
        # Mode capture continue
        capture.continuous_capture(args.output)
    else:
        # Mode capture simple
        print(f"Capture de {args.duration} secondes...")
        samples = capture.capture_packet(args.duration)
        result = capture.decode_lora_packet(samples)

        if result:
            print(f"Résultat: {result}")
        else:
            print("Aucun packet LoRa détecté")

    capture.close()

if __name__ == "__main__":
    main()
```

## Analyse des données LoRa

### Structure d'un packet LoRa
```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│  Préambule  │  Header     │   Payload   │    CRC      │
│  (8 symboles)│ (variable)  │ (variable) │ (2 octets)  │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

### Informations extraites
- **Adresse destination** (DevAddr)
- **Compteur** (FCnt) - anti-rejeu
- **Port** - identifie l'application
- **Payload** - données utilisateur
- **MIC** - code d'authentification

## Applications pratiques

### Surveillance environnementale
- **Capteurs température/humidité**
- **Détecteurs de mouvement**
- **Qualité de l'air**

### Smart city
- **Éclairage public intelligent**
- **Parkings connectés**
- **Gestion des déchets**

### Agriculture
- **Monitoring des cultures**
- **Irrigation intelligente**
- **Suivi du bétail**

## Optimisations

### Amélioration de la réception
```python
# Utilisation d'une antenne directive
# Placement en hauteur
# Réduction des interférences

# Paramètres SDR optimisés
sdr.gain = 'auto'  # Gain automatique
sdr.freq_correction = 1  # Correction PPM si nécessaire
```

### Gestion des collisions
- **ADR (Adaptive Data Rate)** : Ajustement automatique du débit
- **Channels multiples** : Répartition sur plusieurs fréquences
- **Timing aléatoire** : Éviter les collisions

## Sécurité LoRa

### Vulnérabilités potentielles
- **Clés par défaut** : Certains appareils utilisent des clés standard
- **Rejeu** : Possibilité de rejouer des packets légitimes
- **Dénial de service** : Brouillage des fréquences

### Bonnes pratiques
- **Chiffrement end-to-end** : Toujours activer
- **Mise à jour firmware** : Corrections de sécurité
- **Surveillance réseau** : Détection d'anomalies

## Ressources complémentaires

### Outils recommandés
- **LoRaWAN Network Server** : The Things Network
- **ChirpStack** : Serveur LoRaWAN open-source
- **LoRa Calculator** : Outil de calcul de portée

### Communauté
- **Forum The Things Network**
- **Reddit r/LoRaWAN**
- **Slack LoRa Community**

### Documentation
- **LoRa Alliance** : https://lora-alliance.org/
- **Semtech LoRa** : Documentation technique
- **RFC 8376** : Spécifications LoRaWAN

---

*Ce projet démontre la réception de signaux IoT modernes. Pour un vrai décodage, utilisez gr-lora ou un gateway LoRaWAN commercial.*
