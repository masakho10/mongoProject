# Backend de l'Application

Ce repository contient le code source du backend de l'application web qui fournit une API RESTful pour accéder aux données de la base de données MongoDB.

  Installation

1. Clonez ce dépôt :

   #bash
   git clone https://github.com/masakho10/mongoProject
   

2. Accédez au répertoire du projet :



3. Installez les dépendances :

   Il est conseiller d'executer le code dans un environement virtuel avec la commande (installer les paquets ci-dessous)
   
   #bash
   python3 -m venv venv

  #bash
   source venv/bin/activate
   

  Configuration

- Assurez-vous que MongoDB est en cours d'exécution sur votre machine.

  Utilisation

1. Démarrez le serveur Flask :

   #bash
   python app.py
   

2. L'API sera accessible à l'adresse suivante :

   
   http://localhost:5000
  

  Endpoints

- '/' : Renvoie un message de bienvenue indiquant que vous avez atteint le backend de l'application.
- '/publis' : Récupère toutes les publications stockées dans la base de données MongoDB.
- '/publi/<title>' : Récupère les détails d'une publication spécifique, identifiée par son titre.



