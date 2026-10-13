# IS601 Midterm Project

## Description

This project reads customer orders from a JSON file and creates two output files: `customers.json` and `items.json`.

The program stores customer details and keeps track of how many times each menu item is ordered.

## Requirements

* Python 3
* A JSON file containing customer orders

## How to Run

1. Open the terminal in the `midterm_project` folder.
2. Make sure Python 3 is installed.
3. Run the following command:

   ```bash
   python main.py example_orders.json
   ```

You can also use another JSON file by providing its filename:

```bash
python main.py your_file.json
```

The input file must contain customer details and item information in the expected format.

## Input File

The program takes a JSON file as input. Each order contains customer details, such as phone number and name, along with a list of items ordered.

Each item contains its name and price.

## Design

The program uses Python's `argparse` module to accept the input filename from the command line. It uses the `json` module to read the data from the input file.

The program works in two main steps:

1. **Customer Processing:** The program stores customer names in a dictionary, using phone numbers as keys. If the same phone number appears in multiple orders, it is stored only once.
2. **Menu Item Processing:** The program stores each menu item in another dictionary. It saves the item's price and counts how many times the item appears in the orders.

After processing all orders, the program saves the results into two separate JSON files.

## Output

The program creates the following files:

* **`customers.json`**: Stores customer phone numbers as keys and their names as values.
* **`items.json`**: Stores menu item names as keys. Each item has a `price` field and an `orders` field that shows how many times the item appears in the input data.

Both files use indentation to make the JSON data easy to read.

## Data Processing

The program reads each order from the input file and processes the customer and item details.

* Customer details are stored using phone numbers.
* Menu items are grouped by their names.
* The count increases whenever the program finds the same menu item again.
* The final results are saved in separate JSON files.

## Verification

The program was tested using `example_orders.json`, which contains 10,000 orders. The program processed the file successfully and created both output files.

The program showed the following results:

* Total orders: 10,000
* Total customers: 30
* Total menu items: 19
