
## Authentication versus authorization

### Authentication
  This is like coming to the office on the first day, submitting all your papers and documents, and then receiving your employee card. After that, only your employee card will be sufficient to get inside. Authentication works just like that!

  If the credentials are not valid, the client will receive a `401` - `Unauthorized HTTP status code`.


### Authorization
   However, even with your employee card, you will not be able to access all the rooms or spaces in the office. There are some pla ces that are only accessible to a certain group of people who have been given that privilege. 

  On the server side, this is typically done by assigning the user to a group or a set of groups. Then, after verifying the token, the code checks if the user belongs to the appropriate group to perform that task. If not, the client will receive a `403 - Forbidden HTTP status code`.

  **Authentication lets you in, authorization lets you act**


## Mocking APIs
 - Mocking APIs play an essential role in API development because client application developers don't need to wait for the actual API to become live. It minimizes the time of development and reduces the dependencies between API developers and client application developers. 

 - mockaroo[https://www.mockaroo.com/]
 - mockapi[https://mockapi.io/]


## The Django REST framework  (DRF)
  
 ### what's the DRF ?
  - Django REST framework is a powerful and flexible toolkit for building Web APIs.

 ### What is the difference between Django and Django Rest Framework?

   *You can use Django alone to make REST APIs, but you have to write more code and do more design*
   so 
   1.  Django Rest Framework helped you create API endpoints faster like one of the comments with the sample codes.
     (By using Django Rest Framework, you can write less code and reuse your code better.)
   
   for example regular Django:

   ``` 
    from django.core.serializers import serialize
    from django.http import HttpResponse
    class SerializedListView(View):
    
     def get(self, request, *args, **kwargs):
        qs = MyObj.objects.all()
        json_data = serialize("json", qs, fields=('my_field', 'my_other_field'))
        return HttpResponse(json_data, content_type='application/json')
  ```
  And with DRF: 

  ``` 
    from rest_framework import generics
    
    class MyObjListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MyObjSerializer
  ```

  2. Django REST framework focuses on building APIs, which gives it a lot of additional advantages over traditional Django.


## ViewSets in DRF 

 - `ViewSets` are simple class-based views, but they come with benefits. There are a few ViewSets classes available in DRF that you can use to quickly scaffold a functioning API CRUD project. You can also provide permission classes and throttle classes to allow authenticated API calls and rate limiting.

 1. `ViewSet` :
    - When you extend a ViewSet, you will have to manually write code to perform the database operations.
 
  2. `ModelViewSet `: 
    - it can automatically handle CRUD operations for you.
    - All you must do is give this class a queryset and a serializer,and everything else will be done automatically. 
    - You don’t need to write code for all those database operations anymore.

  3. `ReadOnlyModelViewSet`: 
    - when your class-based views extend a ReadOnlyModelViewSet, it can only display a single resource and resource collection.
    - No write-operation is allowed by such views, so it doesn’t handle POST, PUT, PATCH or DELETE methods.


## Function-based and class-based
  
  **Function-based:**
   1. easy to implement
   2. offer better readability
   3. it's easier to use decorators with them.
   4. quickly write a one-off solution

  **class-based:**
   1. don't need to write as much code.
   2. less code duplication, 
   3. can extend the clusters and add features that anytime.
   4. can write specific methods for each type of HTTP request.


## serializers
 - serializers helped to convert model instances into Python datatypes that can be displayed as JSON or XML.
 -  It also helps you to convert HTTP request body into Python datatypes and made them to a model instance.