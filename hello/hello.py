"""Hello World in Fortran or Python."""
from subprocess import Popen, PIPE
from os import chdir, getcwd
from os.path import dirname


def hello(language):
    language = language.lower()
    assert language in ['python', 'fortran']
    if language.lower() == 'python':
        print('Hello World. I am Python.')
    elif language == 'fortran':
        exec_dir = dirname(__file__)
        old_dir = getcwd()
        chdir(exec_dir)
        message, err = Popen('./hello', stdout=PIPE).communicate()
        chdir(old_dir)
        message = message.decode('utf-8').lstrip(' ')
        print(message)

