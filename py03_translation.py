import urllib.request
import urllib.parse
import json

# 1,访问目标的url
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index"

# 2,表单数据
data = {}

#    type:AUTO
#    i:hello
#    doctype:json
#    xmlVersion:1.8
#    keyfrom:fanyi.web
#    ue:UTF-8
#    action:FY_BY_CLICKBUTTON
#    typoResult:true

data["type"] = "AUTO"
#  data["i"] = "hello" 为例
data["i"] = input("请输入你想翻译的文字或句子：")
data["doctype"] = "json"
data["xmlVersion"] = "1.8"
data["keyfrom"] = "fanyi.web"
data["ue"] = "UTF-8"
data["action"] = "FY_BY_CLICKBUTTON"
data["typoResult"] = "true"

# 3,把表单数据加密成标准格式，并加密为utf-8编码
data = urllib.parse.urlencode(data).encode("utf-8")

# 4,持data数据访问url，拿到返回的二进制数据
response = urllib.request.urlopen(url,data)

# 5,读取二进制数据并解密为utf-8编码
html = response.read().decode("utf-8")

#  print(html) 返回 json数据

#    {"type":"EN2ZH_CN","errorCode":0,"elapsedTime":0,"translateResult":[[{"src":"hello","tgt":"你好"}]],
#"smartResult":{"type":1,"entries":["","n. 表示问候， 惊奇或唤起注意时的用语","int. 喂；哈罗","n. (Hello)人名；(法)埃洛"]}}


# 6,json.loads(html) 返回 字典
mydict = json.loads(html)

#    {'smartResult': {'type': 1, 'entries': ['', 'n. 表示问候， 惊奇或唤起注意时的用语', 'int. 喂；哈罗', 'n. (Hello)人名；(法)埃洛']},
#    'type': 'EN2ZH_CN', 'errorCode': 0, 'elapsedTime': 0, 'translateResult': [[{'src': 'hello', 'tgt': '你好'}]]}

# 7,取到列表
mylist = mydict["translateResult"]

#  [[{'src': 'hello', 'tgt': '你好'}]]

# 8,取到列表中字典
include_dict = mylist[0][0]

#  {'src': 'hello', 'tgt': '你好'}

# 9,取到数据并显示
src = include_dict["src"]
tgt = include_dict["tgt"]
print("%s 的翻译结果为：%s" % (src , tgt))


