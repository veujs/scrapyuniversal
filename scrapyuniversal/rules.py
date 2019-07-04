from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = (
    # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    Rule(LinkExtractor(allow=r'article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]')
         , callback='parse_item'),
    Rule(LinkExtractor(restrict_xpaths='//div[@id="page_Style"]//a[contains(.,"下一页")]')),
)
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import Rule
#
# rules = {
#     "china": (
#         Rule(LinkExtractor(allow='article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
#              callback='parse_item'),
#         Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]')),
#     )
# }




