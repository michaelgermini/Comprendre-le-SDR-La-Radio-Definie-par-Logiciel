# Exemples de code SDR

Ce dossier contient des exemples de code pratiques pour différents cas d'usage SDR.

## Structure

```
exemples_code/
├── python/           # Scripts Python
├── gnuradio/         # Flows GNU Radio
├── matlab/           # Scripts MATLAB
└── bash/            # Scripts shell
```

## Utilisation

### Python
```bash
pip install numpy scipy matplotlib pyrtlsdr
python python/scan_fm.py
```

### GNU Radio
```bash
gnuradio-companion gnuradio/fm_receiver.grc
```

### MATLAB
```matlab
% Dans MATLAB avec Communications Toolbox
run(matlab/fm_demodulation.m)
```

## Licence

Tous les exemples sont sous licence MIT. Utilisez-les librement pour vos projets.
