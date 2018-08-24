# pelican-revealmd

Write reveal.js presentations in markdown, in the same way you write markdown
posts for pelican
```markdown
Title: My awesome presentation
Date: 2018-08-08
Category: talks
Summary: This is my summary

# Presentation

With reveal.js!

# Second slide
With whatever you want here
```

Just save your file as `my_presentation.revealjs`, add
```python
PLUGINS = ["revealmd"]
```
to your `pelicanconf.py` and your presentation will be automatically rendered
for you.

You also need to use a blank html template instead of trying to embed the
presentation within the templates provided by your theme. Revealmd provides a
blank html template for this purpose, but in your configuration file, the
templates path needs to be specified
```python
EXTRA_TEMPLATES_PATHS = [
    "path/to/revealmd/templates",  # eg: "plugins/revealmd/templates"
]
```

If you use git to manage your site, you could do something like
```
git submodule add git@github.com:brookskindle/pelican-revealmd.git plugins/revealmd
```
to install the plugin
