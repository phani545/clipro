from django.http import HttpResponse

class MiddleWareLifeCycle:
    def __init__(self,get_response):
        print('INIT')
        self.get_response=get_response

    def __call__(self, request):
        print('Before the view executed')
        response = self.get_response(request)
        print('After view is executed')
        return response
    
class ExceptionHanding:
    def __init__(self,get_response):
        #print('INIT')
        self.get_response=get_response

    def __call__(self, request):
        return self.get_response(request)
    
    def process_exception(self,request,exception):
        return HttpResponse("<b>We are Currently facing some issues, please try agin later</b>")