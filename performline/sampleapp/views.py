from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

from sampleapp.models import List, Link
from sampleapp.forms import ListForm

def index(request):
  all_lists = List.objects.order_by('-date_created')
  template = loader.get_template('list.html')
  context = Context({'all_lists': all_lists,
    })
  return HttpResponse(template.render(context))

def listdetail(request, list_id):
  a_list = get_object_or_404(List, pk=list_id)
  return render(request, 'listdetail.html', {'list': a_list})

@login_required
def edit(request, list_id=None, template_name='list_update_form.html'):
  if list_id:
    a_list = get_object_or_404(List, pk=list_id)
  else:
    a_list = List(name='random list')

  if request.POST:
    form = ListForm(request.POST, instance=a_list)
    if form.is_valid():
      form.save()

      return HttpResponseRedirect('/sampleapp')
  else:
    form = ListForm(instance=a_list)

  return render_to_response(template_name, {'form': form}, context_instance=RequestContext(request))

class ListWizard(SessionWizardView):
  def done(self, form_list, **kwargs):
    l = List(name=form_list[0].cleaned_data['name'], date_created=timezone.now(), date_modified=timezone.now())
    l.save()
    return HttpResponseRedirect('/sampleapp/')
