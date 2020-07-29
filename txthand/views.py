from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import cv2,io,requests,json,os
def home(request):
    return render(request,"home.html")

def convert(request):
        myfile = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url='media/'+ filename  
        img=cv2.imread(url)
        height, width, _ = img.shape
        roi = img[0: height, 0: width]
        url_api = "https://api.ocr.space/parse/image"
        _, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
        file_bytes = io.BytesIO(compressedimage)
        result = requests.post(url_api,
                    files = {"ez.jpg": file_bytes},
                    data = {"apikey": "343e7e20b288957",
                            "language": "eng"})
        result = result.content.decode()
        result = json.loads(result)
        parsed_results = result.get("ParsedResults")[0]
        userText = parsed_results.get("ParsedText")
        os.remove(url)
        return render(request,"result.html",{'result':userText})
        






