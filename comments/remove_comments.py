import pyperclip

def remove_single_line_comments(line):
    if '//' in line:
        return line.split('//')[0].rstrip()
    return line

def remove_block_comments(lines):
    in_block_comment = False
    result_lines = []

    for line in lines:
        stripped_line = line.strip()

        if '/*' in stripped_line:
            in_block_comment = True
            line = line.split('/*')[0].rstrip()

        if in_block_comment:
            if '*/' in stripped_line:
                in_block_comment = False
                line = line.split('*/')[-1].rstrip()
            else:
                line = ''

        result_lines.append(line)

    return result_lines

def remove_comments_from_clipboard():
    input_text = pyperclip.paste()
    lines = input_text.splitlines()

    lines_no_block_comments = remove_block_comments(lines)
    final_lines = []

    for line in lines_no_block_comments:
        if '//' in line or '/*' in line:
            final_line = remove_single_line_comments(line)
            if final_line.strip():
                final_lines.append(final_line)
        else:
            if line.strip():
                final_lines.append(line)

    result_text = '\n'.join(final_lines)
    pyperclip.copy(result_text)
    print("Comment removal completed and result copied to clipboard.")

remove_comments_from_clipboard()
