# 简介：自动获取GitHub相关的IP地址，保存到hots文件，解决GitHub无法显示图片问题
# 需要安装requests、BeautifulSoup库，bs4模块、lxml模块
# 更新：2020/08/21
# 140.82.114.4   github.com
# 140.82.114.3   gist.github.com
# 185.199.108.153   assets-cdn.github.com
# 199.232.68.133   raw.githubusercontent.com
# 199.232.68.133   gist.githubusercontent.com
# 199.232.68.133   cloud.githubusercontent.com
# 199.232.68.133   camo.githubusercontent.com
# 199.232.68.133   avatars0.githubusercontent.com
# 199.232.68.133   avatars1.githubusercontent.com
# 199.232.68.133   avatars2.githubusercontent.com
# 199.232.68.133   avatars3.githubusercontent.com
# 199.232.68.133   avatars4.githubusercontent.com
# 199.232.68.133   avatars5.githubusercontent.com
# 199.232.68.133   avatars6.githubusercontent.com
# 199.232.68.133   avatars7.githubusercontent.com
# 199.232.68.133   avatars8.githubusercontent.com
import requests
from bs4 import BeautifulSoup


def run():
    urls = [
     {'github.com': 'https://github.com.ipaddress.com/'},
     {'gist.github.com': 'https://github.com.ipaddress.com/gist.github.com'},
     {'assets-cdn.github.com': 'https://github.com.ipaddress.com/assets-cdn.github.com'},
     {'raw.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/raw.githubusercontent.com'},
     {'gist.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/gist.githubusercontent.com'},
     {'cloud.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/cloud.githubusercontent.com'},
     {'camo.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/camo.githubusercontent.com'},
     {'avatars0.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/avatars0.githubusercontent.com'},
     {'avatars1.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/avatars1.githubusercontent.com'},
     {'avatars2.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/avatars2.githubusercontent.com'},
     {'avatars3.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/avatars3.githubusercontent.com'},
     {'avatars4.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/avatars4.githubusercontent.com'},
     {'avatars5.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/avatars5.githubusercontent.com'},
     {'avatars6.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/avatars6.githubusercontent.com'},
     {'avatars7.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/avatars7.githubusercontent.com'},
     {'avatars8.githubusercontent.com': 'https://githubusercontent.com.ipaddress.com/avatars8.githubusercontent.com'}
    ]

    for url in urls:
        for u in url:
            wb_data = requests.get(url[u])
            wb_data = wb_data.text

            soup = BeautifulSoup(wb_data, 'lxml')
            ips = soup.select('ul.comma-separated li')
            for i, ip in enumerate(ips):
                if i == 0:
                    print(ip.get_text() + '   ' + u)


if __name__ == '__main__':
    run()
