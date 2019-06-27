
import urllib2
import BeautifulSoup

request = urllib2.Request("http://www.gpsbasecamp.com/national-parks")
response = urllib2.urlopen(request)
soup = BeautifulSoup.BeautifulSoup(response)
for a in soup.findAll('a'):
  if 'national-park' in a['href']:
    print ('found a url with national-park in the link')