from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'MyDjangoProject.views.home', name='home'),
                       # url(r'^MyDjangoProject/', include('MyDjangoProject.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'contact_web_app.views.contacts_home'),
                       url(r'^add_user$', 'contact_web_app.views.add_user'),
                       url(r'^login$', 'contact_web_app.views.login'),
                       url(r'^add_contact_form$', 'contact_web_app.views.add_contact_form'),
                       url(r'^modify_contact_form$', 'contact_web_app.views.modify_contact_form'),
                       url(r'^delete_contact_form$', 'contact_web_app.views.delete_contact_form'),
                       url(r'^get_contact_form$', 'contact_web_app.views.get_contact_form'),
                       url(r'^get_provider_form$', 'contact_web_app.views.get_provider_form'),
                       url(r'^get_contacts_by_provider_form$', 'contact_web_app.views.get_contacts_by_provider_form'),
                       url(r'^get_contacts_by_field_form$', 'contact_web_app.views.get_contacts_by_field_form'),
                       url(r'^add_contact$', 'contact_web_app.views.add_contact'),
                       url(r'^modify_contact$', 'contact_web_app.views.modify_contact'),
                       url(r'^delete_contact$', 'contact_web_app.views.delete_contact'),
                       url(r'^get_contact$', 'contact_web_app.views.get_contact'),
                       url(r'^get_provider', 'contact_web_app.views.get_provider'),
                       url(r'^get_contacts_by_provider$', 'contact_web_app.views.get_contacts_by_provider'),
                       url(r'^get_contacts_by_field$', 'contact_web_app.views.get_contacts_by_field'),
                       url(r'^logout$', 'contact_web_app.views.logout')
                       )
