import guitarClass as guitar
#from guitar import drop2, drop3, drop4, closed


begin = '''

<svg width="100%"   viewBox="0 0 835 200" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">

 <rect x="2" y="13" rx="5" ry="20" width="830" height="163" style="fill:rgb(183, 109, 29);stroke:black;stroke-width:2;opacity:1" />

<rect x="2" y="13" rx="5" ry="20" width="830" height="162" style="fill:rgb(172, 115, 57);opacity:0.4" />
<rect x="2" y="20" rx="5" ry="20" width="830" height="150" style="fill:rgb(140, 97, 53);opacity:0.5" />
<rect x="2" y="30" rx="5" ry="20" width="830" height="130" style="fill:rgb(140, 97, 53);opacity:0.5" />

<g
   transform="matrix(0,0.51439768,-0.35306362,0,-101.3453,-123.90702)"
   style="font-style:oblique;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;line-height:125%;font-family:Sawasdee;-inkscape-font-specification:'Sawasdee, Oblique';text-align:start;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
   id="text4136">
  <path
     inkscape:connector-curvature="0"
     d="m 340.34766,-333.35745 1.62109,0 -4.55078,21.60156 q -0.6836,3.22266 -3.28125,5.54688 -2.59766,2.30468 -5.60547,2.30468 -2.53906,0 -4.10156,-1.71875 -1.5625,-1.71875 -1.5625,-4.33593 0,-0.78125 0.19531,-1.79688 l 1.75781,0 q -0.17578,1.05469 -0.17578,1.42578 0,2.05078 1.21094,3.37891 1.23047,1.30859 3.125,1.30859 2.24609,0 4.23828,-1.77734 1.99219,-1.79688 2.53906,-4.33594 l 4.58985,-21.60156 z"
     id="path4141" />
  <path
     inkscape:connector-curvature="0"
     d="m 356.94922,-304.1973 -1.875,0 0,-0.52734 q 0,-1.13281 0.21484,-2.08984 l 0.29297,-1.54297 q -1.75781,1.95312 -4.02344,3.22265 -2.24609,1.26954 -4.45312,1.26954 -2.61719,0 -3.90625,-1.26954 -1.28906,-1.26953 -1.28906,-3.0664 0,-0.58594 0.11718,-1.11328 0.21485,-0.9961 0.70313,-1.83594 0.48828,-0.83984 1.07422,-1.42578 0.60547,-0.60547 1.5039,-1.07422 0.89844,-0.48828 1.69922,-0.78125 0.80078,-0.3125 1.9336,-0.52734 1.13281,-0.23438 1.95312,-0.33204 0.83984,-0.11718 2.03125,-0.17578 1.21094,-0.0586 1.89453,-0.0586 0.70313,-0.0195 1.77735,-0.0195 l 0.52734,0 q 0.17578,-0.80078 0.17578,-1.71875 0,-2.5 -1.36719,-3.90625 -1.36718,-1.42578 -3.39843,-1.42578 -1.38672,0 -2.85157,0.72265 -1.46484,0.72266 -2.69531,2.10938 l -1.25,-0.91797 q 1.58203,-1.83594 3.47656,-2.75391 1.89453,-0.91797 3.71094,-0.91797 2.67578,0 4.41406,1.75782 1.75782,1.75781 1.75782,4.84375 0,0.74218 -0.21485,2.20703 l -1.83594,8.73047 q -0.21484,1.01562 -0.21484,1.66015 0,0.56641 0.11719,0.95703 z m -9.45313,-1.40625 q 2.26563,0 4.70703,-1.5039 2.44141,-1.52344 3.86719,-3.4375 l 0.80078,-3.75 q -0.9375,0.0195 -1.5625,0.0391 -0.60547,0.0195 -1.67968,0.0977 -1.07422,0.0586 -1.83594,0.15625 -0.76172,0.0781 -1.79688,0.27343 -1.01562,0.19532 -1.75781,0.44922 -0.74219,0.23438 -1.5625,0.625 -0.80078,0.3711 -1.34766,0.83985 -0.52734,0.44922 -0.95703,1.09375 -0.42968,0.64453 -0.58593,1.40625 -0.0781,0.46875 -0.0781,0.66406 0,1.25 0.9375,2.14844 0.9375,0.89843 2.85156,0.89843 z"
     id="path4143" />
  <path
     inkscape:connector-curvature="0"
     d="m 366.98828,-324.00198 13.59375,0 -16.52344,18.04687 12.59766,0 -0.91797,1.75781 -15.35156,0 16.5625,-18.0664 -10.91797,0 0.95703,-1.73828 z"
     id="path4145" />
  <path
     inkscape:connector-curvature="0"
     d="m 384.33203,-324.00198 13.59375,0 -16.52344,18.04687 12.59766,0 -0.91797,1.75781 -15.35156,0 16.5625,-18.0664 -10.91797,0 0.95703,-1.73828 z"
     id="path4147" />
  <path
     inkscape:connector-curvature="0"
     d="m 417.69141,-324.00198 1.875,0 q -0.66407,0.91797 -1.03516,2.61718 l -3.65234,17.1875 q -0.58594,2.73438 -2.30469,5.07813 -1.69922,2.34375 -4.1211,3.71094 -2.40234,1.38672 -4.90234,1.38672 -3.41797,0 -5.42969,-2.53907 l 1.52344,-1.21093 q 1.64063,2.01171 4.35547,2.01171 3.00781,0 5.70312,-2.46093 2.69532,-2.46094 3.4375,-5.97657 l 1.07422,-5.07812 q -1.1914,2.12891 -3.71093,3.75 -2.5,1.62109 -4.76563,1.62109 -3.18359,0 -5.13672,-2.20703 -1.95312,-2.22656 -1.95312,-5.60547 0,-2.38281 0.99609,-4.70703 0.99609,-2.32422 2.57813,-4.04297 1.60156,-1.71875 3.67187,-2.77343 2.08984,-1.07422 4.17969,-1.07422 2.22656,0 4.04297,1.67968 1.83593,1.66016 2.14843,3.71094 l 0.52735,-2.46094 q 0.3125,-1.44531 0.89844,-2.61718 z m -2.5586,9.88281 q 0.21485,-1.07422 0.21485,-1.99219 0,-2.8125 -1.6211,-4.6289 -1.62109,-1.81641 -4.14062,-1.81641 -2.26563,0 -4.4336,1.46484 -2.16797,1.44532 -3.55468,3.88672 -1.36719,2.42188 -1.36719,5.07813 0,2.8125 1.62109,4.64843 1.6211,1.83594 4.14063,1.83594 2.98828,0 5.68359,-2.48047 2.71484,-2.5 3.45703,-5.99609 z"
     id="path4149" />
  <path
     inkscape:connector-curvature="0"
     d="m 425.60156,-324.00198 1.73828,0 -2.57812,12.24609 q -0.17578,0.64453 -0.17578,1.46484 0,2.03125 1.15234,3.33985 1.17188,1.30859 3.04688,1.30859 2.24609,0 4.25781,-1.77734 2.01172,-1.79688 2.55859,-4.33594 l 2.57813,-12.24609 1.75781,0 -2.57813,12.24609 q -0.68359,3.22266 -3.28125,5.54688 -2.59765,2.30468 -5.60546,2.30468 -2.53907,0 -4.1211,-1.71875 -1.5625,-1.71875 -1.5625,-4.33593 0,-0.6836 0.21485,-1.79688 l 2.59765,-12.24609 z"
     id="path4151" />
  <path
     inkscape:connector-curvature="0"
     d="m 446.71484,-328.31839 q 0,-0.76172 0.58594,-1.34766 0.58594,-0.60546 1.34766,-0.60546 0.5664,0 0.9375,0.37109 0.37109,0.35156 0.37109,0.91797 0,0.70312 -0.60547,1.28906 -0.58594,0.58594 -1.36719,0.58594 -0.54687,0 -0.91796,-0.35156 -0.35157,-0.35157 -0.35157,-0.85938 z m -2.69531,24.12109 -1.75781,0 4.19922,-19.80468 1.73828,0 -4.17969,19.80468 z"
     id="path4153" />
  <path
     inkscape:connector-curvature="0"
     d="m 452.30078,-304.1973 -1.75781,0 3.84765,-18.0664 -1.75781,0 0.35156,-1.73828 1.75782,0 0.99609,-4.6875 1.75781,0 -1.01562,4.6875 5.46875,0 -0.91797,1.73828 -4.88281,0 -3.84766,18.0664 z"
     id="path4155" />
  <path
     inkscape:connector-curvature="0"
     d="m 474.76172,-304.1973 -1.875,0 0,-0.52734 q 0,-1.13281 0.21484,-2.08984 l 0.29297,-1.54297 q -1.75781,1.95312 -4.02344,3.22265 -2.24609,1.26954 -4.45312,1.26954 -2.61719,0 -3.90625,-1.26954 -1.28906,-1.26953 -1.28906,-3.0664 0,-0.58594 0.11718,-1.11328 0.21485,-0.9961 0.70313,-1.83594 0.48828,-0.83984 1.07422,-1.42578 0.60547,-0.60547 1.5039,-1.07422 0.89844,-0.48828 1.69922,-0.78125 0.80078,-0.3125 1.9336,-0.52734 1.13281,-0.23438 1.95312,-0.33204 0.83984,-0.11718 2.03125,-0.17578 1.21094,-0.0586 1.89453,-0.0586 0.70313,-0.0195 1.77735,-0.0195 l 0.52734,0 q 0.17578,-0.80078 0.17578,-1.71875 0,-2.5 -1.36719,-3.90625 -1.36718,-1.42578 -3.39843,-1.42578 -1.38672,0 -2.85157,0.72265 -1.46484,0.72266 -2.69531,2.10938 l -1.25,-0.91797 q 1.58203,-1.83594 3.47656,-2.75391 1.89453,-0.91797 3.71094,-0.91797 2.67578,0 4.41406,1.75782 1.75782,1.75781 1.75782,4.84375 0,0.74218 -0.21485,2.20703 l -1.83594,8.73047 q -0.21484,1.01562 -0.21484,1.66015 0,0.56641 0.11719,0.95703 z m -9.45313,-1.40625 q 2.26563,0 4.70703,-1.5039 2.44141,-1.52344 3.86719,-3.4375 l 0.80078,-3.75 q -0.9375,0.0195 -1.5625,0.0391 -0.60547,0.0195 -1.67968,0.0977 -1.07422,0.0586 -1.83594,0.15625 -0.76172,0.0781 -1.79688,0.27343 -1.01562,0.19532 -1.75781,0.44922 -0.74219,0.23438 -1.5625,0.625 -0.80078,0.3711 -1.34766,0.83985 -0.52734,0.44922 -0.95703,1.09375 -0.42968,0.64453 -0.58593,1.40625 -0.0781,0.46875 -0.0781,0.66406 0,1.25 0.9375,2.14844 0.9375,0.89843 2.85156,0.89843 z"
     id="path4157" />
  <path
     inkscape:connector-curvature="0"
     d="m 484.50781,-324.00198 1.875,0 q 0.0391,0.15625 0.0391,0.60547 0,0.9375 -0.2539,2.01171 l -0.54688,2.46094 q 0.80078,-1.5039 2.79297,-3.125 2.01172,-1.62109 3.76953,-2.26562 l 1.66016,1.38672 q -1.71875,0 -3.69141,1.21093 -1.95312,1.21094 -3.49609,3.22266 -1.52344,1.99219 -1.99219,4.12109 l -2.1289,10.17578 -1.75782,0 3.63282,-17.1875 q 0.21484,-1.03515 0.21484,-1.66015 0,-0.54688 -0.11719,-0.95703 z"
     id="path4159" />
  <path
     inkscape:connector-curvature="0"
     d="m 487.86719,-305.25198 q 0,-0.78125 0.64453,-1.34766 0.66406,-0.56641 1.36719,-0.56641 0.58593,0 0.97656,0.3711 0.39062,0.37109 0.39062,0.9375 0,0.80078 -0.66406,1.38672 -0.66406,0.5664 -1.36719,0.5664 -0.58593,0 -0.97656,-0.39062 -0.37109,-0.39063 -0.37109,-0.95703 z"
     id="path4161" />
  <path
     inkscape:connector-curvature="0"
     d="m 501.87109,-328.31839 q 0,-0.76172 0.58594,-1.34766 0.58594,-0.60546 1.34766,-0.60546 0.5664,0 0.9375,0.37109 0.37109,0.35156 0.37109,0.91797 0,0.70312 -0.60547,1.28906 -0.58594,0.58594 -1.36719,0.58594 -0.54687,0 -0.91796,-0.35156 -0.35157,-0.35157 -0.35157,-0.85938 z m -2.69531,24.12109 -1.75781,0 4.19922,-19.80468 1.73828,0 -4.17969,19.80468 z"
     id="path4163" />
  <path
     inkscape:connector-curvature="0"
     d="m 509.42969,-318.63089 q 0,-2.1875 1.75781,-3.94531 1.75781,-1.77735 4.25781,-1.77735 1.66016,0 2.8711,0.9961 1.21093,0.97656 1.46484,2.85156 l -1.75781,0.56641 q -0.17578,-1.3086 -1.01563,-1.99219 -0.83984,-0.70313 -1.95312,-0.70313 -1.60157,0 -2.67578,1.15235 -1.07422,1.15234 -1.07422,2.42187 0,0.66407 0.41015,1.21094 0.42969,0.54688 1.09375,0.9375 0.66407,0.39063 1.46485,0.78125 0.80078,0.37109 1.60156,0.82031 0.82031,0.42969 1.48437,0.95703 0.66407,0.52735 1.07422,1.32813 0.42969,0.80078 0.42969,1.81641 0,1.89453 -1.09375,3.59375 -1.09375,1.69921 -2.92969,2.73437 -1.83593,1.01563 -3.86718,1.01563 -2.14844,0 -3.59375,-1.3086 -1.42579,-1.32812 -1.42579,-3.90625 0,-0.48828 0.0586,-0.76172 l 1.77734,-0.2539 q 0,0.11718 -0.0195,0.3125 -0.0195,0.19531 -0.0195,0.29297 0,1.91406 1.03516,2.91015 1.03515,0.97656 2.59765,0.97656 2.1875,0 3.92578,-1.5625 1.75782,-1.58203 1.75782,-3.59375 0,-1.11328 -0.80079,-1.91406 -0.78125,-0.82031 -1.91406,-1.34765 -1.11328,-0.52735 -2.22656,-1.07422 -1.11328,-0.54688 -1.91406,-1.42578 -0.78125,-0.89844 -0.78125,-2.10938 z"
     id="path4165" />
  <path
     inkscape:connector-curvature="0"
     d="m 524.87891,-304.1973 -1.75782,0 3.84766,-18.0664 -1.75781,0 0.35156,-1.73828 1.75781,0 0.9961,-4.6875 1.75781,0 -1.01563,4.6875 5.46875,0 -0.91797,1.73828 -4.88281,0 -3.84765,18.0664 z"
     id="path4167" />
</g>

<rect x="2" y="40" rx="5" ry="20" width="830" height="110" style="fill:rgb(140, 97, 53);opacity:0.6" />

<circle cx="145" cy="95" r="10" stroke="#804000" stroke-width="5" fill="#DCEBCC" />
<circle cx="245" cy="95" r="10" stroke="#804000" stroke-width="5" fill="#DCEBCC" />
<circle cx="345" cy="95" r="10" stroke="#804000" stroke-width="5" fill="#DCEBCC" />
<circle cx="445" cy="95" r="10" stroke="#804000" stroke-width="5" fill="#DCEBCC" />
<circle cx="595" cy="65" r="10" stroke="#804000" stroke-width="5" fill="#DCEBCC" />
<circle cx="595" cy="125" r="10" stroke="#804000" stroke-width="5" fill="#DCEBCC" />
<circle cx="745" cy="95" r="10" stroke="#804000" stroke-width="5" fill="#DCEBCC" />

<line x1="20" y1="10" x2="20" y2="179" stroke="black" stroke-width="6"  />
<line x1="70" y1="10" x2="70" y2="179" stroke="black" stroke-width="4" />
<line x1="70" y1="11" x2="70" y2="178" stroke="grey" stroke-width="2" />
<line x1="120" y1="10" x2="120" y2="179" stroke="black" stroke-width="4" />
<line x1="120" y1="11" x2="120" y2="178" stroke="grey" stroke-width="2" />
<line x1="170" y1="10" x2="170" y2="179" stroke="black" stroke-width="4" />
<line x1="170" y1="11" x2="170" y2="178" stroke="grey" stroke-width="2" />
<line x1="220" y1="10" x2="220" y2="179" stroke="black" stroke-width="4" />
<line x1="220" y1="11" x2="220" y2="178" stroke="grey" stroke-width="2" />
<line x1="270" y1="10" x2="270" y2="179" stroke="black" stroke-width="4" />
<line x1="270" y1="11" x2="270" y2="178" stroke="grey" stroke-width="2" />
<line x1="320" y1="10" x2="320" y2="179" stroke="black" stroke-width="4" />
<line x1="320" y1="11" x2="320" y2="178" stroke="grey" stroke-width="2" />
<line x1="370" y1="10" x2="370" y2="179" stroke="black" stroke-width="4" />
<line x1="370" y1="11" x2="370" y2="178" stroke="grey" stroke-width="2" />
<line x1="420" y1="10" x2="420" y2="179" stroke="black" stroke-width="4" />
<line x1="420" y1="11" x2="420" y2="178" stroke="grey" stroke-width="2" />
<line x1="470" y1="10" x2="470" y2="179" stroke="black" stroke-width="4" />
<line x1="470" y1="11" x2="470" y2="178" stroke="grey" stroke-width="2" />
<line x1="520" y1="10" x2="520" y2="179" stroke="black" stroke-width="4" />
<line x1="520" y1="11" x2="520" y2="178" stroke="grey" stroke-width="2" />
<line x1="570" y1="10" x2="570" y2="179" stroke="black" stroke-width="4" />
<line x1="570" y1="11" x2="570" y2="178" stroke="grey" stroke-width="2" />
<line x1="620" y1="10" x2="620" y2="179" stroke="black" stroke-width="4" />
<line x1="620" y1="11" x2="620" y2="178" stroke="grey" stroke-width="2" />
<line x1="670" y1="10" x2="670" y2="179" stroke="black" stroke-width="4" />
<line x1="670" y1="11" x2="670" y2="178" stroke="grey" stroke-width="2" />
<line x1="720" y1="10" x2="720" y2="179" stroke="black" stroke-width="4" />
<line x1="720" y1="11" x2="720" y2="178" stroke="grey" stroke-width="2" />
<line x1="770" y1="10" x2="770" y2="179" stroke="black" stroke-width="4" />
<line x1="770" y1="11" x2="770" y2="178" stroke="grey" stroke-width="2" />
<line x1="820" y1="10" x2="820" y2="179" stroke="black" stroke-width="4" />
<line x1="820" y1="11" x2="820" y2="178" stroke="grey" stroke-width="2" />

  <g fill="" stroke="#A9A9A9">
    <path stroke-width="2" d="M22 20 l800 0" />
    <path stroke-width="2" d="M22 50 l800 0" />
    <path stroke-width="2" d="M22 80 l800 0" />
    <path stroke-width="3" d="M22 110 l800 0" />
    <path stroke-width="4" d="M22 140 l800 0" />
    <path stroke-width="5" d="M22 170 l800 0" />
  </g>

 <g fill="" stroke="#808080">
    <path stroke-width="1" d="M24 21 l800 0" />
    <path stroke-width="1" d="M24 51 l800 0" />
    <path stroke-width="1" d="M24 81 l800 0" />
    <path stroke-width="2" d="M24 111 l800 0" />
    <path stroke-width="2" d="M24 141 l800 0" />
    <path stroke-width="3" d="M24 171 l800 0" />
  </g>\n\n'''


class create_svg:  # bv: cchord='D#m7' shape='drop3_inv2_strS1' chordcolor=1

    def __init__(self, cchord, shape, chordcolor):
        self.cchord = cchord
        self.shape = shape
        self.chordcolor = chordcolor
        self.svg_t = []

    # def draw_single_chord(chord1, chord2, count_color):  # chord1 = lijst met alle chords, chord2 = 'drop2_inv1_strS1', count_color= een getal 0tot 4
    def draw_single_chord(self, chord1, chord2, count_color):

        count = 0
        note = ''
        chord = ''

        # find chordtype, inversion and stringset
        count_row = 0
        for rows in chord1:

            if chord2 in rows:
                row1 = chord1[count_row]
                count_row = 0  # reset rowcounter for next run
            else:
                count_row += 1
        # find stringSet and set it
        if 'closed' in row1[0] and 'strS3' in row1[0]:
            hor_l = [110, 80, 50, 20]  # stringset 3
        elif 'closed' in row1[0] and 'strS2' in row1[0]:
            hor_l = [140, 110, 80, 50]  # stringset 2
        elif 'closed' in row1[0] and 'strS1' in row1[0]:
            hor_l = [170, 140, 110, 80]  # stringset 1
        elif 'drop2' in row1[0] and 'strS3' in row1[0]:
            hor_l = [110, 80, 50, 20]  # stringset 3
        elif 'drop2' in row1[0] and 'strS2' in row1[0]:
            hor_l = [140, 110, 80, 50]  # stringset 2
        elif 'drop2' in row1[0] and 'strS1' in row1[0]:
            hor_l = [170, 140, 110, 80]  # stringset 1
        elif 'drop3' in row1[0] and 'strS2' in row1[0]:
            hor_l = [140, 80, 50, 20]  # stringset 3
        elif 'drop3' in row1[0] and 'strS1' in row1[0]:
            hor_l = [170, 110, 80, 50]  # stringset 2
        elif 'drop4' in row1[0] and 'strS2' in row1[0]:
            hor_l = [140, 110, 50, 20]  # stringset 3
        elif 'drop4' in row1[0] and 'strS1' in row1[0]:
            hor_l = [170, 140, 80, 50]  # stringset 2

        else:
            print('Stringset Error, please provide a valid stringset')

        chord1 = [row1[2], row1[4], row1[6], row1[8]]
        intr = [row1[1], row1[3], row1[5], row1[7]]

        if count_color == 0:
            color1 = 'black'
            color2 = '#34A853'  # green (start)
            count_color += 1

        elif count_color == 1:
            color1 = 'black'
            color2 = '#fbbc05'  # orange
            count_color += 1

        elif count_color == 2:
            color1 = 'black'
            color2 = '#4285f4'  # blue
            count_color += 1

        elif count_color == 3:
            color1 = 'black'
            color2 = '#ea4335'  # red
            count_color += 1

        elif count_color == 4:
            color1 = 'black'
            color2 = '#954a97'  # purple
            count_color += 1
        elif count_color == 5:
            color1 = 'black'
            color2 = '#6666ff'
            count_color += 1
        elif count_color == 6:
            color1 = 'black'
            color2 = 'red'
            count_color += 1
        for x in chord1:
            if intr[count] == 'R':
                if x == 0:
                    ver = str(+ 20)
                else:
                    ver = str(x * 50)
                hor = str(hor_l[count])
                interval = str(intr[count])
                # svg.append('<circle cx="{}" cy="{}" r="11" stroke="{}" stroke-width="3" fill="{}" ><title>{}</title></circle<g><circle cx="{}" cy="{}" r="10" stroke="{}" stroke-width="2" fill="{}" ><title>{}</title></circle><text x="{}" y="{}" text-anchor="middle" stroke="{}" stroke-width="1px" dy=".35em">{}</text></g> '.format(ver, hor, color1, color1, chord, ver, hor, color2, color1, chord, ver, hor, color2, interval ))

                self.svg_t.append('<circle cx="')
                self.svg_t.append(ver)
                self.svg_t.append('" cy="')
                self.svg_t.append(hor)
                self.svg_t.append('" r="11" stroke="')
                self.svg_t.append(color2)
                self.svg_t.append('" stroke-width="3" fill="')
                self.svg_t.append(color2)
                self.svg_t.append('" ><title>')
                self.svg_t.append(chord)
                self.svg_t.append('</title></circle>\n<g>\n<circle cx="')
                self.svg_t.append(ver)
                self.svg_t.append('" cy="')
                self.svg_t.append(hor)
                self.svg_t.append('" r="10" stroke="')
                self.svg_t.append(color1)
                self.svg_t.append('" stroke-width="3" fill="')
                self.svg_t.append(color2)
                self.svg_t.append('" ><title>')
                self.svg_t.append(note)
                self.svg_t.append('</title></circle>\n<text x="')
                self.svg_t.append(ver)
                self.svg_t.append('" y="')
                self.svg_t.append(hor)
                self.svg_t.append('" text-anchor="middle" stroke="')
                self.svg_t.append(color1)
                self.svg_t.append('" stroke-width="1px" dy=".35em">')
                self.svg_t.append(interval)
                self.svg_t.append('</text>\n</g>\n')
                count += 1
            else:
                if x == 0:
                    ver = str(+ 20)
                else:
                    ver = str(x * 50)
                # ver = str(x * 50)
                hor = str(hor_l[count])
                interval = str(intr[count])
                # svg.append('<circle cx="' + ver + '" cy="' + hor + '" r="11" stroke="' + color1 + '" stroke-width="3" fill="' + color1 + '" ><title>' + chord + '</title></circle<g><circle cx="' + ver + '" cy="' + hor + '" r="10" stroke="' + color2 + '" stroke-width="2" fill="' + color1 + '" ><title>' + chord + '</title></circle><text x="' + ver + '" y="' + hor + '" text-anchor="middle" stroke="' + color2 + '" stroke-width="1px" dy=".35em">' + interval)
                self.svg_t.append('<circle cx="')
                self.svg_t.append(ver)
                self.svg_t.append('" cy="')
                self.svg_t.append(hor)
                self.svg_t.append('" r="11" stroke="')
                self.svg_t.append(color1)
                self.svg_t.append('" stroke-width="3" fill="')
                self.svg_t.append(color1)
                self.svg_t.append('" ><title>')
                self.svg_t.append(chord)
                self.svg_t.append('</title></circle>\n<g>\n<circle cx="')
                self.svg_t.append(ver)
                self.svg_t.append('" cy="')
                self.svg_t.append(hor)
                self.svg_t.append('" r="10" stroke="')
                self.svg_t.append(color2)
                self.svg_t.append('" stroke-width="2" fill="')
                self.svg_t.append(color1)
                self.svg_t.append('" ><title>')
                self.svg_t.append(chord)
                self.svg_t.append('</title></circle>\n<text x="')
                self.svg_t.append(ver)
                self.svg_t.append('" y="')
                self.svg_t.append(hor)
                self.svg_t.append('" text-anchor="middle" stroke="')
                self.svg_t.append(color2)
                self.svg_t.append('" stroke-width="1px" dy=".35em">')
                self.svg_t.append(interval)
                self.svg_t.append('</text>\n</g>\n')
                count += 1

    def create(self):
        if self.cchord[1] in ('#', 'b'):
            a1 = self.cchord[:2]
            # print('Sharp or flat', a1)
            a2 = self.cchord[2:]
            # print(a2)
            ss = self.shape.index('_')
            a3 = self.shape[0:ss]
            # print(self.shape[0:ss])
            xx = guitar.chords(a1, a2, a3)
            draw_single_chord(xx, self.shape, self.chordcolor)
            return self.svg_t

        else:
            a1 = self.cchord[:1]
            # print(a1)
            a2 = self.cchord[1:]
            # print(a2)
            ss = self.shape.index('_')
            a3 = self.shape[0:ss]
            # print(self.shape[0:ss])
            xx = guitar.chords(a1, a2, a3)
            self.draw_single_chord(xx, self.shape, self.chordcolor)

            # f = open('test.svg', 'w')
            # f.write(''.join(svg))
            # f.close()
            return self.svg_t


# for bb in har:
#  draw_single_chord(bb)
A = create_svg('AM7', 'drop3_inv1_strS1', 2)
A = A.create()
print(A)
# create_svg('Dm7b5', 'drop2_inv3_strS2', 2)
# create_svg('Cdim7', 'drop2_inv1_strS2', 0)
# create_svg('Cdim7', 'drop2_inv2_strS2', 1)
# create_svg('Cdim7', 'drop2_inv3_strS2', 2)
# create_svg('Cdim7', 'drop2_inv4_strS2', 3)
# create_svg('D#M7', 'drop2_inv2_strS2', 2)
# create_svg('D#M7', 'drop2_inv3_strS2', 2)
# create_svg('D#M7', 'drop2_inv4_strS2', 2)
# create_svg('D#M7', 'drop2_inv1_strS3', 2)
# create_svg('D#M7', 'drop2_inv2_strS3', 2)
# create_svg('D#M7', 'drop2_inv3_strS3', 2)
# create_svg('D#M7', 'drop2_inv4_strS3', 2)
# create_svg('Em7', 'drop2_inv4_strS2', 2)
# create_svg('FM7', 'drop2_inv4_strS2', 4)
# create_svg('G7', 'drop2_inv4_strS2', 1)
# create_svg('Am7', 'drop2_inv4_strS2', 2)
# create_svg('Bm7b5', 'drop2_inv4_strS2', 3)
# svg.append('<a xlink:href="http://jazzguita.it"><rect x="2" y="13" rx="5" ry="20" width="830" height="163" style="fill:rgb(183, 109, 29);stroke:black;stroke-width:2;opacity:0" /></a>')
