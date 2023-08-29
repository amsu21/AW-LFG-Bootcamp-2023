from typing import List, Union

from structlog import get_logger

from app import db
from app.api.bugs.models import Bug

logger = get_logger(__name__)

# GET
def get_all_bugs() -> List[Bug]:
    # RETURNS LL BUGS
    logger.debug("get_all_bugs")
    return Bug.query.all()

# GET BY ID
def get_bug_by_id(id: int) -> Bug:
    # RETURNS ONE BUG
    logger.debug("get_bug_by_id")
    return Bug.query.filter_by(id=id).first()

# CREATE
def create_bug(name: str, isClosed: bool, createdAt: date()) -> Bug:
    # CREATES A BUG
    logger.debug("create_bug")
    bug = Bug(name=name, isClosed=isClosed, createdAt=createdAt)
    db.session.add(bug)
    db.session.commit()
    return bug

# UPDATE
def update_bug(bug: Bug, name: str, isClosed: bool) -> Bug:
    # UPDATES A BUG
    logger.debug("update_bug")
    bug.name = name
    bug.is_closed = isClosed
    db.session.commit()
    return bug


def delete_bug(bug: Bug) -> Union[Bug, None]:
    """deletes a single movie"""

    logger.debug("delete_bug")
    db.session.delete(bug)
    db.session.commit()
    return bug