import re
import os

class PhpLinker:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.included_files = set()

    def link(self, filename):
        filepath = os.path.join(self.base_dir, filename)
        if filepath in self.included_files:
            return ''  # Prevent duplicate inclusion
        self.included_files.add(filepath)
        with open(filepath, 'r') as f:
            content = f.read()
        # Find include/require statements (simple regex)
        pattern = r'(include|require)(_once)?\s*[\'"]([^\'"]+)[\'"]\s*;'
        def replacer(match):
            inc_file = match.group(3)
            return self.link(inc_file)
        linked_content = re.sub(pattern, replacer, content)
        return linked_content

# Example usage:
# linker = PhpLinker('/path/to/php/project')
# combined = linker.link('index.php')
# with open('linked_output.php', 'w') as f:
#     f.write(combined)
