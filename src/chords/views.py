from django.shortcuts import render
from django.views.generic import View
import fredboardChords as gs
import random


class ChordsPage(View):
    def get(self, request, *args, **kwargs):
        add = gs.create_svg('CM7', 'drop2_inv1_strS1', 1)
        add = add.create()
        svg1 = ''.join(add)
        title = 'C  M7'
        subtitle = 'drop2 - inv1 - strS1'
        return render(request, "chords.html", {'svg': svg1, 'title': title, 'subtitle': subtitle})


class ArpegiosPage(View):
    def get(self, request, *args, **kwargs):
        add1 = gs.create_svg('CM7', 'drop2_inv1_strS1', 3)
        add1 = add1.create()
        add2 = gs.create_svg('CM7', 'drop2_inv2_strS1', 3)
        add2 = add2.create()
        add3 = gs.create_svg('CM7', 'drop2_inv3_strS1', 3)
        add3 = add3.create()
        add4 = gs.create_svg('CM7', 'drop2_inv4_strS1', 3)
        add4 = add4.create()
        add5 = gs.create_svg('CM7', 'drop2_inv1_strS3', 3)
        add5 = add5.create()
        add6 = gs.create_svg('CM7', 'drop2_inv2_strS3', 3)
        add6 = add6.create()
        add7 = gs.create_svg('CM7', 'drop2_inv3_strS3', 3)
        add7 = add7.create()
        add8 = gs.create_svg('CM7', 'drop2_inv4_strS3', 3)
        add8 = add8.create()

        svg1 = ''.join(add1) + ''.join(add2) + ''.join(add3) + ''.join(add4) + ''.join(add5) + ''.join(add6) + ''.join(add7) + ''.join(add8)
        title = 'C  M7'
        subtitle = 'drop2 - inv1 - strS1'
        return render(request, "chords.html", {'svg': svg1, 'title': title, 'subtitle': subtitle})
    # def post(self, request, *args, **kwargs):
    #     color = random.randrange(0, 3)
    #     x1 = request.POST.get('note', 'C')
    #     x2 = request.POST.get('shape', 'M7')
    #     x3 = request.POST.get('stringset', 'strS1')
    #     add = gs.create_svg(x1 + x2, 'drop2_inv1_' + x3, color)
    #     add = add.create()
    #     svg = ''.join(add)
    #     title = x1 + x2
    #     return render(request, 'scales.html', {'svg': svg, 'title': title})


class AjaxChord(View):
    def post(self, request, *args, **kwargs):
        color = random.randrange(0, 2)
        print(request.POST)
        x1 = request.POST.get('note', 'C')
        x2 = request.POST.get('shape', 'M7')
        x3 = request.POST.get('type_chord', 'drop2')
        x4 = request.POST.get('inv', 'inv1')
        x5 = request.POST.get('string', 'strS1')
        print(x1 + x2, x3 + '_' + x4 + '_' + x5)
        add1 = gs.create_svg(x1 + x2, x3 + '_' + x4 + '_' + x5, color)
        add1 = add1.create()
        svg3 = ''.join(add1)
        title = x1 + '  ' + x2
        subtitle = x3 + ' - ' + x4 + ' - ' + x5
        print('POST request was recieved on AjaxChord')
        return render(request, 'chords.html', {'svg': svg3, 'title': title, 'subtitle': subtitle})
