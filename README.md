# Projet de Simulation du Système Solaire

## 🌌 Introduction
Bienvenue dans le projet de Simulation du Système Solaire ! Cette simulation basée sur Python utilise la bibliothèque Pygame pour créer une représentation dynamique des planètes de notre système solaire, montrant leurs mouvements et interactions basés sur les forces gravitationnelles.

## 🚀 Fonctionnalités
- Simuler les mouvements planétaires dans un espace 2D.
- Interactions gravitationnelles réalistes entre les planètes.
- Représentation visuelle des planètes incluant le Soleil, la Terre, Mars, Vénus, et d'autres.
- Affichage des distances et noms pour chaque planète.

## 🛠️ Installation

### Prérequis
- Python 3.x
- Bibliothèque Pygame

### Configuration
1. Cloner le dépôt :
```bash
git clone https://github.com/votre-repertoire/simulation-systeme-solaire.git
```
2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## 🎮 Comment Exécuter
Exécutez le script `main.py` pour démarrer la simulation :
```bash
python src/main.py
```

## 📂 Structure du Projet
- `src/main.py` : Le point d'entrée principal pour la simulation.
- `src/entities/planet.py` : Définit la classe `Planet` avec des attributs et méthodes pour chaque planète.
- `src/managers/planet_manager.py` : Gère la création et les mises à jour des planètes dans la simulation.
- `core/globals.py` : Contient les variables et paramètres globaux.
- `core/game.py`: Initialise pygame

## 🧑‍🔬 Coulisses

### Dynamique des Planètes
Chaque planète est une instance de la classe `Planet`, avec des propriétés telles que le nom, la position, la vitesse et la masse. La simulation met à jour la position de chaque planète en fonction des forces gravitationnelles.

### Rendu
La bibliothèque Pygame est utilisée pour le rendu des planètes et de leurs orbites. Chaque planète est dessinée comme un cercle, avec son orbite dépeinte comme une ligne traçant son chemin.

## 🤝 Contribuer
Les contributions au projet sont les bienvenues ! Veuillez suivre ces étapes :
1. Forkez le dépôt.
2. Créez une nouvelle branche pour votre fonctionnalité.
3. Commitez vos changements.
4. Poussez vers la branche et ouvrez une demande de tirage (pull request).

## 📜 Licence
Ce projet est sous licence [MIT License](LICENSE).
