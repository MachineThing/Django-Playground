from internals import prender
import sys, contextlib, io

# Thanks Jochen Ritzel on StackOverflow for this beautiful function below

@contextlib.contextmanager
def stdoutIO():
    old = sys.stdout
    stdout = io.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

def homepage(request):
    return prender(request, 'welcome.html')

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
