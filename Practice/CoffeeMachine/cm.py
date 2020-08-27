# Coffee machine simulator. 
# The machine works with typical products: coffee, milk, sugar, and plastic cups.
# If it runs out of something, it shows a notification. 
# You can get three types of coffee: espresso, cappuccino, and latte. 
# Since nothing’s for free, it also collects the money.

class CoffeeMachine:
    espresso = [250, 0, 16, 1, 4]
    latte = [350, 75, 20, 1, 7]
    cappuccino = [200, 100, 12, 1, 6]
    names = ["water", "milk", "coffee beans", "disposable cups"]

    def __init__(self, water, milk, coffee, cups, money):
        self.resource = [water, milk, coffee, cups]
        self.money = money
        self.running = True

    def remaining(self):
        print("The coffee machine has:")
        for r, n in zip(self.resource, CoffeeMachine.names):
            print("{} of {}".format(r, n))
        print("${} of money".format(self.money))

    def buy_coffee(self, coffee):
        for r, c, n in zip(self.resource, coffee[:-1], CoffeeMachine.names):
            if r < c:
                print("Sorry, not enough {}!".format(n))
                break
        else:
            print("I have enough resources, making you a coffee!")
            self.money += coffee[-1]
            for i, c in enumerate(coffee[:-1]):
                self.resource[i] -= c

    def buy(self):
        type_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if type_of_coffee == "1":
            self.buy_coffee(CoffeeMachine.espresso)
        elif type_of_coffee == "2":
            self.buy_coffee(CoffeeMachine.latte)
        elif type_of_coffee == "3":
            self.buy_coffee(CoffeeMachine.cappuccino)
        elif type_of_coffee == "back":
            pass

    def fill(self):
        self.resource[0] += int(input("Write how many ml of water do you want to add:"))
        self.resource[1] += int(input("Write how many ml of milk do you want to add:"))
        self.resource[2] += int(input("Write how many grams of coffee beans do you want to add:"))
        self.resource[3] += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0

    def exit(self):
        self.running = False


    def run(self):
        action_dict = {"exit": self.exit, "fill": self.fill, "take": self.take, "buy": self.buy, "remaining": self.remaining}
        while self.running:
            action = input('Write action (buy, fill, take, remaining, exit):')
            action_dict[action]()

cm = CoffeeMachine(400, 540, 120, 9, 550)
cm.run()
