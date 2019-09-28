from requests_html import HTMLSession

session = HTMLSession()

url = "http://www.247wallst.com/special-report/2017/07/19/states-with-the-most-and-least-cat-owners/amp/"

r = session.get(url)

print(r.text)
