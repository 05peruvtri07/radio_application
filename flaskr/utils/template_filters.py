def replace_newline(text):
    wrapped_text = ''
    for i in range(len(text)//37+1):
        if len(text) <= 37:
            wrapped_text += text
        else:
            wrapped_text += text[:37] + '\n'
            text = text[37:]
            """\n => split"""
    return wrapped_text.split('\n')