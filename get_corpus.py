def read_file(source_text_path):
    with open(source_text_path, 'r') as myfile:
        words = myfile.read().replace('\n', '').lower().split()
    return words
