from flask import Flask
from flask_restful import Api
from Lesson_11.Home_Work.api.resources import ProductResource, CategoryResource, TotalPriceResources

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, '/products', '/products/<product_id>')
api.add_resource(CategoryResource, '/categories', '/categories/<category_id>')
api.add_resource(TotalPriceResources, '/total')

app.run(debug=True)