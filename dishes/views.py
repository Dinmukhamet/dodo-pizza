@require_http_methods(["POST"])
@csrf_exempt
def create_pizza(request: HttpRequest):
    data = loads(request.body.decode("UTF-8"))
    title = data.get("title")
    instance = Dish.objects.create(title=title)
    response = serializers.serialize("json", [instance])
    return JsonResponse(data=loads(response), safe=False)

