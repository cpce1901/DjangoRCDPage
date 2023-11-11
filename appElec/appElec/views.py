from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import HttpResponse

 
def error_404_view(request, exception):  
    return render(request, 'errors/404.html', status=404)


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "",
        "Disallow: /admin/",
        "",
        "Sitemap: https://www.electricidadrcd.cl/sitemap.xml"
        
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

