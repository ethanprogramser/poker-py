import random

class game:
    def __init__(self, balance):
        print("########################################")
        print("#             poker                    #")
        print("########################################")
        print(balance)
        self.balance = balance
        self.bet = int(input("how much:"))
        self.cards = ["A", "K", "Q", "J", "10", "9", "8", "7","6", "5", "4", "3", "2"]
        self.dh = ""
        self.ph = ""
        self.pt = 0
        self.dt = 0
        self.ph, self.pt = self.check(self.ph, self.pt, 2, True)
        self.dh, self.dt = self.check(self.dh, self.dt, 1, False)
        print(self.ph)
        print(self.dh + "#")
        self.hit_or_stand()


    def check(self, hand, total, t, d):
        for i in range(t):
            card = random.choice(self.cards)
            hand += card + " "
            match card:
                case "K":
                    total += 10
                case "Q":
                    total += 10
                case "J":
                    total += 10
                case "A":
                    if d:
                        print(hand)
                        cho = input("1 or 11:")
                        if cho == "1":
                            total += 1
                        else:
                            total += 11
                    else:
                        if self.dt > 10:
                            total += 1
                        else:
                            total += 11
                case _:
                    total += int(card) 
        return hand, total

    def dealers(self):
        if self.pt > self.dt:
            self.dh, self.dt = self.check(self.dh, self.dt, 1, False)
            print(self.dh)
            self.dealers()
        else:
            if self.dt > 21 or self.dt < self.pt:
                print("you win")
                game(self.balance + self.bet)
            elif self.dt == self.pt:
                print("tie")
                game(self.balance)
            else:
                print("dealer wins")
                game(self.balance - self.bet)

    def hit_or_stand(self):
        if self.pt > 21:
            print("you lose")
            game(self.balance - self.bet)
        else:

            ip = input("HIT OR STAND hs:")
            if ip == 'h':
                self.ph, self.pt = self.check(self.ph, self.pt, 1, True)
                print(self.ph)
                self.hit_or_stand()
            else:
                self.dealers()


game(20)
