# sky_intern

The project consists of three chapters each in a separate file.


### Prerequisites

- Python 3.7.3

### Chapter 1

I use this code for test class Car:

```python
c = Car(2, 1300, 4)
print(c)
c.pax_count = 6
print(c)
d = Car(8, 2300, 6)
print(d)
```

To run type this:
```bash
python chapter_1.py
```

### Chapter 2

You can use this commands in terminal to manage tasks. The sqlite3 database create automatically.

```bash
python chapter_2.py add --name Coding [--deadline DATETIME('dd/mm/YYYY')] [--description DESCRIPTION]
python chapter_2.py update [--name Cooking] [--deadline DATETIME('dd/mm/YYYY')] [--description DESCRIPTION] TASK_HASH
python chapter_2.py remove TASK_HASH
python chapter_2.py list [all | today]
```

### Chapter 3

Chapter 3 has 935 solutions.

To run type this:
```bash
python chapter_3.py
```

