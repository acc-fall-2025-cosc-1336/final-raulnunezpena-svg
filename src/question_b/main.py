class Stock:
    def __init__(self, symbol, company_name):
        self.symbol = symbol
        self.company_name = company_name

    def get_symbol(self):
        return self.symbol
    
    def get_stock_list(self):
        stock_list = []

        stock_list.append(Stock("AAPL", "Apple Inc."))
        stock_list.append(Stock("CAT", "Caterpillar Inc."))
        stock_list.append(Stock("EK", "Eastman Kodak Company"))
        stock_list.append(Stock("GOOG", "google LLC"))
        stock_list.append(Stock("MSFT", "Microsoft Corporation"))

        return stock_list
    
    def display_stock_list(self, stock_list):
        print("Stock Report")
        print("company name \t stock symbol")
        print("-----------------------------")
        for stock in stock_list:
            print(f"{stock.company_name} \t {stock.symbol}")


def main():
    stock = Stock("", "")
    stock_list = stock.get_stock_list()

    while True:
        print("\nMenu")
        print("1. Display Stock List")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            stock.display_stock_list(stock_list)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
        

                  
