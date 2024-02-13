import scrapy
import string

class novel_crawler(scrapy.Spider):
    name ='novel_crawler'
    start_urls = ['https://wuxiarealm.com/solo-max-level-newbie/solo-max-level-newbie-chapter-1/']

    for i in range(2,407,1):
        start_urls.append("https://wuxiarealm.com/solo-max-level-newbie/solo-max-level-newbie-chapter-"+str(i)+"")

    def parse(self,response):

        post_cont =  response.xpath("//div[@class='post-body entry-content float-container']//text()").extract()
        title = response.xpath("//h3[@class='post-title mb-4 font-weight-bold']/text()").extract()
        
        
        file_name=f'{title}.txt'
        file_name = file_name.translate({ord(c): None for c in '[]"''"'})
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(' '.join(post_cont))
        self.log(f'Saved file {file_name}')
        # yield {
        #     'title':title,
        #     'post' : post_cont,
        # }
