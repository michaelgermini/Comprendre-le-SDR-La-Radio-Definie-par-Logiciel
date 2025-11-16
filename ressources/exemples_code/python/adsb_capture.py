#!/usr/bin/env python3
"""
Captureur et décodeur ADS-B simple
Capture les signaux ADS-B des avions et extrait les informations de base

Dépendances:
    pip install numpy pyrtlsdr pyModeS

Utilisation:
    python adsb_capture.py --duration 60 --output avions.csv
"""

import argparse
import numpy as np
import pandas as pd
from rtlsdr import RtlSdr
import time
import signal
import sys
from datetime import datetime

try:
    import pyModeS as pms
    PYMODES_AVAILABLE = True
except ImportError:
    print("Warning: pyModeS non installé. Install avec: pip install pyModeS")
    PYMODES_AVAILABLE = False

class ADSBCapture:
    def __init__(self, ppm=0, gain=40):
        """Initialise la capture ADS-B"""
        self.sdr = RtlSdr()
        self.sdr.center_freq = 1090e6  # Fréquence ADS-B
        self.sdr.sample_rate = 2e6     # 2 MHz d'échantillonnage
        self.sdr.freq_correction = ppm
        self.sdr.gain = gain

        # Paramètres PPM (Pulse Position Modulation)
        self.preamble = [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]  # Préambule ADS-B
        self.message_length = 112  # 112 μs pour message complet

        # Stockage des données
        self.aircraft_data = {}

        print("Capture ADS-B initialisée")
        print(f"Fréquence: {self.sdr.center_freq/1e6} MHz")
        print(f"Gain: {self.sdr.gain} dB")

    def capture_samples(self, duration):
        """Capture des échantillons pendant une durée donnée"""
        print(f"Capture pendant {duration} secondes...")
        total_samples = int(duration * self.sdr.sample_rate)
        samples = self.sdr.read_samples(total_samples)
        return samples

    def detect_preamble(self, samples, threshold=0.6):
        """Détecte les préambules ADS-B dans le signal"""
        # Conversion en binaire (seuillage)
        binary_signal = (np.real(samples) > threshold).astype(int)

        # Recherche du préambule
        preamble_indices = []
        preamble_len = len(self.preamble)

        for i in range(len(binary_signal) - preamble_len):
            if np.array_equal(binary_signal[i:i+preamble_len], self.preamble):
                preamble_indices.append(i)

        return preamble_indices

    def decode_message(self, samples, start_index):
        """Décode un message ADS-B depuis les échantillons"""
        if not PYMODES_AVAILABLE:
            return None

        try:
            # Extraction du message (112 μs = 224 échantillons à 2 MHz)
            message_samples = samples[start_index:start_index + 224]

            # Conversion en bits
            bits = (np.real(message_samples) > 0.5).astype(int)

            # Conversion en hexadécimal
            hex_message = ""
            for i in range(0, len(bits), 4):
                nibble = bits[i:i+4]
                hex_digit = hex(int(''.join(map(str, nibble)), 2))[2:].upper()
                hex_message += hex_digit

            # Vérification CRC
            if not pms.crc(hex_message):
                return None

            # Extraction des données
            icao = pms.icao(hex_message)
            callsign = pms.callsign(hex_message)
            altitude = pms.altitude(hex_message)
            speed = pms.speed(hex_message)
            heading = pms.heading(hex_message)
            lat, lon = pms.position(hex_message, lat_ref=48.8566, lon_ref=2.3522)  # Paris par défaut

            return {
                'timestamp': datetime.now(),
                'icao': icao,
                'callsign': callsign,
                'altitude': altitude,
                'speed': speed,
                'heading': heading,
                'latitude': lat,
                'longitude': lon,
                'hex_message': hex_message
            }

        except Exception as e:
            return None

    def process_capture(self, samples):
        """Traite une capture complète et extrait les messages ADS-B"""
        print("Traitement des échantillons...")

        # Détection des préambules
        preamble_indices = self.detect_preamble(samples)
        print(f"{len(preamble_indices)} préambules détectés")

        messages = []
        processed_indices = set()

        for idx in preamble_indices:
            # Évite les doublons
            if any(abs(idx - p) < 200 for p in processed_indices):
                continue

            processed_indices.add(idx)

            # Décode le message
            message = self.decode_message(samples, idx)
            if message:
                messages.append(message)
                print(f"Message décodé: {message['icao']} - {message['callsign']}")

        return messages

    def save_to_csv(self, messages, filename):
        """Sauvegarde les messages dans un fichier CSV"""
        if not messages:
            print("Aucun message à sauvegarder")
            return

        df = pd.DataFrame(messages)
        df.to_csv(filename, index=False)
        print(f"{len(messages)} messages sauvegardés dans {filename}")

    def display_statistics(self, messages):
        """Affiche des statistiques sur les messages capturés"""
        if not messages:
            print("Aucune donnée à analyser")
            return

        print("\nStatistiques de capture:")
        print("-" * 30)

        # Nombre total d'avions
        unique_icao = set(msg['icao'] for msg in messages if msg['icao'])
        print(f"Nombre d'avions uniques: {len(unique_icao)}")

        # Altitude moyenne
        altitudes = [msg['altitude'] for msg in messages if msg['altitude']]
        if altitudes:
            print(f"Altitude moyenne: {np.mean(altitudes):.0f} pieds")

        # Vitesse moyenne
        speeds = [msg['speed'] for msg in messages if msg['speed']]
        if speeds:
            print(f"Vitesse moyenne: {np.mean(speeds):.1f} nœuds")

        # Compagnies aériennes
        callsigns = [msg['callsign'] for msg in messages if msg['callsign']]
        if callsigns:
            airlines = {}
            for callsign in callsigns:
                airline = callsign[:3] if len(callsign) >= 3 else callsign
                airlines[airline] = airlines.get(airline, 0) + 1

            print("Top 5 compagnies:")
            sorted_airlines = sorted(airlines.items(), key=lambda x: x[1], reverse=True)
            for airline, count in sorted_airlines[:5]:
                print(f"  {airline}: {count} messages")

    def close(self):
        """Ferme proprement le SDR"""
        self.sdr.close()

def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description='Captureur ADS-B simple')
    parser.add_argument('--duration', type=int, default=30,
                       help='Durée de capture en secondes (défaut: 30)')
    parser.add_argument('--output', type=str, default='adsb_capture.csv',
                       help='Fichier de sortie CSV (défaut: adsb_capture.csv)')
    parser.add_argument('--ppm', type=int, default=0,
                       help='Correction PPM (défaut: 0)')
    parser.add_argument('--gain', type=int, default=40,
                       help='Gain SDR en dB (défaut: 40)')

    args = parser.parse_args()

    print("ADS-B Capture Tool")
    print("Assurez-vous que votre RTL-SDR est connecté")
    print()

    # Initialisation
    capture = ADSBCapture(ppm=args.ppm, gain=args.gain)

    # Gestionnaire d'interruption
    def signal_handler(sig, frame):
        print("\nInterruption détectée. Fermeture...")
        capture.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        # Capture
        samples = capture.capture_samples(args.duration)

        # Traitement
        messages = capture.process_capture(samples)

        # Statistiques
        capture.display_statistics(messages)

        # Sauvegarde
        if messages:
            capture.save_to_csv(messages, args.output)

    except Exception as e:
        print(f"Erreur: {e}")
        print("Vérifiez que votre SDR est connecté et les dépendances installées.")

    finally:
        capture.close()

if __name__ == "__main__":
    main()
