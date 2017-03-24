from Neck import sharps, flats, string_builder
import operator
import copy

# CLOSED moet nog worden ingevuld
closed = [
    # First inversion: R, 3, 5, 7
    ['closed_inv1_strS1', 'R', 8, '3rd', 7, '5th', 5, '7th', 3], ['closed_inv1_strS2', 'R', 15, '3rd', 14, '5th', 12, '7th', 12], ['closed_inv1_strS3', 'R', 10, '3rd', 9, '5th', 8, '7th', 7],
    # 2nd inversion: 3, 7, R, 5
    #['closed_inv2_strS1', '3rd', 12, '7th', 14, 'R', 10, '5th', 12], ['closed_inv2_strS2', '3rd', 7, '7th', 9, 'R', 5, '5th', 8], ['closed_inv2_strS3', '3rd', 2, '7th', 4, 'R', 1, '5th', 3],
    # 3rd inversion: 5, R, 3, 7
    #['closed_inv3_strS1', '5th', 3, 'R', 3, '3rd', 2, '7th', 4], ['closed_inv3_strS2', '5th', 10, 'R', 10, '3rd', 9, '7th', 12], ['closed_inv3_strS3', '5th', 5, 'R', 5, '3rd', 5, '7th', 7],
    # 4th inversion: 7, 3, 5, R
    #['closed_inv4_strS1', '7th', 7, '3rd', 7, '5th', 5, 'R', 5], ['closed_inv4_strS2', '7th', 14, '3rd', 14, '5th', 12, 'R', 13], ['closed_inv4_strS3', '7th', 9, '3rd', 9, '5th', 8, 'R', 8],
]
# DROP2 is klaar
drop2 = (
    # First inversion: R, 5, 7, 3
    ['drop2_inv1_strS1', 'R', 8, '5th', 10, '7th', 9, '3rd', 9], ['drop2_inv1_strS2', 'R', 3, '5th', 5, '7th', 4, '3rd', 5], ['drop2_inv1_strS3', 'R', 10, '5th', 12, '7th', 12, '3rd', 12],
    # 2nd inversion: 3, 7, R, 5
    ['drop2_inv2_strS1', '3rd', 12, '7th', 14, 'R', 10, '5th', 12], ['drop2_inv2_strS2', '3rd', 7, '7th', 9, 'R', 5, '5th', 8], ['drop2_inv2_strS3', '3rd', 2, '7th', 4, 'R', 1, '5th', 3],
    # 3rd inversion: 5, R, 3, 7
    ['drop2_inv3_strS1', '5th', 3, 'R', 3, '3rd', 2, '7th', 4], ['drop2_inv3_strS2', '5th', 10, 'R', 10, '3rd', 9, '7th', 12], ['drop2_inv3_strS3', '5th', 5, 'R', 5, '3rd', 5, '7th', 7],
    # 4th inversion: 7, 3, 5, R
    ['drop2_inv4_strS1', '7th', 7, '3rd', 7, '5th', 5, 'R', 5], ['drop2_inv4_strS2', '7th', 14, '3rd', 14, '5th', 12, 'R', 13], ['drop2_inv4_strS3', '7th', 9, '3rd', 9, '5th', 8, 'R', 8],
)
# DROP3  is klaar
drop3 = [
    # First inversion: R, 5, 3, 7
    ['drop3_inv1_strS1', 'R', 8, '7th', 9, '3rd', 9, '5th', 8], ['drop3_inv1_strS2', 'R', 3, '7th', 4, '3rd', 5, '5th', 3],
    # 2nd inversion: 3, 7, R, 5
    ['drop3_inv2_strS1', '3rd', 12, 'R', 10, '5th', 12, '7th', 12], ['drop3_inv2_strS2', '3rd', 7, 'R', 5, '5th', 8, '7th', 7],
    # 3rd inversion: 5, R, 3, 7
    ['drop3_inv3_strS1', '5th', 3, '3rd', 2, '7th', 4, 'R', 1], ['drop3_inv3_strS2', '5th', 10, '3rd', 9, '7th', 12, 'R', 8],
    # 4th inversion: 7, 3, 5, R
    ['drop3_inv4_strS1', '7th', 7, '5th', 5, '3rd', 5, 'R', 5], ['drop3_inv4_strS2', '7th', 14, '5th', 12, '3rd', 13, 'R', 12],
]
# DROP24 moet nog worden ingevuld
drop4 = [
    # First inversion: R, 5, 3, 7
    ['drop4_inv1_strS1', 'R', 8, '5th', 8, '3rd', 7, '7th', 9], ['drop4_inv1_strS2', 'R', 3, '5th', 5, '3rd', 5, '7th', 7],
    # 2nd inversion: 3, 7, R, 5
    ['drop4_inv2_strS1', '3rd', 12, '7th', 14, '5th', 12, 'R', 13], ['drop4_inv2_strS2', '3rd', 7, '7th', 9, '5th', 8, 'R', 8],
    # 3rd inversion: 5, R, 3, 7
    ['drop4_inv3_strS1', '5th', 3, 'R', 3, '7th', 4, '3rd', 5], ['drop4_inv3_strS2', '5th', 10, 'R', 10, '7th', 12, '3rd', 12],
    # 4th inversion: 7, 3, 5, R
    ['drop4_inv4_strS1', '7th', 7, '3rd', 7, 'R', 5, '5th', 8], ['drop4_inv4_strS2', '7th', 14, '3rd', 14, 'R', 13, '5th', 15],
]

formsdict = {
    'M7': ['-'],                                    # [R, 3, 5, 7]
    '7': ['-', '7th'],                             # [R, 3, 5, b7]
    'm7': ['-', '3rd', '7th'],                         # [R, b3, 5, b7]
    'm7b5': ['-', '3rd', '5th', '7th'],  # [R, b3, b5, b7]
    'dim7': ['-', '3rd', '5th', '7th', 'b7th'],  # [R, b3, b5, bb7]
    'mM7': ['-', '3rd'],                      # [R, b3, 5, 7]
    '7#11': ['-', '5th', '7th'],           # [R, 3, #4, b7]
    'M7#11': ['-', '5th']                   # [R, 3, #4, 7]
}


def chord_list_generator(root, chord_formula, chord_type):
    fresh_list = copy.deepcopy(chord_type)
    chord_list = make(fresh_list, *formsdict[chord_formula])
    transposed = transpose(root, chord_list)
    return transposed


def make(chord_type1, opr, *args):
    operator_dict = {
        '+': operator.add,
        '-': operator.sub
    }
    templist_mk = []
    for row in chord_type1:

        for arg in args:

            hit = row.index(arg)
            row[hit + 1] = operator_dict[opr](row[hit + 1], 1)
            row[hit] = 'b' + row[hit]
        new = [row[0], row[1].strip('thrd'), row[2], row[3].strip('thrd'), row[4], row[5].strip('thrd'), row[6], row[7].strip('thrd'), row[8]]

        templist_mk.append(new)

    return templist_mk


def transpose(root, chord_list1):
    if root in sharps:
        x = string_builder(sharps, 'C')
        for y in x:
            y = y.index(root)
        templist_tr = []
        for chord in chord_list1:
            new = [chord[0], chord[1], chord[2] + y, chord[3], chord[4] + y, chord[5], chord[6] + y, chord[7], chord[8] + y]
           # print('1ste  :', new)
            if (new[2] >= 12 and new[4] >= 12 and new[6] >= 12 and new[8] >= 12):
                new = [chord[0], chord[1], new[2] - 12, chord[3], new[4] - 12, chord[5], new[6] - 12, chord[7], new[8] - 12]
             #   print('2de  :', new)
            templist_tr.append(new)

        return templist_tr
    elif root in flats:
        x = string_builder(flats, 'C')
        for y in x:
            y = y.index(root)
        templist_tr = []
        for chord in chord_list1:
            new = [chord[0], chord[1], chord[2] + y, chord[3], chord[4] + y, chord[5], chord[6] + y, chord[7], chord[8] + y]
           # print('1ste  :', new)
            if (new[2] >= 12 and new[4] >= 12 and new[6] >= 12 and new[8] >= 12):
                new = [chord[0], chord[1], new[2] - 12, chord[3], new[4] - 12, chord[5], new[6] - 12, chord[7], new[8] - 12]
             #   print('2de  :', new)
            templist_tr.append(new)

        return templist_tr
    else:
        return 'Error! check root note entry, '


#CM7 = chord_list_generator('C', 'dim7', drop4)

#print(CM7)
# Dm7 = chord_list_generator('D', 'm7', drop2)
# Em7 = chord_list_generator('E', 'm7', drop2)
# FM7 = chord_list_generator('F', 'M7', drop2)
# G7 = chord_list_generator('G', '7', drop2)
# Am7 = chord_list_generator('A', 'm7', drop2)
# Bm7b5 = chord_list_generator('B', 'm7b5', drop2)
# har = (CM7[1], Dm7[1], Em7[1], FM7[1], G7[1], Am7[1], Bm7b5[1])
# # print('################')
# # for x in har:
# #     print(x)
