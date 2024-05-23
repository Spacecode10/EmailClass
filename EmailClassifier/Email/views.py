from django.shortcuts import render
from django.http import JsonResponse
from transformers import BertTokenizer, BertForSequenceClassification
import torch
# Create your views here.
def index(request):
    if request.method=="POST":
        return render(request, "classify.html")
