from rest_framework import serializers

from usac.models import Director, Promoter, EventType, EventDay, Race, \
    Participant, Event


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class PromoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promoter
        fields = '__all__'


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'


class EventDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDay
        fields = '__all__'


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
