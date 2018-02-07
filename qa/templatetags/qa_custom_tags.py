from django import template
from comment.models import Comment
register = template.Library()

@register.filter(name='getCommentSet')
def getCommentSet(obj):

	cqset=Comment.objects.filter(ans=obj)

	return cqset