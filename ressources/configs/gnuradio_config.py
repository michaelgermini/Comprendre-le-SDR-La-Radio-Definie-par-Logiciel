# Configuration GNU Radio par défaut
# Fichier: ~/.gnuradio/config.conf
# Copiez ce fichier dans votre répertoire home

[DEFAULT]
# Répertoire des projets
grc_project_dir = ~/sdr_projects

# Éditeur externe (optionnel)
external_editor = gedit

# Options de génération
generate_options = qt_gui
run_options = prompt

# Paramètres par défaut pour les blocs
default_sample_rate = 2e6
default_center_freq = 100e6

# Options de performance
realtime_scheduling = True
max_nouts = 0

# Interface
show_block_comments = True
show_block_ids = False
show_param_expr = True

# Thème (dark/light)
qt_gui_theme = default

# Raccourcis clavier personnalisés
# copy_shortcut = Ctrl+C
# paste_shortcut = Ctrl+V
# delete_shortcut = Delete

# Paramètres de débogage
log_level = info
log_file = ~/.gnuradio/gnuradio.log
