import requests
import random

API_KEY = 'c093a6ac2edf4daf4108b2ac09265733'
BASE_URL = 'https://api.themoviedb.org/3'

def get_genres():
    """Fetches the list of movie genres from TMDb."""
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json().get('genres', [])
        return {genre['name'].lower(): genre['id'] for genre in genres}
    else:
        print("Failed to retrieve genres.")
        return {}

def get_movies_by_genre(genre_id):
    """Fetches movies of a specific genre from TMDb."""
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print("Failed to retrieve movies for the selected genre.")
        return []

def recommend_movie():
    genres = get_genres()
    if not genres:
        return

    print("Available genres:")
    for genre in genres:
        print(f"- {genre.capitalize()}")

    user_genre = input("\nEnter a genre from the list above: ").lower()
    genre_id = genres.get(user_genre)

    if not genre_id:
        print("Invalid genre selected.")
        return

    movies = get_movies_by_genre(genre_id)
    if not movies:
        print(f"No movies found for the genre: {user_genre.capitalize()}")
        return

    recommended_movie = random.choice(movies)
    title = recommended_movie.get('title', 'Unknown Title')
    overview = recommended_movie.get('overview', 'No overview available.')

    print("\nMovie Recommendation:")
    print(f"Title: {title}")
    print(f"Overview: {overview}")

if __name__ == "__main__":
    recommend_movie()
