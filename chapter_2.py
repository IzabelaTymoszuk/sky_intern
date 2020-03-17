import argparse
import sqlite3
from datetime import datetime
from sqlite3 import Error

conn = sqlite3.connect('example.db')
try:
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists task_list (name text, deadline text, description text, task_hash text)''')
    conn.commit()
except Error as e:
    print(e)

parser = argparse.ArgumentParser(prog='task', description='Simple task manager.')
subparsers = parser.add_subparsers(help='Commands')
parser_add = subparsers.add_parser('add', help='Add a new task')
parser_update = subparsers.add_parser('update', help='Update task')
parser_remove = subparsers.add_parser('remove', help='Remove some task')
parser_list = subparsers.add_parser('list', help='Display all tasks')


def func_add(args):
    """Add values to the database."""

    name = getattr(args, 'name')
    deadline = getattr(args, 'deadline')
    description = getattr(args, 'description')
    task_hash = hash(name)
    try:
        c.execute(f"INSERT INTO task_list VALUES ('{name}','{deadline}','{description}', {task_hash})")
        conn.commit()
        print(f"Your hash is: {task_hash}")
    except Error as e:
        print(e)


def func_update(args):
    """Update values in the database."""

    name = getattr(args, 'name')
    deadline = getattr(args, 'deadline')
    description = getattr(args, 'description')
    task_hash = getattr(args, 'task_hash')
    try:
        if name:
            new_name = f"Update task_list set name = '{name}' WHERE task_hash = '{task_hash}'"
            c.execute(new_name)
        if deadline:
            new_deadline = f"Update task_list set deadline = '{deadline}' WHERE task_hash = '{task_hash}'"
            c.execute(new_deadline)
        if description:
            new_description = f"Update task_list set description = '{description}' WHERE task_hash = '{task_hash}'"
            c.execute(new_description)
        conn.commit()
        print('Task successfully updated')
    except Error as e:
        print(e)


def func_remove(args):
    """Remove values from the database."""

    task_hash = getattr(args, 'task_hash')
    try:
        c.execute(f"DELETE FROM task_list WHERE task_hash = '{task_hash}'")
        conn.commit()
        print("Task removed successfully")
    except Error as e:
        print(e)


def func_list(args):
    """Show the list of all tasks or tasks planned for today"""

    date = getattr(args, 'date')
    try:
        if date == 'all':
            c.execute(f"SELECT * FROM task_list")
        elif date == 'today':
            today = datetime.now().strftime('%d/%m/%Y')
            c.execute(f"SELECT * FROM task_list WHERE deadline = '{today}' ")
        conn.commit()
        print(c.fetchall())
    except Error as e:
        print(e)


parser_add.add_argument('--name', required=True, action='store', default='',
                        help='Add name task')
parser_add.add_argument('--deadline', action='store', default='',
                        help='Add deadline task in format day/month/year')
parser_add.add_argument('--description', action='store', default='',
                        help='Add description task')
parser_add.set_defaults(func=func_add)

parser_update.add_argument('--name', help='Update name task')
parser_update.add_argument('--deadline', help='Update deadline task in format day/month/year')
parser_update.add_argument('--description', help='Update description task')
parser_update.add_argument('task_hash', help='Update task hash')
parser_update.set_defaults(func=func_update)

parser_remove.add_argument('task_hash', help='Remove task')
parser_remove.set_defaults(func=func_remove)

parser_list.add_argument('date', choices=['all', 'today'], help='')
parser_list.set_defaults(func=func_list)

args = parser.parse_args()
args.func(args)
conn.close()
