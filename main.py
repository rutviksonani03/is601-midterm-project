
import json
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Process customer orders from a JSON file"
    )
    parser.add_argument(
        "filename",
        help="Input JSON file containing orders"
    )
    args = parser.parse_args()

    # Read the input JSON file
    with open(args.filename, "r", encoding="utf-8") as file:
        orders = json.load(file)

    print(f"Total orders: {len(orders)}")

    # Create the customers dictionary
    customers = {}

    for order in orders:
        phone = order["phone"]
        name = order["name"]
        customers[phone] = name

    print(f"Total customers: {len(customers)}")

    # Save customers to customers.json
    with open("customers.json", "w", encoding="utf-8") as file:
        json.dump(customers, file, indent=4)

    print("Customers saved to customers.json")

    # Create the items dictionary
    items = {}

    for order in orders:
        for item in order["items"]:
            item_name = item["name"]
            item_price = item["price"]

            if item_name not in items:
                items[item_name] = {
                    "price": item_price,
                    "orders": 1
                }
            else:
                items[item_name]["orders"] += 1

    print(f"Total menu items: {len(items)}")

    # Save items to items.json
    with open("items.json", "w", encoding="utf-8") as file:
        json.dump(items, file, indent=4)

    print("Items saved to items.json")


if __name__ == "__main__":
    main()