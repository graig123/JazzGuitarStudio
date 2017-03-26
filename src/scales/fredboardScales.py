import guitar_class as guitar
# from guitar import drop2, drop3, drop4, closed


class create_svg:

    def __init__(self, root, scale, box):
        self.root = root
        self.scale = scale
        self.box = box
        self.hor_l = [170, 140, 110, 80, 50, 20]
        self.svg_t = []

    def draw_single_box(self):

        scale1 = guitar.scale(self.root, self.scale)
        for box in scale1:  # in elke box zitten 6 snaren

            color1 = 'black'
            color2 = '#fbbc05' #fbbc05  #34A853

            string_counter = 0

         # box color
         # counter voor welke snaar count_st

            for strings in box:  # in elke snaar zitten 2 of 4 noten
                hor = self.hor_l[string_counter]

                string_counter = string_counter + 1
                names = strings[0::2]
                notes = strings[1::2]
                note_counter = 0
                for values in notes:

                    if names[note_counter] == 'R':
                        if notes[note_counter] == 0:
                            ver = str(notes[note_counter] + 20)
                        else:
                            ver = str(notes[note_counter] * 50)
                        self.svg_t.append('<circle cx="')
                        self.svg_t.append(ver)
                        self.svg_t.append('" cy="')
                        self.svg_t.append(str(hor))
                        self.svg_t.append('" r="11" stroke="')
                        self.svg_t.append(color2)
                        self.svg_t.append('" stroke-width="3" fill="')
                        self.svg_t.append(color2)
                        self.svg_t.append('" ><title>')
                        # self.svg_t.append(chord)
                        self.svg_t.append('</title></circle>\n<g>\n<circle cx="')
                        self.svg_t.append(ver)
                        self.svg_t.append('" cy="')
                        self.svg_t.append(str(hor))
                        self.svg_t.append('" r="10" stroke="')
                        self.svg_t.append(color1)
                        self.svg_t.append('" stroke-width="3" fill="')
                        self.svg_t.append(color2)
                        self.svg_t.append('" ><title>')
                        # self.svg_t.append(note)
                        self.svg_t.append('</title></circle>\n<text x="')
                        self.svg_t.append(ver)
                        self.svg_t.append('" y="')
                        self.svg_t.append(str(hor))
                        self.svg_t.append('" text-anchor="middle" stroke="')
                        self.svg_t.append(color1)
                        self.svg_t.append('" stroke-width="1px" dy=".35em">')
                        self.svg_t.append(names[note_counter])
                        self.svg_t.append('</text>\n</g>\n')
                        note_counter = note_counter + 1

                    else:
                        if notes[note_counter] == 0:
                            ver = str(notes[note_counter] + 20)
                        else:
                            ver = str(notes[note_counter] * 50)
                        self.svg_t.append('<circle cx="')
                        self.svg_t.append(ver)
                        self.svg_t.append('" cy="')
                        self.svg_t.append(str(hor))
                        self.svg_t.append('" r="11" stroke="')
                        self.svg_t.append(color1)
                        self.svg_t.append('" stroke-width="3" fill="')
                        self.svg_t.append(color1)
                        self.svg_t.append('" ><title>')
                        # self.svg_t.append()
                        self.svg_t.append('</title></circle>\n<g>\n<circle cx="')
                        self.svg_t.append(ver)
                        self.svg_t.append('" cy="')
                        self.svg_t.append(str(hor))
                        self.svg_t.append('" r="10" stroke="')
                        self.svg_t.append(color2)
                        self.svg_t.append('" stroke-width="2" fill="')
                        self.svg_t.append(color1)
                        self.svg_t.append('" ><title>')
                       # self.svg_t.append()
                        self.svg_t.append('</title></circle>\n<text x="')
                        self.svg_t.append(ver)
                        self.svg_t.append('" y="')
                        self.svg_t.append(str(hor))
                        self.svg_t.append('" text-anchor="middle" stroke="')
                        self.svg_t.append(color2)
                        self.svg_t.append('" stroke-width="1px" dy=".35em">')
                        self.svg_t.append(names[note_counter])
                        self.svg_t.append('</text>\n</g>\n')
                        note_counter = note_counter + 1

     # in elke box zitten 6 snaren

     # box color
     # counter voor welke snaar count_st
        string_counter = 0
        for strings in scale1[self.box]:  # in elke snaar zitten 2 of 4 noten
            color1 = 'black'
            color2 = '#fbbc05'

            hor = self.hor_l[string_counter]

            string_counter = string_counter + 1
            names = strings[0::2]
            notes = strings[1::2]
            note_counter = 0
            for values in notes:

                if names[note_counter] == 'R':
                    if notes[note_counter] == 0:
                        ver = str(notes[note_counter] + 20)
                    else:
                        ver = str(notes[note_counter] * 50)
                    self.svg_t.append('<circle cx="')
                    self.svg_t.append(ver)
                    self.svg_t.append('" cy="')
                    self.svg_t.append(str(hor))
                    self.svg_t.append('" r="11" stroke="')
                    self.svg_t.append(color2)
                    self.svg_t.append('" stroke-width="3" fill="')
                    self.svg_t.append(color2)
                    self.svg_t.append('" ><title>')
                    # self.svg_t.append(chord)
                    self.svg_t.append('</title></circle>\n<g>\n<circle cx="')
                    self.svg_t.append(ver)
                    self.svg_t.append('" cy="')
                    self.svg_t.append(str(hor))
                    self.svg_t.append('" r="10" stroke="')
                    self.svg_t.append(color1)
                    self.svg_t.append('" stroke-width="3" fill="')
                    self.svg_t.append(color2)
                    self.svg_t.append('" ><title>')
                    # self.svg_t.append(note)
                    self.svg_t.append('</title></circle>\n<text x="')
                    self.svg_t.append(ver)
                    self.svg_t.append('" y="')
                    self.svg_t.append(str(hor))
                    self.svg_t.append('" text-anchor="middle" stroke="')
                    self.svg_t.append(color1)
                    self.svg_t.append('" stroke-width="1px" dy=".35em">')
                    self.svg_t.append(names[note_counter])
                    self.svg_t.append('</text>\n</g>\n')
                    note_counter = note_counter + 1

                else:
                    if notes[note_counter] == 0:
                        ver = str(notes[note_counter] + 20)
                    else:
                        ver = str(notes[note_counter] * 50)
                    self.svg_t.append('<circle cx="')
                    self.svg_t.append(ver)
                    self.svg_t.append('" cy="')
                    self.svg_t.append(str(hor))
                    self.svg_t.append('" r="11" stroke="')
                    self.svg_t.append(color1)
                    self.svg_t.append('" stroke-width="3" fill="')
                    self.svg_t.append(color1)
                    self.svg_t.append('" ><title>')
                    # self.svg_t.append()
                    self.svg_t.append('</title></circle>\n<g>\n<circle cx="')
                    self.svg_t.append(ver)
                    self.svg_t.append('" cy="')
                    self.svg_t.append(str(hor))
                    self.svg_t.append('" r="10" stroke="')
                    self.svg_t.append(color2)
                    self.svg_t.append('" stroke-width="2" fill="')
                    self.svg_t.append(color1)
                    self.svg_t.append('" ><title>')
                   # self.svg_t.append()
                    self.svg_t.append('</title></circle>\n<text x="')
                    self.svg_t.append(ver)
                    self.svg_t.append('" y="')
                    self.svg_t.append(str(hor))
                    self.svg_t.append('" text-anchor="middle" stroke="')
                    self.svg_t.append(color2)
                    self.svg_t.append('" stroke-width="1px" dy=".35em">')
                    self.svg_t.append(names[note_counter])
                    self.svg_t.append('</text>\n</g>\n')
                    note_counter = note_counter + 1

        return self.svg_t
        # def create(self):
        #     if self.cchord[1] in ('#', 'b'):
        #         a1 = self.cchord[:2]
        #         # print('Sharp or flat', a1)
        #         a2 = self.cchord[2:]
        #         # print(a2)
        #         ss = self.shape.index('_')
        #         a3 = self.shape[0:ss]
        #         # print(self.shape[0:ss])
        #         xx = guitar.chords(a1, a2, a3)
        #         draw_single_chord(xx, self.shape, self.chordcolor)
        #         return self.svg_t

        #     else:
        #         a1 = self.cchord[:1]
        #         # print(a1)
        #         a2 = self.cchord[1:]
        #         # print(a2)
        #         ss = self.shape.index('_')
        #         a3 = self.shape[0:ss]
        #         # print(self.shape[0:ss])
        #         xx = guitar.chords(a1, a2, a3)
        #         self.draw_single_chord(xx, self.shape, self.chordcolor)

        #         # f = open('test.svg', 'w')
        #         # f.write(''.join(svg))
        #         # f.close()
        #         return self.svg_t

        # for bb in har:
        #  draw_single_chord(bb)
# A = create_svg('E', 'Dorian', 3)
# C = A.draw_single_box()
# D = ''.join(C)
# print(C)
