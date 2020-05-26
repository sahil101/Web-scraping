import requests
from bs4 import BeautifulSoup
def start_search():

    r = requests.get("http://www.imdb.com/chart/top")
    soup = BeautifulSoup(r.text,"html.parser")
    # print(soup)
    links = soup.findAll("td",{"class":"titleColumn"})
    count = 0

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
        print(item)
        temp = item.find("a")
        count += 1
        print("{0}.\t{1}".format(count,temp.text))



start_search()