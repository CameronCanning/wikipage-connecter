import pagereader

class Page:
    def __init__(self, name, id, prev_page, depth):
        self.name = name
        self.id = id
        self.prev_page = prev_page
        self.depth = depth

class LinkSearch:
    def __init__(self, start_name, goal_name):
        self.pr = pagereader.PageReader()
        start_id, start_norm_name = self.pr.getPageId(start_name)
        self.start = Page(start_norm_name, start_id, None, 0)
        self.goal_id, _ = self.pr.getPageId(goal_name)
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
                if to_search[0].id == self.goal_id:
                    print('Chain:')
                    return self.getPageChain(to_search[0])
                self.searched_set.add(to_search[0].id)
                to_expand.append(to_search[0])
                to_search = to_search[1:]
            elif to_expand:
                print('Searched:',len(self.searched_set), flush = True, end='\r')
                page_info = self.pr.getPageLinks(to_expand[0].name)
                for page_name, page_id in page_info:
                    if page_id not in self.searched_set:
                        page = Page(page_name, page_id, to_expand[0], to_expand[0].depth + 1)
                        to_search.append(page)
                to_expand = to_expand[1:]


#todo
    #let goal be every page that directs to goal page
    #use categories for priority
