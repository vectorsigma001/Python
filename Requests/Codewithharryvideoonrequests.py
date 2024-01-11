"""

"""GET REQUEST.PY"""
"""
import requests
r = requests.get("https://www.codewithharry.com")
print(r.text)
with open("index.html",'w') as f:
    f.write(r.text)
"""


"""QUICKSTART.py"""
"""
import requests
r = requests.get('https://api.github.com/events')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())
"""

"""GET REQUESTS when you try to access something """
"""GET REQUEST WITH PARAMETER"""
#httpsbin is a website which helps you to test requests
"""
import requests
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.json())
"""


"""POST REQUESTS"""
#SHOWS POST REQUESTS IS SUCCESSFULL AND GIVES KEY AND VALUE
"""
import requests
r = requests.post('https://httpbin,org/post?a=b', data={'keys':'value'})
print(r.text)
"""

"""USE POST REQUESTS YOU TRY TO CREATE SOMETHING """
"""OTHER REQUESTS TYPE"""
"""PUT REQUEST WHEN YOU POST A FORM """
"""
import requests
r = requests.put("https://httpbin.org/put", data={"a": 1, "b":3})
print(r.text)
"""

"""DOWNLOADING IMAGES WITH REQUESTS"""
"""
import requests
from PIL import Image 
from io import BytesIO
url="download link"
r=requests.get(url)
i = Image.open(BytesIO(r.content))
fp = open("img.jpg","wb")
i.save(fp)
fp.close()
"""
"""DOWNLOADING A SOFTWARE WITH REQUESTS"""
"""
import requests
from io import BytesIO
url="download link"
r=requests.get(url)
#i = BytesIO(r.content)
fp = open("filename with extension","wb")
fp.write(r.content)
fp.close()
"""


"""Downloading images"""

"""
import requests
from PIL import Image
from io import BytesIO

def download_image(url, output_path):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open the image using Pillow
        image = Image.open(BytesIO(response.content))

        # Save the image as a file
        image.save(output_path)

        print(f"Image saved as {output_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

# Example usage
url = "https://i.all3dp.com/workers/images/fit=scale-down,w=1920,h=1080,gravity=0.5x0.5,format=auto/wp-content/uploads/2023/03/20150925/wowki-scaled.jpg"
output_path = "downloaded_image.jpg"  # Replace with the desired output file path
download_image(url, output_path)
"""


"""KNOW HOW MUCH A FILE IS DOWNLOADED WITH STREAMS"""
"""
import requests
url = "urlname"
r = requests.get(url,stream=True)
#how total size of the file
totalExpectedBytes = r.headers["Content-Length"]
print(totalExpectedBytes)
bytesReceived = 0
with open("winrar.exe",'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        print(f"{bytesReceived} received out of total {totalExpectedBytes}")
        f.write(chunk)
        bytesReceived +=128


fp = open("winrav.wav", "wb")
fp.write(r.content)
fp.close()
"""

"""PROGRESS BAR OF THE DOWNLOADS"""
"""
import requests
from tqdm import tqdm
url = "urlname"
r = requests.get(url,stream=True)
#how total size of the file
totalExpectedBytes = r.headers["Content-Length"]
print(totalExpectedBytes)
bytesReceived = 0
progress_bar = tqdm(total = totalExpectedBytes, unit='iB', unit_scale = True)
with open("winrar.exe",'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        progress_bar.update(128)
        #print(f"{bytesReceived} received out of total {totalExpectedBytes}")
        f.write(chunk)
        bytesReceived +=128
    progress_bar.close()

"""

"""WORKING ON PROXIES SERVER"""
"""
import requests

http_proxy = ""
http_proxy = ""

proxies = {
            "http"  : http_proxy,
            "https" : https_proxy
        }

r = requests.get("https://httpbin.org/get", proxies=proxies)
print(r.text)
"""
