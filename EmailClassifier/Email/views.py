from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Main, SALES, HR, DEV
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
    predictmodel = AutoModelForSequenceClassification.from_pretrained('D:\IndiaNIC\PriorityModel')
    tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased", max_length=512)
    inputs = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    outputs = model(**inputs)
    predictions=predictmodel(**inputs)
    probs = outputs[0].softmax(1)
    prob2=predictions[0].softmax(1)
    pred_label_idx = probs.argmax()
    pred_label_idx2 = prob2.argmax()
    pred_label = model.config.id2label[pred_label_idx.item()]
    pred_label_priority = predictmodel.config.id2label[pred_label_idx2.item()]

    # return pred_label
    print(pred_label)
    print(pred_label_priority)
    main = Main(content=text)
    main.save()
    if pred_label == "Sales,Interested" or pred_label == "Sales,Not Interested" or pred_label == "Sales,Termination" or pred_label == "Sales,Price negotiation":
        sales = SALES(id=main, subtype=pred_label, content=text)
        print("########Sales############")
        sales.save()
    print(pred_label, text)
    # x.save()
    if pred_label == 'HR, Recruitment' or pred_label == 'HR, Appraisal' or pred_label == 'HR, Leaves':
        hr = HR(id=main, content=text, subtype=pred_label)
        hr.save()
    if pred_label == 'Development,Modification' or pred_label == 'Development, Review':
        dev = DEV(id=main, content=text, subtype=pred_label)
        dev.save()
    return render(request, 'result.html', {'result': pred_label})
