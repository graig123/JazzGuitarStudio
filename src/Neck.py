# hieronder een manier om snel een gitaarneck overzicht te maken me #(kruizen) of b(mollen)


sharps = 'A A# B C C# D D# E F F# G G#'.split() * 3
flats = 'A Bb B C Db D Eb E F Gb G Ab'.split() * 3


def string_builder(notes_type, *args):
    """ building the 6 strings with 24 notes each """
    temp = []
    for arg in args:
        temp.append(notes_type[notes_type.index(arg):notes_type.index(arg) + 25])
    return temp

# neck = string_builder(sharps, 'E', 'A', 'D', 'G', 'B', 'E')
# for string in neck:
#     print(string)


def string_sets():
    standard = ['E', 'A', 'D', 'G', 'B', 'E']
    set_drop2_top = [standard[0], standard[1], standard[2], standard[3], None, None]
    set_drop2_midle = [None, standard[1], standard[2], standard[3], standard[4], None]
    set_drop2_bottom = [None, None, standard[2], standard[3], standard[4], standard[5]]
    set_drop3_top = [standard[0], None, standard[2], standard[3], standard[4], None]
    set_drop3_bottom = [None, standard[1], None, standard[3], standard[4], standard[5]]
    set_drop_2and4_top = [standard[0], standard[1], None, standard[3], standard[4], None]
    set_drop_2and4_bottom = [None, standard[1], standard[2], None, standard[4], standard[5]]

# for i in strings_builder(flats):
#     print(i)
