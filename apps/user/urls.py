from django.conf.urls import url
from apps.user import views
from apps.user.views import RegisterView, ActiveView, LoginView, UserInfoView, UserOrderView, AddressView, LogoutView
from django.contrib.auth.decorators import login_required

# urlpatterns = [
#     url(r'^register$', views.register, name='register'),  # 注册
# ]

# 通过视图类导入
urlpatterns = [
    url(r'^register$', RegisterView.as_view(), name='register'),  # 注册
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 用户激活

    url(r'^login$', LoginView.as_view(), name='login'),  # 登录
    url(r'^logout$', LogoutView.as_view(), name='logout'),  # 注销登录

    # url(r'^$', login_required(UserInfoView.as_view()), name='user'),  # 用户中心信息页
    # url(r'^order$', login_required(UserOrderView.as_view()), name='order'),  # 用户中心订单页
    # url(r'^address$', login_required(AddressView.as_view()), name='address'),  # 用户中心地址页

    url(r'^$', UserInfoView.as_view(), name='user'),  # 用户中心信息页
    url(r'^order/(?P<page>\d+)$', UserOrderView.as_view(), name='order'),  # 用户中心订单页
    url(r'^address$', AddressView.as_view(), name='address'),  # 用户中心地址页
]
