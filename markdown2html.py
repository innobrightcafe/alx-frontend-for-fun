#!usr/bimport sys
import markdown
import os

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as md_file:
        markdown_text = md_file.read()

    html_text = markdown.markdown(markdown_text)

    with open(output_file, 'w') as html_file:
        html_file.write(html_text)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_markdown_file> <output_html_file>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    try:
        convert_markdown_to_html(input_file, output_file)
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"An error occurred: {e}\n")
        sys.exit(1)
        