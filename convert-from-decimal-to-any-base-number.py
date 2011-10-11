#env python
# ----*----- coding: utf-8 ------*---
#
#Convert from decimal to any base number, and vice versa
#========================================================
#
#inspired by: http://code.activestate.com/recipes/65212-convert-from-decimal-to-any-base-number/download/1/
#
#
#It's still a working project currently.
#=========================================

debug = False

mapper_10_to_36 = {0:'0',
        1:'1',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9',
        10:'a',
        11:'b',
        12:'c',
        13:'d',
        14:'e',
        15:'f',
        16:'g',
        17:'h',
        18:'i',
        19:'j',
        20:'k',
        21:'l',
        22:'m',
        23:'n',
        24:'o',
        25:'p',
        26:'q',
        27:'r',
        28:'s',
        29:'t',
        30:'u',
        31:'v',
        32:'w',
        33:'x',
        34:'y',
        35:'z'}

# delete 0, 'o', 1, 'l', 2, 'z' from a normal mapper_10_to_36
mapper_10_to_30_special = {0:'3',
        1:'4',
        2:'5',
        3:'6',
        4:'7',
        5:'8',
        6:'9',
        7:'a',
        8:'b',
        9:'c',
        10:'d',
        11:'e',
        12:'f',
        13:'g',
        14:'h',
        15:'i',
        16:'j',
        17:'k',
        18:'m',
        19:'n',
        20:'p',
        21:'q',
        22:'s',
        23:'t',
        24:'u',
        25:'v',
        26:'w',
        27:'x',
        28:'y',
        29:'z'}


def base10to30(num, mapper_10_to_30=mapper_10_to_30_special):
    """Change a  to a base-n number.
    Up to base-36 is supported without special notation."""
    num_rep = mapper_10_to_30
    dest_base = len(num_rep)
    new_num_string = '' 
    current = num 
    while current != 0:
        remainder = current % dest_base

        if debug:
            print('-----------------------------')
            print('current: %d, %d, remainder: %d') % (current, n, remainder)

        if dest_base > remainder >= 0:
            remainder_string = num_rep[remainder]
        new_num_string = remainder_string + new_num_string

        if debug:
            print('remainer_string: %s') % remainder_string
            print('new_num_string : %s') % new_num_string
        current = current / dest_base
    return new_num_string

def base30to10(str_base30, mapper_10_to_30=mapper_10_to_30_special):
    ''' restore a str(base30) to a num(base10) '''
    str_base = len(mapper_10_to_30)
    mapper_turn_over = {}
    for key in mapper_10_to_30:
        mapper_turn_over.update({ mapper_10_to_30[key] : key })
    if debug:
        print mapper_turn_over
    current = str_base30
    new_num = 0
    while current is not '':
        power = len(current) - 1
        new_num += mapper_turn_over[current[0]] * ( str_base ** power)
        current = current[ 1: ]
    return new_num


def base10toN(num,n):
    """Change a  to a base-n number.
    Up to base-36 is supported without special notation."""
    num_rep = mapper_10_to_36
    dest_base = len(num_rep)
    new_num_string = '' 
    current = num 
    while current!=0:
        remainder = current % n

        if debug:
            print('-----------------------------')
            print('current: %d, %d, remainder: %d') % (current, n, remainder)

        if dest_base > remainder >= 0:
            remainder_string = num_rep[remainder]
        elif remainder >= dest_base:
            remainder_string = ' (' + str (remainder)+')'
        else:
            remainder_string = str (remainder) # this line should be never executed!
        new_num_string = remainder_string + new_num_string

        if debug:
            print('remainer_string: %s') % remainder_string
            print('new_num_string : %s') % new_num_string
        current = current /n
    return new_num_string


if '__name__' == '__main__':
    num = 629
    dest_base = 36
    snum = base10toN(num, dest_base)
    print 'num: %d(base-10), dest_base: %d, dest_string_num: %s(base-%d)' % (num, dest_base, snum, dest_base)
