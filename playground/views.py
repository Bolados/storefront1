from django.shortcuts import render
from django.db import transaction, connection
from django.http import HttpResponse
from store.models import Order, OrderItem, Product


@transaction.atomic()
def say_hello(request):
    queryset = Product.objects.raw('SELECT * FROM store_product')

    return render(request, 'hello.html', {'name': 'Bola', 'result': list(queryset)})

    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()
# collection = Collection.objects.get(pk=11)
    # collection.title = "Games"
    # collection.featured_product = None
    # collection.save()

    # cartitem = CartItem()
    # cartitem.product = Product(pk=1)
    # cartitem = CartItem.objects.filter(pk=1).update(quantity=3)
    # cartitem = CartItem.objects.filter(pk=1).delete()

    # collection = Collection.objects.filter(pk=11).update(featured_product=11)
    # cart = CartItem.objects.create(featured_product=1)
    # or
    #myCOllection = Collection.objects.create(title='Video games', featured_product_id=1)

    #TaggedItem.objects.get_tags_for(Product, 1)

    # discounted_price = ExpressionWrapper(
    #     F('unit_price') * 0.8, output_field=DecimalField())

    # queryset = Customer.objects.annotate(

    #     discounted_price=discounted_price
    # )

    # queryset = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(
    #         ' '), F('last_name', function='CONCAT'))
    # )

    # result = Product.objects.aggregate(counts=Count(
    #    'id'), min_price=Min('unit_price'))
    # orders
    # sold_unit = OrderItem.objects.aggregate(
    #     ord_cont=Sum('quantity')).filter(product__id=1)
    # custom_oreder = Order.objects.filter(
    #     customer__id=1).aggregate(count=Count('id'))
    # ord_number = Order.objects.aggregate(Count(id))
    # collect = Product.objects.filter(
    #     collection__id=3).aggregate(mprice=Max('unit_price'))
    # queryset = Order.objects.select_related(
    #    'custumer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # queryset = Product.objects.prefetch_related(
    #    'promotions').select_related('collection').all()
    #queryset = Product .objects.defer('description')
    # queryset = Product.objects.filter(
    #    id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')

    #queryset = Product.objects.all()[:5]
    #queryset = Product.objects.order_by('unit_price', '-title').reverse()[0]
    # queryset = Product.objects.filter(
    # inventory = F('unit_price'))
    # queryset = Customer.objects.filter(email__icontains='.com')
    # queryset = Collection.objects.filter(featured_product__count=0)

# def ssh_server(ip, username, password, command):
#     s = pxssh.pxssh()
#     if not s.login(ip, username, password):
#         print("SSH session failed on login.")
#         # print str(s)
#     else:
#         print("SSH session login successful")
#         s.sendline(command)
#         s.prompt()  # match the prompt
#         # print(s.before)  # print everything before the prompt.
#         return s.before

#     s.logout()


# def ssh_response(request):
#     output = str(ssh_server("172.17.0.2", "root", "bola", "ls"))
#     output = output.rstrip("\n")
#     return HttpResponse(output)


# def say_hello(request):
#     # return HttpResponse('Hello World')
#     x = calculate()
#     return render(request, "hello.html", {"name": "Bola"})


# Create your views here.
