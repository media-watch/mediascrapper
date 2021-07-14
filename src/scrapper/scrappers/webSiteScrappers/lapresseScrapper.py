from bs4 import BeautifulSoup

class LapresseScrapper:
    
    def scrap(self, html):
        soup = BeautifulSoup(html, features="html.parser")
        title = soup.find("h1").find("span").text
        date = soup.find("div",{"class":"bdaia-post-date"}).find("span",{"class":"bdayh-date"}).text
        article = " ".join([ arti.text for arti in soup.findAll("p", {"class":"p1"})])
        return {"title":title, "date":date, "article":article}
