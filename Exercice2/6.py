import praw

# Définition de la connexion à Reddit
headers = {
    "User-Agent": "mypython/2.0 (kevinadagbe@gmail.com)"  # Ton user agent personnalisé
}

# Configuration de PRAW pour se connecter à Reddit
reddit = praw.Reddit(
    client_id="TON_CLIENT_ID",          # Remplace avec ton client ID
    client_secret="TON_CLIENT_SECRET",  # Remplace avec ton client secret
    user_agent="mypython/2.0 (kevinadagbe@gmail.com)",  # Ton User-Agent
        # Remplace avec ton nom d'utilisateur Reddit
        # Remplace avec ton mot de passe Reddit
)

# Recherche dans un subreddit (ex : "python")
subreddit = reddit.subreddit("python")

# Afficher les 5 premiers posts populaires dans le subreddit "python"
for post in subreddit.hot(limit=5):
    print(f"Title: {post.title}")
    print(f"Score: {post.score}")
    print(f"URL: {post.url}")
    print(f"Author: {post.author}")
    print("-" * 40)
