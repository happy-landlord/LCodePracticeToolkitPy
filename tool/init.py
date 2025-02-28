import sys
import os
import subprocess


def create_file(problem_number: str):
    root_dir = os.path.dirname(os.path.abspath(__file__))  # Get the root directory
    file_name = f"{problem_number}.py"
    file_path = os.path.join(root_dir, "../", file_name)  # Path to the root directory

    # Check if the file already exists
    if os.path.exists(file_path):
        print(f"{file_name} already exists.")
        return

    # Create the content of the new Python file
    file_content = f"""# {problem_number}.py
from test.test_suite import run_tests

test_cases = []

run_tests()
"""

    # Create and write the content to the new file
    with open(file_path, "w") as f:
        f.write(file_content)

    # Open the new file using PyCharm
    try:
        subprocess.run(["open", "-a", "PyCharm", file_path], check=True)
        print(f"{file_name} has been created and opened successfully in PyCharm!")
    except subprocess.CalledProcessError as e:
        print(f"Error opening {file_name} in PyCharm: {e}")

    # Now, call tool/prompt.py to generate the prompt and copy it to the clipboard
    try:
        subprocess.run(["python3", "tool/prompt.py", problem_number], check=True)
        print(f"Prompt for problem #{problem_number} has been copied to clipboard.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating prompt for problem #{problem_number}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 tool/init.py <problem_number>")
    else:
        problem_number = sys.argv[1]
        create_file(problem_number)