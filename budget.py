class Category():
    def __init__(self,categoria):
        self.categoria = categoria
        self.ledger = []

    def __str__(self):
        string = str(self.categoria)
        string = string.center(30,"*") + "\n"
        for i in self.ledger:
            line = i.get("description")[0:23].ljust(23," ")
            formatted_number = "{:.2f}".format(i.get("amount"))
            line = line + str(formatted_number)[0:7].rjust(7," ") + "\n"
            string = string + line
        string = string + "Total: " + "{:.2f}".format(self.get_balance())
        return string

    def deposit(self,amount,description = ""):
        self.ledger.append({"amount":amount, "description":description})

    def withdraw(self,amount,description = ""):
        if self.check_funds(amount) == False:
            return False
        else:
            self.ledger.append({"amount":-amount, "description":description})
            return True

    def get_balance(self):
        balance = 0
        i = 0
        while i < len(self.ledger):
            balance = balance + self.ledger[i].get("amount")
            i += 1
        return balance

    def transfer(self,amount,other_category):
        if self.check_funds(amount) == True:
            self.withdraw(amount,"Transfer to " + str(other_category.categoria))
            other_category.deposit(amount,"Transfer from " + str(self.categoria))
            return True
        else:
            return False

    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        else:
            return True

def create_spend_chart(category_list):
    i = 0
    spent = [0] * len(category_list)
    name_length = 0
    for cat in category_list:
        for item in cat.ledger:
            if item.get("amount") < 0:
                spent[i] -= item.get("amount")
        i += 1
        if len(cat.categoria) > name_length:
            name_length = len(cat.categoria)
    total_spent = sum(spent)
    percentage_spent = [number / total_spent * 100 for number in spent]


    bar_chart = "Percentage spent by category\n"
    for percentage in [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]:
        linea = str(percentage) + "| "
        linea = linea.rjust(5, " ")
        i = 0
        for cat in category_list:
            if percentage_spent[i] > percentage:
                linea = linea + "o  "
            else:
                linea = linea + "   "
            i += 1
        bar_chart = bar_chart + linea + "\n"
    linea = "    " + "---"*len(category_list) + "-"
    bar_chart = bar_chart + linea


    i = 0
    while i < name_length:
        linea = " "*5
        for cat in category_list:
            try:
                linea = linea + cat.categoria[i] + " "*2
            except:
                linea = linea + " "*3

        bar_chart = bar_chart + "\n" + linea
        i += 1


    return bar_chart




#---------------------Testing------------------------



a1 = Category("food")
a2 = Category("clothing")

a1.deposit(1000, "Deposit 1")
a2.deposit(500, "Deposit 2")

a1.withdraw(100, "Withdraw 1")
a1.withdraw(300, "Withdraw 2")
a2.withdraw(450, "Withdraw 3")

print("Ledger 1:", a1.ledger)
print("Ledger 2:", a2.ledger)
print("\n")
print("Balance 1:", a1.get_balance())
print("Balance 2:", a2.get_balance())
print("\n")
print(a1)
print(a2)

print("---------------------------")
print(create_spend_chart([a1, a2]))
