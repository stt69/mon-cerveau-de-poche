#!/usr/bin/env python3
"""
Lanceur de Mon Cerveau de Poche.
Démarre le serveur Streamlit et ouvre le navigateur.
"""

import subprocess
import sys
import os
import socket
import webbrowser
import time
import signal


def port_libre():
    """Trouve un port TCP libre."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]


def main():
    # Répertoire de l'application
    app_dir = os.path.dirname(os.path.abspath(__file__))
    app_py = os.path.join(app_dir, 'app.py')
    config_dir = os.path.join(app_dir, '.streamlit')

    # Variables d'environnement
    env = os.environ.copy()
    env['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'
    if os.path.isdir(config_dir):
        env['STREAMLIT_CONFIG_DIR'] = config_dir

    port = port_libre()

    # Lancer Streamlit
    process = subprocess.Popen(
        [
            sys.executable, '-m', 'streamlit', 'run', app_py,
            f'--server.port={port}',
            '--server.headless=true',
            '--server.address=127.0.0.1',
            '--browser.gatherUsageStats=false',
            '--global.developmentMode=false',
        ],
        env=env,
        cwd=app_dir,
    )

    # Attendre que le serveur soit prêt
    for _ in range(30):
        time.sleep(0.5)
        try:
            with socket.create_connection(('127.0.0.1', port), timeout=1):
                break
        except (ConnectionRefusedError, OSError):
            continue

    # Ouvrir le navigateur
    webbrowser.open(f'http://localhost:{port}')

    # Gérer l'arrêt propre
    def arreter(sig, frame):
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
        sys.exit(0)

    signal.signal(signal.SIGTERM, arreter)
    signal.signal(signal.SIGINT, arreter)

    try:
        process.wait()
    except KeyboardInterrupt:
        arreter(None, None)


if __name__ == '__main__':
    main()
