from tkinter import filedialog
import cv2,io,requests,json
file_path = filedialog.askopenfilename()
img=cv2.imread(file_path)
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
print(userText)
