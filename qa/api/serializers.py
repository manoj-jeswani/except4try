from rest_framework import serializers
from qa.models import Question,Answer,Category
from users.models import Euser



class AllQuestionsSerializer(serializers.ModelSerializer):
	asked_at = serializers.CharField(source='timestamp', read_only=True)
	edited_at= serializers.CharField(source='updated', read_only=True)
	asked_by=serializers.CharField(source='get_uname', read_only=True)
	upvoters_list=serializers.CharField(source='get_upvoters', read_only=True)
	downvoters_list=serializers.CharField(source='get_downvoters', read_only=True)
	ans_count=serializers.CharField(source='get_ans_count', read_only=True)
	tags=serializers.CharField(source='get_tag_list', read_only=True)
	vote_count=serializers.CharField(source='votes', read_only=True)
	tags_list=serializers.ListField(child=serializers.CharField(),write_only=True)

	class Meta:
		model=Question
		fields=('topic','detail','ans_count','tags','tags_list','vote_count','asked_at','edited_at','asked_by','upvoters_list','downvoters_list')


	def create(self, validated_data):
		qobj=Question()
		qobj.topic=validated_data['topic']
		qobj.detail=validated_data['detail']
		
		user = None
		request = self.context.get("request")
		if request and hasattr(request, "user"):
			user = request.user
			uobj=Euser.objects.get(username=str(user.username))
			qobj.user=uobj
		qobj.save()
		
		for t in validated_data['tags_list']:
			
			try:
				cobj = Category.objects.get(tag=t)
			
			except Category.DoesNotExist:
				cobj = None

			if cobj is not None:
				qobj.tag_list.add(cobj)
		
		qobj.save()

		return qobj		


class AllAnswersSerializer(serializers.ModelSerializer):
	answered_at = serializers.CharField(source='timestamp', read_only=True)
	edited_at= serializers.CharField(source='updated', read_only=True)
	answered_by=serializers.CharField(source='get_uname', read_only=True)
	upvoters_list=serializers.CharField(source='get_upvoters', read_only=True)
	downvoters_list=serializers.CharField(source='get_downvoters', read_only=True)

	class Meta:
		model=Answer
		fields=('detail','votes','answered_at','edited_at','answered_by','upvoters_list','downvoters_list')

	


	


# class User_Link_RUD_Serializer(serializers.ModelSerializer):
# 	created = serializers.CharField(source='timestamp', read_only=True)
# 	original_url= serializers.CharField(source='url', read_only=True)
# 	shorturl=serializers.CharField(source='get_short_url', read_only=True)
	
# 	class Meta:
# 		model=urlss
# 		fields=('original_url','shorturl','tag','created')


# 	#gives functionality to update tag associated to url in user's url bank
# 	def update(self, instance, validated_data):

# 		instance.tag = validated_data.get('tag', instance.tag)
# 		instance.save()
# 		return instance


# class All_Link_Serializer(serializers.ModelSerializer):
# 	shorturl = serializers.CharField(source='get_short_url', read_only=True)
# 	created = serializers.CharField(source='timestamp', read_only=True)
	
# 	class Meta:
# 		model=urlss
# 		fields=('url','shorturl','created')

# 	def create(self, validated_data):
			
# 		obj=urlss()
# 		obj.url=validated_data['url']
# 		obj.save()
# 		return obj	




# class User_Link_Analytics_Serializer(serializers.Serializer):
# 	total_hit_count = serializers.IntegerField(read_only=True)
# 	unique_ip_set = serializers.ListField(
# 	child=serializers.IPAddressField(protocol='both')
# 	)
# 	regionwise_unique_hits_percent =serializers.DictField(child=serializers.DecimalField(max_digits=6,decimal_places=2))

# #unique_hits: means hits by different ip addresses
# #unique_ip_set:unique visitors