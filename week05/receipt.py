import csv

def read_dictionary(filename, key_column_index):
   
    result_dict = {}
    with open(filename, "r", newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            if len(row) > 0:
                key = row[key_column_index]
                result_dict[key] = row
    return result_dict


def main():
    
    products_dict = read_dictionary("products.csv", 0)

   
    print("All Products")
    print(products_dict)

    
    with open("request.csv", "r", newline='') as request_file:
        reader = csv.reader(request_file)
        next(reader)  # Skip header row

        subtotal = 0
        SALES_TAX_RATE = 0.06

        print("\nRequested Items:")

        for row in reader:
            if len(row) > 0:
                product_number = row[0]
                quantity = int(row[1])
                
                product_info = products_dict.get(product_number)
                if product_info:
                    name = product_info[1]
                    price = float(product_info[2])
                    line_total = price * quantity
                    subtotal += line_total

                    print(f"{name}: {quantity} @ ${price:.2f}")
        
       
        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax

       
        print()
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")



if __name__ == "__main__":
    main()
