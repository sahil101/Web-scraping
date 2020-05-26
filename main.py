from bs4 import BeautifulSoup
import requests
search = input("enter search item")
parasm = {"q": search}
r = requests.get("https://www.bing.com/search?",params=parasm)
soap = BeautifulSoup(r.text,"html.parser")
# f = open("./text.html","w+")
# f.write(str(soap.encode("utf-8")))
# f.close()
results = soap.find("ol",{"id":"b_results"})
links = results.findAll("li",{"class":"b_algo"})

for items in links:
    item_text = items.find("a").text
    item_link  = items.find("a").attrs["href"]


    if item_link and item_text:
        print(item_text)
        print(item_link)
        # print("Summary: ",items.find("a").parent.parent.find("p").text)

        # children = items.children
            # for child in children:
            # print("child ", child)
        children = items.find("h2")
        print("next sibling of the h2 : ",children.next_sibling)