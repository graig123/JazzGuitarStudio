from django.shortcuts import render
from django.views.generic import View
import fredboardScales as gs
import random

# Create your views here.
postcount = 0


class ScalesPage(View):
    def get(self, request, *args, **kwargs):
        add = gs.create_svg('C', 'Ionian', 0)
        svg = add.draw_single_box()
        svg1 = ''.join(svg)

        return render(request, "scales.html", {'svg': svg1})

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


class AjaxScales(View):
    def post(self, request, *args, **kwargs):
        color = random.randrange(0, 2)
        print(request.POST)
        x1 = request.POST.get('note', 'C')
        x2 = request.POST.get('mode', 'Ionian')
        x3 = request.POST.get('box', 1)
        print(x1 + x2, x3)
        add1 = gs.create_svg(x1, x2, int(x3))
        add1 = add1.draw_single_box()
        svg3 = ''.join(add1)
        print('POST request was recieved on AjaxScales')
        return render(request, 'scales.html', {'svg': svg3})
