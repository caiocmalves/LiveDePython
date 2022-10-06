from os.path import exists

def read_file(file):
    try:
        return open(file)
    except FileNotFoundError:
        raise FileNotFoundError(f'O arquivo {file} não existe')
    
read_file('xpto')