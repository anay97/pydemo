import sys
import json
a=int(sys.argv[1])
b=int(sys.argv[2])

data={}
data['sum']=str(a+b)
data['diff']=str(a-b)
data['prod']=str(a*b)
data['quotient']=str(a/b)
json_data=json.dumps(data)
print(json_data)
sys.stdout.flush()

