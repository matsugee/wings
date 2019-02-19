from django.db import models


class Schedule(models.Model):
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    title = models.CharField(max_length=20)
    date = models.DateField()
    start = models.IntegerField()
    end = models.IntegerField()     
    place = models.CharField(max_length=40)

    #def publish(self):
        #self.save()​
    def __int__(self):
        return self.id

class Member(models.Model):
    # id
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
        
class Action(models.Model):
    # id
    event_id = models.IntegerField()
    member_id =  models.IntegerField()
    status = models.IntegerField()
    comment = models.CharField(max_length=60, blank=True, null=True)
    
    def __int__(self):
        return self.status

