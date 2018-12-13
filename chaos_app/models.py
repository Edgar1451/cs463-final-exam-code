from django.db import models


class Person(models.Model):
    nickname = models.CharField(max_length=48)

    def get_friends(self):
        return [f.friend_b for f in self.friends_a.all()]
        
    def get_bff(self):
        friends = self.friends_a.all().order_by('distance')
        if friends:
            return friends[0].friend_b
        return None

    def get_oldest_friend(self):
        friends = self.friends_a.all().order_by('meet_date')
        
        if friends:
            return friends[0].friend_b
        return None

    def __str__(self):
        return self.nickname


class Location(models.Model):
    place = models.CharField(max_length=512)
    lat = models.FloatField()
    lon = models.FloatField()


class Relation(models.Model):
    friend_a = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='friends_a')
    friend_b = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='friends_b')
    distance = models.IntegerField()
    meet_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('friend_a', 'friend_b'),)







