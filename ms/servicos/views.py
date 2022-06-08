from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from .serializers import CadastroChecklistSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .models import *
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
import entidades.models as emd
import qrcode
import qrcode.image.svg
import json

from PIL import Image
from .forms import *
from io import BytesIO


class IndexView(View):
    def get(self,request):
        context = {
            'nome': 'MS Control',
        }
        return render(request, "index.html", context=context)


class EntidadesView(View):

    def get(self,request):
        entidades = emd.Entidade.objects.all()
        context = {
            'entidades' : entidades
        }
        return render(request,"entidades.html", context=context)


class EntidadeDelete(generic.DeleteView):
    model = emd.Entidade
    success_url = "/"
    template_name = "ambientes.html"






class AmbientesView(View):
    def get(self,request):
        ambientes = emd.Ambiente.objects.all()
        somaambientes = 0
        for i in ambientes:
            somaambientes += 1
        context = {
            'ambientes' : ambientes,
            'soma' : somaambientes,

        }
        return render(request, "ambientes.html", context=context)


class ServicosView(View):
    def get(self,request):
        servicos = TipoServico.objects.all()
        context = {
            'servicos' : servicos,
        }
        return render(request, "servicos.html", context=context)


class APIAmbientesChecklists(APIView):
    def get(self, request,  ambiente_id):
        ambiente = emd.Ambiente.objects.get(pk=ambiente_id)
        serializer = CadastroChecklistSerializer(ambiente.tipo_ambiente.checklists_relacionados, many=True)
        return Response(serializer.data)


class ChecklistView(APIView):
    def get(self, request,  ambiente_id, checklist_id):
        checklist = CadastroChecklist.objects.filter(pk=checklist_id)
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

class APIChecklistPreenchido(APIView):
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

class DashboardView(LoginRequiredMixin,View):
    template_name = 'dashboard.html'
    login_url = '/user/login/'

    def get(self,request):

        ambientes = emd.Ambiente.objects.all()
        checklists_sem_imagens = ChecklistPreenchido.objects.filter(foto_checklist_antes=False, foto_checklist_depois=False )
        cadastros_checklists = CadastroChecklist.objects.all()
        conforme = 0
        inconforme = 0
        percentual = 0
        id_inconformes = []
        for i in cadastros_checklists:
            itens_check = i.itens.all()
            itens = len(itens_check)
            check_preenchido = ChecklistPreenchido.objects.filter(checklist=i)
            for c in check_preenchido:
                a = json.loads(str(c.itens))
                if itens == len(a):
                    conforme+=1
                else:
                    id_inconformes.append(c.id)
                    inconforme+=1

        print(id_inconformes)
        percentual = conforme/(conforme+inconforme)*100
        soma_ambientes = 0
        soma_checklists = 0
        for i in ambientes:
            soma_ambientes += 1
        for i in checklists_sem_imagens:
            soma_checklists += 1
        context = {
            'nome': 'MS Control',
            'total_ambientes': soma_ambientes,
            'total_checklists_sem_imagem' : soma_checklists,
            'percentual_conformidade' : percentual,
            'nao_conforme': inconforme,
            }
        return render(request, self.template_name, context=context)


class ChecklistFormView(View):
    template_name = 'checklist.html'
    def get(self,request,checklist_id, *args, **kwargs):
        checklist = get_object_or_404(CadastroChecklist, pk=checklist_id)
        return render(request, self.template_name, context={'checklists' : checklist})


class QrCodeView(View):
    def get(self,request,ambiente_id):

        ambiente = emd.Ambiente.objects.get(pk=ambiente_id)
        url = '/{}/'.format(ambiente_id)
        context = {'urls' : url, 'ambientes' : ambiente}
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("Ambiente", url), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
        return render(request, "qrcode.html", context=context)


class ChecklistsAmbienteView(View):
    def get(self,request,ambiente_id):
        ambiente = emd.Ambiente.objects.get(pk=ambiente_id)
        tipo = ambiente.tipo_ambiente.id
        tipo_ambiente = emd.TipoAmbiente.objects.get(pk=tipo)
        checklists = tipo_ambiente.checklists_relacionados
        context = {
            'ambiente' : ambiente,
            'tipo_ambiente' : tipo_ambiente,
            'checklists' : checklists
        }
        return render(request, "checklist.html", context=context)

class FormChecklistView(LoginRequiredMixin, View):
    template_name = "form_checklist.html"
    login_url = '/user/login/'


    def get(self, request, ambiente_id, checklist_id):
        ambiente = emd.Ambiente.objects.get(pk=ambiente_id)
        checklist = CadastroChecklist.objects.get(pk=checklist_id)

        context = {
            'ambiente': ambiente,
            'checklist': checklist
        }
        return render(request, self.template_name, context=context)

    def post(self, request, ambiente_id, checklist_id):
        check = ChecklistPreenchido()
        check.ambiente = emd.Ambiente.objects.get(pk=ambiente_id)
        check.checklist = CadastroChecklist.objects.get(pk=checklist_id)
        check.foto_checklist_antes = request.FILES['fotoAmbienteAntes'] if 'fotoAmbienteAntes' in request.FILES else False
        itens_array = json.dumps(request.POST.getlist('itens'))
        check.itens = itens_array
        check.foto_checklist_depois = request.FILES['fotoAmbiente'] if 'fotoAmbiente' in request.FILES else False
        check.usuario = request.user
        check.save()

        return render(request, "checklist_ok.html")

class ChecklistsView(View):
    def get(self,request):
        checklists = ChecklistPreenchido.objects.order_by('-data_hora')[:5]
        context = {
            'checklists': checklists
        }
        return render(request, "lista_checklists.html", context=context)