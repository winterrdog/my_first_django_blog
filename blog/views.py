from django.shortcuts import render


def post_list(request):
    return render(request, "./html/post_list.html", {})
