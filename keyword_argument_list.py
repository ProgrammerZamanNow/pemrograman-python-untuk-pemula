# Belajar Keyword Argument List

def create_html(tag, text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key}='{value}'"

    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "Hello Python", style="paragraf")
print(html)
html = create_html("a", "Ini Link", href="www.google.com", style="link")
print(html)
html = create_html("div", "Ini Div", style="contoh")
print(html)

# <a href="">Ini Link</a>