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
                            
                            