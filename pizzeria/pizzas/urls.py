"""定义pizzas的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
	#主页
	url(r'^$',views.index,name='index'),
	
	#显示披萨种类页面
	url(r'^pizzas/$',views.pizzas,name='pizzas'),
	
	#披萨介绍页面
	url(r'^pizzas/(?P<pizza_id>\d+)/$',views.pizza,name='pizza'),
	
	#添加新的披萨的页面
	url(r'^new_pizza/$',views.new_pizza,name='new_pizza'),
	
	#添加新的介绍的页面
	url(r'^new_topping/(?P<pizza_id>\d+)/$',views.new_topping,
											name='new_topping'),
											
	#添加编辑条目的页面
	url(r'^edit_topping/(?P<topping_id>\d+)/$',views.edit_topping,
											name='edit_topping'),
	]
