def minion_game(string):
    stuart_count = 0
    kelvin_count = 0

    length = len(string)

    for i in range(length):
        if string[i].lower() in 'aeiou':
            kelvin_count += length - i
        else:
            stuart_count += length - i

    if stuart_count > kelvin_count:
        print(f'Stuart {stuart_count}')
    elif stuart_count < kelvin_count:
        print(f'Kevin {kelvin_count}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)