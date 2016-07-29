import urllib2

def fetch_html(url):
    html = urllib2.urlopen(url).read()
    return html

def get_title(html):
    title_start = html.find('<title>')
    title_end = html.find('</title', title_start)
    title = html[title_start+7: title_end]
    return title

urls= ['http://en.wikipedia.org/',
'http://www.google.com/'
]
for url in urls:
    html = fetch_html(url)
    print get_title(html)
