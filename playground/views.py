from django.shortcuts import render
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
            return render(request, 'index.html', {'output':output.getvalue(), 'textbox':request.POST['code']})
        except BaseException as e:
            print(e)
            return render(request, 'index.html', {'output':e, 'textbox':request.POST['code']})

    else:
        return render(request, 'index.html', {'textbox':'print(\"hello, world!\")'})
