import random

PLAYERS = [
    'Alice',
    'bob',
    'Charlie',
    'dylan',
    'Emma',
    'Gregory',
    'john',
    'kevin',
    'Liam',
]


def main() -> None:
    print(f"Initial list of players: {PLAYERS}")

    all_name_capitalized = [p.capitalize() for p in PLAYERS]
    print(f"New list with all names capitalized: {all_name_capitalized}")

    capitalized_name_only = [p for p in PLAYERS if p == p.capitalize()]
    print(f"New list of capitalized names only: {capitalized_name_only}")

    scores_dict = {p: random.randint(1, 1000) for p in all_name_capitalized}
    print(f"Score dict: {scores_dict}")

    score_average = round(sum(scores_dict.values()) / len(scores_dict), 2)
    print(f"Score average is {score_average}")

    high_scores_dict = {
        p: scores_dict[p] for p in scores_dict
        if scores_dict[p] > score_average
    }
    print(f"High scores: {high_scores_dict}")


if __name__ == "__main__":
    main()
