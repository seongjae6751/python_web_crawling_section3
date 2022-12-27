import json
import requests

s = requests.Session()

r = s.get('http://httpbin.org/stream/20', stream = True)
# print(r.text)
print(r.encoding)
# print(r.json())
if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True): # 해당 iterater를 순회하면서 유니코드를 디코딩한다는 뜻
    # print(line) 
    b = json.loads(line)
    for e in b.keys():
        print('key:', e, 'values :', b[e])





























