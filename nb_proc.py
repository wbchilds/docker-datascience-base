from nbconvert import HTMLExporter
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

cwd = os.getcwd()
nb_dir = cwd+'/notebooks'

def read(notebook_filename,as_version=4):
    """Reads a notebook from file"""

    with open(notebook_filename) as f:
        nb = nbformat.read(f,as_version=as_version)

    return nb

def execute(notebook_filename,kernel,timeout=600):
    """Executes a notbook"""

    nb = read(notebook_filename)

    ep = ExecutePreprocessor(timeout=timeout,kernel_name=kernel)
    ep.preprocess(nb, {'metadata': {'path': nb_dir}})

    with open(notebook_filename,'wt') as f:
        nbformat.write(nb,f)

def export_nb2html(notebook_filename):

    with open(notebook_filename, 'r') as f:
        body, _ = HTMLExporter.from_file(exp,f)

    with open(html_filename,'w') as f:
        f.write(body)

