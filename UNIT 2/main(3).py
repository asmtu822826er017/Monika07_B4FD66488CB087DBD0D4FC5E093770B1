# Define the base class Player
class Player:
    def play(self):
        print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of the Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()class BankAccount:
    def _init_(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
      if amount > 0:
            self.__account_balance += amount
            print("Deposited â‚¹{}. New Balance â‚¹{}".format(amount,self.__account_balance))
      else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
      if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdraw â‚¹{}. New balance: â‚¹{}".format(amount,self.__account_balance))
      else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print("Account balance for {} (Account #{}):â‚¹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))

# Create an instance of the BankAccount class
account = BankAccount(account_number="123456789",account_holder_name= "John Doe",initial_balance=1000)

# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()