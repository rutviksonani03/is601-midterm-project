
# IS601 Midterm Project

## Description

This project processes customer orders from a JSON file and generates two output files.

- `customers.json`: Contains customer phone numbers and names.
- `items.json`: Contains menu item prices and the number of times each item was ordered.

## Requirements

- Python 3
- Input JSON file containing customer orders

## How to Run

Open a terminal in the `midterm_project` directory and run:

```bash
python main.py example_orders.json
```

You can also provide another JSON filename as the command-line argument.

## Output

The program generates:

- `customers.json`
- `items.json`

## Data Processing

The program reads each order from the input JSON file.

- Customer information is stored using phone numbers as keys.
- Menu items are grouped by item name.
- The program counts how many orders contain each menu item.
- The results are saved in separate JSON output files.

## Verification

The program was tested using `example_orders.json`, which contains 10,000 orders. The program generated customer and menu-item output files successfully.
