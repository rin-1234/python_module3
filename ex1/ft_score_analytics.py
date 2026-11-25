import sys


def main() -> None:
    scores = []
    argc = len(sys.argv)

    if argc < 2:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    list_len = len(scores)
    if list_len == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    print(f"Scores Processed: {scores}")
    print(f"Total players: {list_len}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / list_len}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    main()
