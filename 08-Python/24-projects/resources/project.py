from flask import jsonify
from flask_restful import Resource, reqparse, inputs
from sqlalchemy import Integer, String

from models.projects import ProjectModel
from resources.projects import new_project_parser

project_parser = new_project_parser.copy()
project_parser.add_argument('id',
                            type=Integer,
                            required=True,
                            help='Invalid Data'
                            )

project_parser.add_argument('title',
                            type=String,
                            required=True,
                            help='Invalid Data'
                            )

project_parser.add_argument('createdAt',
                            type=inputs.datetime_from_rfc822,
                            required=True,
                            help='Invalid Data'
                            )

class Project(Resource):
    def get(slef, id):
        project_from_db = ProjectModel.get_by_id(id)
        return jsonify(project_from_db.to_json())
    
    def put(self, id):
        project_to_update = project_parser.parse_args(id)
        project_from_db = ProjectModel.get_by_id(id)
        project_from_db.title = project_to_update['title']
        project_from_db.save()
        return jsonify(project_from_db.to_json())                           
                            