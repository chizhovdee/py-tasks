class Kassa:
    def __init__(self):
        self.balance = 0

    def top_up(self, amount):
        self.balance += amount

    def count_1000(self):
        return self.balance // 1000

    def take_away(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно денег в кассе")
        self.balance -= amount
