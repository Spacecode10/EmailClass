from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Main, SALES
from transformers import BertTokenizer, BertForSequenceClassification, AutoModelForSequenceClassification, \
    BertTokenizerFast


# Create your views here.
def index(request):
    # if request.method == "get":
    #     text=request.GET.get('email')
    return render(request, 'classify.html')


def result(request):
    # 0 if request.method == "get":
    text = request.GET.get('email')
    model = AutoModelForSequenceClassification.from_pretrained('D:\IndiaNIC\model')
    tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased", max_length=512)
    inputs = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    outputs = model(**inputs)
    probs = outputs[0].softmax(1)
    pred_label_idx = probs.argmax()
    pred_label = model.config.id2label[pred_label_idx.item()]
    # return pred_label
    print(pred_label)
    main=Main(content=text)
    main.save()
    if pred_label == "Sales,Interested" or pred_label == "Sales,Not Interested" or pred_label == "Sales,Termination" or pred_label == "Sales,Price negotiation":
        sales = SALES(id=main, subtype=pred_label, content=text)
        print("########Sales############")
        sales.save()
    print(pred_label, text)
    # x.save()

    return render(request, 'result.html', {'result': pred_label})
