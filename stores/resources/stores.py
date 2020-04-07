from flask_restful import Resource


class StoresResource(Resource):
    def get(self):
        return {"message": "Success"}