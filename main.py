from src.field import field
from src.bots import bot_blind_snake, bot_chaotic_snake

if __name__ == '__main__':
    # create new snake
    field.add_snake()
    # add new food
    field.add_food()

    # cycle controls
    while field.is_death() is False:
        field.tic()

        # bot control
        bot_blind_snake()
        # bot_chaotic_snake()

    print(f'Death! Snake fat count={field.get_score()}.')
