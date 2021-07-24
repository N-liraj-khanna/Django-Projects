from django.shortcuts import render
from PyDictionary import PyDictionary

dictionary=PyDictionary()

def index(request):
  return render(request, 'index.html')

def word(request):
  search=request.GET.get('search')
  meanings = dictionary.meaning(search)
  synonyms = dictionary.synonym(search)
  antonyms = dictionary.antonym(search)
  if  meanings:
    meanings = meanings.get('Noun')[:3]
    
  if not meanings==0:
    meanings=['Nothing Found']
  if not synonyms or len(synonyms)==0:
    synonyms=['Nothing Found']
  if not antonyms or len(antonyms)==0:
    antonyms=['Nothing Found']

  return render(request, 'word.html', context={
    "meanings": meanings,
    "synonyms": synonyms,
    "antonyms": antonyms,
  })