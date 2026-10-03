import sys

inventory = {"magic_item": 90}

def find_max_item(arg: dict) -> str:
    max_item = ""
    value = 0
    for key in arg:
        if value < arg[key]:
            value = arg[key]
            max_item = key
    return max_item

def find_min_item(arg: dict) -> str:
    min_item = ""
    value = float('inf')
    for key in arg:
        if value > arg[key]:
            value = arg[key]
            min_item = key
    return min_item
        

def validate_item(arg: list, new_items: dict) -> None:
    if len(arg) != 2:
        raise ValueError(f"Expected 2 arguments, but {len(arg)} were provided. : {arg}")
    
    key, value = arg

    if key in new_items:
        raise ValueError(f"Redundant item {key} - discarding")
    # valueをintへ
    if int(value) < 0:
        raise ValueError(f"Invalid Value {value}: {arg}")

def receive_items() -> dict:
    argc = len(sys.argv)
    new_items = {}
    if argc < 2:
        print("No new items added")
        return
    
    for i in range(1, argc):
        try:
            entity =sys.argv[i].split(":")
            validate_item(entity, new_items)
            new_items.update([[entity[0], int(entity[1])]])
        except ValueError as e:
            print(f"Error - {e}")
            continue
    
    return new_items

def print_inventory(new_items: dict) -> None:
    total_items = sum(new_items.values())
    print(f"Got inventory: {new_items}")
    print(f"Item list: {new_items.keys()}")
    print(f"Total quantity of the {len(new_items.keys())} items {total_items}")

    for key in new_items:
        value = new_items[key]
        print(f"Item {key} represents {round(value / total_items * 100, 1)}%")

    max_item = find_max_item(new_items)
    min_item = find_min_item(new_items)
    print(f"Item most abundant: {max_item} with quantity {new_items[max_item]}")
    print(f"Item least abundant: {min_item} with quantity {new_items[min_item]}")
    inventory.update(new_items)
    print(f"Updated inventory: {inventory}")

def main():
    new_items = receive_items()
    print_inventory(new_items)

if __name__ == "__main__":
    main()