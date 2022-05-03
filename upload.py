import requests

files = {'data': ('/Benchyyy.gcode', open('Benchyyy.gcode','r').read(),"application/octet-stream")}
r = requests.post("http://192.168.8.150:88/edit",files=files)

print(r.request.headers)
print(r.request.body.decode('ascii'))
