import time
import requests

# Configuration de l'API
API_KEY = '27eb3dad670d407da0ca23be5513c838'
BASE_URL = 'https://api.football-data.org/v4'

headers = {'X-Auth-Token': API_KEY}

# Fonction pour faire une requête API
def fetch_data(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur lors de la récupération des données : {response.status_code}")
        return None

# Fonction pour obtenir les statistiques d'une équipe
def get_team_stats(team_id):
    team_data = fetch_data(f'/teams/{team_id}')
    if team_data:
        print(f"Statistiques pour l'équipe {team_data['name']}:")
        # Affichage des statistiques, ou calculs si nécessaire
        # ...

# Fonction d’analyse complète pour une équipe
def analyze_team_performance(team_id):
    print(f"\n--- Analyse complète de l'équipe ID {team_id} ---")
    get_team_stats(team_id)
    # Ajouter d'autres analyses, comme les performances récentes, forme, etc.
    # ...

# Fonction principale du robot
def run_robot():
    team_ids = [64, 65]  # Exemples d'IDs d'équipes, ajouter celles que tu veux analyser
    while True:
        for team_id in team_ids:
            analyze_team_performance(team_id)
        print("\nAnalyse terminée pour cette itération. Attente avant la prochaine exécution...")
        time.sleep(86400)  # Attente de 24 heures

# Lancer le robot
run_robot()
 

