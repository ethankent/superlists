from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item


# FIXME - Display multiple items in the table
# FIXME - Support more than one list!
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})