from django.http import HttpResponse
from django.template import loader
from bs4 import BeautifulSoup as bs4
from playground import urls

# Basically the render function but prettifies the html file
# Because the programmer has severe OCD when it comes to indents.
def prender(request, template_name, context={}, content_type='text/html', status=200, using=None):
    context['urls'] = []
    for url in urls.urlpatterns:
        context['urls'].append({'name':url.name.replace("_", " ").title(), 'pattern':url.pattern})
        print({'name':url.name, 'pattern':url.pattern})
    content = loader.render_to_string(template_name, context, request, using) # Get HTML code from file
    no_new_line = content.split('\n')
    no_new_list = ''
    for line in no_new_line:
        no_new_list = no_new_list+line
    #document = html.fromstring(no_new_list) # Get HTML string
    soup = bs4(no_new_list, features="lxml")
    pretty_doc = soup.prettify()
    nowhite_doc = '' # Empty string

    # Remove lines that just have whitespace
    for line in pretty_doc.split('\n'):
        if line.rstrip(): # If the line is just whitespace
            nowhite_doc = nowhite_doc+line+'\n'

    # Append <!DOCTYPE HTML> to the top of the document also
    return HttpResponse(nowhite_doc, content_type, status) # Spit out the string
