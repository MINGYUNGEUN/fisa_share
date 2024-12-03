from . import views
from django.urls import path, include # type: ignore

urlpatterns = [
    path('', views.main,name='main'), # 없는 경로를 호출하고 있음
    path('report_ex', views.report_ex,name='report_ex'),
    path('main/', views.main, name='main'),
    path('loginmain', views.summary_view,name='loginmain'),
    path('info/', views.info,name='info'),
    path('mypage', views.mypage,name='mypage'),
    path('top5', views.top5,name='top5'),
    path('log_click_event', views.log_click_event, name='log_click_event'),
    path('spending_mbti', views.spending_mbti, name='spending_mbti'),
    path('originreport/', views.originreport_page, name='originreport'),
    path('logout/', views.logout_view, name='logout'),
    path('update/', views.update_profile, name='update_profile'),
    path('log_click/', views.log_to_elasticsearch, name='log_to_elasticsearch'),
    path('better', views.better_option, name='better'),
]