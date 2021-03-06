from selenium import webdriver
import pandas as pd
import numpy as np
import time
import datetime
import subprocess
import re
import os
import requests
import sys
import json
from selenium.webdriver import ChromeOptions

alias = {}

## global functions
def downloadPdf(output, link):
    '''
    write pdf file based on link address.
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(link, headers=headers)
    with open(output, 'wb') as f:
        f.write(response.content)


def parse(infobox):
    infobox = infobox.lower().split("-")
    infobox = [c.strip() for c in infobox]
    author = infobox[0].split(",")[0].split(" ")[1]  # extract last name
    journal = infobox[1].split(",")[0] # extract journal, "..." may be init, otherwise, we need to get bibtex diredctly, much more time-consuming
    year = infobox[1].split(",")[1].strip()  # extract year
    return author, journal, year

class Article:
    def __init__(self, keywords, target_journal, folder):
        self.keywords = keywords   # search keywords
        self.target_journal = target_journal  # searched journal
        self.output_folder = folder   # output folder
        self.createFolder()
        self.total_articles = {}

    def createFolder(self):
        self.output_fpath = "/".join([self.output_folder, self.keywords, self.target_journal])
        if not os.path.exists(self.output_fpath):
            os.makedirs(self.output_fpath)  # creaet output folder if there is not one.
            print('creating folder {0}'.format(self.output_fpath))

    def getInfo(self, article, driver):
        default = {"title": "NA", "author": "NA", "journal": "NA", "year":"NA", "log": "NA", "citation":"NA"}
        default['title'] = article.find_element_by_class_name("gs_rt").text.lower()
        default['title'] = re.sub("[^a-z0-9\ \-\:]", "", default['title'])
        default['title'] = re.sub("pdf\ ", "", default['title'])
        infobox = article.find_element_by_class_name("gs_a").text
        default['author'], default['journal'], default['year'] = parse(infobox)
        default['citation'] = article.find_element_by_css_selector("div[class=gs_fl]").find_element_by_css_selector("a[href^='/scholar?cites']").text.split(" ")[-1]
        return default

    def getPdf(self, article, driver):
        pdf_link = "NA"
        try:
            tmp = article.find_element_by_css_selector("div[class=gs_or_ggsm")
            pdf_link = tmp.find_element_by_tag_name("a").get_attribute("href")
            if not pdf_link.endswith('.pdf'):
                pdf_link = "NA"
        except:
            self.info['log'] = "pdf missing"
        return pdf_link

    def getFileName(self, alias=alias):
        by = ["author", "year", "title", "journal"]
        if alias:
            if self.info['journal'] in alias.keys():
                self.info['journal-short'] = alias[self.info['journal']]
                by = ["author", "year", "title", "journal-short"]
        if len(self.info['title'].split(" ")) > 10:
            self.info['title-short'] = " ".join(self.info['title'].split(" ")[:10])
            if "journal-short" in self.info.keys():
                by = ["author", "year", "title-short", "journal-short"]
            else:
                by = ["author", "year", "title-short", "journal"]
        filename = "-".join([self.info[c] for c in by]) + ".pdf"
        return filename

    def fit(self, article, driver, num, citation):
        default = {"title": "NA", "author": "NA", "journal": "NA", "year":"NA", "log": "NA", "citation":"NA"}
        try:
            self.info = self.getInfo(article, driver)
        except:
            self.info = default
        if self.info is not default and int(self.info['citation'][:6]) >= citation:
            self.pdf = self.getPdf(article, driver)
            self.filename = self.getFileName()
            self.info['filename'] = self.filename
            output = self.output_fpath + "/" + self.filename
            if self.pdf is not "NA":
                try:
                    downloadPdf(output, self.pdf)
                except:
                    self.log = self.info['log'] + "||| pdf download error"
        self.total_articles[num] = self.info


def run(keywords, journals, citation, recursive = 6):
    '''
    search based on keywords and journals combinations
    recursive is the number of request pages.
    '''
    if not chromedriver_path:
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome(chromedriver_path)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.get('https://scholar.google.com/')
    for i in keywords:
        for j in journals:
            cnt = 1
            articles = Article(i, j, fpath)
            search_keyword = " ".join(['''author:"{}"'''.format(i.lower()), '''source:"{}"'''.format(j.lower())]) ## generate search keyword like "wikipedia source: 'mis quarterly'"
            print("current search key: {0}".format(search_keyword))
            input_element = driver.find_element_by_name("q")
            input_element.clear()
            input_element.send_keys(search_keyword)
            input_element.submit()
            time.sleep(2)
            for n in range(recursive):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                elements = driver.find_elements_by_css_selector("div[class=gs_r\ gs_or\ gs_scl]")  #find article boxs
                for e in elements:
                    try:
                        articles.fit(e, driver, cnt, citation)
                    except:
                        print("page {} number {} parse error!".format(n, cnt))
                    cnt += 1
                try:
                    driver.find_element_by_css_selector("span[class=gs_ico\ gs_ico_nav_next]").click()
                    time.sleep(3)
                except:
                    break   # break the loop if can't find next page
            file_dir = articles.output_fpath
            print(file_dir)
            files_list = os.listdir(file_dir)
            if len(files_list) > 0:
                print(len(files_list), articles.keywords, articles.target_journal)
                log = pd.DataFrame(articles.total_articles).T  # generate log files
                now = datetime.datetime.now()
                log.to_excel(articles.output_fpath+"/"+"logfile_{}.xlsx".format(now.strftime("%m-%d-%Y")))
            else: os.rmdir(file_dir)
    driver.quit()

if __name__ == '__main__':
    config = json.load(open(sys.argv[1]))  # read config
    keywords = config['keywords']
    journals = config['journals']
    citation = config['citation']
    fpath = config['fpath']
    chromedriver_path = config['chromedriver_path']
    run(keywords, journals, citation, recursive=6)
