# Chapitre 7 : Projets pratiques – Émission (légale uniquement)

## 7.1 Premiers pas en émission avec HackRF/LimeSDR

### ⚠️ Rappel légal important

**L'émission radio est strictement réglementée dans tous les pays.** Avant toute émission :

1. **Obtenir une licence radioamateur** appropriée
2. **Respecter les bandes de fréquence autorisées**
3. **Limiter la puissance selon la réglementation**
4. **Ne pas interférer avec les communications légitimes**

#### En France (exemple)
- **Classe B** : Autorisation simple pour émission expérimentale
- **Fréquences autorisées** : Bandes amateurs (144-146 MHz, 430-440 MHz)
- **Puissance maximale** : 10 W PEP en classe B

### Préparation matérielle

#### Matériel nécessaire
- **HackRF One** ou **LimeSDR** (RTL-SDR ne permet pas l'émission)
- **Antenne adaptée** à la bande d'émission
- **Atténuateur RF** (20-30 dB) pour les tests
- **Câble SMA** de qualité

#### Configuration de sécurité
- **Atténuateur en ligne** : Protège contre les surpuissances
- **Charge dummy load** : Pour les tests sans antenne
- **Mesure de puissance** : Wattmètre RF pour vérification

### Installation des logiciels

#### GNU Radio pour HackRF

##### Installation Linux
```bash
sudo apt install gnuradio gnuradio-dev
# ou depuis source pour la dernière version
git clone https://github.com/gnuradio/gnuradio.git
cd gnuradio
mkdir build && cd build
cmake ..
make -j$(nproc)
sudo make install
```

##### Installation des blocs HackRF
```bash
sudo apt install gr-osmosdr
# ou
git clone https://github.com/osmocom/gr-osmosdr.git
cd gr-osmosdr
mkdir build && cd build
cmake ..
make -j$(nproc)
sudo make install
```

### Premier test d'émission

#### Flowgraph GNU Radio simple

##### Création du flowgraph
1. Ouvrir GNU Radio Companion (GRC)
2. Ajouter un "Signal Source" (onde sinusoïdale)
3. Ajouter un "Osmocom Sink" (HackRF)
4. Connecter les blocs

##### Paramètres de base
- **Fréquence** : Bande ISM 433 MHz (autorisée)
- **Puissance** : -20 dBm (avec atténuateur)
- **Forme d'onde** : Sinusoïdale 1 kHz
- **Durée** : Très courte pour les tests

##### Génération du code Python
```python
#!/usr/bin/env python3

from gnuradio import gr, analog, blocks
from gnuradio import osmosdr
import sys

class tx_test(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "TX Test")

        # Paramètres
        samp_rate = 2e6
        freq = 433.92e6  # 433.92 MHz (autorisé)

        # Blocs
        self.source = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 1000, 0.1, 0)
        self.sink = osmosdr.sink(args="numchan=1 hackrf=0")
        self.sink.set_sample_rate(samp_rate)
        self.sink.set_center_freq(freq, 0)
        self.sink.set_gain(0, 0)  # Puissance minimale

        # Connexion
        self.connect(self.source, self.sink)

if __name__ == '__main__':
    tb = tx_test()
    tb.start()
    input("Press Enter to stop...")
    tb.stop()
    tb.wait()
```

### Vérification de l'émission

#### Avec un second SDR
- Utiliser RTL-SDR pour vérifier l'émission
- Observer le spectre avec SDR++
- Mesurer la fréquence et la puissance

#### Tests de sécurité
- Émission très courte (< 1 seconde)
- Puissance minimale
- Fréquence dans bande autorisée

## 7.2 Générer un signal FM

### Principe de la modulation FM

La modulation de fréquence fait varier la fréquence de la porteuse selon le signal audio à transmettre.

#### Paramètres FM
- **Déviation de fréquence** : ±75 kHz pour FM broadcast
- **Bande passante** : 200 kHz par canal
- **Fréquence porteuse** : Dans bande autorisée

### Création d'un émetteur FM simple

#### Flowgraph GNU Radio

##### Blocs nécessaires
1. **Audio Source** : Source audio (fichier ou micro)
2. **FM Mod** : Modulateur FM
3. **Osmocom Sink** : Sortie HackRF

##### Configuration détaillée

```python
#!/usr/bin/env python3

from gnuradio import gr, analog, audio, blocks
from gnuradio import osmosdr
import sys

class fm_transmitter(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "FM Transmitter")

        # Paramètres
        samp_rate = 2e6
        audio_rate = 48e3
        freq = 144.5e6  # 144.5 MHz (bande 2m autorisée)

        # Blocs audio
        self.audio_source = audio.source(audio_rate, "", True)
        self.audio_filter = analog.band_pass_filter_fff(audio_rate, 50, 15000, 1000, 60)

        # Modulation FM
        self.fm_mod = analog.frequency_modulator_fc(audio_rate / (2 * 3.14159 * 75e3))

        # Interpolation et filtrage
        self.interp = blocks.interp_fir_filter_ccc(1, [1])
        self.resampler = blocks.resampler_ccf(samp_rate / audio_rate, [1])

        # Sortie RF
        self.sink = osmosdr.sink(args="numchan=1 hackrf=0")
        self.sink.set_sample_rate(samp_rate)
        self.sink.set_center_freq(freq, 0)
        self.sink.set_gain(10, 0)  # Ajuster selon licence

        # Connexions
        self.connect(self.audio_source, self.audio_filter, self.fm_mod)
        self.connect(self.fm_mod, self.resampler, self.sink)

if __name__ == '__main__':
    tb = fm_transmitter()
    tb.start()
    input("Press Enter to stop...")
    tb.stop()
    tb.wait()
```

### Tests et optimisation

#### Test de réception
- Utiliser un récepteur FM standard
- Vérifier la qualité audio
- Ajuster la déviation de fréquence

#### Ajustements
- **Gain audio** : Éviter la saturation
- **Filtrage** : Supprimer les fréquences parasites
- **Puissance** : Selon licence et distance

### Applications légales

#### Radioamateur
- **QSO locaux** : Communication vocale
- **Relais** : Extension de portée
- **Beacon** : Signal d'identification

#### Éducation
- **Démonstration** : Enseignement des modulations
- **Tests de propagation** : Étude des ondes radio
- **Formation** : Apprentissage des protocoles

## 7.3 Comprendre la puissance, émission, atténuateurs

### Gestion de la puissance RF

#### Unités de puissance
- **dBm** : Puissance en dB par rapport à 1 mW
- **Watt** : Puissance absolue
- **dBW** : Puissance en dB par rapport à 1 W

#### Conversion
- **0 dBm** = 1 mW
- **10 dBm** = 10 mW
- **20 dBm** = 100 mW = 0.1 W
- **30 dBm** = 1 W

### Mesure de la puissance

#### Wattmètre RF
- **Mesure directe** : Puissance réelle transmise
- **Calibration** : Vérification de l'exactitude
- **Types** : Analogique, numérique, USB

#### Mesure indirecte avec SDR
```python
# Estimation de puissance avec un second SDR
import numpy as np
from rtlsdr import RtlSdr

def measure_power(freq, bandwidth):
    sdr = RtlSdr()
    sdr.center_freq = freq
    sdr.sample_rate = bandwidth * 10  # Surtéchantillonnage

    samples = sdr.read_samples(1024*1024)
    power = 10 * np.log10(np.mean(np.abs(samples)**2)) + 30  # dBm

    sdr.close()
    return power
```

### Atténuateurs RF

#### Types d'atténuateurs
- **Fixe** : 10, 20, 30 dB
- **Variable** : Ajustable 0-30 dB
- **Pas-à-pas** : Précision 1 dB

#### Utilisation
- **Tests** : Réduction de puissance pour sécurité
- **Calibration** : Ajustement précis des niveaux
- **Protection** : Prévention des surcharges

### Sécurité en émission

#### Risques électriques
- **Tension RF** : Dangereuse à haute puissance
- **Échauffement** : Composants sensibles à la chaleur
- **Arc électrique** : Connexions défaillantes

#### Mesures de protection
- **Charge dummy** : Résistance 50 ohms pour tests
- **Atténuateur** : Réduction systématique de puissance
- **Monitoring** : Surveillance continue des paramètres

#### Conformité réglementaire
- **Limites de puissance** : Selon licence et bande
- **Durée d'émission** : Éviter les émissions continues
- **Journal de bord** : Enregistrement des émissions

## 7.4 Transmettre un signal numérique simple

### Modulation numérique de base

#### ASK (Amplitude Shift Keying)
- Variation d'amplitude selon les bits
- Simple à implémenter
- Sensible au bruit

#### FSK (Frequency Shift Keying)
- Variation de fréquence
- Bonne immunité au bruit
- Utilisé en radioamateur

### Implémentation ASK simple

#### Flowgraph GNU Radio

```python
#!/usr/bin/env python3

from gnuradio import gr, digital, analog, blocks
from gnuradio import osmosdr
import sys

class ask_transmitter(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "ASK Transmitter")

        # Paramètres
        samp_rate = 2e6
        bit_rate = 1200
        freq = 433.92e6  # Bande ISM

        # Source de données
        self.data_source = blocks.vector_source_b([1,0,1,0,1,1,0,0] * 100, True)

        # Modulation ASK
        self.ask_mod = digital.chunks_to_symbols_bf([0, 1], 1)  # 0->0V, 1->1V

        # Interpolation
        self.interp = blocks.repeat(gr.sizeof_gr_complex, int(samp_rate / bit_rate))

        # Filtrage
        self.filter = analog.band_pass_filter_ccc(samp_rate, freq - 10e3, freq + 10e3, 1e3, 40)

        # Sortie RF
        self.sink = osmosdr.sink(args="numchan=1 hackrf=0")
        self.sink.set_sample_rate(samp_rate)
        self.sink.set_center_freq(freq, 0)
        self.sink.set_gain(0, 0)  # Puissance minimale

        # Connexions
        self.connect(self.data_source, self.ask_mod, self.interp, self.filter, self.sink)

if __name__ == '__main__':
    tb = ask_transmitter()
    tb.start()
    input("Press Enter to stop...")
    tb.stop()
    tb.wait()
```

### Implémentation FSK

#### Flowgraph FSK

```python
#!/usr/bin/env python3

from gnuradio import gr, digital, analog, blocks
from gnuradio import osmosdr

class fsk_transmitter(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "FSK Transmitter")

        # Paramètres
        samp_rate = 2e6
        bit_rate = 1200
        freq = 433.92e6
        freq_dev = 5e3  # Déviation 5 kHz

        # Source de données
        self.data_source = blocks.vector_source_b([1,0,1,0,1,1,0,0] * 100, True)

        # Modulation FSK
        self.fsk_mod = digital.gfsk_mod(
            samples_per_symbol=int(samp_rate / bit_rate),
            bt=0.5,
            freq_dev=freq_dev
        )

        # Sortie RF
        self.sink = osmosdr.sink(args="numchan=1 hackrf=0")
        self.sink.set_sample_rate(samp_rate)
        self.sink.set_center_freq(freq, 0)
        self.sink.set_gain(0, 0)

        # Connexions
        self.connect(self.data_source, self.fsk_mod, self.sink)

if __name__ == '__main__':
    tb = fsk_transmitter()
    tb.start()
    input("Press Enter to stop...")
    tb.stop()
    tb.wait()
```

### Tests de transmission

#### Réception avec RTL-SDR
- Utiliser URH pour analyser le signal
- Vérifier la modulation
- Détecter les erreurs de transmission

#### Mesure des performances
- **BER (Bit Error Rate)** : Taux d'erreur binaire
- **Sensibilité** : Puissance minimale pour réception correcte
- **Portée** : Distance maximale de communication

## 7.5 Créer un réseau radio local expérimental

### Concept de réseau radio local

Un réseau radio local permet la communication entre plusieurs nœuds SDR dans une zone limitée, utilisant des protocoles simples pour l'échange de données.

#### Applications
- **IoT experimental** : Capteurs sans fil
- **Réseau mesh** : Communication décentralisée
- **Formation** : Apprentissage des réseaux

### Architecture proposée

#### Topologie en étoile
- **Nœud central** : Coordinateur du réseau
- **Nœuds périphériques** : Capteurs/actionneurs
- **Protocole simple** : Time Division Multiple Access (TDMA)

#### Fréquences utilisées
- **Bande ISM 433 MHz** : Autorisée sans licence
- **Bande ISM 868 MHz** : Alternative Européenne
- **Bande amateur** : Si licence disponible

### Implémentation du protocole

#### Structure des paquets
```
[Préambule] [Adresse source] [Adresse destination] [Données] [CRC]
```

#### Timing TDMA
- **Trame** : 100 ms
- **Slots** : 5 slots par trame (20 ms chacun)
- **Garde** : 1 ms entre slots

### Flowgraph GNU Radio du nœud

#### Émetteur/récepteur
```python
#!/usr/bin/env python3

from gnuradio import gr, digital, analog, blocks
from gnuradio import osmosdr
import time

class mesh_node(gr.top_block):
    def __init__(self, node_id, freq, slot_time=0.02):
        gr.top_block.__init__(self, f"Mesh Node {node_id}")

        self.node_id = node_id
        self.freq = freq
        self.slot_time = slot_time

        # Configuration SDR commune
        samp_rate = 2e6

        # Récepteur
        self.rx_source = osmosdr.source(args="numchan=1 hackrf=0")
        self.rx_source.set_sample_rate(samp_rate)
        self.rx_source.set_center_freq(freq, 0)
        self.rx_source.set_gain(40, 0)

        # Émetteur
        self.tx_sink = osmosdr.sink(args="numchan=1 hackrf=0")
        self.tx_sink.set_sample_rate(samp_rate)
        self.tx_sink.set_center_freq(freq, 0)
        self.tx_sink.set_gain(10, 0)

        # Logique TDMA (simplifiée)
        self.scheduler = blocks.message_strobe(pmt.cons(pmt.PMT_NIL, pmt.intern("tx")), 1000)  # Toutes les secondes

    def transmit_data(self, data, dest_id):
        # Logique de transmission dans le slot approprié
        packet = self.create_packet(data, dest_id)
        # Transmission...

    def create_packet(self, data, dest_id):
        # Création du paquet avec en-têtes
        preamble = [1,0,1,0,1,0,1,0] * 4
        source_addr = format(self.node_id, '08b')
        dest_addr = format(dest_id, '08b')
        crc = self.calculate_crc(data)

        return preamble + list(source_addr) + list(dest_addr) + data + crc

    def calculate_crc(self, data):
        # CRC simple
        return [0, 1, 1, 0]  # Exemple
```

### Gestion du réseau

#### Attribution des slots
- **Slot 0** : Nœud maître (coordination)
- **Slots 1-4** : Nœuds esclaves
- **Synchronisation** : Horloge commune

#### Routage simple
- **Direct** : Communication directe si portée suffisante
- **Via maître** : Routage à travers le nœud central
- **Broadcast** : Diffusion à tous les nœuds

### Applications pratiques

#### Réseau de capteurs
- **Température** : Mesure et transmission
- **Humidité** : Données environnementales
- **Position** : Localisation GPS

#### Communication M2M
- **Commandes** : Contrôle à distance
- **Alertes** : Notifications automatiques
- **Synchronisation** : Horloge réseau

### Tests et débogage

#### Outils de diagnostic
- **Analyse spectrale** : Vérification des émissions
- **Capture de paquets** : Validation des données
- **Mesure de portée** : Tests de couverture

#### Optimisations
- **Codage correcteur** : Amélioration de la fiabilité
- **Adaptation automatique** : Ajustement des paramètres
- **Gestion d'énergie** : Mode veille pour économie

## 7.6 Précautions légales et limites

### Réglementation par pays

#### France (ARCEP)
- **Licence obligatoire** pour émission publique
- **Classe B** : Émission expérimentale autorisée
- **Bandes ISM** : 433/868 MHz limités à 10 mW
- **Contrôle** : Vérifications régulières

#### États-Unis (FCC)
- **Part 15** : Équipements non-licenciés
- **Part 97** : Radioamateurs
- **Part 90** : Communications privées

#### Union Européenne
- **R&TTE Directive** : Conformité des équipements
- **RED Directive** : Réseaux radio
- **Harmonisation** : Bandes communes

### Limites techniques et légales

#### Puissance maximale autorisée
- **433 MHz ISM** : 10 mW ERP (France)
- **Bande amateur** : Selon classe de licence
- **Mesure obligatoire** : Vérification régulière

#### Durée d'émission
- **Pas de limite** pour communications légitimes
- **Tests courts** : Émissions de durée limitée
- **Journal** : Enregistrement des émissions

### Éthique et responsabilité

#### Respect des autres utilisateurs
- **Non-interférence** : Éviter les brouillages
- **Écoute préalable** : Vérification de la fréquence libre
- **Signal d'identification** : Indicatif radioamateur

#### Sécurité
- **Pas d'émission dangereuse** : Évite les risques pour la santé
- **Confidentialité** : Protection des données transmises
- **Traçabilité** : Possibilité d'identifier l'émetteur

### Recommandations pratiques

#### Avant émission
- **Vérifier la licence** : Validité et conditions
- **Tester l'équipement** : Fonctionnement correct
- **Mesurer la puissance** : Conformité réglementaire

#### Pendant l'émission
- **Surveillance** : Écoute des interférences
- **Puissance minimale** : Nécessaire uniquement
- **Durée raisonnable** : Évite la monopolisation

#### Après émission
- **Documentation** : Journal des activités
- **Maintenance** : Vérification de l'équipement
- **Formation** : Mise à jour des connaissances

### Sanctions en cas de non-respect

#### Administratives
- **Amendes** : Plusieurs milliers d'euros
- **Saisie** : Matériel confisqué
- **Radiation** : Perte de licence

#### Pénales
- **Brouillage** : Atteinte aux communications
- **Usage illégal** : Tromperie sur l'identité
- **Dangers** : Risques pour la sécurité publique

#### Prévention
- **Formation** : Connaissance de la réglementation
- **Conseil** : Consultation des autorités
- **Association** : Rejoindre un club radioamateur
