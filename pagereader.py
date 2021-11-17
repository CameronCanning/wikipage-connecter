import requests
import json

class PageReader:
    def __init__(self):
        self.sess = requests.Session()
        self.url = "https://en.wikipedia.org/w/api.php"
        self.glhcontinue = None

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
        #print(json.dumps(data, indent=4))
        if "nomalized" in data["query"].keys():
            page_title = data["query"]["normalized"][0]["to"]

        page_id = int(list(data["query"]["pages"])[0])
        #-1 is returned when page doesn't exist
        assert(page_id >= 0)
        #page id, normalized name
        return page_id, page_title

    def getLinksHere(self, page_id, max_batches=float('inf')):
        page_info = []
        batches = 1
        complete = False
        params = {
            "action": "query",
            "format": "json",
            "pageids": page_id,
            "generator": "linkshere",
            "glhprop": "redirect",
            "glhlimit": "50",
            "glhnamespace": 0,           
        }
            
        if self.glhcontinue:
            params["glhcontinue"] = self.glhcontinue
        
        page_info_batch, b_continue = self.getBatch(params)
        page_info += page_info_batch

        while b_continue and batches < max_batches:
            self.glhcontinue = self.data["continue"]["glhcontinue"]
            params["glhcontinue"] = self.glhcontinue
            page_info_batch, b_continue = self.getBatch(params)
            page_info += page_info_batch               
            batches += 1
        
        if b_continue: 
            self.glhcontinue = self.data["continue"]["glhcontinue"]

        return page_info