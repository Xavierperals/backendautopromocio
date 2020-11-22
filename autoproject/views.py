from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_user_agents.utils import get_user_agent
from user_agents.parsers import UserAgent, OperatingSystem, Browser, Device

from autoproject.forms import FormContactForm
from autoproject.models import FormContact


@csrf_exempt
def create_form_contact(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Wrong method.'})

    request_form = FormContactForm(request.POST)

    if request_form.is_valid():
        user_agent: UserAgent = get_user_agent(request)
        os: OperatingSystem = user_agent.os
        browser: Browser = user_agent.browser
        device: Device = user_agent.device

        form_contact: FormContact = request_form.save(commit=False)
        form_contact.os = os.family
        form_contact.os_version = os.version_string
        form_contact.browser = browser.family
        form_contact.browser_version = browser.version_string
        form_contact.device_brand = device.brand
        form_contact.device_family = device.family
        form_contact.device_model = device.model
        form_contact.raw_user_agent = user_agent.ua_string
        form_contact.ip = request.META.get('REMOTE_ADDR')

        form_contact.save()

        return JsonResponse({
            'success': True,
        })
    else:
        return JsonResponse({
            'success': False,
            'errors': request_form.errors,
        })
