from django.test import TestCase
from .models import Plan

# Create your tests here.

class PlanTestCase(TestCase):
    def setUp(self):
        Plan.objects.create(
            nombre= "Plan S",
            precio= 15990
        )

        Plan.objects.create(
            nombre= "Plan M",
            precio= 22990
        )

        Plan.objects.create(
            nombre= "Plan L",
            precio= 29990
        )

        Plan.objects.create(
            nombre= "Plan XL",
            precio= 35990
        )

    
    def test_plan_price(self):
        plan = Plan.objects.get(nombre="Plan S")
        self.assertEqual(plan.precio, 15990)

    def test_assert_equal_generar_descuento(self):
        plan = Plan.objects.get(nombre="Plan M")
        self.assertEqual(plan.generarDescuento(), 0.1)

    def test_assert_equal_precio_final(self):
        plan = Plan.objects.get(nombre="Plan L")
        self.assertEqual(plan.calcularPrecioFinal(), 23992)

        plan = Plan.objects.get(nombre="Plan XL")
        self.assertEqual(plan.calcularPrecioFinal(), 21594)

