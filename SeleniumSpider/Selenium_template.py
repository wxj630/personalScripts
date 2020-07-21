# Selenium爬取网易云音乐评论
# https: // blog.csdn.net / weixin_41169182 / java / article / details / 100864763
# https://github.com/wxj630/team-learning/tree/master/01%20%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80%E4%B8%8E%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/%E7%BC%96%E7%A8%8B%E5%AE%9E%E8%B7%B5%EF%BC%88Python%20%E7%88%AC%E8%99%AB%EF%BC%89

from selenium import webdriver


# 禁止加载图片
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

# 设为无头模式
options.add_argument('-headless')

driver = webdriver.Chrome(options=options)
url = 'https://music.163.com/#/song?id=29343376'  # 歌曲页面的URL地址
driver.get(url)
driver.implicitly_wait(1)  # 显式等待1秒
driver.switch_to.frame('contentFrame')  # 切入contentFrame

comments_list = []

for i in range(10):  # 爬取评论的页数
    next_button = driver.find_element_by_xpath('//*[@class="m-cmmt"]/div[3]/div/a[11]')  # 找到下一页的按钮
    comments = driver.find_elements_by_xpath('//*[@class="m-cmmt"]/div[2]/div/div[2]/div[1]/div')  # 找到评论
    for item in comments:
        index = item.text.index('：') + 1
        comment = item.text[index:]  # 解析评论
        print(comment)
        comments_list.append(comment)
    driver.execute_script("arguments[0].click();", next_button)  # 触发next_button的JS进入下一页评论

print(comments_list)



