from bs4 import BeautifulSoup

class RealitesScrapper:
    
    def scrap(self, html):
        soup = BeautifulSoup(html, features="html.parser")
        title = soup.find("h1").find("span").text
        date = soup.find("time").text
        article = " ".join([ arti.text for arti in soup.find("div", {"class":"entry-content"}).findChildren()])
        return {"title":title, "date":date, "article":article}
    