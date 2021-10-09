import http.client
import json
from types import SimpleNamespace

cookie = ""

conn = http.client.HTTPSConnection("www.roblox.com")
conn.request("GET", "/mobileapi/userinfo", headers={"Cookie": f".ROBLOSECURITY={cookie}"})
resp = conn.getresponse()
data = resp.read()
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

print(f"UserName(Id) : {x.UserName}({x.UserID})")
print("RobuxBalance : " + str(x.RobuxBalance))
print("IsPremium:" + str(x.IsPremium))