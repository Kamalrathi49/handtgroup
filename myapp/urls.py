from django.urls import path
from django.conf.urls import url
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'myapp'

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^about_us/$', views.AboutUs, name='about-us'),
    url(r'^services/$', views.Services, name='services'),
    url(r'^our-team/$', views.OurTeam, name='team'),
    url(r'^contact/$', views.Contact, name='contact'),
    url(r'^projects/$', views.Projects, name='projects'),
    url(r'^project/(?P<our_project_id>\d+)/$', views.ProjectSingle, name='project-single'),
    url(r'^testimonial/$', views.Testimonal, name='testimonial'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)