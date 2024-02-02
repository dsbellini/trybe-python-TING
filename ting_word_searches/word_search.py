from ting_file_management.queue import Queue


def process_file(word: str, file_data: dict, include_content: bool = False):
    file_name = file_data["nome_do_arquivo"]
    file_lines = file_data["linhas_do_arquivo"]
    occurrences = []

    for index, line in enumerate(file_lines, start=1):
        lower_line = line.lower()

        if word in lower_line:
            occurrence_info = {"linha": index}
            if include_content:
                occurrence_info["conteudo"] = line
            occurrences.append(occurrence_info)

    if occurrences:
        return {
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": occurrences,
        }
    else:
        return None


def verify_data(word: str, instance: Queue, include_content: bool = False):
    result_list = []

    for file_data in instance._data:
        result = process_file(word, file_data, include_content)
        if result:
            result_list.append(result)

    return result_list


def exists_word(word: str, instance: Queue):
    return verify_data(word, instance)


def search_by_word(word, instance):
    return verify_data(word, instance, True)
