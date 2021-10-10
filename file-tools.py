import uuid
import os
import subprocess


def random_filename():
    """
    generate a random filename
    """
    new_filename = uuid.uuid4().hex
    return new_filename


def save(filename, binaries):
    """
    given a path and binaries, save it to a file
    """
    filename = open(filename, "wb")
    filename.write(binaries)
    filename.close()


def list_files_with_ext(dir, ext):
    """
    list all files with a given extension from a given dir
    """
    return [os.path.join(dir, f) for f in os.listdir(dir) if f.endswith(ext)]


def read(file_name):
    """
    given a file_name return the data
    """
    with open(file_name, 'r') as f:
        data = f.read()
    return data


def render_svg(filename):
    """
    given a picture as a file_name and convert it to an svg using convert and potrace.
    Example:
        convert < file_name > .png < file_name > .pnm
        potrace < file_name > .pnm -s -o < file_name > .svg
    """
    buffer = replace_extension(filename, ".pnm")
    target = replace_extension(filename, ".svg")
    # convert <file_name>.jpeg <file_name>.pnm
    subprocess.call(["convert", filename, buffer])
    # potrace <file_name>.pnm -s -o <file_name>.svg
    subprocess.call(["potrace", buffer, "--group", "-s", "-o", target])
    # rm <file_name>.pnm
    subprocess.call(["rm", buffer])


def replace_extension(filename, extension):
    """
    Given a `filename` and an `extension`, replace the current extension with the new one
    """
    return os.path.splitext(filename)[0] + extension
