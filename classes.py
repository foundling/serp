import scrapy
''' OOP Basics
    motivation: why use OOP?
        - structured code: data and functions bound together in one place
        - re-usable code: take a base class and extend it.
    applications:
        - game development. extremely complex and parallel operations going on.
        OOP makes the logic easier to handle.
    downsides:
        - inheritance can be easy to get wrong (Liskov Substitution Principle)
            - the point: If you replace the parent with the child, functionality should still work.
        - have to be aware of entire object inheritance context 
'''

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)

class Employee:
    pass

class Developer:
    pass

class Manager:
    pass