import requests
import time

# rt = requests.get('http://www.zhidaow.com')  # 发送请求
# print(rt.status_code)# 返回码
# print(rt.headers['content-type'] )# 返回头部信息
# print(rt.encoding)# 编码信息
# print(rt.text)  #内容部分（PS，由于编码问题，建议这里使用r.content）


# payload = {'wd': '张三', 'rn': '100'}
# re=requests.get('http://www.baidu.com/s',payload)
# print(re.text)

t1 = time.time()
print(t1)
for i in range(0, 100):

    r = requests.get('https://www.52mylife.cn/xhz')
    if r.status_code == 200:
        print('第', i + 1, '次 request ', r.status_code, 'successful')
    else:
        print('第', i + 1, '次 request ', r.status_code, 'error')

t2 = time.time()
t3 = t2 - t1
print('QPS:', (100 / t3), '用时', t3)
