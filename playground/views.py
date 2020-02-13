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

def index(request):
    if request.method == 'POST':
        try:
            codehead = """def input(*args, **kwargs):
                raise Exception(\"Input function is not allowed!\")
            """
            code = codehead+'\n'+request.POST['code']
            with stdoutIO() as output:
                exec(code)
            if output.getvalue() == '':
                return prender(request, 'index.html', {'output':'No output', 'textbox':request.POST['code']})
            else:
                return prender(request, 'index.html', {'output':output.getvalue(), 'textbox':request.POST['code']})
        except BaseException as error:
            print(error)
            return prender(request, 'index.html', {'output':error, 'textbox':request.POST['code']})

    else:
        return prender(request, 'index.html', {'textbox':'print(\"hello, world!\")'})
