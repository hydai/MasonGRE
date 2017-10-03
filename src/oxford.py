import requests
import json
import time
from config import app_id, app_key, api_url


class QueryBuilder():
    def __init__(self, url):
        self.base_url = url

    def entries(self, word_id):
        return ''.join([self.base_url,
                        '/entries/en/',
                        word_id.lower()])


class Oxford():
    def __init__(self):
        self.query_builder = QueryBuilder(api_url)

    def query_entries(self, word_id):
        print("=============================================")
        print("WORD {} START.", word_id)
        url = self.query_builder.entries(word_id)
        r = requests.get(url,
                         headers={
                             'app_id': app_id,
                             'app_key': app_key})

        if int(r.status_code) == 200:
            with open('./words/'+word_id+'.entries', 'w') as writter:
                writter.write(r.text)
                print("WORD {} DONE.", word_id)
        else:
            print("WORD {} FAILED.", word_id)


def main():
    oxford = Oxford()
    with open('./wordlist/mason1000.txt') as f:
        for word in f:
            oxford.query_entries(word.strip())
            time.sleep(1)

if __name__ == '__main__':
    main()
