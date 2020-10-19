from typing import List

from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, JsonResponse
from autopromotion.models import Project


def all_projects(request: HttpRequest) -> JsonResponse:
    projects = Project.objects.all()
    print(projects)
    return mount_response(projects)


def project(request: HttpRequest, pid: int) -> JsonResponse:
    try:
        return JsonResponse(model_to_dict(Project.objects.get(pk=pid)))
    except ObjectDoesNotExist:
        return JsonResponse({
            'error': 'Project not found.'
        }, status=404)


def home_page_projects(request: HttpRequest) -> JsonResponse:
    projects = Project.objects.filter(home_page=True).all()
    return mount_response(projects)


# Helper
def mount_response(projects: List[Project]) -> JsonResponse:
    return JsonResponse({
        'projects': [
            model_to_dict(project) for project in projects
        ],
    })
