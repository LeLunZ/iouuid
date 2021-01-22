import random
import string

# copied long time ago from a stack overflow answer
from io import BytesIO, StringIO
from pathlib import Path


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_id(path, dir=False, **kwargs):
    file = path.stem
    parent_path = path.parent
    suffix = path.suffix
    id = ''
    while (parent_path / f'{file}{id}{suffix}').is_dir() if dir else (parent_path / f'{file}{id}{suffix}').is_file():
        id = id_generator(**kwargs)
    return f'{file}{id}{suffix}'


def io_mkdir(path, m='', **kwargs):
    if path is None:
        raise ValueError

    path = Path(path)
    name = generate_id(path, dir=True, **kwargs)
    (path.parent / name).mkdir()
    return


def io_writer(path, data=None, m='', **kwargs):
    if path is None:
        raise ValueError

    path = Path(path)
    fname = ''
    if data is None:
        raise ValueError
    if type(data) is str:
        mo = 'w'
    elif type(data) is bytes:
        try:
            data = data.decode()
            mo = 'w'
        except (UnicodeDecodeError, AttributeError):
            mo = 'wb'
    else:
        if type(data) is BytesIO:
            mo = 'wb'
        elif type(data) is StringIO:
            mo = 'w'
        else:
            raise ValueError
        if not (not hasattr(data, 'name') or data.name is None or data.name == ''):
            fname = data.name
        else:
            if not path.is_dir():
                fname = path.name
        data = data.read()

    name = generate_id(path / fname, **kwargs)

    if m == '':
        m = mo
    with open((path.parent / name) if fname == '' else (path / fname), m) as file:
        file.write(data)
    return
