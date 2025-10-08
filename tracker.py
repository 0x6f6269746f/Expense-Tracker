def main():
    print(f"Running Expense Tracker")
    #Get user expense
    get_expense()
    #write expense to file
    write_expenes()
    #read the expense
    read_expense()

def get_expense():
    expense = input(f"Enter in an expense: ")
    print(f"Expense is: {expense}")

def write_expenes():
    print(f"Write")


def read_expense():
    print(f"Read")


if __name__ == "__main__":
    main()
