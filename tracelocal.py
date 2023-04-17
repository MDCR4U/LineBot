import json

import urllib.request   

    
url = "https://mdcgenius.000webhostapp.com/json/c000.json"
print(url)
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
print(data)
js_dta = json.load(data)
print(js_dta)
image_url  = js_dta["image"]   
alt_text   = js_dta["alt_text"]
print(alt_text)
print(js_dta["title"])
title      = js_dta["title"]
text0      = js_dta["text0"]
label1     = js_dta["label1"]
label2     = js_dta["label2"]
 
url1       = js_dta["url1"]
text2      = js_dta["text2"]