from django.conf.urls import url
from views import home, app

urlpatterns = [
    # Main index page -- where the user first lands
    #url(r'^$', home.index, name='index'),
    
    url(r'^$', app.submit_app, name='submit-app'),
    # App specific routes
    url(r'^submit-app$', app.submit_app, name='submit-app'),
    url(r'^success$', app.success, name='success'),
    #url(r'^app/(?P<app_id>[0-9]+)$', app.app_details, name='app-details'),

]
