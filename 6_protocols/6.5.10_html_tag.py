class HtmlTag:
    level = -1

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        HtmlTag.level += 1
        if not self.inline:
            print(f'{"  " * HtmlTag.level}<{self.tag}>')
        return self

    def __exit__(self, *args, **kwargs):
        if not self.inline:
            print(f'{"  " * HtmlTag.level}</{self.tag}>')
        HtmlTag.level -= 1

    def print(self, content=''):
        if self.inline:
            print(f'{"  " * HtmlTag.level}<{self.tag}>{content}</{self.tag}>')
        else:
            print(f'{"  " * HtmlTag.level}  {content}')


with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')
        