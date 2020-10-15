from flask_restful import Resource, request
from models import User
import json


class UserResource(Resource):

    def get(self, user_id=None):
        if user_id:
            data_result = User.objects.get(id=user_id)
        else:
            data_result = User.objects()
        data_result = json.loads(data_result.to_json())
        return data_result

    def post(self):
        user = User.objects.create(**request.json)
        return json.loads(user.to_json())

    def put(self, user_id):
        user = User.objects(id=user_id)
        user.update(**request.json)
        return json.loads(user.to_json())

    def delete(self, user_id):
        user = User.objects(id=user_id)
        user.delete()
        return json.loads(user.to_json())