import pagereader

class Page:
    def __init__(self, name, prev_page, depth):
        self.name = name
        self.prev_page = prev_page
        self.depth = depth

class LinkSearch:
    def __init__(self, name_start, goal_name):
        self.start = Page(name_start, None, 0)
        self.goal_names = goal_name
        self.pr = pagereader.PageReader()
        self.searched_set = set()

    def getPageChain(self, last_page):
        current_page = last_page
        page_chain = []
        while current_page != None:
            page_chain.append(current_page.name)
            current_page = current_page.prev_page
        return page_chain[::-1]


    def bfs(self, max_depth=3):
        to_search = [self.start]
        to_expand = []
        while True:
            if to_search:
                print(to_search[0].name.encode("utf-8"))
                if to_search[0].name == self.goal_name:
                    return self.getPageChain(to_search[0])
                self.searched_set.add(to_search[0])
                to_expand.append(to_search[0])
                to_search = to_search[1:]
            elif to_expand:
                new_page_names = self.pr.getPageLinks(to_expand[0].name)
                for page_name in new_page_names:
                    if page_name not in self.searched_set:
                        page = Page(page_name, to_expand[0], to_expand[0].depth + 1)
                        to_search.append(page)
                to_expand = to_expand[1:]
