import os

from markdown import Markdown
from pelican import signals
from pelican.readers import BaseReader, MarkdownReader
import pypandoc


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

        # TODO: use markdown reader to parse the reveal.js markdown
        # https://github.com/danielfrg/pelican-ipynb/blob/master/markup.py#L62
        reader = MarkdownReader(self.settings)
        md_content, metadata = reader.read(filename)
        metadata["template"] = "blank"

        # TODO: using the markdown reader converts the file contents to HTML,
        # but we just want plain text because pandoc should be converting it
        # instead. The trouble is, we also want to get the metadata

        md_converter = Markdown(**self.settings["MARKDOWN"])
        md_converter.convertFile(filename, output=os.devnull)

        md_content = "\n".join(md_converter.lines)
        # metadata = getattr(md_converter, "Meta", {})

        revealjs_content = pypandoc.convert_text(md_content, to="revealjs",
            format="md",
            extra_args=[
                "-s",
                "-V", "revealjs-url=https://lab.hakim.se/reveal-js",
                # "--slide-level", "2",
            ],
        )

        return (revealjs_content, metadata)


def add_reader(readers):
    for extension in RevealJSMarkdownReader.file_extensions:
        readers.reader_classes[extension] = RevealJSMarkdownReader


def register():
    signals.readers_init.connect(add_reader)
