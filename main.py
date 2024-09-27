import re
import os

# 全局变量，控制是否删除 note 和 month 字段
remove_note = True
remove_month = True


def remove_fields_from_bibtex(input_file):
    # 定义输出文件名
    output_file = 'output.bib'

    with open(input_file, 'r', encoding='utf-8') as file:
        bibtex_content = file.read()

    # Regular expression to find the note field
    if remove_note:
        note_pattern = re.compile(r'\s*note\s*=\s*\{[^}]*\},?\n', re.IGNORECASE)
        bibtex_content = re.sub(note_pattern, '', bibtex_content)

    # Regular expression to find the month field without braces
    if remove_month:
        month_pattern = re.compile(r'\s*month\s*=\s*[^,]+,?\n', re.IGNORECASE)
        bibtex_content = re.sub(month_pattern, '', bibtex_content)

    print(bibtex_content)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(bibtex_content)

    # 重命名 input_file 为 xxx_2.bib
    base, ext = os.path.splitext(input_file)
    new_input_file = f"{base}_2{ext}"
    os.rename(input_file, new_input_file)


# 使用示例
input_file = 'input.bib'
remove_fields_from_bibtex(input_file)
