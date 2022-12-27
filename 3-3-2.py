import requests, json

#Rest : POST(데이터를 보냄), GET(가져옴), PUT:UPDATE, REPLACE(FETCH:UPDATE, MODIFY), DELETE(삭제)

payload1 = {'key1':'value1','key2':'value2'} # 딕셔너리 
payload2 = (('key1','value1'),('key2','value2')) # 튜플
payload3 = {'some':'nice'}

# r = requests.put('http://httpbin.org/put', data=payload1)
# print(r.text)

# r = requests.put('https://jsonplaceholder.typicode.com/posts/1',data=payload1)
# print(r.text) 

r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)