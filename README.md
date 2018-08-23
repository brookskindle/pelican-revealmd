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

If you use git to manage your site, you could do something like
```
git submodule add https://github.com/brookskindle/pelican-revealmd.git plugins/revealmd
```
to install the plugin
