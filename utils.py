import re


def replace_computer_quotation_marks_with_guillemets(text):
    text = re.sub(r"(?<!\S)'(?=\S)", '«', text)
    text = re.sub(r"(?<=\S)'(?!\w)", '»', text)
    text = re.sub(r'(?<!\S)"(?=\S)', '«', text)
    text = re.sub(r'(?<=\S)"(?!\w)', '»', text)
    return text


def typograph_text(text):
    filters = [
        replace_computer_quotation_marks_with_guillemets,
    ]
    for typographer_filter in filters:
        text = typographer_filter(text)
    return text