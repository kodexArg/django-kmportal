import os

# Obtén el ID de la ventana de Chrome.
window_id = os.popen('xdotool search --name "Chrome"').read().split()[0]

# Usa xdotool para enviar la tecla F5 a la ventana de Chrome.
os.system(f'xdotool key --window {window_id} F5')

