# sierra

<p align='center'>
<img src="https://github.com/BrainStormYourWayIn/sierra/blob/main/logo.jpg" alt="Sierra"/>
</p>

![GitHub](https://img.shields.io/github/license/BrainStormYourWayIn/sierra?color=blue)

Sierra is a Python library to write HTML and CSS in pure Python using the DOM API in a simple yet elegant manner. Take advantage of Python's powerful 
functionalities with ease. Loops, variables, functions, libraries - you name it, you have it.

Here are a few advantages of using Sierra over other Python libraries that use the DOM API:

- It has out-of-the-box support for all CSS styling attributes
- Display a table by simply putting in a CSV file
- Create your own tag functions with absolute ease using `@tag` and `@CmTag`. You can decide their behavior and use them within content-managers too
- Create definition lists, ul/ol lists by inputting in a nested list
- Support for all HTML tag attributes
- Improvement in the arrangement look of the code and intelligent handling of tags with    
`autoPrettify()` - Powered by bs4 and a feature like no other
- Use it as a templating engine for web frameworks (Although note that jinja and Django handle this task much better)

________________________________

## Documentation

- **Check out the [documentation of Sierra](https://brainstormyourwayin.github.io/sierra.github.io/)**
- **Check out a [few examples](https://github.com/BrainStormYourWayIn/sierra_examples/) of its use**

> It is recommended to look at the examples only after going through the documentation.
>> The examples mentioned above is a simple bare-boned book search engine created with requests, bs4, Flask and Sierra; and the documentation of Sierra, which was written with Sierra standalone 

________________________________

**Install using**

    pip install sierra
    
Starting off is pretty simple and straightforward:
```python
from sierra import *
    
title('Hello World!')
```
    
The `title()` function at the start is mandatory, since it commences the HTML and the CSS file.

You can create custom tag functions with @tag and @CmTag with just three lines of code. Say you want to create a function for &lt;meta&gt;:
```python
@tag
def meta(**kwargs):
    pass
        
# Using them
    
meta(name="description", content="This is some description")
meta(name="viewport", content="width=device-width", initial_scale=1.0)
```

Underscores are used for hyphens (same applies to CSS) and Python-conficting arguments are prefixed with a double underscore.

Using argument `text` inside of a function defined in `@tag` will create a tag that opens, enters text, and closes. Something like this:
```python
@tag
def script(**kwargs):
    pass
script(__async="", src="some_src", text="some_text")
```
Is the equivalent of:
```html
<script async="" src="some_src">some_text</script>
```
Want to add some JS? Simple enough. Just create a function for the &lt;script&gt; tag with a context manager behavior using `@CmTag` and you're golden.   
```python
@CmTag
def script(**kwargs):
    pass

# Here I'll be replicating the script needed to add Google Analytics to a webpage

with script(__aync="", src="https://www.googletagmanager.com/gtag/js?id=UA—XXXXXXXX-X"):
    pass
    
with script():

    writeWA('''
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA—XXXXXXXX-X');
  ''')
```
This is the equivalent of:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=UA—XXXXXXXX-X"></script>

<script>
    
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA—XXXXXXXX-X');
    
</script>
```
You can add fonts using `addFont()`
```python
addFont("https://fonts.googleapis.com/css2?family=Roboto&display=swap")
```
Once things at the `<head>` of the HTML are settled (CSS is automatically linked), begin the body of the HTML with
```python
openBody()
# You can add any number of styling arguments to the body within openBody()
openBody(background_color='yellowgreen', opacity='0.9')
```
You can create `div` and `section` tags this way:
```python
with div(__class="some_class") as d:
    p('This is a paragraph!')
    d.css(background_color="#5886d1")
```
Let's break this down but-by-bit:  
First, we start a `div` with a context manager behavior and give it an attribute `__class`, which is essentially the tag attribute `class` (remember Python-conflicting) arguments are prefixed by a double underscore.

`p()` is a function, as the name suggests, to add a `<p>` tag. You can give the tag attributes with `**kwargs`, if you like.   
`p('Hello World!', __class='p_class')` is the same as `<p class="p_class">Hello World!</p>`

After the paragraph, there's a `d.css()`. This adds CSS to the `class` mentioned within `div()`. If a `class` is mentioned, CSS is added to that class as the first priority. If an `id` is mentioned, CSS is added to that `id` as a second priority. If none of both are mentioned, CSS is just added to 
