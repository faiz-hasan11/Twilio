from django.shortcuts import render
from twilio.rest import Client
# Create your views here.
def home(request):
    return render(request,'home.html')

def predictResult(request):
    if request.method == 'POST':
        temp={}
        temp['Sid'] = str(request.POST.get('SidVal'))
        temp['Token'] = str(request.POST.get('TokenVal'))
        temp['Cell'] = str(request.POST.get('CellVal'))
        temp['Twilio'] = str(request.POST.get('TwilioVal'))
        temp['Message'] = str(request.POST.get('MessageVal'))
        error = False
        try:
            client = Client(temp['Sid'],temp['Token'])
            my_msg = temp['Message']
            message = client.messages.create(to=temp['Cell'], from_=temp['Twilio'],body=temp['Message'])
        except:
            error = True
        return render(request,'pred.html',{'error':error})
