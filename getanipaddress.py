import bs4
import requests
res = requests.get('https://www.myip.com/')

res.text

soup = bs4.BeautifulSoup(res.text, 'lxml')

soup

ip = soup.find_all('span', {'id': 'ip'})
ip[0].getText()
my_ip = ip[0].getText()
print(my_ip)
