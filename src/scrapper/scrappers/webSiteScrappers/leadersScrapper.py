from bs4 import BeautifulSoup

class LeadersScrapper:
    
    def scrap(self, html):
        soup = BeautifulSoup(html, features="html.parser")
        title = soup.find("h1").text
        date = soup.find("div",{"class":"infos"}).text
        data = [ arti.text for arti in soup.find("div", {"class":"article_body"}).findChildren()]
        idx = data.index("Lire aussi")
        article = " ".join(data[:idx])
        return {"title":title, "date":date, "article":article}
        