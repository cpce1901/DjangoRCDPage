from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import math


class CapacitorApiView(APIView):
    def calcular_condensador(
        self,
        factor_potencia_actual,
        factor_potencia_deseado,
        potencia_activa,
    ):
        potencia_activa = potencia_activa * 1000
        factor_potencia_objetivo = factor_potencia_deseado

        angulo_desfase_actual = math.degrees(math.acos(factor_potencia_actual))
        angulo_desfase_objetivo = math.degrees(math.acos(factor_potencia_objetivo))

        # Carga en VAR necesaria
        carga_capacitiva = potencia_activa * (
            math.tan(math.radians(angulo_desfase_actual))
            - math.tan(math.radians(angulo_desfase_objetivo))
        )

        return carga_capacitiva

    def capacitancia(self, carga_capacitancia):
        tension = 440
        omega = 2 * math.pi * 60

        # Cálculo de la capacitancia en microfaradios
        capacitancia_delta = carga_capacitancia / (tension**2 * omega)

        return capacitancia_delta * 1e6

    def get(self, request, kw, fp, fp_need, *args, **kwargs):
        factor_potencia_actual = fp
        factor_potencia_deseado = fp_need
        potencia_activa = kw

        carga = self.calcular_condensador(
            factor_potencia_actual,
            factor_potencia_deseado,
            potencia_activa,
        )

        delta = self.capacitancia(carga)

        data = {
            "KVAR": carga / 1000,
            "uF": delta,
            "mensaje": "Acción realizada con éxito",
        }
        return Response(data, status=status.HTTP_200_OK)
