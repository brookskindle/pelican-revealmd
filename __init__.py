from pelican import signals
from pelican.readers import BaseReader, MarkdownReader

class RevealJSMarkdownReader(BaseReader):
    """Reads a markdown document and converts it to a reveal.js presentation

    http://docs.getpelican.com/en/stable/plugins.html#how-to-create-a-new-reader
    """
    enabled = True
    file_extensions = ["revealjs"]

    def read(self, filename):
        """Convert a revealjs markdown file to html and return it

        Requires pypandoc (https://github.com/bebraw/pypandoc) and pandoc
        (https://pandoc.org/) to work correctly.
        """
        import datetime

        print(f"revealjsmarkdownreader reading {filename}")
        # TODO: use markdown reader to parse the reveal.js markdown
        # https://github.com/danielfrg/pelican-ipynb/blob/master/markup.py#L62
        content, metadata = MarkdownReader(self.settings).read(filename)
        print(f"metadata is {metadata}")

        # content = "<p>These are sample contents. Hello!</p>"
        metadata = {
            "title": "test reader title",
            "date": datetime.datetime(2018, 8, 1),
        }
        return (content, metadata)


def add_reader(readers):
    for extension in RevealJSMarkdownReader.file_extensions:
        readers.reader_classes[extension] = RevealJSMarkdownReader


def register():
    signals.readers_init.connect(add_reader)
