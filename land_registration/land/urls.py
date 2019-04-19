from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^home/$',home, name="home"),
    url(r'^register-land/$',register_new_land       ,name="register_new_land"),
    url(r'^load-data/$',load_data       ,name="load_data"),
    url(r'^dashboard$',dashboard_home       ,name="dashboard_home"),
    url(r'^user-land-details/$',user_land_details       ,name="user_land_details"),
    url(r'^lands-available/$',lands_available       ,name="lands_available"),
    url(r'^add-land-available-to-sell/(?P<pk>\d+)/$',add_land_available_to_sell       ,name="add_land_available_to_sell"),
    url(r'^bid/home/$',lands_available_db       ,name="lands_available_db"),
    url(r'^bid/save/$',save_bid       ,name="save_bid"),
    url(r'^bid/(?P<pk>\d+)/$',bidding       ,name="bidding"),
#    url(r'^bid/home/$',bidding_home_page       ,name="bidding_home"),
#    url(r'^register-land/$'          ,MovieListAPIView.as_view()       ,name="movie_list"),
#    url(r'^add-movie/$'                     ,add_movie       ,name="add_movie"),
#    url(r'^home/$'                     ,home       ,name="home"),
#    url(r'^detail/(?P<pk>\d+)/$'            ,movie_detail             ,name="movie_detail"),


]
