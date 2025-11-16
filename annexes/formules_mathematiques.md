# 📐 Formules Mathématiques - SDR et Télécommunications

## Électromagnétisme & Propagation

### Lois de Maxwell (forme différentielle)
```
∇ × E = -∂B/∂t    (loi de Faraday)
∇ × H = J + ∂D/∂t  (loi d'Ampère-Maxwell)
∇ · D = ρ          (loi de Gauss électrique)
∇ · B = 0          (loi de Gauss magnétique)
```

### Équation d'onde électromagnétique
```
∇²E - (1/c²)∂²E/∂t² = μ₀ ∂J/∂t    (équation d'onde)
```

Où :
- E : champ électrique (V/m)
- H : champ magnétique (A/m)
- c : vitesse lumière = 3×10⁸ m/s
- μ₀ : perméabilité vide = 4π×10⁻⁷ H/m

### Vitesse de propagation
```
c = 1/√(μ₀ ε₀) = 299 792 458 m/s
```

### Relation fréquence-longueur d'onde
```
λ = c / f    (longueur d'onde en mètres)
```

Exemples :
- f = 100 MHz → λ = 3 m
- f = 1 GHz → λ = 0.3 m
- f = 10 GHz → λ = 3 cm

## Théorie du Signal

### Transformée de Fourier (continue)
```
X(f) = ∫ x(t) e^(-j2πft) dt    (transformée)
x(t) = ∫ X(f) e^(j2πft) df     (transformée inverse)
```

### Transformée de Fourier discrète (DFT)
```
X[k] = Σ(n=0 à N-1) x[n] e^(-j2πkn/N)    pour k = 0 à N-1
```

### Théorème de Nyquist-Shannon
```
f_s ≥ 2 f_max    (fréquence d'échantillonnage minimale)
```

Où f_max est la fréquence maximale du signal.

### Rapport signal/bruit (SNR)
```
SNR = 10 log₁₀(P_signal / P_bruit)    (en dB)
SNR = P_signal / P_bruit              (ratio linéaire)
```

### Rapport Eb/N0 (énergie par bit sur densité bruit)
```
Eb/N0 = (S/N) × (f_s / débit)    (en dB)
```

## Modulations Analogiques

### Modulation d'amplitude (AM)
```
Signal modulé : s(t) = [A + m(t)] cos(2π f_c t)

Où :
- A : amplitude porteuse
- m(t) : signal modulant (normalisé -1 à +1)
- f_c : fréquence porteuse

Bande passante : 2 × bande passante de m(t)
```

### Modulation de fréquence (FM)
```
s(t) = A cos(2π f_c t + 2π k_f ∫ m(τ) dτ)

Où :
- k_f : constante de déviation (Hz/V)
- Déviation maximale : Δf = k_f × amplitude_max de m(t)

Bande passante approximative (règle de Carson) :
B = 2(Δf + f_m) où f_m = fréquence maximale de m(t)
```

### Modulation de phase (PM)
```
s(t) = A cos(2π f_c t + k_p m(t))

Où :
- k_p : constante de modulation de phase (rad/V)
- Déviation de phase maximale : Δφ = k_p × amplitude_max
```

## Modulations Numériques

### Probabilité d'erreur binaire (BER)

#### Canal AWGN - BPSK
```
Pe = Q(√(2 Eb/N0))    où Q(x) = ∫_x^∞ (1/√(2π)) e^(-t²/2) dt
```

#### Canal AWGN - QPSK (identique à BPSK)
```
Pe = Q(√(2 Eb/N0))
```

#### Canal AWGN - M-QAM
```
Pe ≈ (4/√M) Q(√(3 log₂M × 2 Eb/N0 / (M-1)))
```

### Capacité de canal (théorème de Shannon)
```
C = B log₂(1 + SNR)    (bits/seconde)

Où :
- C : capacité maximale
- B : bande passante (Hz)
- SNR : rapport signal/bruit
```

### Efficacité spectrale
```
η = débit / bande passante    (bits/s/Hz)
```

## Traitement Numérique du Signal

### Filtre FIR (Réponse Impulsionnelle Finie)
```
y[n] = Σ(k=0 à M) b_k x[n-k]

Ordre du filtre : M
Fréquence de coupure : f_c / (f_s/2)
```

### Filtre IIR (Réponse Impulsionnelle Infinie)
```
y[n] = Σ(k=0 à M) b_k x[n-k] - Σ(k=1 à N) a_k y[n-k]

Fonction de transfert : H(z) = Σ b_k z^-k / (1 + Σ a_k z^-k)
```

### Transformée de Fourier rapide (FFT)
```
Complexité : O(N log N) au lieu de O(N²) pour DFT
Taille optimale : puissance de 2
Résolution fréquentielle : f_s / N
```

### Corrélation croisée
```
R_xy[k] = Σ n x[n] y*[n+k]    (pour signaux complexes)
```

### Convolution
```
y[n] = Σ k x[k] h[n-k] = x[n] * h[n]
```

Propriété : TF{y} = TF{x} × TF{h}

## Propagation & Antennes

### Atténuation en espace libre
```
L_fs = (4π d f / c)²    (en puissance, linéaire)
L_fs_dB = 32.4 + 20 log₁₀(d) + 20 log₁₀(f)    (en dB)

Où :
- d : distance (km)
- f : fréquence (MHz)
```

### Gain d'antenne isotrope
```
Gain (dBi) = 10 log₁₀(Directivité)
```

### Longueur d'antenne dipôle
```
L = λ/2 = c/(2f)    (dipôle demi-onde)
L = λ/4 = c/(4f)    (monopôle quart d'onde)
```

### Rapport onde stationnaire (VSWR)
```
VSWR = (1 + |Γ|) / (1 - |Γ|)    où Γ = coefficient de réflexion
VSWR = (Z_L - Z_0) / (Z_L + Z_0)   pour ligne adaptée (Z_0 = 50Ω)
```

## Puissance & Mesures RF

### Unités de puissance
```
dBm = 10 log₁₀(P_mW)          P_mW = puissance en milliwatts
dBW = 10 log₁₀(P_W)            P_W = puissance en watts
dBm = dBW + 30
```

### EIRP (Effective Isotropic Radiated Power)
```
EIRP = P_tx + G_antenne - Pertes    (en dBm)
```

### Budget de liaison
```
P_rx = P_tx + G_tx + G_rx - L_path - L_misc    (en dB)
```

Où :
- P_tx : puissance transmise
- G_tx, G_rx : gains d'antenne
- L_path : pertes de propagation
- L_misc : autres pertes (câbles, etc.)

## Synchronisation & Estimation

### Boucle à verrouillage de phase (PLL)
```
Erreur de phase : e(t) = sin(φ_error)
Fréquence de coupure : ω_n = 2π f_n
Facteur d'amortissement : ζ
```

### Filtre de Kalman (estimation)
```
Prédiction : x̂_k = F x̂_{k-1} + B u_k
Correction : x̂_k = x̂_k + K (z_k - H x̂_k)

Matrice de gain : K = P H^T (H P H^T + R)^-1
```

### Algorithme LMS (Least Mean Squares)
```
Erreur : e_k = d_k - y_k
Mise à jour : w_{k+1} = w_k + μ e_k x_k

Pas d'adaptation : μ (typiquement 0.01 à 0.1)
```

## Statistiques & Probabilités

### Distribution Gaussienne (normale)
```
f(x) = (1/√(2π σ²)) exp(-(x-μ)²/(2σ²))

Moyenne : μ
Variance : σ²
Écart-type : σ
```

### Fonction Q (queue de distribution normale)
```
Q(x) = ∫_x^∞ (1/√(2π)) exp(-t²/2) dt

Approximation : Q(x) ≈ (1/√(2π x²)) exp(-x²/2) pour x > 3
```

### Théorème central limite
```
Somme de variables aléatoires indépendantes → distribution normale
Moyenne : μ_total = Σ μ_i
Variance : σ²_total = Σ σ²_i
```

## Théorie de l'Information

### Entropie (Shannon)
```
H(X) = -Σ p(x_i) log₂ p(x_i)    (bits)

Entropie maximale : H(X) ≤ log₂ M    (M états possibles)
```

### Capacité de canal bruité
```
C = max I(X;Y) = max H(Y) - H(Y|X) = B log₂(1 + SNR)
```

### Codage correcteur d'erreurs
```
Taux de code : r = k/n    (k bits utiles, n bits transmis)
Gain de codage : dB d'amélioration pour même BER
```

## Constantes Physiques

### Constantes fondamentales
```
c = 299 792 458 m/s          (vitesse lumière)
μ₀ = 4π × 10^-7 H/m         (perméabilité vide)
ε₀ = 8.854 × 10^-12 F/m     (permittivité vide)
k = 1.381 × 10^-23 J/K      (constante Boltzmann)
h = 6.626 × 10^-34 J⋅s      (constante Planck)
```

### Constantes dérivées
```
Z₀ = √(μ₀/ε₀) = 376.73 Ω    (impédance espace libre)
k_B T = 4.00 × 10^-21 J      (énergie thermique à 290K)
```

## Conversion d'unités

### Fréquences
```
1 Hz = 1 s^-1
1 kHz = 10^3 Hz
1 MHz = 10^6 Hz
1 GHz = 10^9 Hz
```

### Puissances
```
0 dBm = 1 mW = 10^-3 W
10 dBm = 10 mW
20 dBm = 100 mW = 0.1 W
30 dBm = 1 W
40 dBm = 10 W
```

### Distances
```
1 m = 100 cm = 1000 mm
1 km = 1000 m
1 mile = 1.609 km
```

### Angles
```
360° = 2π radians
1° = π/180 radians ≈ 0.0175 rad
1 radian ≈ 57.3°
```

## Tableaux de conversion

### dB vers ratio linéaire
```
dB │ Ratio │ Application
────┼───────┼────────────
 0  │ 1.00  │ référence
 3  │ 2.00  │ double puissance
 6  │ 4.00  │
10  │ 10.0  │ décade
20  │ 100   │ puissance ×100
30  │ 1000  │ puissance ×1000
```

### Bits vers symboles
```
Bits/symbole │ Symboles │ Modulation typique
─────────────┼──────────┼───────────────────
1            │ 2        │ BPSK
2            │ 4        │ QPSK
3            │ 8        │ 8-PSK
4            │ 16       │ 16-QAM
6            │ 64       │ 64-QAM
8            │ 256      │ 256-QAM
```

---

*Ces formules constituent la base mathématique du SDR. Elles sont essentielles pour comprendre et calculer les performances des systèmes de communication.*
