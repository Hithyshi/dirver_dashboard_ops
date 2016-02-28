from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
import json,httplib

# Create your views here.


def home(request):
  connection = httplib.HTTPSConnection('api.parse.com', 443)
  connection.connect()
  connection.request('GET', '/1/classes/Driver', '', {
         "X-Parse-Application-Id": "IBArnAuw83Th0SfDmF55VdMUgsNXFiL2TuC6qwiC",
         "X-Parse-REST-API-Key": "2coKSQ3ZGvWRJW3ZVReOs7ETy4rXiMP2i54eTO4N"
       })
  result = json.loads(connection.getresponse().read())
#  print result

  connection.request('GET', '/1/classes/Route', '', {
         "X-Parse-Application-Id": "IBArnAuw83Th0SfDmF55VdMUgsNXFiL2TuC6qwiC",
         "X-Parse-REST-API-Key": "2coKSQ3ZGvWRJW3ZVReOs7ETy4rXiMP2i54eTO4N"
       })
  result2 = json.loads(connection.getresponse().read())

  drivers_list=[]
  for i in result['results'] :
    drivers_list.append(str(i['driver_name']) + "---" + str(i['phone']))
#  print drivers_list

  route_list=[]
  for j in result2['results'] :
    route_list.append(str(j['displayName'])) 


  return render_to_response("dashboardpage.html",{'drivers':drivers_list, 'routes':route_list}, context_instance=RequestContext(request))


def savetotrip(request):
  the_driver = request.POST["SelectDriver"]
  the_route = request.POST["SelectRoute"]
  trip_details=the_driver + "***" + the_route

  connection = httplib.HTTPSConnection('api.parse.com', 443)
  connection.connect()
  connection.request('POST', '/1/classes/Trip', json.dumps({

         "name": trip_details,
         "routeStr": the_route,
         "driverStr": the_driver[:-13],
         "drivernumber": the_driver[-10:]

       }), {
         "X-Parse-Application-Id": "IBArnAuw83Th0SfDmF55VdMUgsNXFiL2TuC6qwiC",
         "X-Parse-REST-API-Key": "2coKSQ3ZGvWRJW3ZVReOs7ETy4rXiMP2i54eTO4N",
         "Content-Type": "application/json"
       })  
  return HttpResponseRedirect("/")

def savetodriver(request):
  drivername = request.POST["name"]
  drivernumber = request.POST["number"]


  connection = httplib.HTTPSConnection('api.parse.com', 443)
  connection.connect()
  connection.request('POST', '/1/classes/Driver', json.dumps({

         "driver_name": drivername,
         "phone": drivernumber

       }), {
         "X-Parse-Application-Id": "IBArnAuw83Th0SfDmF55VdMUgsNXFiL2TuC6qwiC",
         "X-Parse-REST-API-Key": "2coKSQ3ZGvWRJW3ZVReOs7ETy4rXiMP2i54eTO4N",
         "Content-Type": "application/json"
       })
  return HttpResponseRedirect("/")


