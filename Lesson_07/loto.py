import random


class Card:

    def __init__(self, name):
        seq = [i for i in range(1, 91)]
        random.shuffle(seq)
        self._numbers = self._make_line(seq[0:5]) + self._make_line(seq[5:10]) + self._make_line(seq[10:15])
        self.name = name

    def _make_line(self, seq):
        seq.sort()
        for _ in range(0, 4):
            seq.insert(random.randint(0, len(seq)), '--')
        return seq

    def _print_line(self, line_lst):
        line = ' '.join([str(i).rjust(2) for i in line_lst])
        print(line)

    def print_card(self):
        print(self.name.center(26, '-'))
        self._print_line(self._numbers[0:9])
        self._print_line(self._numbers[9:18])
        self._print_line(self._numbers[18:27])
        print('-' * 26)

    def _check_number(self, number):
        return number in self._numbers

    def _cross_number(self, number):
        index = self._numbers.index(number)
        self._numbers[index] = '--'
        print(f'{self.name} - зачеркнут номер {number}')

    def empty(self):
        return set(self._numbers) == {'--'}


class UserCard(Card):
    def treat_choise(self, number, cross_out):
        if self._check_number(number):
            if cross_out:
                self._cross_number(number)
            return cross_out
        else:
            return not cross_out


class CompCard(Card):
    def treat_number(self, number):
        if self._check_number(number):
            self._cross_number(number)


class Game:
    def __init__(self):
        self._user_card = UserCard('Ваша карточка')
        self._comp_card = CompCard('Карточка компьютера')
        self._barrels_bag = LottoBarrelsBag()

    def start(self):

        for barrel in self._barrels_bag:
            self._user_card.print_card()
            self._comp_card.print_card()
            if not self._user_card.treat_choise(barrel,input('Зачеркнуть цифру? (y/n)')=='y'):
            # if not self._user_card.treat_choise(barrel, barrel in self._user_card._numbers):
                print('Неверный выбор! Вы проиграли.')
                break
            self._comp_card.treat_number(barrel)
            if self._comp_card.empty() and self._user_card.empty():
                print('Ничья.')
                break
            elif self._comp_card.empty():
                print('Компьютер победил.')
                break
            elif self._user_card.empty():
                print('Вы победили.')
                break
        self._barrels_bag.print_barrels()


class LottoBarrelsBag:
    def __init__(self):
        self._barrels = [i for i in range(1, 91)]

    def get_barrel(self):
        if self._barrels:
            barrel = random.choice(self._barrels)
            self._barrels.remove(barrel)
            print(f'Новый боченок: {barrel} (осталось {self.quantity()})')
        else:
            print('Боченков больше нет')
            barrel = 0
        return barrel

    def quantity(self):
        return len(self._barrels)

    def __iter__(self):
        return self

    def __next__(self):
        barrel = self.get_barrel()
        if barrel:
            return barrel
        else:
            raise StopIteration

    def print_barrels(self):
        shablon = '<{}>' * self.quantity()
        shablon = 'Оставшиеся боченки: ' + shablon
        print(shablon.format(*self._barrels))


game = Game()
game.start()
