import random
import typing

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "move", "eat", "grab", "sleep"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)


def main() -> None:
    gen = gen_event()
    events = []
    for i in range(1000):
        data = next(gen)
        print(f"Event{i}: Player {data[0]} did action {data[1]}")

    for i in range(10):
        event = next(gen)
        events.append(event)

    print(f"Built list of 10 events: {events}")

    consume = consume_event(events)
    for eve in consume:
        print(f"Got event from list: {eve}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
