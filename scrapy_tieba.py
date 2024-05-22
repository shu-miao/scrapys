import requests
import time
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    try:
        r = requests.get(url,headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "


def get_content(url):
    comments = []

    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')
    # print('soup:',soup)

    liTags = soup.find_all('li', attrs={'class': 'j_thread_list clearfix thread_item_box'})

    print('liTags:',liTags)

    for li in liTags:

        comment = {}

        try:
            comment['title'] = li.find(
                'div', attrs={'class': 'threadlist_title pull_left j_th_tit '}).text.strip()
            print('t:',comment['title'])
            comment['body'] = li.find(
                'a', attrs={'class': 'j_th_tit'}).text.strip()
            comment['link'] = "http://tieba.baidu.com/" + \
                              li.find('a', attrs={'class': 'j_th_tit '})['href']
            comment['name'] = li.find(
                'span', attrs={'class': 'tb_icon_author '}).text.strip()
            comment['time'] = li.find(
                'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comments.append(comment)
            print('comments:',comments)
        except:
            print('筛选失败')

    return comments


def Out2File(dict):
    with open('ruozhi.txt', 'a+') as f:
        for comment in dict:
            f.write('标题： {} \t 内容： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \n'.format(
                comment['title'], comment['body'], comment['link'], comment['name'], comment['time']))

        print('爬取完成')


def main(base_url, deep):
    url_list = []
    # 将所有需要爬去的url存入列表
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    # print('所有的网页已经下载到本地！ 开始筛选信息')

    # 循环写入所有的数据
    for url in url_list:
        content = get_content(url)
        Out2File(content)
    print('保存完毕！')


url = 'https://tieba.baidu.com/f?kw=%E5%BC%B1%E6%99%BA&ie=utf-8'
deep = 1

if __name__ == '__main__':
    main(url, deep)
