# Chapitre 8 : DSP (Traitement numérique du signal)

## 8.1 Échantillonnage et fréquence de Nyquist

### Théorème de Nyquist-Shannon

Le théorème fondamental de l'échantillonnage stipule qu'un signal continu peut être parfaitement reconstruit à partir de ses échantillons si la fréquence d'échantillonnage est supérieure au double de la fréquence maximale du signal.

#### Formulation mathématique
Si un signal x(t) est limité en bande à B Hz, alors :
```
f_s ≥ 2B
```

Où f_s est la fréquence d'échantillonnage.

#### Conséquences pratiques
- **Sous-échantillonnage** : f_s < 2B → repliement de spectre (aliasing)
- **Sur-échantillonnage** : f_s >> 2B → marge de sécurité
- **Échantillonnage critique** : f_s = 2B

### Conversion analogique-numérique (ADC)

#### Processus d'échantillonnage
1. **Filtrage anti-aliasing** : Suppression des fréquences > f_s/2
2. **Échantillonnage** : Conversion temps discret
3. **Quantification** : Conversion amplitude discrète
4. **Codage** : Représentation binaire

#### Paramètres importants
- **Résolution** : Nombre de bits (8, 12, 14, 16 bits typiques)
- **Rapport signal/bruit** : SNR = 6.02N + 1.76 dB (N = bits)
- **Erreur de quantification** : ±0.5 LSB

### Fréquences d'échantillonnage standards

#### SDR courants
- **RTL-SDR** : 2.4 MHz maximum
- **HackRF One** : 20 MHz
- **LimeSDR** : 30.72 MHz (multiple de 61.44 MHz ÷ 2)
- **USRP B210** : 56 MHz

#### Applications spécifiques
- **Audio** : 44.1 kHz, 48 kHz, 96 kHz
- **Télévision** : 6 MHz (bande passante)
- **Radar** : Dépend de la portée souhaitée

### Effets du sous-échantillonnage

#### Repliement de spectre (Aliasing)
Quand f_s < 2f_max, les fréquences hautes se replient dans la bande de base :
```
f_alias = |f_signal - k × f_s|
```

#### Exemple concret
Signal à 30 MHz échantillonné à 20 MHz :
- f_alias = |30 - 1×20| = 10 MHz
- Le signal de 30 MHz apparaît à 10 MHz

### Échantillonnage en quadrature (I/Q)

#### Principe
Au lieu d'échantillonner le signal réel, on échantillonne ses composantes I (In-phase) et Q (Quadrature) :
```
x(t) = I(t) × cos(2πf_c t) - Q(t) × sin(2πf_c t)
```

#### Avantages
- **Largeur de bande réduite** : Bande de base au lieu de RF
- **Précision de phase** : Conservation de l'information de phase
- **Traitement simplifié** : Tous les calculs en bande de base

#### Implémentation
```python
import numpy as np

def quadrature_sampling(signal, f_carrier, f_sample):
    t = np.arange(len(signal)) / f_sample
    I = signal * np.cos(2 * np.pi * f_carrier * t)
    Q = signal * np.sin(2 * np.pi * f_carrier * t)
    return I + 1j * Q
```

## 8.2 Filtres (FIR, IIR)

### Filtres numériques

Les filtres numériques permettent de modifier la composition spectrale d'un signal en atténuant ou amplifiant certaines fréquences.

#### Classification
- **Passe-bas** : Fréquences basses passent, hautes atténuées
- **Passe-haut** : Fréquences hautes passent, basses atténuées
- **Passe-bande** : Bande de fréquences spécifique
- **Coupe-bande** : Atténuation d'une bande spécifique

### Filtres FIR (Finite Impulse Response)

#### Propriétés
- **Réponse impulsionnelle finie** : h[n] = 0 pour n < 0 et n ≥ N
- **Stabilité garantie** : Pas de pôles instables
- **Phase linéaire possible** : Déphasage constant vs fréquence
- **Complexité** : Ordre N généralement plus élevé que IIR

#### Conception
```python
import numpy as np
from scipy import signal

def fir_lowpass(cutoff, numtaps, fs):
    # Filtre passe-bas FIR
    nyquist = fs / 2
    normalized_cutoff = cutoff / nyquist
    return signal.firwin(numtaps, normalized_cutoff, window='hamming')

# Exemple : Filtre passe-bas 10 kHz, 51 coefficients, fs=48 kHz
fir_coeffs = fir_lowpass(10000, 51, 48000)
```

#### Fenêtrage
- **Rectangulaire** : Lobe principal étroit, lobes secondaires importants
- **Hamming** : Bon compromis
- **Blackman** : Lobe principal plus large, lobes secondaires faibles

### Filtres IIR (Infinite Impulse Response)

#### Propriétés
- **Réponse impulsionnelle infinie** : h[n] ≠ 0 pour tout n
- **Efficacité** : Moins de coefficients pour même performance
- **Risque d'instabilité** : Pôles peuvent être instables
- **Phase non-linéaire** : Déphasage variable

#### Types courants
- **Butterworth** : Réponse plate dans la bande passante
- **Chebyshev** : Ondulations dans bande passante, plus sélectif
- **Elliptique** : Ondulations dans les deux bandes, très sélectif

#### Conception
```python
from scipy import signal

def iir_lowpass(cutoff, order, fs, btype='butter'):
    nyquist = fs / 2
    normalized_cutoff = cutoff / nyquist

    if btype == 'butter':
        return signal.butter(order, normalized_cutoff)
    elif btype == 'cheby1':
        return signal.cheby1(order, 1, normalized_cutoff)  # 1 dB ripple

# Exemple : Filtre Butterworth passe-bas 10 kHz, ordre 4
b, a = iir_lowpass(10000, 4, 48000, 'butter')
```

### Comparaison FIR vs IIR

| Critère | FIR | IIR |
|---------|-----|-----|
| Stabilité | Toujours stable | Peut être instable |
| Phase linéaire | Possible | Difficile |
| Complexité | Plus de coefficients | Moins de coefficients |
| Mémoire | Plus de mémoire | Moins de mémoire |
| Robustesse | Très robuste | Sensible aux coefficients |

### Applications en SDR

#### Filtrage canal
- Extraction d'un signal dans une bande fréquentielle donnée
- Suppression des signaux adjacents

#### Correction d'erreurs
- Compensation des imperfections du SDR
- Correction IQ (déséquilibre entre voies I et Q)

#### Démodulation
- Filtres adaptés pour optimisation du rapport S/N
- Filtres racine de cosinus surélevé (RCOS)

## 8.3 FFT et analyse spectrale

### Transformée de Fourier discrète (DFT)

La DFT convertit un signal du domaine temporel vers le domaine fréquentiel :

```
X[k] = Σ(n=0 à N-1) x[n] × e^(-j2πkn/N)
```

#### Propriétés
- **Réversibilité** : La transformée inverse existe
- **Symétrie** : X[N-k] = X[k]*
- **Énergie conservée** : Σ|x[n]|² = (1/N) Σ|X[k]|²

### Transformée de Fourier rapide (FFT)

#### Algorithme de Cooley-Tukey
L'FFT exploite la périodicité et la symétrie pour réduire la complexité :
- **Complexité DFT** : O(N²)
- **Complexité FFT** : O(N log N)

#### Conditions d'application
- Longueur de signal = puissance de 2 (padding sinon)
- Signal périodique (fenêtrage pour signaux finis)

### Analyse spectrale en temps réel

#### Fenêtrage
Le fenêtrage réduit les effets de bord :
```python
import numpy as np

def apply_window(signal, window_type='hann'):
    if window_type == 'hann':
        return signal * np.hanning(len(signal))
    elif window_type == 'hamming':
        return signal * np.hamming(len(signal))
    elif window_type == 'blackman':
        return signal * np.blackman(len(signal))

# Application
windowed_signal = apply_window(signal)
fft_result = np.fft.fft(windowed_signal)
```

#### Résolution fréquentielle
```
Δf = f_s / N
```

Où N est la taille de la FFT.

#### Lissage spectral
- **Averaging** : Moyennage de plusieurs FFT
- **Exponentielle** : Pondération temporelle
- **Welch** : Méthode de périodogramme moyenné

### Visualisation spectrale

#### Spectrogramme
Représentation temps-fréquence :
```python
import matplotlib.pyplot as plt
from scipy import signal

def plot_spectrogram(signal, fs, nperseg=1024):
    f, t, Sxx = signal.spectrogram(signal, fs, nperseg=nperseg)
    plt.pcolormesh(t, f, 10 * np.log10(Sxx))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.show()

# Utilisation
plot_spectrogram(audio_signal, 48000)
```

#### Waterfall display
Accumulation temporelle de spectres :
- Chaque ligne = FFT à un instant t
- Couleur = puissance spectrale
- Défilement temporel

### Applications en SDR

#### Analyse de signaux inconnus
- Identification de modulations
- Détection de signaux cachés
- Mesure de la pureté spectrale

#### Mesure de performances
- Rapport signal/bruit
- Distorsion harmonique
- Occupation spectrale

#### Débogage
- Vérification des filtres
- Contrôle de la stabilité fréquentielle
- Diagnostic des interférences

## 8.4 Décodage des modulations numériques

### Démarche générale de décodage

#### Étapes du processus
1. **Synchronisation** : Alignement temporel et fréquentiel
2. **Égalisation** : Correction des distorsions de canal
3. **Démodulation** : Extraction des symboles
4. **Décodage** : Récupération des bits
5. **Correction d'erreurs** : Amélioration de la fiabilité

### Démodulation PSK

#### BPSK (Binary Phase Shift Keying)
- 2 symboles : 0° et 180°
- Décision simple : signe de la partie réelle

```python
def demodulate_bpsk(samples):
    # Synchronisation de phase supposée
    symbols = np.real(samples) > 0  # Seuillage
    return symbols.astype(int)
```

#### QPSK (Quadrature Phase Shift Keying)
- 4 symboles : 45°, 135°, 225°, 315°
- Décodage par quadrants

```python
def demodulate_qpsk(samples):
    I = np.real(samples)
    Q = np.imag(samples)

    symbols = np.zeros(len(samples), dtype=int)
    symbols[(I > 0) & (Q > 0)] = 0  # 00
    symbols[(I < 0) & (Q > 0)] = 1  # 01
    symbols[(I < 0) & (Q < 0)] = 2  # 11
    symbols[(I > 0) & (Q < 0)] = 3  # 10

    return symbols
```

### Démodulation QAM

#### Constellation QAM
- **16-QAM** : 16 points en grille carrée
- **64-QAM** : 64 points
- **256-QAM** : 256 points

#### Décodage
```python
def demodulate_16qam(samples):
    # Normalisation
    samples = samples / np.max(np.abs(samples))

    I = np.real(samples)
    Q = np.imag(samples)

    # Quantification
    I_levels = np.array([-3, -1, 1, 3]) / 3
    Q_levels = np.array([-3, -1, 1, 3]) / 3

    I_symbols = np.argmin(np.abs(I[:, np.newaxis] - I_levels), axis=1)
    Q_symbols = np.argmin(np.abs(Q[:, np.newaxis] - Q_levels), axis=1)

    # Conversion en bits
    bits = np.zeros((len(samples), 4), dtype=int)
    bits[:, 0] = (I_symbols >> 1) & 1
    bits[:, 1] = I_symbols & 1
    bits[:, 2] = (Q_symbols >> 1) & 1
    bits[:, 3] = Q_symbols & 1

    return bits.flatten()
```

### Démodulation OFDM

#### Principe OFDM
- Division en sous-porteuses orthogonales
- FFT pour séparation des sous-porteuses
- Égalisation par sous-porteuse

#### Implémentation simplifiée
```python
def demodulate_ofdm(signal, fft_size, cp_length):
    # Suppression du préfixe cyclique
    useful_samples = signal[cp_length:cp_length + fft_size]

    # FFT
    symbols = np.fft.fft(useful_samples)

    # Égalisation (simplifiée)
    # Dans la pratique : utiliser pilotes ou préambules
    equalized = symbols / channel_estimate

    # Démodulation par sous-porteuse
    bits = []
    for subcarrier in equalized:
        # Démodulation QAM par sous-porteuse
        subcarrier_bits = demodulate_qam(subcarrier)
        bits.extend(subcarrier_bits)

    return np.array(bits)
```

### Synchronisation

#### Synchronisation fréquentielle
Correction de l'erreur de fréquence porteuse :
```python
def frequency_sync(samples, expected_freq, fs):
    # Méthode par corrélation
    phase_offset = np.angle(np.sum(samples * np.conj(expected_pilot)))
    freq_offset = phase_offset * fs / (2 * np.pi * len(samples))

    # Correction
    t = np.arange(len(samples)) / fs
    correction = np.exp(-1j * 2 * np.pi * freq_offset * t)
    return samples * correction
```

#### Synchronisation temporelle
Détection du début des symboles :
```python
def timing_sync(samples, pattern):
    # Corrélation avec séquence connue
    correlation = np.correlate(samples, pattern, mode='full')
    peak_index = np.argmax(np.abs(correlation))

    # Extraction des symboles synchronisés
    return samples[peak_index:peak_index + len(pattern)]
```

## 8.5 Corrélation et synchronisation

### Corrélation croisée

La corrélation mesure la similarité entre deux signaux :
```
R[k] = Σ x[n] × y[n+k]
```

#### Applications
- **Détection de signaux** : Recherche de patterns connus
- **Estimation de délai** : Mesure du retard de propagation
- **Synchronisation** : Alignement temporel

### Détection de préambules

#### Préambules connus
- **Barker codes** : Séquences à autocorrélation idéale
- **M-séquences** : Séquences pseudo-aléatoires
- **Gold codes** : Pour GPS

#### Exemple de détection
```python
def detect_preamble(signal, preamble):
    correlation = np.correlate(signal, preamble, mode='full')
    peaks = np.where(np.abs(correlation) > threshold)[0]

    if len(peaks) > 0:
        return peaks[0] - len(preamble) + 1  # Position du début
    else:
        return None
```

### Synchronisation d'horloge

#### Récupération d'horloge
Extraction de la fréquence d'horloge à partir du signal :
```python
def clock_recovery(samples, samples_per_symbol):
    # Méthode de Mueller-Muller simplifiée
    error = np.zeros(len(samples))

    for i in range(1, len(samples)):
        # Calcul de l'erreur de timing
        current = samples[i]
        previous = samples[i-1]
        error[i] = np.real(current * np.conj(previous))

    # Filtrage de l'erreur
    filtered_error = np.convolve(error, [0.1, 0.2, 0.3, 0.2, 0.1], mode='same')

    # Interpolation pour correction
    timing_correction = np.cumsum(filtered_error) * 0.01

    return timing_correction
```

### Estimation de canal

#### Canal statique
Estimation simple par pilote :
```python
def estimate_channel(rx_pilots, tx_pilots):
    # Division élément par élément
    channel_est = rx_pilots / tx_pilots

    # Lissage fréquentiel
    channel_est_smooth = np.convolve(channel_est, np.ones(5)/5, mode='same')

    return channel_est_smooth
```

#### Canal sélectif en fréquence
Utilisation de l'algorithme LMS :
```python
def lms_equalizer(input_signal, desired_signal, num_taps=11, step_size=0.01):
    # Initialisation
    weights = np.zeros(num_taps, dtype=complex)
    output = np.zeros(len(input_signal), dtype=complex)

    for i in range(num_taps, len(input_signal)):
        # Signal d'entrée (fenêtre)
        x = input_signal[i-num_taps:i]

        # Sortie du filtre
        y = np.dot(weights, x)

        # Erreur
        e = desired_signal[i] - y

        # Mise à jour des coefficients
        weights += step_size * np.conj(e) * x

        output[i] = y

    return output, weights
```

## 8.6 Analyse d'un signal bruité

### Modèles de bruit

#### Bruit blanc gaussien (AWGN)
- **Distribution** : Gaussienne centrée
- **Puissance spectrale** : Constante
- **Modèle** : x[n] = s[n] + w[n], w[n] ~ N(0, σ²)

#### Bruit coloré
- **Bruit 1/f** : Puissance décroissante avec la fréquence
- **Bruit impulsionnel** : Impulsions sporadiques
- **Interférences** : Signaux non désirés

### Mesure du rapport signal/bruit

#### SNR en puissance
```
SNR = 10 log₁₀(P_signal / P_bruit)
```

#### Estimation
```python
def estimate_snr(signal, noise_samples=None):
    if noise_samples is None:
        # Méthode par percentiles
        signal_power = np.mean(np.abs(signal)**2)
        noise_power = np.mean(np.abs(signal - np.mean(signal))**2)
    else:
        # Mesure directe du bruit
        noise_power = np.mean(np.abs(noise_samples)**2)
        signal_power = np.mean(np.abs(signal)**2)

    snr = 10 * np.log10(signal_power / noise_power)
    return snr
```

### Débruitage et amélioration

#### Filtrage adaptatif
- **Wiener filter** : Minimisation de l'erreur quadratique moyenne
- **Kalman filter** : Pour signaux variant lentement
- **Wavelets** : Décomposition multi-résolution

#### Exemple de filtre Wiener
```python
def wiener_filter(signal, noise_variance, signal_variance):
    # Facteur de Wiener
    wiener_factor = signal_variance / (signal_variance + noise_variance)

    # FFT pour filtrage fréquentiel
    signal_fft = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal))

    # Application du filtre
    filtered_fft = signal_fft * wiener_factor

    # Transformée inverse
    filtered_signal = np.fft.ifft(filtered_fft)

    return np.real(filtered_signal)
```

### Détection en présence de bruit

#### Détection de seuil
- **Critère de Neyman-Pearson** : Maximisation de la probabilité de détection pour fausse alarme fixée
- **Seuil adaptatif** : Ajustement selon l'estimation du bruit

#### Exemple de détection binaire
```python
def binary_detection(samples, threshold):
    # Seuillage simple
    decisions = np.abs(samples) > threshold
    return decisions.astype(int)

def adaptive_threshold(samples, false_alarm_rate=0.01):
    # Tri des échantillons par amplitude
    sorted_samples = np.sort(np.abs(samples))

    # Calcul du seuil pour taux de fausse alarme souhaité
    index = int((1 - false_alarm_rate) * len(sorted_samples))
    threshold = sorted_samples[index]

    return threshold
```

### Analyse de performance

#### Taux d'erreur binaire (BER)
```
BER = (Nombre d'erreurs) / (Nombre total de bits)
```

#### Fonction de performance
- **ROC curve** : Taux de détection vs taux de fausse alarme
- **Capacité de canal** : Débit maximum en fonction du SNR

#### Simulation Monte Carlo
```python
def monte_carlo_ber(snr_range, num_trials=1000):
    ber_results = []

    for snr in snr_range:
        errors = 0
        total_bits = 0

        for trial in range(num_trials):
            # Génération signal + bruit
            signal = generate_signal()
            noisy_signal = add_noise(signal, snr)

            # Détection
            detected = detect_signal(noisy_signal)

            # Comptage erreurs
            errors += np.sum(detected != signal)
            total_bits += len(signal)

        ber = errors / total_bits
        ber_results.append(ber)

    return ber_results
```

### Applications pratiques

#### Communications fiables
- **Codage correcteur d'erreurs** : Reed-Solomon, LDPC
- **Modulations robustes** : BPSK au lieu de 256-QAM à faible SNR
- **Diversité** : Antennes multiples, fréquences multiples

#### Détection de signaux faibles
- **Intégration longue** : Accumulation temporelle
- **Filtrage adapté** : Optimisation du rapport S/N
- **Techniques d'angle** : Utilisation de la phase

#### Analyse spectrale avancée
- **Détection de signaux cachés** : Recherche de faibles émissions
- **Classification automatique** : Identification de modulations
- **Monitoring environnemental** : Détection de changements
