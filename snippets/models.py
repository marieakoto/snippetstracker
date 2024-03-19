from django.db import models
from pygments.lexers import get_all_lexers  #To get all available lexers(programming language) supported by pygment.
from pygments.styles import get_all_styles   #To get all available styles supported by pygments.
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
# get_all_lexers() returns a list of tuples, where each tuple represents a lexer supported by the Pygments
# library. The first element of the tuple is a list of lexer aliases, and the second element is a short 
# description of the lexer.The list comprehension [item for item in get_all_lexers() if item[1]] iterates over
# each item (tuple) returned by get_all_lexers(). It filters out items where the second element of the tuple 
# (description) is not empty.The resulting list LEXERS contains only the lexers with non-empty descriptions.


LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#This line creates a list of tuples representing choices for the language field in the Snippet model.
#It uses a list comprehension to iterate over each item in the LEXERS list (which contains filtered lexers 
#with non-empty descriptions). For each item, it extracts the first alias of the lexer (item[1][0]) and the 
#lexer name (item[0]).The resulting list of tuples is then sorted alphabetically based on the first element 
#of each tuple (the first lexer alias).



STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
#This line creates a list of tuples representing choices for the style field in the Snippet model.
#It uses a list comprehension to iterate over each item (style) returned by get_all_styles().
#For each style, it creates a tuple with the style repeated twice (item, item).
#The resulting list of tuples is then sorted alphabetically.


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()  ## a TextField for the code content of the snippet.
    linenos = models.BooleanField(default=False)  ##a BooleanField to specify whether line numbers should be displayed with the snippet.
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100) # a CharField with choices defined by LANGUAGE_CHOICES, representing the programming language of the snippet.
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100) #a CharField with choices defined by STYLE_CHOICES, representing the code highlighting style.
    owner = models.ForeignKey('auth.User', related_name = 'snippets', on_delete = models.CASCADE)  #Represnts the user who created the snippet. 
    highlighted = models.TextField()   # stores the html representaion of the code.

    class Meta:
        ordering = ['created']   # specifies that the results should be ordered by the created field in ascending order by default.



    def save(self, *args, **kwargs):
    
    #Use the `pygments` library to create a highlighted HTML representation of the code snippet.
   
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
        