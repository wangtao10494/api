from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Pizza,Topping
from .forms import PizzaForm,ToppingForm
# Create your views here.
def index(request):
	"""披萨店主页"""
	return render(request,'pizzas/index.html')
	
def pizzas(request):
	"""显示披萨种类"""
	pizzas = Pizza.objects.order_by('date_added')
	context = {'pizzas':pizzas}
	return render(request,'pizzas/pizzas.html',context)
	
	
def pizza(request,pizza_id):
	"""显示每个披萨和对应介绍"""
	pizza = Pizza.objects.get(id = pizza_id)
	toppings = pizza.topping_set.order_by('-date_added')
	context = {'pizza':pizza,'toppings':toppings}
	return render(request,'pizzas/pizza.html',context)


def new_pizza(request):
	"""添加新的披萨种类"""
	if request.method != 'POST':
		#未提交数据：创建一个新表单
		form = PizzaForm()
	else:
		#post提交的数据，对数据进行处理
		form = PizzaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('pizzas:pizzas'))
			
	context = {'form':form}
	return render(request,'pizzas/new_pizza.html',context)
	
	
def new_topping(request,pizza_id):
	"""在披萨中添加介绍"""
	pizza = Pizza.objects.get(id=pizza_id)
	
	if request.method != 'POST':
		form = ToppingForm()
	else:
		form = ToppingForm(data=request.POST)
		if form.is_valid():
			new_topping = form.save(commit=False)
			new_topping.pizza = pizza
			new_topping.save()
			return HttpResponseRedirect(reverse('pizzas:pizza',
											args=[pizza_id]))
											
	context = {'pizza':pizza,'form':form}
	return render(request,'pizzas/new_topping.html',context)
	

def edit_topping(request,topping_id):
	"""编辑介绍"""
	topping = Topping.objects.get(id = topping_id)
	pizza = topping.pizza
	
	if request.method != 'POST':
		form = ToppingForm(instance=topping)
	else:
		form = ToppingForm(instance=topping,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('pizzas:pizza',
												args=[pizza.id]))
	
	context = {'topping':topping,'pizza':pizza,'form':form}
	return render(request,'pizzas/edit_topping.html',context)
	
	
	
	
	
