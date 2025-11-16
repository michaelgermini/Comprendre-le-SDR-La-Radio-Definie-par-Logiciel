# Flows GNU Radio prêts à l'emploi

## Installation et configuration

### Prérequis système
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install gnuradio gnuradio-dev python3-pip

# Vérification
gnuradio-companion --version
```

### Installation drivers SDR
```bash
# RTL-SDR
sudo apt install librtlsdr-dev

# HackRF
sudo apt install hackrf libhackrf-dev

# LimeSDR
# Télécharger depuis https://myriadrf.org/

# USRP
sudo apt install libuhd-dev uhd-host
uhd_images_downloader  # Téléchargement FPGA
```

## Flow 1 : Récepteur FM stéréo simple

### Description
Récepteur FM avec démodulation stéréo et sortie audio.

### Blocs utilisés
```
Osmocom Source → Low Pass Filter → FM Demodulator → Stereo Demodulator → Audio Sink
```

### Code GRC (fichier .grc)
```xml
<?xml version='1.0' encoding='utf-8'?>
<flow_graph>
  <timestamp>Sun Nov 16 12:00:00 2025</timestamp>
  <block>
    <key>options</key>
    <param>
      <key>author</key>
      <value>Votre nom</value>
    </param>
    <param>
      <key>copyright</key>
      <value>2025</value>
    </param>
    <param>
      <key>description</key>
      <value>Récepteur FM stéréo simple</value>
    </param>
    <param>
      <key>generate_options</key>
      <value>qt_gui</value>
    </param>
    <param>
      <key>category</key>
      <value>Custom</value>
    </param>
    <param>
      <key>run_options</key>
      <value>prompt</value>
    </param>
    <param>
      <key>run</key>
      <value>True</value>
    </param>
    <param>
      <key>max_nouts</key>
      <value>0</value>
    </param>
    <param>
      <key>realtime_scheduling</key>
      <value></value>
    </param>
    <param>
      <key>thread_safe_setters</key>
      <value></value>
    </param>
    <param>
      <key>title</key>
      <value>Récepteur FM Stéréo</value>
    </param>
  </block>

  <block>
    <key>variable</key>
    <param>
      <key>comment</key>
      <value></value>
    </param>
    <param>
      <key>id</key>
      <value>samp_rate</value>
    </param>
    <param>
      <key>value</key>
      <value>2e6</value>
    </param>
  </block>

  <block>
    <key>variable</key>
    <param>
      <key>comment</key>
      <value></value>
    </param>
    <param>
      <key>id</key>
      <value>freq</value>
    </param>
    <param>
      <key>value</key>
      <value>93.5e6</value>
    </param>
  </block>

  <block>
    <key>osmosdr_source</key>
    <param>
      <key>id</key>
      <value>osmosdr_source_0</value>
    </param>
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
      <value>freq</value>
    </param>
    <param>
      <key>rf_gain</key>
      <value>30</value>
    </param>
    <param>
      <key>if_gain</key>
      <value>20</value>
    </param>
    <param>
      <key>bb_gain</key>
      <value>20</value>
    </param>
    <param>
      <key>antennas</key>
      <value></value>
    </param>
    <param>
      <key>bw</key>
      <value>0</value>
    </param>
  </block>

  <block>
    <key>low_pass_filter</key>
    <param>
      <key>id</key>
      <value>low_pass_filter_0</value>
    </param>
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
      <value>100e3</value>
    </param>
    <param>
      <key>transition_width</key>
      <value>10e3</value>
    </param>
    <param>
      <key>window</key>
      <value>WIN_HAMMING</value>
    </param>
    <param>
      <key>beta</key>
      <value>6.76</value>
    </param>
  </block>

  <block>
    <key>wfm_rcv</key>
    <param>
      <key>id</key>
      <value>wfm_rcv_0</value>
    </param>
    <param>
      <key>quad_rate</key>
      <value>samp_rate</value>
    </param>
    <param>
      <key>audio_decimation</key>
      <value>1</value>
    </param>
  </block>

  <block>
    <key>audio_sink</key>
    <param>
      <key>id</key>
      <value>audio_sink_0</value>
    </param>
    <param>
      <key>sample_rate</key>
      <value>48e3</value>
    </param>
    <param>
      <key>device_name</key>
      <value></value>
    </param>
    <param>
      <key>ok_to_block</key>
      <value>True</value>
    </param>
  </block>

  <connection>
    <source_block_id>osmosdr_source_0</source_block_id>
    <sink_block_id>low_pass_filter_0</sink_block_id>
    <source_key>0</source_key>
    <sink_key>0</sink_key>
  </connection>

  <connection>
    <source_block_id>low_pass_filter_0</source_block_id>
    <sink_block_id>wfm_rcv_0</sink_block_id>
    <source_key>0</source_key>
    <sink_key>0</sink_key>
  </connection>

  <connection>
    <source_block_id>wfm_rcv_0</source_block_id>
    <sink_block_id>audio_sink_0</sink_block_id>
    <source_key>0</source_key>
    <sink_key>0</sink_key>
  </connection>
</flow_graph>
```

### Utilisation
1. Ouvrir dans GNU Radio Companion
2. Générer (F5) et exécuter (F6)
3. Ajuster fréquence pour station FM locale

## Flow 2 : Analyseur de spectre temps réel

### Description
Visualisation du spectre avec waterfall et mesures.

### Blocs utilisés
```
Osmocom Source → FFT → Complex to Mag^2 → QT GUI Waterfall Sink
```

### Code Python simplifié
```python
#!/usr/bin/env python3

from gnuradio import gr, blocks, fft, qtgui
from gnuradio.fft import window
import sys
import signal

class spectrum_analyzer(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "Spectrum Analyzer")

        # Paramètres
        self.samp_rate = 2e6
        self.center_freq = 100e6
        self.fft_size = 2048

        # Source SDR
        self.osmosdr_source = osmosdr.source(args="numchan=1")
        self.osmosdr_source.set_sample_rate(self.samp_rate)
        self.osmosdr_source.set_center_freq(self.center_freq, 0)

        # Traitement FFT
        self.stream_to_vec = blocks.stream_to_vector(gr.sizeof_gr_complex, self.fft_size)
        self.fft_block = fft.fft_vcc(self.fft_size, True, window.blackmanharris(self.fft_size), True, 1)
        self.complex_to_mag = blocks.complex_to_mag_squared(self.fft_size)

        # Interface graphique
        self.qtgui_waterfall = qtgui.waterfall_sink_c(
            self.fft_size,          # fft size
            window.WIN_BLACKMAN_hARRIS,  # wintype
            self.center_freq,       # fc
            self.samp_rate,         # bw
            "",                     # name
            1                       # nconnections
        )

        # Connexions
        self.connect(self.osmosdr_source, self.stream_to_vec, self.fft_block, self.complex_to_mag, self.qtgui_waterfall)

if __name__ == '__main__':
    tb = spectrum_analyzer()
    tb.start()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.pause()
```

## Flow 3 : Émetteur FM simple

### ⚠️ Usage légal uniquement avec licence appropriée

### Description
Génération d'un signal FM modulé par audio.

### Blocs utilisés
```
Audio Source → FM Modulator → Osmocom Sink
```

### Code GRC
```xml
<?xml version='1.0' encoding='utf-8'?>
<flow_graph>
  <timestamp>Sun Nov 16 13:00:00 2025</timestamp>
  <block>
    <key>options</key>
    <param>
      <key>title</key>
      <value>Émetteur FM Simple</value>
    </param>
    <param>
      <key>generate_options</key>
      <value>qt_gui</value>
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
      <value>2e6</value>
    </param>
  </block>

  <block>
    <key>variable</key>
    <param>
      <key>id</key>
      <value>audio_rate</value>
    </param>
    <param>
      <key>value</key>
      <value>48e3</value>
    </param>
  </block>

  <block>
    <key>audio_source</key>
    <param>
      <key>id</key>
      <value>audio_source_0</value>
    </param>
    <param>
      <key>sample_rate</key>
      <value>audio_rate</value>
    </param>
    <param>
      <key>device_name</key>
      <value></value>
    </param>
    <param>
      <key>ok_to_block</key>
      <value>True</value>
    </param>
  </block>

  <block>
    <key>analog_frequency_modulator_fc</key>
    <param>
      <key>id</key>
      <value>analog_frequency_modulator_fc_0</value>
    </param>
    <param>
      <key>sensitivity</key>
      <value>audio_rate / (2 * 3.14159 * 75e3)</value>
    </param>
  </block>

  <block>
    <key>multiply_const_cc</key>
    <param>
      <key>id</key>
      <value>multiply_const_cc_0</value>
    </param>
    <param>
      <key>const</key>
      <value>0.1</value>
    </param>
  </block>

  <block>
    <key>osmosdr_sink</key>
    <param>
      <key>id</key>
      <value>osmosdr_sink_0</value>
    </param>
    <param>
      <key>args</key>
      <value>numchan=1 hackrf=0</value>
    </param>
    <param>
      <key>sample_rate</key>
      <value>samp_rate</value>
    </param>
    <param>
      <key>center_freq</key>
      <value>144.5e6</value>
    </param>
    <param>
      <key>rf_gain</key>
      <value>0</value>
    </param>
    <param>
      <key>if_gain</key>
      <value>20</value>
    </param>
    <param>
      <key>bb_gain</key>
      <value>20</value>
    </param>
  </block>

  <connection>
    <source_block_id>audio_source_0</source_block_id>
    <sink_block_id>analog_frequency_modulator_fc_0</sink_block_id>
    <source_key>0</source_key>
    <sink_key>0</sink_key>
  </connection>

  <connection>
    <source_block_id>analog_frequency_modulator_fc_0</source_block_id>
    <sink_block_id>multiply_const_cc_0</sink_block_id>
    <source_key>0</source_key>
    <sink_key>0</sink_key>
  </connection>

  <connection>
    <source_block_id>multiply_const_cc_0</source_block_id>
    <sink_block_id>osmosdr_sink_0</sink_block_id>
    <source_key>0</source_key>
    <sink_key>0</sink_key>
  </connection>
</flow_graph>
```

## Flow 4 : Décodeur ADS-B

### Description
Réception et décodage des signaux ADS-B des avions.

### Blocs utilisés
```
Osmocom Source → Frequency Xlating FIR → ADS-B Framer → ADS-B Decoder → File Sink
```

### Installation bloc ADS-B
```bash
# Installation gr-adsb
git clone https://github.com/bkerler/gr-adsb.git
cd gr-adsb
mkdir build && cd build
cmake ..
make
sudo make install
```

## Flow 5 : Générateur de signal de test

### Description
Génération de signaux modulés pour tests.

### Blocs utilisés
```
Signal Source → Modulator → Throttle → Osmocom Sink
```

## Flow 6 : Simulateur de canal

### Description
Simulation de conditions de propagation réalistes.

### Blocs utilisés
```
Signal Source → Channel Model → Fading Model → Noise Source → Receiver
```

### Modèles disponibles
- Rayleigh : Propagation urbaine
- Rician : Ligne de vue
- AWGN : Bruit blanc gaussien

## Flow 7 : Démodulateur QPSK

### Description
Démodulation de signaux QPSK avec correction d'erreur.

### Blocs utilisés
```
Source → AGC → Costas Loop → FLL → QPSK Demod → Viterbi → BER Calculator
```

## Scripts utilitaires

### Script de scan automatique
```python
#!/usr/bin/env python3
"""
Script de scan automatique des fréquences
"""

import time
from rtlsdr import RtlSdr

def scan_frequencies(start_freq, end_freq, step, dwell_time=1.0):
    sdr = RtlSdr()
    sdr.sample_rate = 2.4e6
    sdr.gain = 30

    freq = start_freq
    results = {}

    while freq <= end_freq:
        sdr.center_freq = freq
        time.sleep(dwell_time)

        # Mesure puissance
        samples = sdr.read_samples(1024*1024)
        power = sum(abs(s)**2 for s in samples) / len(samples)

        if power > threshold:  # threshold à définir
            results[freq] = power
            print(f"Signal détecté à {freq/1e6:.1f} MHz : {10*np.log10(power):.1f} dB")

        freq += step

    sdr.close()
    return results

# Utilisation
results = scan_frequencies(87.5e6, 108e6, 0.1e6)  # FM
```

### Script de capture IQ
```python
#!/usr/bin/env python3
"""
Capture de fichiers IQ pour analyse
"""

import numpy as np
from rtlsdr import RtlSdr

def capture_iq(filename, frequency, duration, sample_rate=2e6):
    sdr = RtlSdr()
    sdr.center_freq = frequency
    sdr.sample_rate = sample_rate
    sdr.gain = 40

    print(f"Capture à {frequency/1e6:.1f} MHz pendant {duration} secondes...")

    samples = sdr.read_samples(int(duration * sample_rate))

    # Sauvegarde en format complexe
    np.save(filename, samples)

    sdr.close()
    print(f"Capture sauvegardée dans {filename}.npy")

# Utilisation
capture_iq('adsb_capture', 1090e6, 30)
```

## Dépannage courant

### Problèmes fréquents

#### Erreur "No module named 'gnuradio'"
```bash
# Solution
export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3/dist-packages
```

#### HackRF non détecté
```bash
# Vérification
hackrf_info

# Permissions
sudo usermod -a -G plugdev $USER
```

#### Performances insuffisantes
- Réduire sample_rate
- Utiliser décimation
- Fermer autres applications

### Optimisations

#### Utilisation CPU/GPU
```python
# Activer Volk (vector library)
export VOLK_GENERIC=0
volk_profile
```

#### Buffers optimisés
- Augmenter buffer_size dans blocs
- Utiliser real-time scheduling
- `chrt --rr 50`

## Ressources d'apprentissage

### Tutoriels officiels
- [GNU Radio Tutorials](https://wiki.gnuradio.org/index.php/Tutorials)
- [GNU Radio Guided Tutorials](https://wiki.gnuradio.org/index.php/Guided_Tutorials)

### Communauté
- [GNU Radio Mailing List](https://lists.gnu.org/mailman/listinfo/discuss-gnuradio)
- [Reddit r/GNURadio](https://www.reddit.com/r/GNURadio/)
- [Discord GNU Radio](https://discord.gg/gnuradio)

### Livres
- "GNU Radio for Software Defined Radio" - R. Olsson
- "Exploring GNU Radio" - H. Paul

---

*Ces flows sont fournis à titre éducatif. Respectez toujours la législation locale concernant l'émission radio.*
