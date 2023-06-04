import urllib3
import typing 

#using poolmanager
http = urllib3.PoolManager()

resp = http.request("GET", "https://www.google.com")
print(resp.status)
print(resp.data)