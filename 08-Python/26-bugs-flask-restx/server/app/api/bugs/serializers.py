from flask_restx import reqparse

post_bug_serializer = reqparse.RequestParser()
post_bug_serializer.add_argument("name", required=True)
post_bug_serializer.add_argument("is_closed", required=True)
post_bug_serializer.add_argument("created_at", required=True)