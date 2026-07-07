import re
with open(r'C:\Users\Dell\projects\ecolens-ai\ecolens\ui\theme.py', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('CUSTOM_CSS = """') + len('CUSTOM_CSS = """\n<style>\n')
end_idx = content.find('</style>\n"""')
css = content[start_idx:end_idx]

css = css.replace('{', '{{').replace('}', '}}')
css = css.replace('{{{{', '{{').replace('}}}}', '}}')

vars = ['primary', 'primary_light', 'surface', 'background', 'text', 'border', 'muted', 'success']
for v in vars:
    css = css.replace(f'{{{{{v}}}}}', f'{{{v}}}')

# Append black background override
css += '\n.stApp {{ background-color: #000000 !important; }}\n'

new_content = content[:start_idx] + css + content[end_idx:]

with open(r'C:\Users\Dell\projects\ecolens-ai\ecolens\ui\theme.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Fixed theme.py')
