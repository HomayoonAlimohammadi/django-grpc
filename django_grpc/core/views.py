import json
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


User = get_user_model()


@require_http_methods(["GET"])
def user_list_view(request):
    users = {user.pk: model_to_dict(user) for user in User.objects.all()}
    return JsonResponse(users)


@require_http_methods(["POST"])
def user_create_view(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    content = body["content"]
    user = User.objects.create(
        username=content.get("username"), password=content.get("password")
    )
    return JsonResponse(model_to_dict(user))
