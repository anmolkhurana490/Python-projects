import requests
url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png"
image=requests.get(url).content
with open("Download/1.png", "wb") as file:
	file.write(image)
