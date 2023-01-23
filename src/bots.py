import random

from src.field import field


def is_positive(val: int) -> bool:
    if val > 0:
        return True
    elif val < 0:
        return False
    else:
        raise ValueError


def bot_blind_snake():
    """
    Snake find the way to food, but ignore dimension borders

    :return:
    """
    do_change_direction = False
    rand_val = random.randint(0, 500)
    if rand_val <= 100:
        food_pos = field.get_food_pos()
        head_pos = field.get_snake_head_pos()
        head_direction = field.get_snake_direction()

        distance = 0
        dist_dimension = 0
        for i in range(len(food_pos)):
            tmp_distance = abs(food_pos[i] - head_pos[i])
            if tmp_distance > distance:
                dist_dimension = i
                distance = tmp_distance

        if food_pos[dist_dimension] > head_pos[dist_dimension]:
            rotate = 1
        else:
            rotate = -1

        if abs(head_direction/10) != dist_dimension or is_positive(head_direction) != is_positive(rotate):
            print(f'Rotate: {dist_dimension},{rotate}')
            field.control(dist_dimension, rotate)


def bot_chaotic_snake():
    """
    Snake rotating chaotically, food and border ignored

    :return:
    """
    do_change_direction = False
    rand_val = random.randint(0, 500)

    if rand_val <= 50:
        direction = 0
        do_change_direction = True
    elif 50 < rand_val <= 100:
        direction = 1
        do_change_direction = True

    if rand_val < 25 or 75 < rand_val <= 100:
        rotate = -1
    elif 25 < rand_val <= 50 or 50 < rand_val <= 75:
        rotate = 1
    else:
        do_change_direction = False

    if do_change_direction:
        print(f'Rotate: {direction},{rotate}')
        field.control(direction, rotate)
