import sys
from scrapy.utils.project import get_project_settings
from scrapyuniversal.spiders.universal import UniversalSpider
from scrapyuniversal.utils import get_config
from scrapy.crawler import CrawlerProcess

def run():
    name = sys.argv[1]
    print(name)
    custom_settings = get_config(name)
    spider = custom_settings.get('spider', 'universal')
    print(spider)

    rules = custom_settings.get('rules')
    print("rules: %s " % rules)

    project_settings = get_project_settings()
    print(project_settings)

    settings = dict(project_settings.copy())
    print(settings)

    settings.update(custom_settings.get('settings'))

    print(settings)

    process = CrawlerProcess(settings)
    print("######################################################################process is: %s " % process)
    # c = process.crawl(spider, **{'name': name})
    c = process.crawl(UniversalSpider, **{'name': name})
    print("######################################################################processrrrrr is: %s " % c)

    process.start()
    print("######################################################################process iseeeeeeee: %s " % process)


if __name__ == '__main__':
    run()

