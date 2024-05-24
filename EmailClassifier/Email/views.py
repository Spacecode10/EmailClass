from django.shortcuts import render
from transformers import AutoModelForSequenceClassification
from transformers import BertForSequenceClassification,BertTokenizerFast
from django.http import JsonResponse, HttpResponse
from transformers import BertTokenizer, BertForSequenceClassification
import torch
# Create your views here.
def index(request):
    if request.method=="post":
        print(request.POST)
    return render(request, "classify.html")

def result(request):
    email=request.POST.get("email")
    model = AutoModelForSequenceClassification.from_pretrained('E:\project\model-params')
    tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased", max_length=512)
    inputs = tokenizer(email, padding=True, truncation=True, max_length=512, return_tensors="pt")
    outputs = model(**inputs)
    probs = outputs[0].softmax(1)
    pred_label_idx = probs.argmax()
    pred_label = model.config.id2label[pred_label_idx.item()]
    # return pred_label
    print(pred_label)
    return render(request, "result.html",{'result':pred_label})