from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Contacto, Plan
# Serializers define the API representation.
class ContactoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id', 'titulo', 'nombre', 'email', 'numeroTelefono','mensaje', 'estado']

# ViewSets define the view behavior.
class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ['id','nombre','minutos','internet','precio']

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'Contacto', ContactoViewSet)
router.register(r'Plan', PlanViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
