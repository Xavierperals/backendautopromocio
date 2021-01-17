from typing import List

from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from autopromotion.forms import ProjectContactForm, ContactForm
from autopromotion.models import Project, ProjectContact


def all_projects(request: HttpRequest) -> JsonResponse:
    projects = Project.objects.filter(status='active')
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

        project_contact: ProjectContact = form.save(commit=False)
        project_contact.project = db_project
        project_contact.save()

        return JsonResponse({
            'success': True,
        })
    else:
        return JsonResponse({
            'success': False,
            'errors': form.errors,
        })


@csrf_exempt
def contact(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Wrong method.'})

    form = ContactForm(request.POST)

    if form.is_valid():
        form.save()
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
    response['grid_image'] = p.grid_image.url
    response['pictures'] = [
        image.file.url for image in p.images()
    ]
    return response
