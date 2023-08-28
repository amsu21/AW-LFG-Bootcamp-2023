from flask import jsonify
from flask_restful import Resource, reqparse, inputs

from models.projects import ProjectModel

new_project_parser = reqparse.RequestParser()
new_project_parser.add_argument('name',
                                type=str,
                                help='The field cannot be blank',
                                required=True)

class Projects(Resource):
    def get(self):
        return jsonify([project.to_json() for project in ProjectModel.get_all()])
    
    def post(self):
        new_project = new_project_parser.parse_args()
        new_project_model = ProjectModel(**new_project)
        new_project_model.save()
        return jsonify(new_project_model.to_json())