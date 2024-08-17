import markdown2
from pathlib import Path

def convert_markdown_to_html(input_file, output_file):
    # Read the input markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split content by 4 blank lines to separate pages
    pages = content.split('\n\n\n\n')

    # Background colors and text colors to alternate between pages
    background_colors = ["#FFF4E6", "#FBE9FF", "#E6F7FF", "#F9FBE7", "#FFF7F3", "#EFF8FF", "#F4FFF4"]
    text_colors = ["#333333", "#2C3E50", "#34495E", "#2C3E50", "#3E2723", "#1B5E20", "#4A148C"]
    bold_text_color = "#D35400"

    # Initialize HTML content
    html_content = "<html><head><meta charset='utf-8'><style>"
    
    # General page styles
    html_content += """
    body { font-family: Arial, sans-serif; line-height: 1.6; }
    .page { padding: 20px; margin-bottom: 50px; border-radius: 8px; }
    h1, h2, h3, h4, h5, h6 { margin-top: 0; }
    .tags { font-style: italic; color: #888; margin-top: 20px; }
    """

    # Page specific styles with alternating background and text colors
    for i in range(len(pages)):
        html_content += f"""
        .page-{i} {{
            background-color: {background_colors[i % len(background_colors)]};
            color: {text_colors[i % len(text_colors)]};
        }}
        """

    # Bold text style
    html_content += f"""
    strong {{
        color: {bold_text_color};
    }}
    """

    html_content += "</style></head><body>"

    # Convert each page's markdown to HTML and add to HTML content
    for i, page in enumerate(pages):
        # Convert Markdown to HTML
        page_html = markdown2.markdown(page)
        
        # Handle tags specifically
        if "Tags:" in page:
            page_html_parts = page_html.split('<p>Tags:')
            tags_html = f"<p class='tags'>Tags:{page_html_parts[1]}</p>"
            page_html = page_html_parts[0] + tags_html
        
        # Add the page to the final HTML content with a div wrapper for styling
        html_content += f"<div class='page page-{i}'>{page_html}</div>"

    # Closing HTML tags
    html_content += "</body></html>"

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Markdown file has been converted to {output_file}")

if __name__ == "__main__":
    input_file = "combined_output.txt"  # Your input Markdown file
    output_file = "study_notes.html"
    convert_markdown_to_html(input_file, output_file)

