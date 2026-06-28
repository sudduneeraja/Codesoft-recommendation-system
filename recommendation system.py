import os
# ============================================================
# MOVIE DATASET
# ============================================================

movies = [
    {"id": 1, "title": "Inception", "genre": "Sci-Fi", "rating": 8.8,
     "description": "A thief enters people's dreams to steal secrets."},

    {"id": 2, "title": "Interstellar", "genre": "Sci-Fi", "rating": 8.7,
     "description": "Astronauts search for a new home for humanity."},

    {"id": 3, "title": "The Dark Knight", "genre": "Action", "rating": 9.0,
     "description": "Batman faces the Joker in Gotham City."},

    {"id": 4, "title": "Avengers: Endgame", "genre": "Action", "rating": 8.4,
     "description": "The Avengers fight Thanos in the final battle."},

    {"id": 5, "title": "Titanic", "genre": "Romance", "rating": 7.9,
     "description": "A love story aboard the Titanic."},

    {"id": 6, "title": "The Notebook", "genre": "Romance", "rating": 7.8,
     "description": "A touching love story across decades."},

    {"id": 7, "title": "The Conjuring", "genre": "Horror", "rating": 7.5,
     "description": "Paranormal investigators help a haunted family."},

    {"id": 8, "title": "It", "genre": "Horror", "rating": 7.3,
     "description": "Children confront an evil clown."},

    {"id": 9, "title": "Finding Nemo", "genre": "Animation", "rating": 8.2,
     "description": "A clownfish searches for his lost son."},

    {"id": 10, "title": "Toy Story", "genre": "Animation", "rating": 8.3,
     "description": "Toys come to life when humans aren't around."},

    {"id": 11, "title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3,
     "description": "A banker forms friendships in prison."},

    {"id": 12, "title": "Forrest Gump", "genre": "Drama", "rating": 8.8,
     "description": "The extraordinary life journey of Forrest."},

    {"id": 13, "title": "The Hangover", "genre": "Comedy", "rating": 7.7,
     "description": "Friends wake up after a wild bachelor party."},

    {"id": 14, "title": "3 Idiots", "genre": "Comedy", "rating": 8.4,
     "description": "Engineering students learn life lessons."},

    {"id": 15, "title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7,
     "description": "A hacker discovers reality is a simulation."},

    {"id": 16, "title": "Gladiator", "genre": "Action", "rating": 8.5,
     "description": "A Roman general seeks revenge."},

    {"id": 17, "title": "Coco", "genre": "Animation", "rating": 8.4,
     "description": "A boy journeys to the Land of the Dead."},

    {"id": 18, "title": "Parasite", "genre": "Drama", "rating": 8.6,
     "description": "Two families become unexpectedly connected."},

    {"id": 19, "title": "A Quiet Place", "genre": "Horror", "rating": 7.5,
     "description": "A family survives creatures attracted by sound."},

    {"id": 20, "title": "La La Land", "genre": "Romance", "rating": 8.0,
     "description": "A musician and actress pursue their dreams."}
]

# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def print_line():
    print("=" * 60)


# ============================================================
# CORE FEATURES
# ============================================================

def view_all_movies():
    print_line()
    print(f"{'ID':<4}{'Title':<30}{'Genre':<15}{'Rating'}")
    print_line()

    for m in movies:
        print(f"{m['id']:<4}{m['title']:<30}{m['genre']:<15}{m['rating']}")


def search_movie():
    keyword = input("\nEnter movie title: ").lower().strip()

    if not keyword:
        print("Empty input not allowed.")
        return

    found = False

    for m in movies:
        if keyword in m["title"].lower():
            if not found:
                print_line()
                print("SEARCH RESULTS")
                print_line()
                found = True

            print(f"{m['id']} - {m['title']} ({m['genre']}) | Rating: {m['rating']}")

    if not found:
        print("No movie found.")


def view_movie_details():
    try:
        movie_id = int(input("\nEnter Movie ID: "))

        for m in movies:
            if m["id"] == movie_id:
                print_line()
                print("MOVIE DETAILS")
                print_line()
                print(f"Title       : {m['title']}")
                print(f"Genre       : {m['genre']}")
                print(f"Rating      : {m['rating']}")
                print(f"Description : {m['description']}")
                return

        print("Movie not found.")

    except ValueError:
        print("Invalid input. Enter numeric ID.")


def display_top_rated():
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)

    print_line()
    print("TOP RATED MOVIES")
    print_line()

    for i, m in enumerate(sorted_movies[:5], 1):
        print(f"{i}. {m['title']} ({m['genre']}) - ⭐ {m['rating']}")


def get_available_genres():
    return sorted(set(m["genre"] for m in movies))


def display_genres():
    print("\nAvailable Genres:")
    for i, g in enumerate(get_available_genres(), 1):
        print(f"{i}. {g}")


# ============================================================
# AI RECOMMENDATION ENGINE
# ============================================================

def recommend_movies():
    print("\nAI MOVIE RECOMMENDATION SYSTEM")
    print_line()

    user_genre = input("Preferred genre (optional): ").strip().lower()
    user_keywords = input("Keywords (optional): ").strip().lower()

    results = []

    for m in movies:
        score = 0

        # Genre match (high weight)
        if user_genre and user_genre == m["genre"].lower():
            score += 5

        # Rating boost
        score += m["rating"] * 0.6

        # Keyword matching
        text = (m["title"] + " " + m["description"]).lower()

        for word in user_keywords.split():
            if word in text:
                score += 3

        results.append((m, score))

    results.sort(key=lambda x: x[1], reverse=True)

    print_line()
    print("TOP RECOMMENDATIONS")
    print_line()

    for m, score in results[:5]:
        print(f"{m['title']} ({m['genre']})")
        print(f"Rating: {m['rating']} | Score: {round(score, 2)}")
        print("-" * 50)


# ============================================================
# MAIN MENU
# ============================================================

def main():
    while True:
        clear_screen()
        print_line()
        print("MINI AI MOVIE RECOMMENDER")
        print_line()

        print("1. View All Movies")
        print("2. Search Movie")
        print("3. AI Recommendations")
        print("4. View Movie Details")
        print("5. Top Rated Movies")
        print("6. View Genres")
        print("7. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            view_all_movies()
            pause()

        elif choice == "2":
            search_movie()
            pause()

        elif choice == "3":
            recommend_movies()
            pause()

        elif choice == "4":
            view_movie_details()
            pause()

        elif choice == "5":
            display_top_rated()
            pause()

        elif choice == "6":
            display_genres()
            pause()

        elif choice == "7":
            print("\nExiting... Goodbye!")
            break

        else:
            print("Invalid choice!")
            pause()


# RUN PROGRAM
if __name__ == "__main__":
    main()