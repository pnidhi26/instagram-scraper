# PRAKASH NIDHI VERMA
# CODEMARKET


# importing all the required libraries
import requests
import re
import json
import csv
from bs4 import BeautifulSoup


# Creating a class
class Insta_Info_Scraper:

    def getinfo(self, url):
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        data = soup.find_all('meta', attrs= {'property':'og:description'})
        text = data[0].get('content').split()
        user = '%s %s %s %s' % (text[-4], text[-3], text[-2], text[-1])

        followers = text[0]
        following = text[2]
        posts = text[4]

        data = soup.find('script', attrs={'type': 'application/ld+json'}).get_text
        
        data = str(data)
        email = re.findall(r'[\w\.-]+@[\w\.-]+', data)

        print ('User:', user)
        print ('Followers:', followers)
        print ('Following:', following)
        print ('Posts:', posts)
        print ('Email:', email)
        print ('--------------Scraping completed!-----------------')
        self.email.append(email)


# reading the usres id and urls
    def main(self):
        self.email = []
        with open('users.txt') as f:
            self.content = f.readlines()
        self.content = [x.strip() for x in self.content]
        for url in self.content:
            self.getinfo(url)
        self.generate_csv()


# colleting all the mails id into csv file
    def generate_csv(self):
        with open('email.csv', 'w', newline='') as file:
            file_write = csv.writer(file)
            file_write.writerow(["e-mails"])
            for email in self.email:
                file_write.writerow(email)


if __name__ == '__main__':
    obj = Insta_Info_Scraper()
    obj.main()