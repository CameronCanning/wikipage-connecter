import requests
import json

class PageReader:
    def __init__(self):
        self.sess = requests.Session()
        self.url = "https://en.wikipedia.org/w/api.php"

    def getBatch(self, params):
        page_titles = []
        req = self.sess.get(url=self.url ,params=params)
        data = req.json()

        if "warnings" in data.keys():
            print(json.dumps(data["warnings"], indent=4))
            return

        pages = data["query"]["pages"]
        for val in pages.values():
            for link in val["links"]:
                page_titles.append(link["title"])
        return page_titles, ("continue" in data.keys())

    def getPageLinks(self, page_title):
        page_titles = []
        params = {
            "action": "query",
            "format": "json",
            "titles": page_title,
            "prop": "links",
            "pllimit": "max"
        }

        pages_batch, b_continue = self.getBatch(params)
        page_titles.append(pages_batch)

        while b_continue:
            params["plcontinue"] = data["continue"]["plcontinue"]
            pages_batch, b_continue = self.getBatch(params)
            page_titles.append(pages_batch)

        return page_titles




pr = PageReader()
pages = pr.getPageLinks("Bit")
print(pages)
