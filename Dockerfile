# Utiliser l'image officielle de Python comme image de base
FROM python:3.12

LABEL authors="cfredj"

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur au répertoire de travail
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du projet dans le conteneur
COPY . .


RUN chmod -R 777 .
# Exposer le port sur lequel l'application va tourner
EXPOSE 8200

# Définir la commande par défaut pour exécuter le serveur de développement
CMD ["python", "manage.py", "runserver", "0.0.0.0:8200"]
