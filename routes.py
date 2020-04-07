from flask_restful import Api
from stores.resources.stores import StoresResource


def configure_routes(api: Api):
    api.add_resource(StoresResource, "/stores")

