from distutils.command.upload import upload
from html.entities import name2codepoint
from django.db import models

# Create your models here.
class IndexLogo(models.Model):
    img = models.ImageField('logo', upload_to='media')
    def __img__(self):
        return self.img

    class Meta:
        verbose_name = 'IndexLogo'
        verbose_name_plural = 'IndexSLogo'

class IndexSl(models.Model):
    name = models.CharField('sl name', max_length=40)
    nam2 = models.CharField('sl name2', max_length=40)
    img = models.ImageField('In image', upload_to='media')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'IndexSl'
        verbose_name_plural = 'IndexSls'


class IndexBg(models.Model):
    name = models.CharField('bg name', max_length=30)
    name2 = models.TextField('bg text')
    img = models.ImageField('bg image', upload_to='media')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'IndexBg'
        verbose_name_plural = 'IndexBgs'



class IndexWelc(models.Model):
    name = models.CharField('welc name', max_length=30 )
    name2 = models.CharField('welc name2', max_length=80, null=True )
    name3 = models.TextField('text name')
    img = models.ImageField('welc img', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'IndexWelc'
        verbose_name_plural = 'IndexWelcs'



class IndexProg(models.Model):
    name = models.CharField('prog name', max_length=40)
    name2 = models.TextField('prog text')
    img = models.ImageField('prog img', null=True, upload_to='media' )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'IndexProg'
        verbose_name_plural = 'IndexProgs'


class IndexProg2(models.Model):
    name = models.CharField('prog2 name', max_length=40)
    name2 = models.TextField('prog2 text')
    img = models.ImageField('prog2 img', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'IndexProg2'
        verbose_name_plural = 'IndexProg2s'



class IndexPlan(models.Model):
    name = models.CharField('plan name', max_length=80)
    name2 = models.TextField('plan text')
    img = models.ImageField('plan2 img', upload_to='media')
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'IndexPlan'
        verbose_name_plural = 'IndexPlans'


class IndexPlan2M(models.Model):
    name =  models.CharField('plan2 name', max_length=80)
    price = models.IntegerField('plan2 price')
    name2 =  models.CharField('plan2 name', max_length=80)
    name3 =  models.CharField('plan2 name', max_length=80)
    name4 =  models.CharField('plan2 name', max_length=80)
    name5 =  models.CharField('plan2 name', max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'IndexPlan2M'
        verbose_name_plural = 'IndexPlan2Ms'



class IndexChoos(models.Model):
    name = models.CharField('ch name', max_length=80)
    name2 = models.TextField('ch text')
    img = models.ImageField('img name', upload_to='media')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'IndexChoos'
        verbose_name_plural = 'IndexChooss'

class IndexVideo(models.Model):
    name = models.CharField('Video name', max_length=90)
    img = models.ImageField('Video img', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'IndexVideo'
        verbose_name_plural = 'IndexVideos'


class IndexBlog(models.Model):
    name = models.CharField('blog name', max_length=90)
    name2 = models.CharField('blog name2', max_length=90)
    img = models.ImageField('img bolo', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'IndexBlog'
        verbose_name_plural = 'IndexBlogs'


# About

class AboutBg(models.Model):
    name = models.CharField('bg name', max_length=90)
    name2 = models.TextField('bg text')
    img = models.ImageField('img', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutBg'
        verbose_name_plural = 'AboutBgs'


class AboutUs(models.Model):
    name = models.CharField('name ', max_length=80)
    name2 = models.TextField('Us text')
    name3 = models.TextField('Us text2', null=True)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUss'


class AboutQu(models.Model):
    name = models.CharField('name', max_length=90)
    text = models.TextField('taxt')
    numb = models.CharField('numb', max_length=90)
    numb2 = models.CharField('numb2', max_length=90, null=True)
    numb3 = models.CharField('numb3', max_length=90, null=True)
    numb4 = models.CharField('numb4', max_length=90, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutQu'
        verbose_name_plural = 'AboutQus'


class  AboutSl(models.Model):
    name = models.CharField('name1', max_length=80)
    name2 = models.CharField('name2', max_length=90)
    text = models.TextField('text')
    img = models.ImageField('img1', upload_to='media')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutSl'
        verbose_name_plural = 'AboutSls'


class  AboutSl2(models.Model):
    img = models.ImageField('img1', upload_to='media')
    def __img__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutSl1'
        verbose_name_plural = 'AboutSls2'



class AboutTr(models.Model):
    name = models.CharField('name trainer', max_length=90)
    img = models.ImageField('img trainer', upload_to='media')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutTr'
        verbose_name_plural = 'AboutTrs'


class Aboutlogo(models.Model):
    img = models.ImageField('logo', upload_to='media')

    def __img__(self):
        return self.img

    class Meta:
        verbose_name = 'Aboutlogo'
        verbose_name_plural = 'Aboutlogos'



class  ScOur(models.Model):
    name = models.CharField('class', max_length=40)
    text = models.TextField('text')
    img = models.ImageField('img class', upload_to='media')

    def __img__(self):
        return self.img

    class Meta:
        verbose_name = 'ScOur'
        verbose_name_plural = 'ScOurs'




class Logo(models.Model):
    img = models.ImageField('logo', upload_to='media')

    def __img__(self):
        return self.img

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'




class Logo2(models.Model):
    img = models.ImageField('logo', upload_to='media')


    def __img__(self):
        return self.img

    class Meta:
        verbose_name = 'Logo2'
        verbose_name_plural = 'Logos2'


class Logo3(models.Model):
    img = models.ImageField('Logo', upload_to='media')

    def __img__(self):
        return self.img

    class Meta:
        verbose_name = 'Logo3'
        verbose_name_plural = 'Logos3'




class Logo4(models.Model):
    img = models.ImageField('logo', upload_to='media')
    name = models.CharField('name logo1', max_length=90, null=True)
    name2 = models.CharField('name logo2', max_length=90, null=True)
    name3 = models.CharField('name logo3', max_length=90, null=True)

    def __img__(self):
        return self.img

    class Meta:
        verbose_name = 'Logo4'
        verbose_name_plural = 'Logos4'

class Blog1(models.Model):
    name1 = models.CharField('blog name1', max_length=40)
    name2 = models.CharField('blog name2', max_length=40)
    img = models.ImageField('blog img', upload_to='media')


    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Blog1'
        verbose_name_plural = 'Blog1s'

class Blog2(models.Model):
    name1 = models.CharField('blog2 name1', max_length=40)
    name2 = models.CharField('blog2 name2', max_length=40)
    img = models.ImageField('blog2 img', upload_to='media')


    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Blog2'
        verbose_name_plural = 'Blog2s'


class BlogVideo(models.Model):
    name = models.CharField('video name', max_length=30)
    name2 = models.CharField('video name2', max_length=80, null=True)
    img = models.ImageField('videp img', upload_to='media', null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BlogVideo'
        verbose_name_plural = 'BlogVideos'



class BlogDet(models.Model):
    text = models.TextField('text 1' )
    text2 = models.TextField('text 2' )
    img = models.ImageField ('img 1', upload_to='media')
    img2 = models.ImageField('img 2', upload_to='media')
    img3 =  models.ImageField('img 3', upload_to='media')
    img4 = models.ImageField('img 4', upload_to='media')



    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'BlogDet'
        verbose_name_plural = 'BlogDets'

class BlogDeth(models.Model):
    name = models.CharField('name1', max_length=40)
    name2 = models.CharField('name2', max_length=30)
    img = models.ImageField('img ', upload_to='media')
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BlogDeth'
        verbose_name_plural = 'BlogDeths'


class BlogDet2(models.Model):
    name = models.CharField('Blog name', max_length=50)
    text = models.TextField('text1')
    text2 = models.TextField('text2')
    text3 = models.TextField('text3')
    stname = models.CharField('str name1', max_length=120, null = True)
    strnam2 = models.CharField('str author name', max_length=120, null = True)
    strnam3 = models.CharField('str  name3', max_length=120, null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BlogDet2'
        verbose_name_plural = 'BlogDet2s'

class BlogDet3(models.Model):
    name = models.CharField('name1', max_length=190, null=True)
    name2 = models.CharField('name2', max_length=190, null=True)
    img = models.ImageField('img', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BlogDet3'
        verbose_name_plural = 'BlogDet3s'


class BlogDetN(models.Model):
    name = models.CharField('name1', max_length=80)
    name2 = models.CharField('name2', max_length=80)
    img = models.ImageField('img', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BlogDetN'
        verbose_name_plural = 'BlogDetNs'



class GalCat(models.Model):
    name = models.CharField('name categgory', max_length=90)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'GalCat'
        verbose_name_plural = 'GalCats'




class Gallery(models.Model):
    galcat = models.ForeignKey(GalCat, on_delete=models.CASCADE, related_name='gal')
    name = models.CharField('name', max_length=90, null=True)
    name2 = models.CharField('name2 ', max_length=90, null=True)
    img = models.ImageField('img', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallerys'