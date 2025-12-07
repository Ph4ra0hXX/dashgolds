from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Menu


def hello(request):
    return render(request, "home/hello.html")


def registrar_menu(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        img = request.POST.get("img")
        descricao = request.POST.get("descricao")
        url = request.POST.get("url")
        ativo = request.POST.get("ativo") == "on"

        if not nome or not url:
            messages.error(request, "Nome e URL são obrigatórios!")
            return redirect("registrar_menu")

        # Verificar se URL já existe
        if Menu.objects.filter(url=url).exists():
            messages.error(request, "Esta URL já está registrada!")
            return redirect("registrar_menu")

        Menu.objects.create(
            nome=nome, img=img, descricao=descricao, url=url, ativo=ativo
        )
        messages.success(request, "Menu registrado com sucesso!")
        return redirect("registrar_menu")

    menus = Menu.objects.all()
    return render(request, "home/registrar.html", {"menus": menus})


def editar_menu(request, id):
    menu = get_object_or_404(Menu, id=id)

    if request.method == "POST":
        nome = request.POST.get("nome")
        img = request.POST.get("img")
        descricao = request.POST.get("descricao")
        url = request.POST.get("url")
        ativo = request.POST.get("ativo") == "on"

        if not nome or not url:
            messages.error(request, "Nome e URL são obrigatórios!")
            return redirect("editar_menu", id=id)

        # Verificar se URL já existe (e não é a mesma do menu atual)
        if Menu.objects.filter(url=url).exclude(id=id).exists():
            messages.error(request, "Esta URL já está registrada!")
            return redirect("editar_menu", id=id)

        menu.nome = nome
        menu.img = img
        menu.descricao = descricao
        menu.url = url
        menu.ativo = ativo
        menu.save()

        messages.success(request, "Menu atualizado com sucesso!")
        return redirect("registrar_menu")

    menus = Menu.objects.all()
    return render(request, "home/registrar.html", {"menu_edit": menu, "menus": menus})


def deletar_menu(request, id):
    menu = get_object_or_404(Menu, id=id)

    if request.method == "POST":
        nome_menu = menu.nome
        menu.delete()
        messages.success(request, f"Menu '{nome_menu}' deletado com sucesso!")

    return redirect("registrar_menu")
