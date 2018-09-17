
from urllib import request
import json
import os

url = "http://52.71.186.103:19999/api/v1/data?chart=system.load"

req = request.urlopen(url)
encoding = req.headers.get_content_charset()
j = json.loads(req.read().decode(encoding))

if os.path.exists("netdata_systemload.json"):
    append_write = 'r' # append if already exists
else:
    append_write = 'w' # make a new file if not

f=open("netdata_systemload.json",append_write)
if (append_write=='w'):
	j=json.dumps(j)
	f.write(j)
else:
	temp_dict=json.load(f)
	#print(temp_dict)
	try:
		merge_index=j["data"].index(temp_dict["data"][0])
		j["data"]=j["data"][:merge_index]+temp_dict["data"]

	except:
		j["data"]=j["data"]+temp_dict["data"]
	print("new data length: " + str( len(j["data"])))
	d=open("netdata_systemload.json","w")
	j=json.dumps(j)
	d.write(j)
	d.close()

	

f.close()


