import scrapy

from vintourage.models import Category

class CategorySpider(scrapy.Spider):
    category_mapping = None
    start_urls = []

    def __init__(self, category=None, *args, **kwargs):
        if not category:
            return

        if not self.category_mapping:
            raise Exception('Spider has to implement categories mapping')

        print("------------------------")
        print(category)
        print(category.value)

        self.start_urls = self.category_mapping.get(category)
        if not self.start_urls:
            raise ValueError(f"{type(self).__name__} must have a proper category_mapping")

        print(self.start_urls)

        category = Category.query.filter_by(path=category.value).first()
        if not category:
            raise Exception(f'There is no category matching the path {category}')
        self.category = category

        print("Got category")
        print(self.category)
        super().__init__(*args, **kwargs)

    def parse(self, request):
        returned_item = super().parse(self, request)

        if isinstance(returned_item, dict):
            returned_item.update({
                "category_id": self.category.id
            })

        yield returned_item