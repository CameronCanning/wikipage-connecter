import requests
import json

class PageReader:
    def __init__(self):
        self.sess = requests.Session()
        self.url = "https://en.wikipedia.org/w/api.php"

    def getBatch(self, params, verbose = False):
        page_titles = []
        req = self.sess.get(url=self.url ,params=params)
        self.data = req.json()
        if verbose:
            print(json.dumps(self.data, indent=4))
        if "warnings" in self.data.keys():
            print(json.dumps(self.data["warnings"], indent=4))
            return


        pages = self.data["query"]["pages"]

        for val in pages.values():
            if "links" in val.keys() and "missing" not in val.keys():
                for link in val["links"]:
                    page_titles.append(link["title"])

        return page_titles, ("continue" in self.data.keys())

    def getPageLinks(self, page_title):
        page_titles = []
        params = {
            "action": "query",
            "format": "json",
            "titles": page_title,
            "prop": "links",
            "pllimit": "max",
            "plnamespace": 0
        }

        pages_batch, b_continue = self.getBatch(params)
        page_titles += pages_batch

        while b_continue:
            params["plcontinue"] = self.data["continue"]["plcontinue"]
            pages_batch, b_continue = self.getBatch(params)
            page_titles += pages_batch

        return page_titles
