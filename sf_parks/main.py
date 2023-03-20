import argparse
from .db import create_db_and_tables, teardown_db
from .data import insert_into_db, insert_all_data, data_dict, data_models_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', '--database')
    parser.add_argument('--d', '--data')
    args = parser.parse_args()

    if args.db is not None:
        if args.db == 'create':
            print('Creating database and tables.')
            create_db_and_tables()
        elif args.db == 'destroy':
            print('Tearing down database.')
            teardown_db()
        else:
            raise ValueError(
                f'Argument to --db or --database must be either `create` or `destroy` not {args.db}.'
                )
    if args.d is not None:
        if args.d.lower() == 'all':
            insert_all_data()
        if args.d in data_dict:
            dataset = data_dict.get(args.d)
            model = data_models_dict.get(args.d)
            insert_into_db(dataset, model)