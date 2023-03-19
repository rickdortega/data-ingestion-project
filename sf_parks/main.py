import argparse
from .db import create_db_and_tables, teardown_db
from .data import insert_into_db, insert_all_data, data_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', '-database')
    parser.add_argument('-d', '-data')
    args = parser.parse_args()

    if args.db is not None:
        if args.db == 'create':
            print('Creating database and tables.')
            create_db_and_tables()
        elif args.db == 'destroy':
            teardown_db('Tearing down database.')
        else:
            raise ValueError(
                f'Argument to --db or --database must be either `create` or `destroy` not {args.db}.'
                )
    if args.d is not None:
        if args.d.lower() == 'all':
            insert_all_data()
        if args.d in data_dict:
            model = data_dict.get(args.d)
            insert_into_db(args.d, model)

    if args.command == 'create':
        create_db_and_tables()
    elif args.command == 'destroy':
        teardown_db()
    else:
        raise ValueError(f'Command passed to db.py must be one of `create` or `destroy` not {args.command}')