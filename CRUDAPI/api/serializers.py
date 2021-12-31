from rest_framework import serializers, validators
from .models import Student

#validators
def start_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError("name should start with R")


class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[start_with_r])#you could add multiple validators by adding ,
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.roll=validate_data.get('roll',instance.roll)
        instance.city=validate_data.get('city',instance.city)
        instance.save()
        return instance

    #field level validation
    def validate_roll(self,value):
        if value>200:
            return serializers.ValidationError('Seat Full') 
        return value       

    #object level validation
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='abhi' and ct.lower()!='ranchi':
            return serializers.ValidationError('City must be Ranchi') 
        return data    





