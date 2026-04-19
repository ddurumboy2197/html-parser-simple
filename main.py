from html.parser import HTMLParser

class SimpleHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.texts = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)

    def handle_data(self, data):
        self.texts.append(data)

    def get_result(self):
        return self.tags, self.texts

# Misol foydalanish:
parser = SimpleHTMLParser()
html = "<html><body><h1>Hello, World!</h1><p>This is a paragraph.</p></body></html>"
parser.feed(html)
tags, texts = parser.get_result()
print("Tags:", tags)
print("Texts:", texts)
```

Kodda `SimpleHTMLParser` klassi yaratilgan, u `html.parser.HTMLParser` dan voris klass. Ushbu klassda `handle_starttag` va `handle_data` metodlari o'zgartirilgan, ular tag va matnni chop etish uchun mo'ljallangan. `get_result` metodida taglar va matnnlar qaytariladi. Misol foydalanishda `SimpleHTMLParser` klassi yaratilgan, unga HTML matni berilgan, keyin taglar va matnnlar chop etilgan.
