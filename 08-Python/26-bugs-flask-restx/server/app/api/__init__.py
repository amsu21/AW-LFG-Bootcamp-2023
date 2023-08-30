from flask_restx import Api

from app.api.bugs.views import bugs_namespace

api = Api(version="1.0", title="Flask API", doc="/api/v1/docs")
api.add_namespace(bugs_namespace, path="/api/v1/bugs")
