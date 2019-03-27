from django.conf.urls import url
                       
from .views import *                   
                    
urlpatterns = [

    url(r'^register-land/$'          ,register_new_land       ,name="register_new_land"),
    url(r'^user-land-details/$'          ,user_land_details       ,name="user_land_details"),
#    url(r'^register-land/$'          ,MovieListAPIView.as_view()       ,name="movie_list"),
#    url(r'^add-movie/$'                     ,add_movie       ,name="add_movie"),
#    url(r'^home/$'                     ,home       ,name="home"),
#    url(r'^detail/(?P<pk>\d+)/$'            ,movie_detail             ,name="movie_detail"),

    
]
