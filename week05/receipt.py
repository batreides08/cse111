import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    
    result_dict = {}
    with open(filename, "r", newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if len(row) > 0:
                key = row[key_column_index]
                result_dict[key] = row
    return result_dict


def main():
    try:
        # Store name
        print("Gentri Store")

        # Load products dictionary
        products_dict = read_dictionary("products.csv", 0)

        # Open and read the request file
        with open("request.csv", "r", newline='') as request_file:
            reader = csv.reader(request_file)
            next(reader) 
            subtotal = 0
            total_items = 0
            SALES_TAX_RATE = 0.06

            for row in reader:
                if len(row) > 0:
                    prod_num = row[0]
                    quantity = int(row[1])
                    try:
                        prod_info_list = products_dict[prod_num]
                        name = prod_info_list[1]
                        price = float(prod_info_list[2])
                        line_total = price * quantity
                        subtotal += line_total
                        total_items += quantity

                        print(f"{name}: {quantity} @ ${price:.2f}")
                    except KeyError:
                        print(f"Error: unknown product ID in the request.csv file\n'{prod_num}'")

            # Totals
            sales_tax = subtotal * SALES_TAX_RATE
            total = subtotal + sales_tax

            print(f"Number of Items: {total_items}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales Tax: {sales_tax:.2f}")
            print(f"Total: {total:.2f}")
            print("Thank you for shopping at the Gentri Store.")

            # Current date and time
            current_date_and_time = datetime.now()
            print(current_date_and_time.strftime("%a %b %d %I:%M:%S %Y"))

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
    except PermissionError as e:
        print("Error: permission denied")
        print(e)


if __name__ == "__main__":
    main()
