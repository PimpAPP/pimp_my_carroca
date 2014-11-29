from django.shortcuts import render

# Create your views here.

def hallo(request):
    template = "hello.html"
    return render_to_response(
        template, {}, context_instance=RequestContext(request))

def show_maps(request):
    template = "maps/show_map.html"
    return render_to_response(
        template, {}, context_instance=RequestContext(request))

def new_carroca(request):
    template = "maps/new_carroca.html"
    return render_to_response(
        template, {}, context_instance=RequestContext(request))
