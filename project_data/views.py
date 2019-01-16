from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings

from .models import Project


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def project_list_view(request):
    """
    this is the view that shows the list of projects
    """
    if not request.GET.get('page'):
        page = 1

    else:
        page = request.GET.get('page')

    projects_all = get_list_or_404(Project)
    paginator = Paginator(projects_all, 20)

    projects = paginator.get_page(page)

    context = {
        'projects': projects
    }

    return render(request, 'list_view.html', context)


def project_detail_view(request, pk=None):
    """
    this shows a detail for one specific project
    format: /<int:id>
    """
    context = {
        'project': get_object_or_404(Project, id=pk)
    }

    return render(request, 'detail_view.html', context)
