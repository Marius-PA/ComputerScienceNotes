class Account:
    def __init_ (self, number, password, balance): #A new bank wucount should be defined with a given account number, password nce
        self.__accountNumber = number
        self.__accountPassword = password
        self.__accountBalance = balance

    def getNumber (self):
    #This method should return the account number of this account
        return self.__accountNumber

    def checkPassword(self, password):
    #This method should check if a given password is equal to the password for this
        if self.__accountPassword == password:
            return True
        else:
            return False

    def getBalance(self) :
    #This method should return the balance of this acceunt
        return self.__accountBalance

    def setBalance(self, newBalance):
    # This method should change the balance of this account to a specified new v;
        self.__accountBalance += newBalance


class Bank:
    def __init__(self): #A new bank is defined with a list of bank account value that keeps track of the account number of
        self.__accounts = []
        self.__latestAccount = 0

    def login(self):
        account = input("account")
        password = input("password")
        if account in self.__accounts and Account.checkPassword(password) == True:
            return self.__accounts
        else:
            return -1


    def deposit(self, number):
        money = float(input("how much deposit?"))

    def withdraw(self, number):

    def checkBalance(self, number):


    def addAccount (self):
        password = input("set ur password")
        self.__latestAccount += 1
        self.__accounts[self.__latestAccount] = Account(self.__latestAccount, password, 0)
        