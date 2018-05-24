from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^healthcheck/?$', views.healthCheck),
	url(r'^v2/catalog/?$', views.renderCatalog),
	url(r'^v2/service_instances/(?P<instance_id>[a-zA-Z0-9-_]+)/?$', views.createDeleteServiceInstance),
	url(r'^v2/service_instances/(?P<instance_id>[a-zA-Z0-9-_]+)/service_bindings/(?P<service_bind_id>[a-zA-Z0-9-_]+)/?$', views.createDeleteServiceBinding),
]