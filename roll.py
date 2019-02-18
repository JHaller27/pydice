#!/usr/bin/python3

import sys
import random


def parse_dice(sin: str) -> (int, int, str, int, int):
    """
    :return: tuple of the form:
        (# dice, die size, <<k|d><h|l>|>, # to keep/drop, mod)
    """

    # Find split indices
    try:
        idx_d = sin.index('d')
    except ValueError:
        print('Must use dice format (XdY[<d|k><l|h>#][<+|->#])')
        exit(1)

    try:
        idx_mod = sin.index('+')
    except ValueError:
        try:
            idx_mod = sin.index('-')
        except ValueError:
            idx_mod = len(sin)

    try:
        idx_dk = sin[idx_d+1:].index('d') + idx_d + 1
    except ValueError:
        try:
            idx_dk = sin.index('k')
        except ValueError:
            idx_dk = idx_mod
   
    # Actually do the splitting
    num_dice = int(sin[:idx_d])
    dice_size = int(sin[idx_d+1:idx_dk])

    if idx_dk == idx_mod:
        dk_str = ''
        dk_num = 0
    else:
        dk_str = sin[idx_dk:idx_dk+2]
        dk_num = int(sin[idx_dk+2:idx_mod])

    if idx_mod == len(sin):
        mod_num = 0
    else:
        mod_num = int(sin[idx_mod:])

    return num_dice, dice_size, dk_str, dk_num, mod_num


def roll(num_dice: int, dice_size: int, dk_str: str, dk_num: int, mod_num: int) -> int:
    rolls = [random.randint(1, dice_size) for _ in range(num_dice)]
    rolls.sort()

    if mod_num == 0:
        print('Rolls: [{}]'.format(', '.join(map(str, rolls))))
    else:
        print('[{}] {:+}'.format(', '.join(map(str, rolls)), mod_num))

    if len(dk_str) != 2:
        keep = rolls
    else:
        print('Drop' if dk_str[0] == 'd' else 'Keep', end=' ')
        print('highest' if dk_str[1] == 'h' else 'lowest', end=' ')
        print(dk_num)
        
        if dk_str[1] == 'l':
            l, h = rolls[:dk_num], rolls[dk_num:]
            if dk_str[0] == 'd':
                keep = h
            elif dk_str[0] == 'k':
                keep = l
        elif dk_str[1] == 'h':
            l, h = rolls[:-dk_num], rolls[-dk_num:]
            if dk_str[0] == 'd':
                keep = l
            elif dk_str[0] == 'k':
                keep = h
    
    return sum(keep) + mod_num


if __name__ == '__main__':
    dice_str = sys.argv[1]
    dice_tup = parse_dice(dice_str)
    print('Result: %d' % roll(*dice_tup))

