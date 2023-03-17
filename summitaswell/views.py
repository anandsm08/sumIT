from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
import openai


@api_view(['POST'])
def summit(request):
    
    data = request.data
    prompt = data.get('q')
    

    openai.api_key = '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'
    
  
    summary = openai.Completion.create(
    model="text-davinci-003",
    prompt="summurize this: " + prompt,
    temperature=1,
    max_tokens=1000,
  )["choices"][0]["text"].strip('\n')
    
    title = openai.Completion.create(
    model="text-davinci-003",
    prompt="Give a 3-4 word title for: "+prompt,
    temperature=1,
    max_tokens=20,
  )["choices"][0]["text"].strip('\n')

    return Response({"summary":summary,"title":title})
