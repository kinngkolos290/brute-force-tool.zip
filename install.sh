#!/bin/bash
echo "Installation de l'outil de brute force..."

pkg update -y
pkg install python -y
pip install requests

echo "Installation terminée. Tu peux lancer le script avec : python brute.py"
