from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Project


def project_list_view(request):
    """
    this is the view that shows the list of projects
    """
    context = {
        'projects': get_list_or_404(Project)
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
