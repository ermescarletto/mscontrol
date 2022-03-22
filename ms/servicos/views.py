from django.views import View
from .serializers import CadastroChecklistSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .models import *
from django.shortcuts import render, get_object_or_404
import entidades.models as emd
import qrcode
import qrcode.image.svg
from io import BytesIO


class IndexView(View):
    def get(self,request):
        context = {
            'nome' : 'MS Control',
        }

        return render(request, "index.html", context=context)


class ChecklistView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        checklist = CadastroChecklist.objects.all()
        serializer = CadastroChecklistSerializer(checklist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CadastroChecklistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(View):
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)



class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):

        checklists = Checklist.objects.all()
        print(checklists)

        return render(request, self.template_name, context={'checklists' : checklists})


class ChecklistFormView(View):
    template_name = 'checklist.html'

    def get(self,request,checklist_id, *args, **kwargs):

        checklist = get_object_or_404(CadastroChecklist, pk=checklist_id)
        print(checklist)
        print(checklist.itens)

        print(checklist_id)

        return render(request, self.template_name, context={'checklists' : checklist})

class QrCodeView(View):
    def get(self,request,checklist_id,ambiente_id):
        base = 'http://localhost:8000/'
        cadastro_checklist = CadastroChecklist.objects.get(pk=checklist_id)
        ambiente = emd.Ambiente.objects.get(pk=ambiente_id)
        itens = cadastro_checklist.itens.all().values('id','descricao')
        url = base + 'checklist/{}/{}/'.format(checklist_id,ambiente_id)
        print(ambiente)
        print(itens)

        context = {'checklists' : cadastro_checklist , 'urls' : url, 'ambientes' : ambiente}
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("Checklist", url), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
        return render(request, "qrcode.html", context=context)
