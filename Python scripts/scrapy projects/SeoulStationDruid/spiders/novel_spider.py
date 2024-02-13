import scrapy

class novel_crawler(scrapy.Spider):
    name ='novel_crawler'
    start_urls = ['https://wuxiarealm.com/seoul-station-druid/seoul-station-druid-chapter-1']

    for i in range(2,401,1):
        start_urls.append("https://wuxiarealm.com/seoul-station-druid/seoul-station-druid-chapter-"+str(i)+"")

    def parse(self,response):

        post_cont =  response.xpath("//div[@class='post-body entry-content float-container']//text()").extract()
        title = response.xpath("//h3[@class='post-title mb-4 font-weight-bold']/text()").extract()
        
        
        file_name=f'{title}.txt'
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(' '.join(post_cont))
        self.log(f'Saved file {file_name}')
        # yield {
        #     'title':title,
        #     'post' : post_cont,
        # }
