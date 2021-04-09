import pathlib
import os
from backend.utils import calculate_hash
from backend.database import init_db, Files, session
from sqlalchemy.exc import IntegrityError

class Document:
    def __init__(self, file_name, file_hash=None):
        self.file_name = file_name
        if not file_hash:
            self.file_hash = calculate_hash(file_name)
        else:
            self.file_hash = file_hash
        self.file_path = pathlib.Path(file_name).resolve().parent.as_posix()

        db = init_db()
        self.session = session(db)
    
    def add(self, tags=None):
        new_file = Files(file_name=os.path.basename(self.file_name), file_hash=self.file_hash, file_path=self.file_path, tags='')
        if tags:
            new_file.add_tags(tags)
        self.session.add(new_file)

    def edit(self, tags):
        edit_file = self.session.query(Files).filter_by(file_hash=self.file_hash).first()
        if edit_file:
            edit_file.tags = tags
        else:
            print("File does not exist in database")

    def remove(self):
        file = self.session.query(Files).filter_by(file_hash=self.file_hash).first()
        self.session.delete(file)

    def save_to_db(self):
        try:
            self.session.commit()
        except IntegrityError as error:
            self.session.rollback()
            if 'UNIQUE constraint failed:':
                print('File already exists in database')
            else:
                print('Unknown error occured: ' + error)
            