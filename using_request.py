import urllib3

#without using poolmanager
resp = urllib3.request("GET", "https://www.google.com")
print(resp.status)