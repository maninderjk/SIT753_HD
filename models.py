import itertools
from utils import get_current_timestamp

_id_counter = itertools.count(1)

class Task:
    def __init__(self, name, status="running", created_at=None, updated_at=None, id=None):
        self.id = id or next(_id_counter)
        self.name = name
        self.status = status
        self.created_at = created_at or get_current_timestamp()
        self.updated_at = updated_at or self.created_at

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            name=data["name"],
            status=data["status"],
            created_at=data["created_at"],
            updated_at=data["updated_at"]
        )

