"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    test_profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.3,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
        },
        "Adversarial Conflicting Profile": {
            "genre": "rock",
            "mood": "moody",
            "energy": 0.95,
        },
    }

    for profile_name, user_prefs in test_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{profile_name}")
        print(f"Preferences: {user_prefs}")
        print("Top recommendations:\n")

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()