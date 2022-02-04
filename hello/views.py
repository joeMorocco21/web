from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
import sqlite3 as db
import pandas as pd
# Create your views here.
def index(request):
    return render(request, 'hello/index.html')
def upload(request):
    der ='hello'
    file = request.FILES['file1']
    fs = FileSystemStorage(location=der, base_url=None, file_permissions_mode=None, directory_permissions_mode=None)
    filename = fs.save(file.name, file)
    file_url = fs.url(filename)
# Create your connection.
    df = pd.read_csv(os.path.join(os.path.dirname(__file__),filename), delimiter=',')
    tf = df[df.balcony == True]
    conn = db.connect('/tmp/8d9c3248c81cf5e/db.sqlite3')
    tf.to_sql(name='data_view_data_view', con=conn, if_exists='append')
    msg = 'File successfully saved'
    return redirect("https://immoapp.azurewebsites.net/data_view/")