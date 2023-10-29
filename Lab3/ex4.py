def build_xml_element(tag, content, **args):
    attributes = ''
    for key, value in args.items():
        attributes += ' ' + key + '="' + value + '"'
    return '<' + tag + attributes + '>' + content + '</' + tag + '>'


def main():
    print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))


if __name__ == '__main__':
    main()
