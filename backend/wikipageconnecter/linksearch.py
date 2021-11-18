import pagereader

class Page:
    def __init__(self, name, id, prev_page=None, next_page=None):
        self.name = name
        self.id = id
        self.prev_page = prev_page
        self.next_page = next_page

    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        if isinstance(other, type(self)):
            if other:
                return self.id == other.id
        return False
    def __repr__(self):
        return '<Page {}>'.format(self.name)

class LinkSearch:
    def __init__(self, start_name, goal_name):
        self.pr = pagereader.PageReader()
        start_id, start_norm_name = self.pr.getPageId(start_name)
        self.start = Page(start_norm_name, start_id)
        goal_id, goal_norm_name = self.pr.getPageId(goal_name)
        self.goal = Page(goal_norm_name, goal_id)
        self.searched_set = set()
        self.goal_set = set()
        self.count = 0

    #TODO parse html of each page to find link name
    #since <a http=/Almond (fruit)> nut</a> != nut
    def getPageChain(self):
        current_page = self.goal
        page_chain = []
        while current_page != None:
            page_chain.append(current_page.name)
            current_page = current_page.prev_page
        return page_chain[::-1]


    def search(self):
        to_search = [self.start]
        to_expand = []
        print('Generating Goal Set...')
        for page_name, page_id in self.pr.getLinksHere(self.goal.id, 8):
            self.goal_set.add(Page(page_name, page_id, None, self.goal))

        while True:
            if to_search:
                if to_search[0] == self.goal:
                    self.goal.prev_page = to_search[0].prev
                    return self.getPageChain()
                elif to_search[0] in self.goal_set:
                    self.goal.prev_page = to_search[0]
                    return self.getPageChain()
                self.count += len(self.goal_set) + 1
                print('Searched:', self.count, flush = True, end='\r')
                self.searched_set.add(to_search[0].id)
                to_expand.append(to_search[0])
                to_search = to_search[1:]
            elif to_expand:
                page_info = self.pr.getPageLinks(to_expand[0].name)
                for page_name, page_id in page_info:
                    if page_id not in self.searched_set:
                        page = Page(page_name, page_id, to_expand[0])
                        to_search.append(page)
                to_expand = to_expand[1:]
