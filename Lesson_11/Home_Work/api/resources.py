from flask_restful import Resource, request
import json
from Lesson_11.Home_Work.models.models import Product, Category


class ProductResource(Resource):

    def get(self, product_id=None):
        if product_id:
            data_result = Product.objects.get(id=product_id)
            data_result.increase_views()
        else:
            data_result = Product.objects()
        data_result = json.loads(data_result.to_json())
        return data_result

    def post(self):
        product = Product.objects.create(**request.json)
        return json.loads(product.to_json())

    def put(self, product_id):
        product = Product.objects(id=product_id)
        product.update(**request.json)
        return json.loads(product.to_json())

    def delete(self, product_id):
        product = Product.objects(id=product_id)
        product.delete()
        return json.loads(product.to_json())


class CategoryResource(Resource):

    def get(self, category_id=None):
        if category_id:
            data_result = Category.objects.get(id=category_id)
        else:
            data_result = Category.objects()
        data_result = json.loads(data_result.to_json())
        return data_result

    def post(self):
        category = Category.objects.create(**request.json)
        return json.loads(category.to_json())

    def put(self, category_id):
        category = Category.objects(id=category_id)
        category.update(**request.json)
        return json.loads(category.to_json())

    def delete(self, category_id):
        category = Category.objects(id=category_id)
        category.delete()
        return json.loads(category.to_json())


class TotalPriceResources(Resource):

    def get(self):
        all_products = Product.objects()
        total_price = 0
        for product in all_products:
            total_price += product.price
        return total_price
