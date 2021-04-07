from backend.database import init_db, Files, session
from backend.utils import flatten

class Tags:
    def __init__(self):
        db = init_db()
        self.session = session(db)

    def get(self, tag):
        tag = self.session.query(Files).filter(Files.tags.like("%" + tag + "%")).all()
        return tag
    
    def get_all(self):
        tags = self.session.query(Files.tags).all()
        out = [item.split(',') for t in tags for item in t]
        comma_separated = ", ".join(set(flatten(out)))
        return comma_separated
