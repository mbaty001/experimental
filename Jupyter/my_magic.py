from IPython.core.magic import register_line_magic, register_cell_magic

@register_line_magic
def hello(line):
    if line == 'french':
        print("Salut tout le monde!")
    else:
        print("Hello world!")