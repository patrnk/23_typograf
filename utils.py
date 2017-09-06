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


def replace_hyphen_with_em_dash(text, additional_filter=''):
    hyphen = r"{}(?<!\S)-(?!\S)".format(additional_filter)
    text = re.sub(hyphen, '—', text)
    return text


def replace_hyphen_with_en_dash(text, additional_filter=''):
    hyphen = r"{}(?<=\d)-(?=\d)".format(additional_filter)
    text = re.sub(hyphen, '–', text)
    return text


def tie_numbers_with_words_by_non_breaking_space(text, additional_filter=''):
    space = r'{}(?<=\d) (?=\w)'.format(additional_filter)
    text = re.sub(space, ' ', text)
    return text


def typograph_text(text):
    filters = [
        replace_computer_quotation_marks_with_guillemets,
        replace_hyphen_with_em_dash,
        replace_hyphen_with_en_dash,
        tie_numbers_with_words_by_non_breaking_space,
    ]
    no_html_regex = r"(?![^<]*\>)"
    for typographer_filter in filters:
        text = typographer_filter(text, additional_filter=no_html_regex)
    return text
