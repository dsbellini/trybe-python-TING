from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    for file in instance._data:
        if file["nome_do_arquivo"] == path_file:
            print()
            return

    file_content = txt_importer(path_file)
    new_dict = {
        "nome_do_arquivo": f"{path_file}",
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }
    instance.enqueue(new_dict)
    print(new_dict)


def remove(instance: Queue):
    if len(instance) == 0:
        return print("Não há elementos")

    file_dict = instance.dequeue()
    path_file = file_dict["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        return sys.stderr.write("Posição inválida")

    file_dict = instance.search(position)
    print(file_dict)
