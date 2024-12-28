from prompt_toolkit import PromptSession


def print_line(
        session: PromptSession,
        line: str | tuple[str, str,] | list[tuple[str, str]],
        trunc_lines: bool
) -> None:
    if type(line) == str:
        line = [('', line)]
    if type(line) == tuple:
        line = [line]
    if not trunc_lines:
        session.app.print_text(line + [('', '\n')])
        return
    max_width = session.app.output.get_size().columns
    next_line = []
    curr_width = 0
    for style, text in line:
        next_curr_width = curr_width + len(text)
        text = text.replace('\r', '')     # new line to space - everything expected on 1 line
        text = text.replace('\n', ' ')    # new line to space - everything expected on 1 line
        if next_curr_width >= max_width:
            text = text[:max_width - curr_width]  # truncate to match max_width
            text = text[:-1]  # remove last char as well
            next_line.append((style, text))  # add
            next_line.append(('bg:ansired', '>'))  # replace last char with a red > to indicate spillover
        else:
            next_line.append((style, text))
        curr_width = next_curr_width
    next_line.append(('', '\n'))
    session.app.print_text(next_line)