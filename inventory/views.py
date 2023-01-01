from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import AddForm, SaleForm, Add_Product
from .models import Product,Sale
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Home_Page(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/index.html'
    
class Search_Product(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/index.html'
    
    def get_queryset(self):
        search_item = self.request.GET.get('q')   
        search_object = Product.objects.filter(Q(item_name__icontains=search_item)| Q(unit_price__icontains=search_item) )
        return search_object


'''
def home(request):
    products = Product.objects.all().order_by('-id')
    product_filters = ProductFilter(request.GET, queryset = products)
    products = product_filters.qs

    return render(request, 'products/index.html', {
        'products': products, 'product_filters': product_filters,
    })

'''

class Add_Product(LoginRequiredMixin, CreateView):
    form_class = Add_Product
    template_name = 'products/new_product.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

        

class Reciept_Views(ListView):
    model = Sale
    context_object_name = 'sales'
    template_name = 'products/receipt.html'


'''
@login_required
def receipt(request): 
    sales = Sale.objects.all().order_by('-id')
    return render(request, 
    'products/receipt.html', 
    {'sales': sales,
    })

'''

class Total_Sales(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'products/all_sales.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales'] = Sale.objects.all()
        context['total'] = sum([items.amount_received for items in context['sales']])
        context['net'] = sum([(items.unit_price * items.quantity) for items in context['sales']])
        context['change'] =  context['total'] - context['net']
        return context
'''
def all_sales(request):
    sales = Sale.objects.all()
    total  = sum([items.amount_received for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change
    return render(request, 'products/all_sales.html',
     {
     'sales': sales, 
     'total': total,
     'change': change, 
     'net': net,
      })
'''

class Product_Detail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

'''
@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'products/product_detail.html', {'product': product})

'''

class Reciept_Detail(LoginRequiredMixin, DetailView):
    model = Sale
    template_name = 'products/receipt_detail.html'
    context_object_name = 'receipt'

'''
@login_required
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request, 'products/receipt_detail.html', {'receipt': receipt})
'''

    

@login_required
def issue_item(request, pk):
    issued_item = Product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)  

    if request.method == 'POST':     
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price   
            new_sale.save()
            #To keep track of the stock remaining after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)

            return redirect('receipt') 

    return render (request, 'products/issue_item.html',
     {
    'sales_form': sales_form,
    })
    

@login_required
def add_to_stock(request, pk):
    issued_item = Product.objects.get(id = pk)
    form = AddForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()

            #To add to the remaining stock quantity is reducing
            print(added_quantity)
            print (issued_item.total_quantity)
            return redirect('home')

    return render (request, 'products/add_to_stock.html', {'form': form})