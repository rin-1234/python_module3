import random

ALL_ACHIEVEMENTS = [
    'Boss Slayer',
    'Collector Supreme',
    'Crafting Genius',
    'First Steps',
    'Master Explorer',
    'Sharp Mind',
    'Speed Runner',
    'Strategist',
    'Survivor',
    'Treasure Hunter'
]

def get_player_achievements():
    num = random.randint(1,10)
    achivements = set(random.sample(ALL_ACHIEVEMENTS, num))
    return achivements


def main():
    print("=== Achievement Tracker System ===")

    all_achievements = set(ALL_ACHIEVEMENTS)

    alice = get_player_achievements()
    bob = get_player_achievements()
    charlie = get_player_achievements()
    dylan = get_player_achievements()



    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print(f"All distict achievement: {alice.union(bob, charlie, dylan)}")
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}")

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    
    print(f"Alice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")

if __name__ == "__main__":
    main()