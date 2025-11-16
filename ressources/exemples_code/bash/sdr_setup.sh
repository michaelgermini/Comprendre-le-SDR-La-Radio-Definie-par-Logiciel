#!/bin/bash
#
# SDR Setup Script
# Configuration automatique d'un environnement SDR sous Linux
#
# Utilisation: ./sdr_setup.sh [option]
# Options:
#   --full     : Installation complète
#   --minimal  : Installation minimale
#   --update   : Mise à jour des paquets
#   --test     : Test des installations
#

set -e  # Arrêt en cas d'erreur

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Fonctions d'affichage
print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}  SDR Environment Setup${NC}"
    echo -e "${BLUE}================================${NC}"
}

print_step() {
    echo -e "${GREEN}[STEP]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# Vérification des droits root
check_root() {
    if [[ $EUID -eq 0 ]]; then
        print_error "Ne pas exécuter en tant que root !"
        exit 1
    fi
}

# Détection de la distribution
detect_distro() {
    if [[ -f /etc/debian_version ]]; then
        DISTRO="debian"
        PACKAGE_MANAGER="apt"
    elif [[ -f /etc/redhat-release ]]; then
        DISTRO="redhat"
        PACKAGE_MANAGER="dnf"
    elif [[ -f /etc/arch-release ]]; then
        DISTRO="arch"
        PACKAGE_MANAGER="pacman"
    else
        print_error "Distribution non supportée"
        exit 1
    fi

    print_step "Distribution détectée: $DISTRO ($PACKAGE_MANAGER)"
}

# Mise à jour du système
update_system() {
    print_step "Mise à jour du système..."

    case $PACKAGE_MANAGER in
        apt)
            sudo apt update && sudo apt upgrade -y
            ;;
        dnf)
            sudo dnf update -y
            ;;
        pacman)
            sudo pacman -Syu --noconfirm
            ;;
    esac

    print_success "Système mis à jour"
}

# Installation des dépendances de base
install_base_deps() {
    print_step "Installation des dépendances de base..."

    case $PACKAGE_MANAGER in
        apt)
            sudo apt install -y build-essential cmake git libfftw3-dev \
                libboost-all-dev libcppunit-dev swig python3-dev \
                python3-pip python3-numpy python3-scipy python3-matplotlib \
                libgtk-3-dev libcanberra-gtk-module
            ;;
        dnf)
            sudo dnf install -y gcc gcc-c++ cmake git fftw-devel \
                boost-devel cppunit-devel swig python3-devel \
                python3-pip numpy scipy matplotlib gtk3-devel
            ;;
        pacman)
            sudo pacman -S --noconfirm base-devel cmake git fftw \
                boost cppunit swig python python-pip python-numpy \
                python-scipy python-matplotlib gtk3
            ;;
    esac

    print_success "Dépendances de base installées"
}

# Installation de GNU Radio
install_gnuradio() {
    print_step "Installation de GNU Radio..."

    # Création du répertoire de build
    mkdir -p ~/sdr_build
    cd ~/sdr_build

    # Téléchargement
    if [[ ! -d "gnuradio" ]]; then
        git clone --recursive https://github.com/gnuradio/gnuradio.git
    fi
    cd gnuradio

    # Configuration et compilation
    mkdir -p build
    cd build

    cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DPYTHON_EXECUTABLE=/usr/bin/python3 ..
    make -j$(nproc)
    sudo make install

    # Mise à jour des liens
    sudo ldconfig

    print_success "GNU Radio installé"
}

# Installation des drivers SDR
install_sdr_drivers() {
    print_step "Installation des drivers SDR..."

    cd ~/sdr_build

    # RTL-SDR
    if [[ ! -d "rtl-sdr" ]]; then
        git clone https://github.com/osmocom/rtl-sdr.git
    fi
    cd rtl-sdr
    mkdir -p build && cd build
    cmake ..
    make -j$(nproc)
    sudo make install

    # HackRF
    cd ~/sdr_build
    if [[ ! -d "hackrf" ]]; then
        git clone https://github.com/greatscottgadgets/hackrf.git
    fi
    cd hackrf/host
    mkdir -p build && cd build
    cmake ..
    make -j$(nproc)
    sudo make install

    # LimeSDR
    cd ~/sdr_build
    if [[ ! -d "LimeSuite" ]]; then
        git clone https://github.com/myriadrf/LimeSuite.git
    fi
    cd LimeSuite
    mkdir -p build && cd build
    cmake ..
    make -j$(nproc)
    sudo make install

    # Mise à jour des règles udev
    sudo cp ~/sdr_build/rtl-sdr/rtl-sdr.rules /etc/udev/rules.d/
    sudo cp ~/sdr_build/hackrf/host/libhackrf/53-hackrf.rules /etc/udev/rules.d/
    sudo udevadm control --reload-rules

    print_success "Drivers SDR installés"
}

# Installation des bibliothèques Python
install_python_libs() {
    print_step "Installation des bibliothèques Python..."

    pip3 install --user pyrtlsdr pyModeS scikit-dsp-comm

    print_success "Bibliothèques Python installées"
}

# Installation d'applications SDR
install_sdr_apps() {
    print_step "Installation des applications SDR..."

    cd ~/sdr_build

    # GQRX
    case $PACKAGE_MANAGER in
        apt)
            sudo apt install -y gqrx-sdr
            ;;
        dnf)
            sudo dnf install -y gqrx
            ;;
        pacman)
            sudo pacman -S --noconfirm gqrx
            ;;
    esac

    # SDR++ (compilation)
    if [[ ! -d "SDRPlusPlus" ]]; then
        git clone https://github.com/AlexandreRouma/SDRPlusPlus.git
    fi
    cd SDRPlusPlus
    mkdir -p build && cd build
    cmake ..
    make -j$(nproc)
    sudo make install

    print_success "Applications SDR installées"
}

# Tests des installations
test_installations() {
    print_step "Test des installations..."

    # Test GNU Radio
    if command -v gnuradio-companion &> /dev/null; then
        print_success "GNU Radio: OK"
    else
        print_error "GNU Radio: ÉCHEC"
    fi

    # Test RTL-SDR
    if command -v rtl_test &> /dev/null; then
        print_success "RTL-SDR: OK"
    else
        print_error "RTL-SDR: ÉCHEC"
    fi

    # Test HackRF
    if command -v hackrf_info &> /dev/null; then
        print_success "HackRF: OK"
    else
        print_error "HackRF: ÉCHEC"
    fi

    # Test GQRX
    if command -v gqrx &> /dev/null; then
        print_success "GQRX: OK"
    else
        print_error "GQRX: ÉCHEC"
    fi
}

# Configuration finale
final_setup() {
    print_step "Configuration finale..."

    # Ajout au PATH si nécessaire
    if [[ ":$PATH:" != *":/usr/local/bin:"* ]]; then
        echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc
        source ~/.bashrc
    fi

    # Création des répertoires de travail
    mkdir -p ~/sdr_projects ~/sdr_captures

    # Règles udev pour accès utilisateur
    sudo usermod -a -G plugdev $USER

    print_success "Configuration terminée"
    print_warning "Redémarrez votre session ou exécutez 'newgrp plugdev' pour appliquer les changements de groupe"
}

# Menu principal
show_help() {
    echo "Usage: $0 [OPTION]"
    echo "Configuration automatique d'un environnement SDR"
    echo ""
    echo "Options:"
    echo "  --full      Installation complète (recommandé)"
    echo "  --minimal   Installation minimale (GNU Radio + RTL-SDR)"
    echo "  --update    Mise à jour du système uniquement"
    echo "  --test      Test des installations existantes"
    echo "  --help      Afficher cette aide"
}

# Fonction principale
main() {
    local option="${1:-}"

    print_header
    check_root

    case $option in
        --full)
            detect_distro
            update_system
            install_base_deps
            install_gnuradio
            install_sdr_drivers
            install_python_libs
            install_sdr_apps
            final_setup
            test_installations
            ;;
        --minimal)
            detect_distro
            install_base_deps
            install_gnuradio
            install_sdr_drivers
            final_setup
            ;;
        --update)
            detect_distro
            update_system
            ;;
        --test)
            test_installations
            ;;
        --help|*)
            show_help
            ;;
    esac

    print_success "Script terminé !"
    echo ""
    echo "Prochaines étapes:"
    echo "1. Connectez votre SDR"
    echo "2. Lancez 'gqrx' pour tester"
    echo "3. Consultez la documentation pour les premiers pas"
}

# Exécution
main "$@"
