import math


def get_player_pos():
    while True:
        input_str = input("Enter new coordinates as floats in format 'x,y,z':")
        parts = input_str.split(",")
        if len(parts) != 3:
            print("Invaild syntax")
            continue

        try:
            coordinates = tuple(float(p) for p in parts)
        except ValueError as e:
            print(f"Error on parameter :{e}")
            continue
        break

    return coordinates


def calc_distance(parts1, parts2):
    distance = math.sqrt(
        (parts2[0] - parts1[0]) ** 2
        + (parts2[1] - parts1[1]) ** 2
        + (parts2[2] - parts1[2]) ** 2
    )
    return distance


def main():
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coordinates = get_player_pos()
    print(f"Got a first tuple: {coordinates}")
    print(f"It includes: X={coordinates[0]}, Y={coordinates[1]}, Z={coordinates[2]}")
    origin = (0.0, 0.0, 0.0)
    distance = calc_distance(origin, coordinates)
    print(f"Distance to center:{distance:.4f}")
    print()

    print("Get a second set of coordinates")
    coordinates2 = get_player_pos()
    distance2 = calc_distance(coordinates, coordinates2)
    print(f"Distance between the 2 sets of coordinates:{distance2:.4f}")


if __name__ == "__main__":
    main()
