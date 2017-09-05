import re


def replace_computer_quotation_marks_with_guillemets(text, additional_filter=''):
    opening_mark_template = r"{}(?<!\w){}(?=\S)"
    closing_mark_template = r"{}(?<=\S){}(?!\w)"
    opening_single_quotation_mark = opening_mark_template.format(additional_filter, "'")
    closing_single_quotation_mark = closing_mark_template.format(additional_filter, "'")
    opening_double_quotation_mark = opening_mark_template.format(additional_filter, '"')
    closing_double_quotation_mark = closing_mark_template.format(additional_filter, '"')
    text = re.sub(opening_single_quotation_mark, '«', text)
    text = re.sub(closing_single_quotation_mark, '»', text)
    text = re.sub(opening_double_quotation_mark, '«', text)
    text = re.sub(closing_double_quotation_mark, '»', text)
    return text


def typograph_text(text):
    filters = [
        replace_computer_quotation_marks_with_guillemets,
    ]
    no_html_regex = r"(?![^<]*\>)"
    for typographer_filter in filters:
        text = typographer_filter(text, additional_filter=no_html_regex)
    return text
