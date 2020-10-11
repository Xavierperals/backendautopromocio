from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from autoproject.forms import FormContactForm


@csrf_exempt
def create_form_contact(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Wrong method.'})

    request_form = FormContactForm(request.POST)

    if request_form.is_valid():
        request_form.save()
        return JsonResponse({
            'success': True,
        })
    else:
        return JsonResponse({
            'success': False,
            'errors': request_form.errors,
        })
