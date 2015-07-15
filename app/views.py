from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Calc(object):

    def __init__(self, text):
        self.text = text or ''

    def find_substring(self):
        lines = self.text.replace('" "', '\n').split('\n')
        return self.long_substr(lines)

    def long_substr(self, data):
        substr = ''
        if len(data) > 1:
            for line in data:
                if len(line) == 0: continue
                for i in range(len(line)):
                    for j in range(len(line)-i+1):
                        if j > len(substr) and self.is_substr(line[i:i+j], data):
                            substr = line[i:i+j]
        return substr

    def is_substr(self, find, data):
        count = 0
        if len(data) < 1 and len(find) < 1:
            return False
        for i in range(len(data)):
            if find in data[i]:
                count += 1
                if count >= 2:
                    return True
        return False


class RESTView(APIView):

    def get(self, request, *args, **kw):
        get_text = request.GET.get('text', None)
        print get_text
        result = Calc(get_text).find_substring()
        response = Response(result, status=status.HTTP_200_OK)
        return response


def index(request):
    text = request.POST.get('text', '')
    result = Calc(text).find_substring()
    context = {'result': result}
    return render(request, 'app/index.html', context)
