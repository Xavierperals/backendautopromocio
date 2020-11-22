from typing import List

from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from autopromotion.forms import ProjectContactForm
from autopromotion.models import Project, ProjectContact


def all_projects(request: HttpRequest) -> JsonResponse:
    projects = Project.objects.all()
    return mount_response(projects)


def project(request: HttpRequest, pid: int) -> JsonResponse:
    try:
        db_project = Project.objects.get(pk=pid)
        return JsonResponse(mount_single_project_response(db_project))
    except ObjectDoesNotExist:
        return JsonResponse({
            'error': 'Project not found.'
        }, status=404)


def home_page_projects(request: HttpRequest) -> JsonResponse:
    projects = Project.objects.filter(home_page=True).all()
    return mount_response(projects)


@csrf_exempt
def project_contact(request: HttpRequest, pid: int) -> JsonResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Wrong method.'})

    form = ProjectContactForm(request.POST)

    if form.is_valid():
        db_project = Project.objects.get(pk=pid)

        contact: ProjectContact = form.save(commit=False)
        contact.project = db_project
        contact.save()

        return JsonResponse({
            'success': True,
        })
    else:
        return JsonResponse({
            'success': False,
            'errors': form.errors,
        })


# Helper
def mount_response(projects: List[Project]) -> JsonResponse:
    return JsonResponse({
        'projects': [
            mount_single_project_response(p) for p in projects
        ],
    })


def mount_single_project_response(p: Project) -> dict:
    response = model_to_dict(p)
    response['amenties'] = p.splitted_amenties()
    response['pictures'] = [
        image.file.url for image in p.images()
    ]
    return response
