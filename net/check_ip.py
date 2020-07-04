import requests, json, time

while True:
    r = requests.get("https://api.ipify.org?format=json")
    ip = json.loads(r.text)["ip"]
    r = requests.get("http://tb.ip4market.ru/?page=update&apikey=a268a7d7a11dfdb3580d1ddd7675e4d7&ip="+str(ip))
    print("Current ip is " + str(ip))
    time.sleep(600)
