from urllib import response
from django.http import HttpResponse  
from .tasks import createcsv


    # response = HttpResponse(content_type='text/csv')  
    # response['Content-Disposition'] = 'attachment; filename="file.csv"'
    # writer = csv.writer(response)
    # print(response,'\n--------------------------------------------------------------')
    # writer = csv.writer(settings.MEDIA_ROOT,File(response))
    # numberofrow = int(input('enter the number of rows = '))

def test(request):  
    # call the test_function using delay, calling task  
    FileName = input('Enter the the file name ?')
    numberOfRow = int(input('Enter the number of rows ? '))
    createcsv.delay(FileName,numberOfRow)
    return HttpResponse("hai it is done")
