from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    result_list = []

    for file_data in instance._data:
        file_name = file_data["nome_do_arquivo"]
        file_lines = file_data["linhas_do_arquivo"]
        occurrences = []

        for index, line in enumerate(file_lines, start=1):
            if word in line.lower():
                occurrences.append({"linha": index})

        if occurrences:
            new_dict = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences,
            }

            result_list.append(new_dict)

    return result_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
