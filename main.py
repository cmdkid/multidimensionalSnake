from time import sleep

from src.field import field

from config import conf


if __name__ == '__main__':
    # create new snake
    field.add_snake()
    # add new food
    field.add_food()

    # cycle controls
    while field.is_death() is False:
        field.tic()

    print(f'Death! Snake fat count={field.get_score()}.')
