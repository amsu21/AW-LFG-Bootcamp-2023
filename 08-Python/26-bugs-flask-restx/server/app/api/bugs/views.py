from flask_restx import Namespace, Resource, fields
from structlog import get_logger

from app.api.bugs.crud import (
    get_all_bugs,
    get_bug_by_id,
    create_bug,
    update_bug,
    delete_bug
)

from app.api.bugs.serializers import post_bug_serializer

logger = get_logger(__name__)

bugs_namespace = Namespace("bugs")

# VIEW MODEL
bug = bugs_namespace.model(
    "Bug",
    {
        "id": fields.Integer(readonly=True),
        "name": fields.String(required=True),
        "is_closed": fields.Boolean(required=True)
    },
)

class BugsList(Resource):
    pass