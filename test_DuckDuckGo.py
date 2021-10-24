'''
This code extracts name of Presidents from the website and renders them using Django
The pytest checks for any name value in the file
'''
from django.shortcuts import render
import requests

def ok(request):
    return render(request, 'ok.txt')

def home(request):
    resp = requests.get('https://api.duckduckgo.com/?q=https%3A%2F%2Fwww.whitehouse.gov%2Fabout-the-white-house%2Fpresidents%2F&ia=web')
    return render(request, 'RelatedTopics.txt',{'resp':resp})
  
def test_for_presidents():
    assert home() is None
