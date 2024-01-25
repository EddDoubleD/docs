import os
import queue
import string
import threading
import uuid
import markdown
import json

import nltk

# fix nltk: Resource punkt not found.
# ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.X/etc/openssl

# hande: use
# >> import nltk
# >> nltk.download()
# >> nltk.download('popular')
nltk.download('punkt')

from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from bloomfilter import BloomFilter

FINISH = object()


class DirWalker(threading.Thread):
    """
    bypass the folders by putting them in a queue for ourselves, and put the md files in a separate one to form json
    """

    def __init__(self, start: string, mdQueue: queue.Queue):
        """
        :param start: root for file search
        :param mdQueue: queue for md-file handler
        """
        super().__init__()
        self.start = start
        self.uuid = str(uuid.uuid4())
        self.mdQueue = mdQueue

    def run(self) -> None:
        print(f'start {self.uuid} walker task')
        for root, dirs, files in os.walk(self.start):
            md = (file for file in files if file.endswith('.md'))
            # print(f'processing {root} found {files.__len__()} md-files')
            self.mdQueue.put({'root': root, 'files': md})
        self.mdQueue.put(FINISH)
        print(f'finish {self.uuid} walker task')


class MdParser(threading.Thread):
    def __init__(self, mdQueue: queue.Queue):
        super().__init__()
        self.mdQueue = mdQueue
        self.filter = set()
        self.counter = 0
        self.multiplexor = 1
        self.bloom = BloomFilter(size=150000, fp_prob=1e-6)

    @staticmethod
    def parse_md_to_text(file_path) -> []:
        with open(file_path, 'r') as file:
            markdown_string = file.read()
            # convert md to html
            html = markdown.markdown(markdown_string)
            soup = BeautifulSoup(html, features="html.parser")
            # get text from html
            text = soup.get_text()
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            return chunks

    def parse_lines(self, lines):
        vals = []
        for line in lines:
            words = (part.strip().lower() for word in word_tokenize(line) for part in word.split("."))
            for word in words:
                if len(word) < 3 or not word.isalpha() or word in self.bloom:
                    continue

                self.bloom.add(word)
                if word not in self.filter and word.isalnum():
                    self.filter.add(word)
                    self.counter += 1
                    data = {
                        "id": str(self.counter),
                        "key": word
                    }
                    vals.append(str(json.dumps(data, ensure_ascii=False)))

        with open("./dictionary/dictionary.json", "a", encoding="utf8") as dictionary:
            for val in vals:
                dictionary.write(val)
                dictionary.write(',\n')

    def run(self) -> None:
        value = None
        while value != FINISH:
            while not self.mdQueue.empty():
                value = self.mdQueue.get()
                if value != FINISH:
                    root = value['root']
                    files = value['files']
                    for file in files:
                        lines = self.parse_md_to_text(f'{root}/{file}')
                        self.parse_lines(lines)

        with open("./dictionary/dictionary.json", "a", encoding="utf8") as dictionary:
            dictionary.write(']')
