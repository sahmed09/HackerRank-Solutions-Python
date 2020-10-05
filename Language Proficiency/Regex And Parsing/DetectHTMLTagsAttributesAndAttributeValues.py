from html.parser import HTMLParser


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)


html = ""
for _ in range(int(input())):
    html += input()
    html += '\n'

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(html)
parser.close()
