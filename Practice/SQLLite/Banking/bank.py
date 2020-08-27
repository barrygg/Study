import random
import sqlite3


class BankingSystem:
    conn = sqlite3.connect('card.s3db')
    conn.execute('CREATE TABLE IF NOT EXISTS card'
                 '(ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                 'number TEXT NOT NULL,'
                 'PIN TEXT NOT NULL,'
                 'balance INTEGER DEFAULT 0);')
    work = True

    @staticmethod
    def luhn(n):
        n = [int(e) * 2 if i % 2 else int(e) for i, e in enumerate(n, 1)]
        n = [e - 9 if e > 9 else e for e in n]
        return 10 - sum(n) % 10 if sum(n) % 10 else 0

    @staticmethod
    def pin_generator():
        return str(random.randint(0, 9999)).rjust(4, '0')

    @classmethod
    def cls_exit_bank(cls):
        print('Bye!')
        cls.work = False

    @classmethod
    def check_luhn(cls, n):
        return int(n[-1]) != cls.luhn(n[:-1])

    @classmethod
    def card_generator(cls):
        number = str(random.randint(0, 999999999)).rjust(9, '0')
        random_number = '400000' + number
        full_number = random_number + str(cls.luhn(random_number))
        cursor = cls.conn.execute('SELECT number FROM card')
        numbers = [el[0] for el in cursor.fetchall()]
        if full_number not in numbers:
            return full_number
        else:
            cls.card_generator()

    @classmethod
    def create(cls):
        n = cls.card_generator()
        p = cls.pin_generator()
        cls.conn.execute('INSERT INTO card (number, PIN)'
                         'VALUES (?, ?)', (n, p))
        cls.conn.commit()
        print('Your card has been created')
        print('Your card number:', n, sep='\n')
        print('Your card PIN', p, sep='\n')

    @classmethod
    def login(cls):
        print('Enter your card number:')
        n = input()
        print('Enter your PIN:')
        p = input()
        cursor = cls.conn.execute('SELECT number from card')
        numbers = [el[0] for el in cursor.fetchall()]
        if n not in numbers:
            print('Wrong card number or PIN!')
        else:
            cursor = cls.conn.execute('SELECT PIN FROM card WHERE number = ?', (n, ))
            card = cursor.fetchone()
            if p != card[0]:
                print('Wrong card number or PIN!')
            else:
                print('You have successfully logged in!')
                return n

    def __init__(self, number):
        self.number = number
        self.run = True

    def balance(self):
        cursor = self.conn.execute('SELECT balance FROM card WHERE number = ?', (self.number,))
        balance_tuple = cursor.fetchone()
        print('Balance:', balance_tuple[0])

    def income(self):
        print('Enter income:')
        income_sum = int(input())
        self.conn.execute('UPDATE card SET balance = balance + ? WHERE number = ?', (income_sum, self.number))
        self.conn.commit()
        print('Income was added!')

    def transfer(self):
        cursor = self.conn.execute('SELECT number from card')
        numbers = [el[0] for el in cursor.fetchall()]
        print('Transfer')
        print('Enter card number:')
        other_number = input()
        if other_number == self.number:
            print('You can\'t transfer money to the same account!')
        elif self.check_luhn(other_number):
            print('Probably you made mistake in the card number. Please try again!')
        elif other_number not in numbers:
            print('Such a card does not exist.')
        else:
            print('Enter how much money you want to transfer:')
            transfer_sum = int(input())
            cursor = self.conn.execute('SELECT balance FROM card WHERE number = ?', (self.number,))
            balance_tuple = cursor.fetchone()
            if transfer_sum > balance_tuple[0]:
                print('Not enough money!')
            else:
                self.conn.execute('UPDATE card SET balance = balance - ? WHERE number = ?',
                                  (transfer_sum, self.number))
                self.conn.execute('UPDATE card SET balance = balance + ? WHERE number = ?',
                                  (transfer_sum, other_number))
                self.conn.commit()
                print('Success!')

    def close(self):
        self.conn.execute('DELETE FROM card WHERE number = ?', (self.number,))
        self.conn.commit()
        print('The account has been closed!')
        self.run = False

    def log_out(self):
        print('You have successfully logged out!')
        self.run = False

    def exit_bank(self):
        self.run = False
        self.cls_exit_bank()

    def choose(self):
        option_dict = {'1': self.balance, '2': self.income, '3': self.transfer,
                       '4': self.close, '5': self.log_out, '0': self.exit_bank}
        while self.run:
            print('1. Balance')
            print('2. Add income')
            print('3. Do transfer')
            print('4. Close account')
            print('5. Log out')
            print('0. Exit')
            option = input()
            option_dict[option]()


while BankingSystem.work:
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    option_bank = input()
    if option_bank == '1':
        BankingSystem.create()
    elif option_bank == '2':
        card_number = BankingSystem.login()
        account = BankingSystem(card_number)
        account.choose()
    else:
        BankingSystem.cls_exit_bank()