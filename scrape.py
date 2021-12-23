# project: p3
# submitter: zluo43
# partner: jkang96@wisc.edu 
# hours: 10


import os, zipfile

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from IPython.core.display import display, Image





class GraphScraper:
    def __init__(self):
        self.visited = set()
        self.BFSorder = []
        self.DFSorder = []


def go(self, node):
    raise Exception("must be overridden in sub classes -- don't change me here!")

def bfs_search(self, node):
    visit = []
    todo = []
    todo.append(node)
    while todo:
        node = todo.pop(0)
        if node not in visit:
            visit.append(node)
            todo.extend(self.go(self,node))


def dfs_search(self, node):
        visit = []
        todo = []
        todo.append(node)
        while todo:
            node = todo.pop()
            if node not in visit:
                visit.append(node)
                todo.extend(reversed(self.go(self,node)))

class FileScraper(GraphScraper):
    def __init__(self):
        super().__init__()
        if not os.path.exists("Files"):
            with zipfile.ZipFile("files.zip") as zf:
                zf.extractall()

    def go(self, node):
        with open("Files/"+node+".txt") as f:
            data=f.read()
            lines=data.split("\n")
            self.BFSorder.append(lines[2][-1])
            self.DFSorder.append(lines[3][-1])
        return lines[1].split(" ")

class WebScraper(GraphScraper):

    def __init__(self, driver=None):
        super().__init__()
        self.driver = driver

# these three can be done as groupwork
    def go(self, url):
        self.driver.get(url)
        link = self.driver.find_elements_by_tag_name("a")

        list_dfs=self.driver.find_element_by_id("DFS")
        list_dfs.click()
        self.DFSorder.append(list_dfs.text)

        list_bfs=self.driver.find_element_by_id("BFS")
        list_bfs.click()
        self.BFSorder.append(list_bfs.text)

        return [link.get_attribute("href") for link in links]

    def dfs_pass(self, start_url):
        super().__init__()
        super().dfs_search(start_url)
        return ''.join(self.DFSorder)

    def bfs_pass(self, start_url):
        super().__init__()
        super().bfs_search(start_url)
        return ''.join(self.BFSorder)


