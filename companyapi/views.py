from django.http import HttpResponse,JsonResponse
def home_page(request):
  print("Home page requested")
  friends=['Alan','Aayushma','Aakriti']
  return JsonResponse(friends,safe=False)