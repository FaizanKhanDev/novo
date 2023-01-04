from django.shortcuts import render
from .models import (
    Navlogo,
    NavLogoImage,
    Navitem,
    Navsubitem,
    LeftMenu,
    Latesttitle,
    LastestPicture,
    LeftContact,
    HomeBackground,
    Creativestitle,
    Creative,
    MainServicesTitle,
    OurCompleteService,
    AboutSection,
    MySkills,
    WhyChooseU,


)

def homePage(request):
    navlogo = Navlogo.objects.all()
    navlogoimg = NavLogoImage.objects.all()
    navitems = Navitem.objects.all()
    navsubitems = Navsubitem.objects.all()
    leftmenu = LeftMenu.objects.all()
    latestitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact =LeftContact.objects.all()
    homebackground = HomeBackground.objects.all()
    creativetitle =  Creativestitle.objects.all()
    creative =  Creative.objects.all()

    return render (request,'app/home.html',
        {
            'navlogo':navlogo,
            'navlogoimg':navlogoimg,
            'navitems':navitems,
            'navsubitems':navsubitems,
            'leftmenu':leftmenu,
            'latestitle':latestitle,
            'lastestpicture':lastestpicture,
            'leftcontact':leftcontact,
            'homebackground':homebackground,
            'creativetitle':creativetitle,
            'creative':creative,
        }
    
    )


def blog(request):
    navlogo = Navlogo.objects.all()
    navlogoimg = NavLogoImage.objects.all()
    navitems = Navitem.objects.all()
    navsubitems = Navsubitem.objects.all()
    leftmenu = LeftMenu.objects.all()
    latestitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact =LeftContact.objects.all()
    return render (request,'app/blog.html',
    {   
            'navlogo':navlogo,
            'navlogoimg':navlogoimg,
            'navitems':navitems,
            'navsubitems':navsubitems,
            'leftmenu':leftmenu,
            'latestitle':latestitle,
            'lastestpicture':lastestpicture,
            'leftcontact':leftcontact,
    })



def services(request):
    navlogo = Navlogo.objects.all()
    navlogoimg = NavLogoImage.objects.all()
    navitems = Navitem.objects.all()
    navsubitems = Navsubitem.objects.all()
    leftMenu = LeftMenu.objects.all()
    latesttitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact = LeftContact.objects.all()
    mainservicetitle = MainServicesTitle.objects.all()
    mainservice = OurCompleteService.objects.all()
    
 
    return render(request,'app/services.html',
    {
        "navlogo":navlogo,
        "navlogoimg":navlogoimg,
        "navitems":navitems,
        "navsubitems":navsubitems,
        "leftMenu": leftMenu,
        "latesttitle": latesttitle,
        "lastestpicture":lastestpicture,
        "leftcontact": leftcontact,
        "mainservicetitle":mainservicetitle,
        "mainservice":mainservice,

    })


def aboutus(request):
    navlogo = Navlogo.objects.all()
    navlogoimg = NavLogoImage.objects.all()
    navitems = Navitem.objects.all()
    navsubitems = Navsubitem.objects.all()
    leftmenu = LeftMenu.objects.all()
    latestitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact =LeftContact.objects.all()
    aboutsec_1 = AboutSection.objects.all()
    myskills = MySkills.objects.all()
    whychooseme = WhyChooseU.objects.all()
   

    
    return render(request,'app/aboutus.html',
    {
        'navlogo':navlogo,
        'navlogoimg':navlogoimg,
        'navitems':navitems,
        'navsubitems':navsubitems,
        'leftmenu':leftmenu,
        'latestitle':latestitle,
        'lastestpicture':lastestpicture,
        'leftcontact':leftcontact,
        "aboutsec_1":aboutsec_1,
        "myskills":myskills,
        "whychooseme":whychooseme,
    
    })




