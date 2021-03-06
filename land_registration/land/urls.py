from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^home/$',home, name="home"),
    url(r'^register-land/$',register_new_land       ,name="register_new_land"),
    url(r'^load-data/$',load_data       ,name="load_data"),
    url(r'^dashboard$',dashboard_home       ,name="dashboard_home"),
    url(r'^user-land-details/$',user_land_details       ,name="user_land_details"),
    # for getting land details from the user account address
    url(r'^user-lands/$',user_lands       ,name="user_lands"),
    url(r'^first-bid/$',first_bid       ,name="first_bid"),
    url(r'^my-bid/$',my_bid       ,name="my_bid"),

    url(r'^all-bid-iter/$',all_bid_iter       ,name="all_bid_iter"),
    url(r'^increase-iter/(?P<pk>\d+)/$',increase_iter       ,name="increase_iter"),
    url(r'^auto-bid/(?P<pk>\d+)/$',auto_bid       ,name="auto_bid"),

    url(r'^graph/(?P<pk>\d+)/$',graph       ,name="graph"),
    url(r'^lands-available/$',lands_available       ,name="lands_available"),
    url(r'^set-budget/$',set_budget       ,name="set_budget"),
#    url(r'^add-land-available-to-sell/(?P<pk>\d+)/$',add_land_available_to_sell       ,name="add_land_available_to_sell"),
    url(r'^land-details/(?P<pk>\d+)/$',land_details       ,name="land_details"),
    url(r'^bid/home/$',lands_available_db       ,name="lands_available_db"),
    url(r'^bid/save-first-bid/$',save_first_bid       ,name="save_first_bid"),
    url(r'^bid/save/$',save_bid       ,name="save_bid"),
    url(r'^bid/(?P<pk>\d+)/$',bidding       ,name="bidding"),
#    url(r'^bid/home/$',bidding_home_page       ,name="bidding_home"),
#    url(r'^register-land/$'          ,MovieListAPIView.as_view()       ,name="movie_list"),
#    url(r'^add-movie/$'                     ,add_movie       ,name="add_movie"),
#    url(r'^home/$'                     ,home       ,name="home"),
#    url(r'^detail/(?P<pk>\d+)/$'            ,movie_detail             ,name="movie_detail"),


]
