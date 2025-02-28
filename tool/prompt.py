import sys
import pyperclip
import os

# 获取传入的参数（问题编号）
if len(sys.argv) != 2:
    print("Usage: python3 tool/prompt.py <problem_number>")
    sys.exit(1)

problem_number = sys.argv[1]

# 读取 prompt_generate_lc_problem.md 文件内容
file_path = os.path.join(os.path.dirname(__file__), 'prompt_generate_lc_problem.md')
with open(file_path, 'r') as file:
    content = file.read()

# 替换 #{problem_number} 为传入的参数
updated_content = content.replace("#{problem_number}", f"#{problem_number}")

# 将替换后的内容复制到剪贴板
pyperclip.copy(updated_content)

print(f"Prompt for problem #{problem_number} has been copied to clipboard.")
