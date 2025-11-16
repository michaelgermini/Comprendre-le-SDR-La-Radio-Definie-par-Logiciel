% FM Demodulation Example
% Démonstration de démodulation FM avec MATLAB
%
% Prérequis: MATLAB avec Communications Toolbox
%
% Utilisation: fm_demodulation

clear all; close all; clc;

%% Paramètres du signal
fs = 48000;         % Fréquence d'échantillonnage (Hz)
fc = 100e6;         % Fréquence porteuse (100 MHz)
fm_dev = 75e3;      % Déviation FM (75 kHz)
duration = 2;       % Durée du signal (secondes)

%% Génération du signal audio de test
t = 0:1/fs:duration-1/fs;
audio_freq = 1000;  % Ton de test à 1 kHz
audio_signal = sin(2*pi*audio_freq*t);

%% Modulation FM
% Signal FM: y(t) = cos(2πfc t + 2π fm_dev ∫ m(τ)dτ)
phase_dev = 2*pi*fm_dev * cumsum(audio_signal)/fs;
fm_signal = cos(2*pi*fc*t + phase_dev);

%% Démodulation FM
% Méthode: différentiation puis enveloppe
diff_signal = diff(fm_signal);
envelope = abs(hilbert(diff_signal));

% Normalisation
demodulated = envelope / max(abs(envelope));

%% Filtrage du signal démodulé
% Filtre passe-bas pour supprimer les hautes fréquences
[b, a] = butter(6, audio_freq*2/fs, 'low');
filtered_audio = filter(b, a, demodulated);

%% Affichage des résultats
figure('Name', 'FM Modulation/Demodulation', 'Position', [100, 100, 1200, 800]);

% Signal original
subplot(4,1,1);
plot(t(1:1000), audio_signal(1:1000));
title('Signal audio original (1 kHz)');
xlabel('Temps (s)');
ylabel('Amplitude');
grid on;

% Signal FM modulé (portion)
subplot(4,1,2);
plot(t(1:1000), fm_signal(1:1000));
title('Signal FM modulé (portion)');
xlabel('Temps (s)');
ylabel('Amplitude');
grid on;

% Spectre du signal FM
subplot(4,1,3);
[S, F] = pwelch(fm_signal, [], [], [], fs);
plot(F/1e6, 10*log10(S));
title('Spectre du signal FM');
xlabel('Fréquence (MHz)');
ylabel('Puissance (dB)');
xlim([fc/1e6 - 0.2, fc/1e6 + 0.2]);
grid on;

% Signal démodulé
subplot(4,1,4);
plot(t(1:2000), filtered_audio(1:2000));
title('Signal audio démodulé');
xlabel('Temps (s)');
ylabel('Amplitude');
grid on;

%% Calcul de la qualité
% Rapport signal/bruit
noise_power = var(filtered_audio - audio_signal');
snr = 10*log10(var(audio_signal) / noise_power);
fprintf('Rapport signal/bruit: %.2f dB\n', snr);

%% Lecture audio (optionnel)
% Pour écouter le résultat
% sound(filtered_audio, fs);

%% Fonction de modulation FM (pour référence)
function y = fm_modulate(signal, fc, fs, freq_dev)
    % Modulation FM
    t = (0:length(signal)-1)/fs;
    phase_dev = 2*pi*freq_dev * cumsum(signal)/fs;
    y = cos(2*pi*fc*t + phase_dev);
end

%% Fonction de démodulation FM (pour référence)
function y = fm_demodulate(signal, fs, freq_dev)
    % Démodulation FM par différentiation
    diff_sig = diff([0, signal]);  % Ajout d'un échantillon pour compenser diff
    y = diff_sig .* imag(hilbert(signal));
    y = y / (2*pi*freq_dev/fs);  % Normalisation
end
