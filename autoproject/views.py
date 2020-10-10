from django.http import HttpRequest, JsonResponse


def create_form_contact(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Wrong method.'})

    print(request.body)

    return JsonResponse({
        'success': True,
    })
