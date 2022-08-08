from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *


class IndexListView(ListView):
    template_name: str = 'index.html'

    def get(self, request):
        indexlogo = IndexLogo.objects.all()
        indexsl = IndexSl.objects.all()
        indexbg = IndexBg.objects.all()
        indexwelc = IndexWelc.objects.all()
        indexprog = IndexProg.objects.all()
        indexprog2 = IndexProg2.objects.all()
        indexplan =  IndexPlan.objects.all()
        indexplan2m = IndexPlan2M.objects.all()
        indexvideo = IndexVideo.objects.all()
        indexblog = IndexBlog.objects.all()
        indexchoos = IndexChoos.objects.all()

        return render(request, self.template_name, {'indexsl':indexsl, 'indexbg':indexbg, 
        'indexwelc':indexwelc, 'indexprog':indexprog, 'indexprog2':indexprog2,
         'indexplan':indexplan, 'indexplan2m':indexplan2m, 'indexvideo':indexvideo,
        'indexblog':indexblog, 'indexchoos':indexchoos, 'indexlogo':indexlogo } )



class AboutListView(ListView):
    template_name: str = 'about-us.html'

    def get(self, request):
        aboutbg = AboutBg.objects.all()
        aboutus = AboutUs.objects.all()
        aboutqu = AboutQu.objects.all()
        aboutsl = AboutSl.objects.all()
        abouttr = AboutTr.objects.all()
        aboutsl2 = AboutSl2.objects.all()
        aboutlogo = Aboutlogo.objects.all()
        indexlogo = IndexLogo.objects.all()
        

        return render(request, self.template_name, {'aboutbg':aboutbg, 'aboutus':aboutus,
        'aboutsl':aboutsl, 'aboutqu':aboutqu, 'abouttr':abouttr,'aboutsl2':aboutsl2, 'aboutlogo':aboutlogo, 'indexlogo':indexlogo})



class ScheduleListView(ListView):
    template_name = 'schedule.html'

    def get(self, request):
        indexchoos = IndexChoos.objects.all()
        scour = ScOur.objects.all()
        indexlogo = IndexLogo.objects.all()
        logo = Logo.objects.all()
        

        return render(request, self.template_name,{'indexchoos':indexchoos, 'scour':scour,'indexlogo':indexlogo,
        'logo':logo})

class GalleryListView(ListView):
    template_name = 'gallery.html'
    def get(self, request):
        gallerycat = GalCat.objects.all()
        gallery = Gallery.objects.all
        indexlogo = IndexLogo.objects.all()
        logo2 =Logo2.objects.all()
        return render(request, self.template_name,{'gallerycat ':gallerycat , 'gallery':gallery,'indexlogo':indexlogo,
        'logo2':logo2})





class BlogListView(ListView):
    template_name = 'blog.html'


    def get(self, request):
        blog1 = Blog1.objects.all()
        blog2 = Blog2.objects.all()
        indexlogo = IndexLogo.objects.all()
        logo3 = Logo3.objects.all()
        blogvideo =BlogVideo.objects.all()

        return render(request, self.template_name, {'blog1':blog1, 'blog2':blog2, 'indexlogo':indexlogo, 
        'logo3':logo3, 'blogvideo': blogvideo})

class BlogDetailListView(ListView):
    template_name = 'blog-single.html'


    def get(self, request):
        blogdet2 = BlogDet2.objects.all()
        blogdeth = BlogDeth.objects.all()
        blogdet = BlogDet.objects.all()
        blogdet3 = BlogDet3.objects.all()
        blogdetn = BlogDetN.objects.all()
        indexlogo = IndexLogo.objects.all()
        logo4 = Logo4.objects.all()
        return render(request, self.template_name, {'blogdet2':blogdet2, 'blogdeth':blogdeth, 'blogdet':blogdet, 'blogdet3':blogdet3,
        'blogdetn':blogdetn, 'indexlogo':indexlogo, 'logo4':logo4})


class ContactDetailView(DetailView):
    template_name = 'contact.html'
    indexlogo = IndexLogo.objects.all()

    def get(self, request):
        indexlogo = IndexLogo.objects.all()
        return render(request, self.template_name,{'indexlogo':indexlogo})