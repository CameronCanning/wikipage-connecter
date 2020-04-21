import pagereader

class Page:
    def __init__(self, name, prev_page, depth):
        self.name = name
        self.prev_page = prev_page
        self.depth = depth

class LinkSearch:
    def __init__(self, name_start, goal_name):
        self.start = Page(name_start, None, 0)
        self.goal_name = goal_name
        self.pr = pagereader.PageReader()


    def getPageChain(self, last_page):
        current_page = last_page
        page_chain = []
        while current_page != None:
            page_chain.append(current_page.name)
            current_page = current_page.prev_page
        return page_chain[::-1]
    #0 = inf
    def bfs(self, max_depth=0):
        to_search = [self.start]
        while to_search:
            current_page = to_search[0]
            if (max_depth != 0) and (current_page.depth >= max_depth):
                print('max depth reached')
                return None
            if current_page.name == self.goal_name:
                return self.getPageChain(current_page)

            new_page_names = self.pr.getPageLinks(current_page.name)
            for page_name in new_page_names:
                to_search.append(Page(page_name, current_page, current_page.depth + 1))

            to_search = to_search[1:]
