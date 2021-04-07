import os
from argparse import ArgumentParser
from lib.document import Document
from lib.tags import Tags

def is_file_valid(parser, arg):
    if not os.path.exists(arg):
        parser.error(f'The file {arg} does not exist')
    else:
        return arg

def main():
    parser = ArgumentParser(description='Tag files')
    parser.add_argument('file', help='File to tag', type=lambda file: is_file_valid(parser, file))
    parser.add_argument('-t', '--tags', help='Add tags to file')
    parser.add_argument('-e', '--edit', help='Edit tags for file', action='store_true')
    parser.add_argument('--list', help='List all tags', action='store_true')

    doc = Document(parser.parse_args().file)

    if parser.parse_args().edit:
        if parser.parse_args().tags:
            doc.edit(parser.parse_args().tags)
        else:
            print('Add -t to edit tags')
    else:
        doc.add(tags=parser.parse_args().tags)

    if parser.parse_args().list:
        tags = Tags()
        print(tags.get('database'))

    doc.save_to_db()

if __name__ == '__main__':
    main()