"""定义pizzas的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
	#主页
	url(r'^$',views.index,name='index'),
	
	#显示披萨种类页面
	url(r'^pizzas/$',views.pizzas,name='pizzas'),
	
	#披萨介绍页面
	url(r'^pizzas/(?P<pizza_id>\d+)/$',views.pizza,name='pizza')
	]
