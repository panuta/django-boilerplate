from django.conf.urls.defaults import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('django_boilerplate.sample_app.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)

# Reference
# http://docs.python.org/library/re.html
# https://docs.djangoproject.com/en/1.3/topics/http/urls/
# https://docs.djangoproject.com/en/1.3/ref/class-based-views/