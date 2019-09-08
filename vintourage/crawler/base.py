import scrapy

from .models import Category

class CategorySpider(scrapy.Spider):
    category_mapping = None
    start_urls = []

    def __init__(self, category_path=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.category_mapping:
            raise Exception('Spider has to implement categories mapping')

        self.start_urls = self.category_mapping.get(category_path)
        if not self.start_urls:
            return

        category = Category.query.filter_by(path=category_path).first()
        if not category:
            raise Exception('There is no category matching the path %s', category_path)
        self.category = category

    def parse(self, request):
        returned_item = super().parse(self, request)

        if isinstance(returned_item, dict):
            returned_item.update({
                "category_id": self.category.id
            })

        yield returned_item