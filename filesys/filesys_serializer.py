from rest_framework import serializers
from . import models
class FileSerializer(serializers.ModelSerializer):
    id=serializers.CharField(required=False)
    filename=serializers.CharField(required=False)
    category=serializers.CharField(required=False)
    post_time=serializers.DateTimeField(required=False)
    downloads = serializers.CharField(required=False)
    ip = serializers.CharField(required=False)
    filesize = serializers.CharField(required=False)
    filepath = serializers.CharField(required=False)
    filebrief = serializers.CharField(required=False)
    user_id=serializers.CharField(required=False)
    class Meta:
        model=models.File
        fields=['id','filename','category','post_time','downloads','ip','filesize','filepath','filebrief','user_id']

class UserSerisalizer(serializers.ModelSerializer):
    id=serializers.CharField(required=False)
    username=serializers.CharField(required=False)
    password=serializers.CharField(write_only=True,required=False)
    email=serializers.EmailField(required=False)
    class Meta:
        model=models.User
        fields=['id','username','password','email']