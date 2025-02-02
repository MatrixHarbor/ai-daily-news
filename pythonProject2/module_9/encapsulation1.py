# # Encapsulation refers to the ability to hide certain class attributes (data members and/or methods)
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
# class AccountHolder:
#     def __init__(self, name, account):
#         self.name = name
#         self.account = account
# account = BankAccount(1000)
# customer = AccountHolder("Joe", account)
#
# print(account.__dict__)
# print(customer.account.BankAccount__balance)
# print(customer.account.__balance)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):  # Getter method
        return self.__balance

class AccountHolder:
    def __init__(self, name, account):
        self.name = name
        self.account = account

account = BankAccount(1000)
customer = AccountHolder("Joe", account)

print(customer.account.get_balance())  # Correct way to access the balance