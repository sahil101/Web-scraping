import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import os
def start_search():
    search = input("search for : ")
    dir_name  = search.replace(" ","_").lower()

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    params = {"q":search}

    r = requests.get("http://www.bing.com/images/search",params =params)
    soup = BeautifulSoup(r.text,"html.parser")
    links = soup.findAll("a",{"class":"thumb"})
    print(links)

    for item in links:
        try:
            img_obj  = requests.get(item.attrs["href"])
            print("images",item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]

            try:
                img  = Image.open(BytesIO(img_obj.content))
                img.save("./"+dir_name+"/"+title,img.format)

            except:
                print("could not save the image !")
        except:
            print("could not request the image")

    start_search()




start_search()