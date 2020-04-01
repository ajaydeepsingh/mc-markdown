class Line:
    def __init__(self, type, content):
        self.type = type
        self.content = content


def get_paragraphs(file):
    paragraphs = file.split('\n')

    for i in range(0, len(paragraphs)):
        paragraphs[i] = paragraphs[i].rstrip()

        if paragraphs[i] == "":
            paragraphs[i] = "\n"
    return paragraphs


def covert_to_object(paragraph):
    header_level = 0
    content = ""
    for char in paragraph:
        if char == "#":
            header_level += 1
        elif char == "\n":
            header_level = -1
        else:
            content = content + char

    para_object = Line(object_type(header_level), content.strip())

    return para_object


def object_type(header_level):
    if header_level == -1:
        return 'br'
    elif header_level == 0:
        return 'p'
    else:
        return 'h' + str(header_level)
