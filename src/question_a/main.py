def create_mult_table():

    table = []

    for row in range (1,6):
        row_list = []
        for col in range(1,11):
            row_list.append(row * col)
        table.append(row_list)

    return table


def display_mult_table(table):

    for row in table:
        for value in row:
            print(value, end = " ")
        print()

def main():
    while True:
        table = create_mult_table()
        display_mult_table(table)

        choice = input("Do you want to see the multiplication table again? (y/n): ")
        if choice.lower() != 'y':
            break
if __name__ == "__main__":
    main()
    
