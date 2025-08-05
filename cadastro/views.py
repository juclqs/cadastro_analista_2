import pandas as pd
import openpyxl
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from .models import Usuario, Campus, GrupoTrabalho, Cidade, Estado, Edital
from .forms import UsuarioForm, CidadeForm, EstadoForm, CampusForm, GrupoTrabalhoForm, EditalForm, GrupoAtendimentoForm

# ==================== USUÁRIOS ====================


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})


def adicionar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/formulario.html', {'form': form})


def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/formulario.html', {'form': form})


def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect('lista_usuarios')

# ==================== CIDADES ====================


def lista_cidades(request):
    cidades = Cidade.objects.all()
    return render(request, 'lista_cidades.html', {'cidades': cidades})


def adicionar_cidade(request):
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cidades')
    else:
        form = CidadeForm()
    return render(request, 'usuarios/formulario.html', {'form': form})


def editar_cidade(request, cidade_id):
    cidade = get_object_or_404(Cidade, id=cidade_id)
    if request.method == 'POST':
        form = CidadeForm(request.POST, instance=cidade)
        if form.is_valid():
            form.save()
            return redirect('lista_cidades')
    else:
        form = CidadeForm(instance=cidade)
    return render(request, 'usuarios/formulario.html', {'form': form})


def excluir_cidade(request, cidade_id):
    cidade = get_object_or_404(Cidade, id=cidade_id)
    cidade.delete()
    return redirect('lista_cidades')

# ==================== ESTADOS ====================


def lista_estados(request):
    estados = Estado.objects.all()
    return render(request, 'lista_estados.html', {'estados': estados})


def adicionar_estado(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estados')
    else:
        form = EstadoForm()
    return render(request, 'usuarios/formulario.html', {'form': form})


def editar_estado(request, estado_id):
    estado = get_object_or_404(Estado, id=estado_id)
    if request.method == 'POST':
        form = EstadoForm(request.POST, instance=estado)
        if form.is_valid():
            form.save()
            return redirect('lista_estados')
    else:
        form = EstadoForm(instance=estado)
    return render(request, 'usuarios/formulario.html', {'form': form})


def excluir_estado(request, estado_id):
    estado = get_object_or_404(Estado, id=estado_id)
    estado.delete()
    return redirect('lista_estados')

# ==================== CAMPUS ====================


def lista_campus(request):
    campus = Campus.objects.all()
    return render(request, 'lista_campus.html', {'campus': campus})


def adicionar_campus(request):
    if request.method == 'POST':
        form = CampusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_campus')
    else:
        form = CampusForm()
    return render(request, 'usuarios/formulario.html', {'form': form})


def editar_campus(request, campus_id):
    campus = get_object_or_404(Campus, id=campus_id)
    if request.method == 'POST':
        form = CampusForm(request.POST, instance=campus)
        if form.is_valid():
            form.save()
            return redirect('lista_campus')
    else:
        form = CampusForm(instance=campus)
    return render(request, 'usuarios/formulario.html', {'form': form})


def excluir_campus(request, campus_id):
    campus = get_object_or_404(Campus, id=campus_id)
    campus.delete()
    return redirect('lista_campus')

# ==================== GRUPOS DE TRABALHO ====================


def lista_grupos(request):
    grupos = GrupoTrabalho.objects.all()
    return render(request, 'lista_grupos.html', {'grupos': grupos})


def adicionar_grupo(request):
    if request.method == 'POST':
        form = GrupoTrabalhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_grupos')
    else:
        form = GrupoTrabalhoForm()
    return render(request, 'usuarios/formulario.html', {'form': form})


def editar_grupo(request, grupo_id):
    grupo = get_object_or_404(GrupoTrabalho, id=grupo_id)
    if request.method == 'POST':
        form = GrupoTrabalhoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('lista_grupos')
    else:
        form = GrupoTrabalhoForm(instance=grupo)
    return render(request, 'usuarios/formulario.html', {'form': form})


def excluir_grupo(request, grupo_id):
    grupo = get_object_or_404(GrupoTrabalho, id=grupo_id)
    grupo.delete()
    return redirect('lista_grupos')


def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

# ==================== EXPORTAÇÃO / IMPORTAÇÃO ====================


def exportar_usuarios(request):
    usuarios = Usuario.objects.select_related('campus__cidade__estado').all()
    dados = []

    for u in usuarios:
        dados.append({
            'Nome': u.nome,
            'CPF': u.cpf,
            'Matrícula': u.matricula,
            'Campus': u.campus.nome,
            'Email': u.email,
            'Endereço': u.endereco,
            'banco': u.banco,
            'Agencia': u.agencia,
            'Conta': u.conta,
            'Chave Pix': u.chave_pix,
            'Cidade': u.campus.cidade.nome,
            'Estado': u.campus.cidade.estado.nome,
            'Bairro': u.bairro,
            'Cep': u.cep,
            'Telefone': u.telefone,
            'Grupos': ", ".join([g.nome for g in u.grupos.all()])
        })

    df = pd.DataFrame(dados)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=usuarios.xlsx'
    df.to_excel(response, index=False)
    return response


def exportar_grupos(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Grupos"

    # Cabeçalhos
    ws.append(['Nome do Grupo'])

    # Dados
    for grupo in GrupoTrabalho.objects.all():
        ws.append([grupo.nome])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=grupos.xlsx'
    wb.save(response)
    return response


def exportar_cidades(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Cidades"

    # Cabeçalhos
    ws.append(['Nome da Cidade', 'Estado'])

    # Dados
    for cidade in Cidade.objects.select_related('estado').all():
        ws.append([cidade.nome, cidade.estado.nome])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=cidades.xlsx'
    wb.save(response)
    return response


def exportar_estados(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Estados"

    # Cabeçalhos
    ws.append(['Nome do Estado'])

    # Dados
    for estado in Estado.objects.all():
        ws.append([estado.nome])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=estados.xlsx'
    wb.save(response)
    return response


def exportar_campus(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Campus"

    # Cabeçalhos
    ws.append(['Nome do Campus', 'Sigla do Campus'])

    # Dados
    for campus in Campus.objects.all():
        ws.append([campus.nome, campus.sigla])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=campus.xlsx'
    wb.save(response)
    return response


def importar_excel(request):
    if request.method == 'POST' and request.FILES['arquivo']:
        df = pd.read_excel(request.FILES['arquivo'])

        for _, row in df.iterrows():
            estado, _ = Estado.objects.get_or_create(nome=row['Estado'])
            cidade, _ = Cidade.objects.get_or_create(
                nome=row['Cidade'], estado=estado)
            campus, _ = Campus.objects.get_or_create(
                nome=row['Campus'], cidade=cidade)

            usuario = Usuario.objects.create(
                nome=row['Nome'],
                cpf=row['CPF'],
                matricula=row['Matrícula'],
                chave_pix=row['Chave Pix'],
                conta=row['Conta'],
                agencia=row['Agencia'],
                endereco=row['Endereço'],
                bairro=row['Bairro'],
                cep=row['Cep'],
                telefone=row['Telefone'],
                campus=campus
            )

            grupos = row.get('Grupos', '').split(',')
            for nome_grupo in grupos:
                nome_grupo = nome_grupo.strip()
                if nome_grupo:
                    grupo, _ = GrupoTrabalho.objects.get_or_create(
                        nome=nome_grupo)
                    usuario.grupos.add(grupo)

        return redirect('lista_usuarios')

    return render(request, 'cadastro/lista.html', {'usuarios': Usuario.objects.all()})


# ==================== EDITAIS ====================

def lista_edital(request):
    editais = Edital.objects.all()
    return render(request, 'lista_editais.html', {'editais': editais})


def adicionar_edital(request):
    if request.method == 'POST':
        form = EditalForm(request.POST)
        if form.is_valid():
            form.save()
            # redireciona para a lista de editais
            return redirect('lista_editais')
    else:
        form = EditalForm()
    return render(request, 'usuarios/formulario.html', {'form': form})


def editar_edital(request, edital_id):
    edital = get_object_or_404(Edital, id=edital_id)
    if request.method == 'POST':
        form = EditalForm(request.POST, instance=edital)
        if form.is_valid():
            form.save()
            return redirect('lista_editais')
    else:
        form = EditalForm(instance=edital)
    return render(request, 'usuarios/formulario.html', {'form': form})


def excluir_edital(request, edital_id):
    edital = get_object_or_404(Edital, id=edital_id)
    edital.delete()
    return redirect('lista_editais')


def exportar_editais(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Editais"

    # Cabeçalhos
    ws.append(['Nome do Edital', 'Numero', 'Campus'])

    # Dados
    for edital in Edital.objects.all():
        ws.append([edital.nome, edital.numero,
                  edital.campus.nome if edital.campus else ''])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=editais.xlsx'
    wb.save(response)
    return response


def visualizar_edital(request, edital_id):
    edital = get_object_or_404(Edital, pk=edital_id)

    if request.method == 'POST':
        form = EditalForm(request.POST, instance=edital)
        if form.is_valid():
            form.save()
            return redirect('visualizar_edital', edital_id=edital.pk)
    else:
        form = EditalForm(instance=edital)

    return render(request, 'visualizar_edital.html', {'form': form, 'edital': edital})


def importar_equipe_edital(request, id):
    edital = get_object_or_404(Edital, id=id)

    # Ajuste para relacionamento correto com grupos de trabalho
    grupos = edital.grupos_trabalho.all()  # ajustar conforme seu modelo

    usuarios_importados = 0
    for grupo in grupos:
        usuarios = grupo.usuarios.all()  # ou o nome correto do relacionamento
        for usuario in usuarios:
            if not edital.equipe.filter(id=usuario.id).exists():
                edital.equipe.add(usuario)
                usuarios_importados += 1

    messages.success(
        request, f'{usuarios_importados} usuários importados para a equipe do edital.')
    return redirect('visualizar_edital', edital_id=edital.id)


def adicionar_grupo_atendimento(request, edital_id):
    edital = get_object_or_404(Edital, id=edital_id)

    if request.method == 'POST':
        form = GrupoAtendimentoForm(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.edital = edital
            grupo.save()
            return redirect('visualizar_edital', edital_id=edital.id)
    else:
        form = GrupoAtendimentoForm()

    return render(request, 'adicionar_grupo_atendimento.html', {'form': form, 'edital': edital})


def selecionar_grupo_trabalho(request, edital_id):
    edital = get_object_or_404(Edital, id=edital_id)
    grupos = edital.grupos_trabalho.all()
    return render(request, 'selecionar_grupo_trabalho.html', {'edital': edital, 'grupos': grupos})


def visualizar_edital_grupo(request, edital_id, grupo_id):
    edital = get_object_or_404(Edital, id=edital_id)
    grupo = get_object_or_404(GrupoTrabalho, id=grupo_id, editais=edital)
    return render(request, 'editais/visualizar_edital_grupo.html', {'edital': edital, 'grupo': grupo})
