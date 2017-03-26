from Neck import sharps, flats, string_builder
from string import maketrans
import operator
import copy


class jscale:

    def __init__(self, root, scale_formula):
        self.root = root
        self.scale_formula = scale_formula
        # if self.scale_formula == 'Dorian':
        #     x = string_builder(sharps, self.root)
        #     # print(x)
        #     for y in x:

        #         findR = y.index(self.root) - 2
        #         self.root = y[findR]
        # print(self.root)

        self.scale_boxes = [
            # Box 1
            [['3', 0, '4', 1, '5', 3],
             ['6', 0, '7', 2, 'R', 3],
             ['2', 0, '3', 2, '4', 3],
             ['5', 0, '6', 2, 'X', 20],
             ['7', 0, 'R', 1, '2', 3],
             ['3', 0, '4', 1, '5', 3]],
            # Box 2
            [['5', 3, '6', 5, 'X', 20],
             ['7', 2, 'R', 3, '2', 5],
             ['3', 2, '4', 3, '5', 5],
             ['6', 2, '7', 4, 'R', 5],
             ['2', 3, '3', 5, '4', 6],
             ['5', 3, '6', 5, 'X', 20]],

            # Box 3
            [['6', 5, '7', 7, 'R', 8],
             ['2', 5, '3', 7, '4', 8],
             ['5', 5, '6', 7, 'X', 20],
             ['7', 4, 'R', 5, '2', 7],
             ['3', 5, '4', 6, '5', 8],
             ['6', 5, '7', 7, 'R', 8]],

            # Box 4
            [['7', 7, 'R', 8, '2', 10],
             ['3', 7, '4', 8, '5', 10],
             ['6', 7, '7', 9, 'R', 10],
             ['2', 7, '3', 9, '4', 10],
             ['5', 8, '6', 10, 'X', 20],
             ['7', 7, 'R', 8, '2', 10]],

            # Box 5
            [['2', 10, '3', 12, '4', 13],
             ['5', 10, '6', 12, 'X', 20],
             ['7', 9, 'R', 10, '2', 12],
             ['3', 9, '4', 10, '5', 12],
             ['6', 10, '7', 12, 'R', 13],
             ['2', 10, '3', 12, '4', 13]],

        ]

    def transpose(self):
        if self.root in sharps:
            x = string_builder(sharps, 'C')
            for y in x:
                y = y.index(self.root)

            for box in self.scale_boxes:
                for st in box:
                    size = len(st)
                    if size == 4:
                        st[1] = st[1] + y
                        st[3] = st[3] + y
                    else:
                        st[1] = st[1] + y
                        st[3] = st[3] + y
                        st[5] = st[5] + y
            for box in self.scale_boxes:
                if all(b[1] >= 12 and b[3] >= 12 and b[5] >= 12 for b in box) == True:
                    box[0][1], box[0][3], box[0][5] = box[0][1] - 12, box[0][3] - 12, box[0][5] - 12
                    box[1][1], box[1][3], box[1][5] = box[1][1] - 12, box[1][3] - 12, box[1][5] - 12
                    box[2][1], box[2][3], box[2][5] = box[2][1] - 12, box[2][3] - 12, box[2][5] - 12
                    box[3][1], box[3][3], box[3][5] = box[3][1] - 12, box[3][3] - 12, box[3][5] - 12
                    box[4][1], box[4][3], box[4][5] = box[4][1] - 12, box[4][3] - 12, box[4][5] - 12
                    box[5][1], box[5][3], box[5][5] = box[5][1] - 12, box[5][3] - 12, box[5][5] - 12

        self.formsdict = {
            'Ionian': 'R234567',
            'Dorian': '7R23456',
            'Phrygian': '67R2345',
            'Lydian': '567R234',
            'Mixolidian': '4567R23',
            'Aolian': '34567R2',
            'Locrian': '234567R',
        }

    def make(self):
        if self.scale_formula == 'Ionian':
            adj = 0
        elif self.scale_formula == 'Dorian':
            adj = 2
        trans1 = self.formsdict['Ionian']
        trans2 = self.formsdict[self.scale_formula]
        trans = maketrans(trans1, trans2)
        for box in self.scale_boxes:

            for st in box:
                count = 0
                st[0], st[2], st[4] = st[0].translate(trans), st[2].translate(trans), st[4].translate(trans)
                st[1], st[3], st[5] = (st[1] - adj), (st[3] - adj), (st[5] - adj)
        for box in self.scale_boxes:
            for st in box:
                if st[4] == 'X':
                    st.pop(4)
                    st.pop(4)
        for box in self.scale_boxes:
            if self.scale_formula == 'Dorian':
                for st in box:

                    if '3' in st:
                        ch = st.index('3')
                        st[ch] = 'b3'
                    if '7' in st:
                        ch = st.index('7')
                        st[ch] = 'b7'

        return (self.scale_boxes)


def scale(root, scale_type):
    x = jscale(root, scale_type)
    y = x.transpose()
    z = x.make()
    return z

scale('C', 'Dorian')
