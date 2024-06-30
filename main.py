from bs4 import BeautifulSoup
import requests


def main():
    """
    This function is for scraping divar web site.
    search topic --> get information
    """
    
    # get params
    search = input("Search About: ")
    params = {"q": search }

    # send request
    request = requests.get(f"https://divar.ir/s/tehran", params=params)

    # BeautifulSoup
    soup = BeautifulSoup(request.text, "html.parser")
    results = soup.find("div", {"id": "post-list-container-id"})
    links = results.findAll("div", {"class": "post-list__widget-col-a3fe3"})

    for item in links:
        item_txt = item.find("a").text
        item_href = f"https://divar.ir{item.find('a').attrs['href']}/"
        
        if item_txt and item_href:
            
            # print on console
            print(f"title: {item_txt}")
            print(f"link: {item_href}\n")
            
            # save on response file
            response = f"title: {item_txt}\nlink: {item_href}\n\n\n"
            file = open("response.txt", "a")
            file.write(response)
            file.close()


if __name__ == "__main__":
    main()
