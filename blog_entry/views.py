from django.shortcuts import render_to_response
from blog_entry.models import Entry 
from django.views.decorators.cache import cache_page
from django.core.cache import cache


#For RESTful API
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from blog_entry.models import Entry
from blog_entry.post_serializers import ModelSerializer

# Create your views here.

#@cache_page(60 * 15)
def index(request):
	cache.set("Milan" , "This is a dummy string showing the Redis cache")
	redis_cache_data = cache.get("Milan")
	if redis_cache_data is None :
		redis_cache_data = "Could Not retrieve from the Redis Cache"
	all_posts = Entry.objects.all()[:5]
	template_data = {'posts' : all_posts , 'redis_cache' : redis_cache_data}
 
	return render_to_response('index.html', template_data)




class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def posts_list(request):
    """
    List all Posts, or create a new snippet.
    """
    if request.method == 'GET':
        posts = Entry.objects.all()
        serializer = ModelSerializer(posts, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def post_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    cache_entry= cache.get(pk) ; 
    if cache_entry is not None :
    	return cache_entry 
    try:
        snippet = Entry.objects.get(pk=pk)
    except Entry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ModelSerializer(snippet)
        cache.set(pk , JSONResponse(serializer.data)) 
        return cache.get(pk)
