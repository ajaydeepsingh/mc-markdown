from disassemble import Line

class Link:
    def __init__(self, s_idx, e_idx, description, url):
        self.type = 'link'
        self.start_idx = s_idx
        self.end_idx = e_idx
        self.description = description
        self.url = url[1:]
        self.converted = '<a href="' + url[1:] + '">' + description + '</a>'

def get_links(text):
    in_description = False
    in_url = False
    start_idx = 0
    end_idx = 0
    description = ""
    url = ""
    links = []

    for i in range(len(text)):
        if text[i] == "[" and in_description is False:
            in_description = True
            start_idx = i

        elif text[i:i+2] == "](":
            in_description = False
            in_url = True

        elif in_url is True and text[i] == ")":
            in_url = False
            end_idx = i
            new_link = Link(start_idx, end_idx, description, url)
            links.append(new_link)
            start_idx = 0
            end_index = 0
            description = ""
            url = ""

        elif in_description:
            description = description + text[i]

        elif in_url:
            url = url + text[i]

    return links


def convert_text(text, links):
    result = ""
    for idx, link in enumerate(links):
        if idx == 0:
            result = result + text[0:link.start_idx]
        else:
            result = result + text[links[idx - 1].end_idx + 1: link.start_idx]
        result = result + link.converted
    
    result = result + text[links[len(links) - 1].end_idx + 1:]
    return result


def convert_links(object_array):
    for idx, line in enumerate(object_array):
        links = get_links(line.content)

        if len(links) > 0:
            new_text = convert_text(line.content, links)
            new_line = Line(line.type, new_text)
            object_array[idx] = new_line

    return object_array
