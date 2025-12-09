from guess_the_number import GuessTheNumber


def gtn():
    g = GuessTheNumber(min_number=1, max_number=100)
    g.game()

if __name__ == '__main__':
    gtn()


