import pathlib
a = pathlib.Path('.')
for pf in a.glob('a*'):
    if pf.is_dir():
        print(pf)

