from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test



# Create your views here.
# votreprojet/votreapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadedFileForm
from .models import UploadedFile, UploadHistory

import hashlib, os
def hash_file(file_path):
    if os.path.exists(file_path):
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    else:
        return None


def index(request):
    context = {
        }
    if not request.user.is_authenticated:
        return redirect('login')
    error = False
    message = ""
    success=False
    upload_history = UploadHistory.objects.all()
    current_user=request.user
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Enregistrez le fichier avec l'utilisateur actuel
            uploaded_file = form.save(commit=False)
            uploaded_file.save()
            uploaded_file.hash_value = uploaded_file.calculate_hash()  # Ajoutez cette ligne
            uploaded_file.save()
            history_repos=upload_history.filter(client=uploaded_file.client).first()
            if history_repos:
                if uploaded_file.hash_value==history_repos.hash_value:
                    success=True
                    message="Ce document est déjà enregistré. Aucune nouvelle modification n'as ete apporter"
                else:
                    if current_user.groups.filter(name='Interne').exists() or current_user.is_staff:
                        history_repos.uploaded_file=uploaded_file
                        history_repos.hash_value=uploaded_file.hash_value
                        history_repos.save()
                        success=True
                        message="Document modifier avec succes"
                    else:
                        error=True
                        message="Vous n'est pas Authoriser a effectuer cette action"
            else:
                UploadHistory.objects.create(client=uploaded_file.client, uploaded_file=uploaded_file, hash_value=uploaded_file.hash_value)
                success=True
                message="Document modifier avec succes"
            # Ajoutez ici le code pour rediriger l'utilisateur ou afficher un message de succès
        else:
            error=True
            message="Tous s'est pas bien passer , Veuillez recommencer"
        context = {
        'error':error,
        'message':message,
        'form': form,
        'success': success,
        'upload': upload_history,
        }

    else:
        form = UploadedFileForm()
        context = {
        'form': form,
        'upload': upload_history
        }
    return render(request, 'db_secu/index.html', context)


def profil(request):
    if not request.user.is_authenticated:
        return redirect('login')
    upload_history = UploadHistory.objects.all()

    context = {
        "user": request.user,
        'upload': upload_history.filter(client=request.user)
        }
    
    return render(request, 'db_secu/profils.html', context)
