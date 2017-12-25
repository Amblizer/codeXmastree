""" christmas.py 
Prints a christmas tree on the terminal using coloured and blinking characters.
Uses ansi terminal escape sequences.
The '\033[' part is the escape code. 
We pass '5;' for the colours other than green to make them blink.
The next part is the colour code and the 'm' ends the sequence.
To reset the colour we pass "\033[0m" after each character.
Python 3 version by antiloquax (2015), based on code from datamungeblog.com.
"""

import random

def main(sizeTree=21, probGreen=0.6):
    # Make the tree according to demanded size, only use odd number
    # probGreen is the probability of green charactors
    if sizeTree % 2 != 1:
        sizeTree = int(sizeTree) + 1
        print('Odd integer only, increased to', sizeTree)
    if probGreen < 0 or probGreen > 1:
        probGreen = random.random()
        print('Must within [0, 1], randomly changed to', probGreen)
    print(makeTree(sizeTree, probGreen))

def makeTree(sizeTree, probGreen):
    colors = [31, 33, 34, 35, 36, 37]
    decors = ['@', '&', '*', chr(169), chr(174)]

    # blinking characters
    blink = '\033[5;{0}m{1}\033[0m'
    # leaves
    leaf = '\033[32m#\033[0m'
    # width of the tree
    width = 1
    # init the star at the top
    tree = '\n{}*\n'.format(' ' * (sizeTree))

    for pad in range(sizeTree-1, -1, -1):
        width += 2
        # put chars in 'temp'
        temp = ''
        for j in range(width):
            if random.random() < probGreen:
                temp += leaf
            # add baubles
            else:
                temp += blink.format(random.choice(colors), \
                                     random.choice(decors))
        tree += "{0}{1}\n".format(' ' * pad, temp)
    # add a trunk
    return tree + '{0}{1}\n'.format(' ' * (sizeTree - 1), "000") * 2

main()
input()