@echo off
echo ================================================
echo   SmartCity Django — Setup Automatique
echo   FST Tanger 2025/2026
echo ================================================
echo.

echo [1/4] Installation des dependances...
py -3.12 -m pip install django --quiet
echo OK

echo [2/4] Creation des tables (migrations)...
py -3.12 manage.py makemigrations
py -3.12 manage.py migrate
echo OK

echo [3/4] Population de la base de donnees...
py -3.12 manage.py shell < seed_data.py
echo OK

echo [4/4] Lancement du serveur...
echo.
echo   Ouvrez votre navigateur sur : http://127.0.0.1:8000
echo   Connexion : admin / admin123
echo.
py -3.12 manage.py runserver

pause
