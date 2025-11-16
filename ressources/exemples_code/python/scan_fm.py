#!/usr/bin/env python3
"""
Scanner automatique de fréquences FM
Scanne la bande FM (87.5-108 MHz) et détecte les stations actives

Dépendances:
    pip install numpy pyrtlsdr matplotlib

Utilisation:
    python scan_fm.py
"""

import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
import time

class FMScanner:
    def __init__(self, ppm=0, gain='auto'):
        """Initialise le scanner FM"""
        self.sdr = RtlSdr()
        self.sdr.sample_rate = 2.4e6  # 2.4 MHz
        self.sdr.freq_correction = ppm
        if gain == 'auto':
            self.sdr.gain = 30  # Gain manuel pour cohérence
        else:
            self.sdr.gain = gain

        # Paramètres de scan
        self.fm_min = 87.5e6   # 87.5 MHz
        self.fm_max = 108e6    # 108 MHz
        self.step = 0.1e6      # 100 kHz steps
        self.dwell_time = 0.5  # 0.5 secondes par fréquence

        # Seuil de détection (ajuster selon environnement)
        self.threshold = 0.01  # Seuil de puissance normalisée

    def measure_power(self, frequency):
        """Mesure la puissance à une fréquence donnée"""
        self.sdr.center_freq = frequency
        time.sleep(0.1)  # Stabilité

        # Capture d'échantillons
        samples = self.sdr.read_samples(1024 * 256)  # 256k échantillons

        # Calcul de puissance (moyenne des carrés)
        power = np.mean(np.abs(samples)**2)

        return power

    def scan_band(self):
        """Scanne toute la bande FM"""
        print("Début du scan FM...")
        print("=" * 50)

        frequencies = np.arange(self.fm_min, self.fm_max, self.step)
        results = {}

        for i, freq in enumerate(frequencies):
            power = self.measure_power(freq)

            # Affichage progressif
            progress = (i + 1) / len(frequencies) * 100
            print(f"\rProgression: {progress:.1f}% - {freq/1e6:.1f} MHz", end="", flush=True)

            # Stockage si signal détecté
            if power > self.threshold:
                results[freq] = power

        print("\nScan terminé !")
        return results

    def display_results(self, results):
        """Affiche les résultats du scan"""
        if not results:
            print("Aucune station FM détectée.")
            return

        print("\nStations FM détectées:")
        print("-" * 30)

        # Tri par puissance décroissante
        sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

        for freq, power in sorted_results:
            freq_mhz = freq / 1e6
            power_db = 10 * np.log10(power)
            print(".1f")

        return sorted_results

    def plot_spectrum(self, results):
        """Trace le spectre des signaux détectés"""
        if not results:
            print("Pas de données à tracer.")
            return

        frequencies = [f/1e6 for f in results.keys()]
        powers_db = [10 * np.log10(p) for p in results.values()]

        plt.figure(figsize=(12, 6))
        plt.scatter(frequencies, powers_db, c='red', s=50, alpha=0.7)
        plt.xlabel('Fréquence (MHz)')
        plt.ylabel('Puissance (dB)')
        plt.title('Stations FM détectées')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def close(self):
        """Ferme proprement le SDR"""
        self.sdr.close()

def main():
    """Fonction principale"""
    print("Scanner FM - SDR")
    print("Assurez-vous que votre RTL-SDR est connecté")
    print()

    # Initialisation
    scanner = FMScanner(ppm=0, gain=30)

    try:
        # Scan
        results = scanner.scan_band()

        # Affichage résultats
        sorted_results = scanner.display_results(results)

        # Sauvegarde optionnelle
        save = input("\nSauvegarder les résultats ? (o/N): ").lower().strip()
        if save == 'o':
            filename = f"fm_scan_{int(time.time())}.txt"
            with open(filename, 'w') as f:
                f.write("Fréquence (MHz)\tPuissance (dB)\n")
                for freq, power in sorted_results:
                    f.write(".1f")
            print(f"Résultats sauvegardés dans {filename}")

        # Graphique
        plot = input("Afficher le graphique ? (o/N): ").lower().strip()
        if plot == 'o':
            scanner.plot_spectrum(dict(sorted_results))

    except KeyboardInterrupt:
        print("\nScan interrompu par l'utilisateur.")

    except Exception as e:
        print(f"Erreur: {e}")
        print("Vérifiez que votre SDR est connecté et les drivers installés.")

    finally:
        scanner.close()

if __name__ == "__main__":
    main()
