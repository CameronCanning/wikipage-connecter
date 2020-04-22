import requests
import json

class PageReader:
    def __init__(self):
        self.sess = requests.Session()
        self.url = "https://en.wikipedia.org/w/api.php"

    def getBatch(self, params, verbose = False):
        page_info = []
        req = self.sess.get(url=self.url ,params=params)
        self.data = req.json()
        if verbose:
            print(json.dumps(self.data, indent=4))
        if "warnings" in self.data.keys():
            print(json.dumps(self.data["warnings"], indent=4))
            return

        pages = self.data["query"]["pages"]

        for page in pages.values():
            if "missing" not in page.keys():
                page_info.append((page["title"], int(page["pageid"])))

        return page_info, ("continue" in self.data.keys())

    def getPageLinks(self, page_title):
        page_info = []
        params = {
            "action": "query",
            "format": "json",
            "titles": page_title,
            "generator": "links",
            "gpllimit": "max",
            "gplnamespace": 0
        }

        page_info_batch, b_continue = self.getBatch(params)
        page_info += page_info_batch

        while b_continue:
            params["gplcontinue"] = self.data["continue"]["gplcontinue"]
            page_info_batch, b_continue = self.getBatch(params)
            page_info += page_info_batch

        return page_info

    def getPageId(self, page_title):
        params = {
            "action": "query",
            "format": "json",
            "titles": page_title,
            "prop": "pageprops",
        }

        req = self.sess.get(url=self.url ,params=params)
        data = req.json()
        #page id, normalized name
        return int(list(data["query"]["pages"])[0]), data["query"]["normalized"][0]["to"]
