import requests

def unshorten_url(url):
    return requests.head(url, allow_redirects=True).url

url = input("Enter the shortened URL: ")
a = unshorten_url(url)
print("Original URL is: {}".format(a))
