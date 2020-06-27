from django.views.generic import ListView, DetailView

from .models import Quote


# Create your views here.
class QuoteDetailView(DetailView):
    model = Quote
    template = 'quote_detail.html'

class QuoteListView(ListView):
    model = Quote
    template = 'quote_list.html'

    paginate_by = 10
