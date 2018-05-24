# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ServiceSerializer
from .models import ServiceRecord
import json
import random, string
import logging

logger = logging.getLogger(__name__)

def randomString():
	return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
@api_view(['GET'])
def healthCheck(request):
	return Response("App is working fine.", status=status.HTTP_200_OK)

@api_view(['GET'])
def renderCatalog(request):
	logger.info("In get catalog method...")
	return_data = {
		'services':[
			{
				'name': 'DBaaService',
				'id': 'f10bcd9f-21d0-4ad9-bd32-f4d5516ewe65ec',
				'description': 'Database as service',
				'bindable': True,
				'plan_updateable': True,
				'plans': [
							{
								'name': 'plan_small',
								'id': 'a9d88190-d97c-43dsds-ac8f-3ff9dfa86e8c',
								'description': 'Database as a service'
					 		}
						]
			}
		]
	}
	return Response(return_data)

@api_view(['PUT', 'DELETE'])
def createDeleteServiceInstance(request, instance_id):
	if request.method == 'PUT':
		data = {
			'service_id': request.data.get('service_id'),
			'plan_id': request.data.get('plan_id'),
			'organization_guid': request.data.get('organization_guid'),
			'space_guid': request.data.get('space_guid')
		}
		serializer = ServiceSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return_data = {'dashboard_uri': 'http://localhost:8000/dbService/instance_id'}
			logger.info("Service instance got created successfully with id = " + instance_id)
			return Response(return_data, status=status.HTTP_201_CREATED)
		else:
			logger.error("Error occurred while creating service.")
			return Response("Error while creating service instance", status=status.HTTP_400_BAD_REQUEST)
	else:
		print("in delete service method")
		logger.info("In delete service. " + instance_id)
		try:
			service = ServiceRecord.objects.all().filter(service_id__exact = instance_id)
			service.delete()
			logger.info("Service instance with id = " + instance_id + " deleted...")
			return Response({'': ''}, status=status.HTTP_200_OK)
		except:
			logger.error("Service instance with id = " + instance_id + " could not be deleted!!!")
			return Response({'description': 'Error occured while deleting service.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def createDeleteServiceBinding(request, instance_id, service_bind_id):
	if request.method == 'PUT':
		logger.error("Service binding created.")
		credentials = {
			'name': 'myproject',
			'user': 'myprojectuser',
			'password': 'password',
			'host': "10.53.219.114",
			'port': 5432,
			'uri': 'jdbc:postgresql://10.11.241.0:36552/ZBLgSawLQ5QEaPFd'
		}
		response = {
			'credentials': credentials
		}
		return Response(response, status=status.HTTP_201_CREATED)
	else:
		print("in delete service binding view")
		logger.info("In delete service binding...")
		response = {
			'': ''
		}
		return Response(response, status=status.HTTP_200_OK)
