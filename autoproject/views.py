from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django_user_agents.utils import get_user_agent
from user_agents.parsers import UserAgent, OperatingSystem, Browser, Device

from autoproject.forms import FormContactForm


@csrf_exempt
def create_form_contact(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Wrong method.'})

    request_form = FormContactForm(request.POST)

    if request_form.is_valid():
        request_form.save()

        user_agent: UserAgent = get_user_agent(request)

        print(user_agent.os)
        print(user_agent.browser)
        print(user_agent.device)

        return JsonResponse({
            'success': True,
            'agent': {
                'os': user_agent.os,
                'browser': user_agent.browser,
                'device': user_agent.device,
            }
        })
    else:
        return JsonResponse({
            'success': False,
            'errors': request_form.errors,
        })
