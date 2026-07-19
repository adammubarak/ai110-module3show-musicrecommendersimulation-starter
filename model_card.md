# 🎧 Model Card: Music Recommender Simulation
## 1. Model Name

**VibeMatch 1.0**

---

## 2. Intended Use

VibeMatch 1.0 is a classroom music recommender simulation. Its goal is to predict which songs may best match a user's preferred genre, mood, and energy level. It is designed for students learning how content-based recommendation systems score and rank items.

This system is not intended to replace a real music platform or make important decisions about real users. It should not be used as proof of a person's full musical taste because it uses a small fictional dataset and only a few preferences.

## 3. How the Model Works

The recommender compares every song in the catalog with a user preference profile. Each song contains features including genre, mood, energy, tempo, valence, danceability, and acousticness. However, the current scoring function uses genre, mood, and energy.

A song receives `+2.0` points when its genre matches the user's preferred genre and `+1.0` point when its mood matches the user's preferred mood. Energy is scored based on how close the song's energy is to the user's target energy. A smaller difference produces a higher energy score.

After every song receives a score, the system sorts the songs from highest score to lowest score and returns the top recommendations. The implementation also provides reasons explaining which parts of the user's profile contributed to each score.

## 4. Data

The recommender uses a CSV catalog containing 18 songs. The starter dataset originally contained 10 songs, and I added 8 fictional songs to increase the variety of genres and moods.

The catalog includes genres such as pop, lofi, rock, soul, country, classical, hip hop, folk, disco, funk, and reggae. It also includes moods such as happy, chill, intense, dreamy, nostalgic, reflective, playful, hopeful, romantic, triumphant, and serene.

Each song includes an ID, title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The dataset is still small and does not represent every genre, culture, artist style, language, or type of musical preference.

## 5. Strengths

The system works well when a user's preferences clearly match songs in the catalog. For example, the High-Energy Pop profile correctly ranked `Sunrise City` first because it matched the requested genre and mood and had energy close to the user's target.

The Chill Lofi and Deep Intense Rock profiles also produced results that matched my expectations. The scoring process is transparent because every recommendation includes a numeric score and specific reasons. This makes it easy to understand why one song ranked above another.

## 6. Limitations and Bias 
The recommender uses a small catalog of only 18 songs, so it can repeatedly recommend the same tracks and create a filter bubble. It also gives points only for exact genre and mood matches, which means a song with a similar style or feeling may be ranked too low just because its label is different. The system represents user taste with only genre, mood, and energy, so it does not account for artist preference, tempo, lyrics, era, or users who enjoy multiple genres. The experiments also showed that the rankings are sensitive to the chosen weights, because changing the importance of genre and energy caused noticeable shifts in the results.

## 7. Evaluation  

### High-Energy Pop

```
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.9}

Sunrise City - Score: 4.84
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.84)

Gym Hero - Score: 3.94
Because: genre match (+2.0), energy similarity (+1.94)

Rooftop Lights - Score: 2.72
Because: mood match (+1.0), energy similarity (+1.72)

Storm Runner - Score: 1.98
Because: energy similarity (+1.98)

Sunset Circuit - Score: 1.96
Because: energy similarity (+1.96)
```

### Chill Lofi

```
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.3}

Library Rain - Score: 4.90
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.90)

Midnight Coding - Score: 4.76
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.76)

Focus Flow - Score: 3.80
Because: genre match (+2.0), energy similarity (+1.80)

Spacewalk Thoughts - Score: 2.96
Because: mood match (+1.0), energy similarity (+1.96)

Glass Skyline - Score: 1.98
Because: energy similarity (+1.98)
```

### Deep Intense Rock

```
Preferences: {'genre': 'rock', 'mood': 'intense', 'energy': 0.9}

Storm Runner - Score: 4.98
Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.98)

Gym Hero - Score: 2.94
Because: mood match (+1.0), energy similarity (+1.94)

Sunset Circuit - Score: 1.96
Because: energy similarity (+1.96)

Sunrise City - Score: 1.84
Because: energy similarity (+1.84)

Backbeat Bloom - Score: 1.82
Because: energy similarity (+1.82)
```

### Adversarial Conflicting Profile

```
Preferences: {'genre': 'rock', 'mood': 'moody', 'energy': 0.95}

Storm Runner - Score: 3.92
Because: genre match (+2.0), energy similarity (+1.92)

Night Drive Loop - Score: 2.60
Because: mood match (+1.0), energy similarity (+1.60)

Gym Hero - Score: 1.96
Because: energy similarity (+1.96)

Sunset Circuit - Score: 1.86
Because: energy similarity (+1.86)

Sunrise City - Score: 1.74
Because: energy similarity (+1.74)
```
### Accuracy and Surprises

The High-Energy Pop results felt accurate because `Sunrise City` matched the requested genre, mood, and target energy. It ranked first with a score of 4.84 because it received `+2.0` for matching pop, `+1.0` for matching happy, and `+1.84` for having energy close to 0.9.

The result makes sense, but the experiment also showed a limitation. The system only considers a few features, so a lower-ranked song could still feel better to a real listener because the recommender does not consider artist preference, tempo, or other personal details.

### Weight Shift Experiment

I tested the system by reducing the genre bonus from `+2.0` to `+1.0` and increasing the energy multiplier from `2.0` to `4.0`. This made energy similarity much more influential in the rankings.

The recommendations became different rather than clearly more accurate. For example, in the Chill Lofi profile, `Spacewalk Thoughts` moved above `Focus Flow` because its energy was closer to the user's target, even though `Focus Flow` matched the preferred lofi genre. This experiment showed that small weight changes can strongly affect which songs appear near the top.

### Profile Comparisons

The High-Energy Pop and Chill Lofi profiles produced very different results because their target genres, moods, and energy levels were almost opposites. The pop profile favored upbeat songs such as `Sunrise City`, while the lofi profile favored calmer songs such as `Library Rain` and `Midnight Coding`.

The High-Energy Pop and Deep Intense Rock profiles both preferred high-energy songs, so some energetic tracks appeared in both lists. However, the genre and mood bonuses caused `Sunrise City` to rank first for pop and `Storm Runner` to rank first for rock.

The Chill Lofi and Deep Intense Rock profiles showed the clearest contrast. The lofi profile rewarded low-energy and chill songs, while the rock profile rewarded intense songs with energy close to 0.9.

The Adversarial Conflicting Profile showed that the recommender can struggle with mixed preferences. `Storm Runner` ranked first because its rock genre and high energy earned more points, even though it did not match the requested moody mood.

One surprising result was that `Gym Hero` appeared near the top of multiple high-energy profiles. This happened because its energy was very close to the target, even when it did not match every requested genre or mood.

## 8. Future Work

Future versions could use more song features, including tempo, valence, danceability, and acousticness, when calculating scores. The user profile could also support multiple favorite genres and moods instead of requiring only one exact choice.

The system could improve recommendation diversity by limiting repeated genres or adding a novelty bonus for songs that are slightly different from the user's normal preferences. A larger and more balanced dataset would also reduce filter bubbles and better represent different musical tastes. Recommendation explanations could be expanded to show how every numerical feature affected the final score.

---

## 9. Personal Reflection

My biggest learning moment was seeing how much the scoring weights affected the recommendations. When I reduced the genre weight and increased the energy weight, some songs changed positions even though the dataset and user profiles stayed the same. This showed me that recommendation results depend heavily on choices made by the developer.

AI tools helped me understand recommendation concepts, suggest test profiles, generate additional song data, and implement parts of the Python code. However, I still needed to double-check the AI's suggestions against the actual starter files, tests, dataset columns, and project instructions. Sometimes the suggested design was more complicated than the code structure required, so I had to keep the solution aligned with the real project.

I was surprised that a simple formula using only genre, mood, and energy could still produce recommendations that felt reasonable. At the same time, the experiments showed that simple systems can miss good songs, repeat similar results, and create filter bubbles.

If I continued developing this project, I would use more features such as tempo, valence, danceability, and acousticness. I would also support multiple favorite genres and add more diverse songs to the dataset.