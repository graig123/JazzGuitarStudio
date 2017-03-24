from neck import sharps, flats, string_builder
import operator
import copy


class jchord:

    def __init__(self, root, chord_formula, chord_type=''):
        self.root = root
        self.chord_formula = chord_formula
        chord_types = ['closed', 'drop2', 'drop3', 'drop4']
        if chord_type == 'closed':

            self.chord_type = [
                ['closed_inv1_strS1', 'R', 8, '3rd', 7, '5th', 5, '7th', 3], ['closed_inv1_strS2', 'R', 15, '3rd', 14, '5th', 12, '7th', 12], ['closed_inv1_strS3', 'R', 10, '3rd', 9, '5th', 8, '7th', 7]]

        elif chord_type == 'drop2':
            self.chord_type = [
                # First inversion: R, 5, 7, 3
                ['drop2_inv1_strS1', 'R', 8, '5th', 10, '7th', 9, '3rd', 9], ['drop2_inv1_strS2', 'R', 3, '5th', 5, '7th', 4, '3rd', 5], ['drop2_inv1_strS3', 'R', 10, '5th', 12, '7th', 12, '3rd', 12],
                # 2nd inversion: 3, 7, R, 5
                ['drop2_inv2_strS1', '3rd', 12, '7th', 14, 'R', 10, '5th', 12], ['drop2_inv2_strS2', '3rd', 7, '7th', 9, 'R', 5, '5th', 8], ['drop2_inv2_strS3', '3rd', 2, '7th', 4, 'R', 1, '5th', 3],
                # 3rd inversion: 5, R, 3, 7
                ['drop2_inv3_strS1', '5th', 3, 'R', 3, '3rd', 2, '7th', 4], ['drop2_inv3_strS2', '5th', 10, 'R', 10, '3rd', 9, '7th', 12], ['drop2_inv3_strS3', '5th', 5, 'R', 5, '3rd', 5, '7th', 7],
                # 4th inversion: 7, 3, 5, R
                ['drop2_inv4_strS1', '7th', 7, '3rd', 7, '5th', 5, 'R', 5], ['drop2_inv4_strS2', '7th', 14, '3rd', 14, '5th', 12, 'R', 13], ['drop2_inv4_strS3', '7th', 9, '3rd', 9, '5th', 8, 'R', 8],
            ]
        elif chord_type == 'drop3':
            self.chord_type = [
                # First inversion: R, 5, 3, 7
                ['drop3_inv1_strS1', 'R', 8, '7th', 9, '3rd', 9, '5th', 8], ['drop3_inv1_strS2', 'R', 3, '7th', 4, '3rd', 5, '5th', 3],
                # 2nd inversion: 3, 7, R, 5
                ['drop3_inv2_strS1', '3rd', 12, 'R', 10, '5th', 12, '7th', 12], ['drop3_inv2_strS2', '3rd', 7, 'R', 5, '5th', 8, '7th', 7],
                # 3rd inversion: 5, R, 3, 7
                ['drop3_inv3_strS1', '5th', 3, '3rd', 2, '7th', 4, 'R', 1], ['drop3_inv3_strS2', '5th', 10, '3rd', 9, '7th', 12, 'R', 8],
                # 4th inversion: 7, 3, 5, R
                ['drop3_inv4_strS1', '7th', 7, '5th', 5, '3rd', 5, 'R', 5], ['drop3_inv4_strS2', '7th', 14, '5th', 12, '3rd', 13, 'R', 12],
            ]

        elif chord_type == 'drop4':
            self.chord_type = [
                # First inversion: R, 5, 3, 7
                ['drop4_inv1_strS1', 'R', 8, '5th', 8, '3rd', 7, '7th', 9], ['drop4_inv1_strS2', 'R', 3, '5th', 5, '3rd', 5, '7th', 7],
                # 2nd inversion: 3, 7, R, 5
                ['drop4_inv2_strS1', '3rd', 12, '7th', 14, '5th', 12, 'R', 13], ['drop4_inv2_strS2', '3rd', 7, '7th', 9, '5th', 8, 'R', 8],
                # 3rd inversion: 5, R, 3, 7
                ['drop4_inv3_strS1', '5th', 3, 'R', 3, '7th', 4, '3rd', 5], ['drop4_inv3_strS2', '5th', 10, 'R', 10, '7th', 12, '3rd', 12],
                # 4th inversion: 7, 3, 5, R
                ['drop4_inv4_strS1', '7th', 7, '3rd', 7, 'R', 5, '5th', 8], ['drop4_inv4_strS2', '7th', 14, '3rd', 14, 'R', 13, '5th', 15],
            ]
        else:
            raise ValueError("Invalid chord type. Expected one of: %s" % chord_types)

        self.formsdict = {
            'M7': ['-'],                                    # [R, 3, 5, 7]
            '7': ['7th', '-'],                             # [R, 3, 5, b7]
            'm7': ['3rd', '7th', '-'],                         # [R, b3, 5, b7]
            'm7b5': ['3rd', '5th', '7th', '-'],  # [R, b3, b5, b7]
            'dim7': ['3rd', '5th', '7th', 'b7th', '-'],  # [R, b3, b5, bb7]
            'mM7': ['3rd', '-'],                      # [R, b3, 5, 7]
            '7#11': ['5th', '7th', '-'],           # [R, 3, #4, b7]
            'M7#11': ['5th', '-']                   # [R, 3, #4, 7]
        }

    def make(self):
        opr = self.formsdict[self.chord_formula].pop()
        operator_dict = {
            '+': operator.add,
            '-': operator.sub
        }
        templist_mk = []
        for row in self.chord_type:
            for arg in self.formsdict[self.chord_formula]:
                hit = row.index(arg)
                row[hit + 1] = operator_dict[opr](row[hit + 1], 1)
                row[hit] = 'b' + row[hit]

            new = [row[0], row[1].strip('thrd'), row[2], row[3].strip('thrd'), row[4], row[5].strip('thrd'), row[6], row[7].strip('thrd'), row[8]]
            # print(new)
            templist_mk.append(new)
        self.chord_type = templist_mk
        return self.chord_type

    def transpose(self):
        if self.root in sharps:
            x = string_builder(sharps, 'C')
            for y in x:
                y = y.index(self.root)
            templist_tr = []
            for chord in self.chord_type:
                new = [chord[0], chord[1], chord[2] + y, chord[3], chord[4] + y, chord[5], chord[6] + y, chord[7], chord[8] + y]
               # print('1ste  :', new)
                if (new[2] >= 12 and new[4] >= 12 and new[6] >= 12 and new[8] >= 12):
                    new = [chord[0], chord[1], new[2] - 12, chord[3], new[4] - 12, chord[5], new[6] - 12, chord[7], new[8] - 12]
                 #   print('2de  :', new)
                templist_tr.append(new)
            # print(templist_tr)
            return templist_tr
        elif self.root in flats:
            x = string_builder(flats, 'C')
            for y in x:
                y = y.index(self.root)
            templist_tr = []
            for chord in self.chord_type:
                new = [chord[0], chord[1], chord[2] + y, chord[3], chord[4] + y, chord[5], chord[6] + y, chord[7], chord[8] + y]
               # print('1ste  :', new)
                if (new[2] >= 12 and new[4] >= 12 and new[6] >= 12 and new[8] >= 12):
                    new = [chord[0], chord[1], new[2] - 12, chord[3], new[4] - 12, chord[5], new[6] - 12, chord[7], new[8] - 12]
                 #   print('2de  :', new)
                templist_tr.append(new)
            # print(templist_tr)
            return templist_tr
        else:
            return 'Error! check root note entry, '


def chords(xx, yy, zz):
    x = jchord(xx, yy, zz)
    # print(x)
    y = x.make()
    # print(y)
    z = x.transpose()
    # print(z)
    return z
