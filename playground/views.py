from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from internals import prender
import sys, contextlib, io, random

# Thanks Jochen Ritzel on StackOverflow for this beautiful function below

@contextlib.contextmanager
def stdoutIO():
    old = sys.stdout
    stdout = io.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

def homepage(request):
    if request.method == 'POST':
        return HttpResponseRedirect(request.POST['app'])
    else:
        return prender(request, 'welcome.html')

def ajax_test(request):
    return prender(request, 'ajax.html')

@csrf_exempt
def ajax_text(request):
    if request.method == 'POST':
        facts = [
            'That the Python programming language name comes from the British comedy series “Monty Python’s Flying Circus”?',
            'The first high-level programming language is named Plankalkül.',
            'AJAX is used in many websites!',
            'The origin of a \"Hello World!\" program is from the 1978 book \"The C Programming Language\", the program just prints \"Hello world\".'
        ]
        list_ind = random.randint(0, len(facts)-1)
        if request.POST['index'] != 'null':
            while list_ind == int(request.POST['index']):
                list_ind = random.randint(0, len(facts)-1)
        return HttpResponse(str(list_ind)+'__'+facts[list_ind])
    else:
        return HttpResponse('<h1>403 - Forbidden</h1>')

def python_compiler(request):
    if request.method == 'POST': # If the user sent a 'POST' HTTP request
        codehead = """def input(*args, **kwargs):
            raise Exception(\"Input function is not allowed!\")
        """
        code = codehead+'\n'+request.POST['code']
        try:
            with stdoutIO() as output:
                exec(code)
                execval = output.getvalue()
        except BaseException as error: # If there was an error during execution
            print(error)
            execval = error
        if execval == '': # If there was no output in the program
            return prender(request, 'pyexec.html', {'output':'No output', 'textbox':request.POST['code']})
        else: # If there was a output in the program
            return prender(request, 'pyexec.html', {'output':output.getvalue(), 'textbox':request.POST['code']})
    else: # If the user sent a 'GET' HTTP request
        return prender(request, 'pyexec.html', {'textbox':'print(\"hello, world!\")'})
