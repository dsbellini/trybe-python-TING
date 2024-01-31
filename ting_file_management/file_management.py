import os
import sys


def txt_importer(path_file):
    file_format = os.path.splitext(path_file)

    if file_format[1] == ".txt":
        try:
            with open(path_file, "r") as file:
                file_content = file.read()
                file_lines = file_content.split("\n")
                return file_lines
        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        sys.stderr.write("Formato inválido")
