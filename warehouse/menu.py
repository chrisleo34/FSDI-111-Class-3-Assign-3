import os


def print_menu():
    print("-*-" * 10)
    print("Warehouse Mgn Sys")
    print("Auto Inventory Management")
    print("-*-" * 10)

    print("[1] Register New Item")
    print("[2] Display Catalog")

    print("[6] Out of stock Catalog")
    print("[7] Total stock value")
    print("[8] List of categories")
    print("[x] Close")


def print_item(item):
    print(
        str(item.id).rjust(3)
        + " | " + item.title.ljust(25)
                + " | " + item.category.ljust(12)
                + " | $" + str(item.price).rjust(15)
                + " | " + str(item.stock).rjust(12)
    )
    print('-' * 90)


def print_header(title):
    clear()
    print("-" * 90)
    print(title)
    print("-" * 90)


def do_not_duplicate(item):
    for title in catalog:
        if str(item.id) > 1:
            str(item.id).remove(item.id)
    print(item)


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')
