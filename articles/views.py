from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializers import ArticleSerializer

#해당함수가 지정한 HTTP요청을 처리할 수 있도록 API뷰를 만들어 주는 역할
@api_view(['GET','POST'])
def article_API(request):
  if request.method == 'GET':
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = ArticleSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      print(serializer.errors)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def article_view(request, article_id):
  if request.method == 'GET':
    article = get_object_or_404(Article, id=article_id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
  elif request.method == 'PUT':
    article = get_object_or_404(Article, id=article_id)
    serializer = ArticleSerializer(article, data=request.data) #(원래 data, 새로운 data) 
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  elif request.method == 'DELETE':
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)