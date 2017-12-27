from django.db import models


class Director(models.Model):
    """
    Person Directing the Event
    Many Events for each Director
    """
    name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return self.name


class Promoter(models.Model):
    """
    Company promoting the Event
    Many Event promoted by Each company
    """
    name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return self.name


class EventType(models.Model):
    """
    Each event has an event type. This is not well defined
    This is many to many with event
    Each even has many types and each type is part of many events
    """
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)
    # TODO: Should state have its own class
    state = models.CharField(max_length=2, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    flyer_url = models.URLField(max_length=255, null=True)
    flyer = models.FileField(upload_to='uploads/flyers/',
                             null=True, blank=True)
    website_url = models.URLField(max_length=255, null=True)
    online_reg = models.URLField(max_length=255, null=True)
    # TODO: is permit number unique? I am assuming yes.
    permit_number = models.CharField(max_length=255, null=False, unique=True)
    director = models.ForeignKey(Director, null=True, related_name="events",
                                 on_delete=models.SET_NULL)
    promoter = models.ForeignKey(Promoter, null=True, related_name="events",
                                 on_delete=models.SET_NULL)
    etypes = models.ManyToManyField(EventType, default=list, blank=True)

    def __str__(self):
        return self.name


class EventDay(models.Model):
    """
    Each day or races is part of an event.
    Each race is part of a day, see rece below.
    The day has an id on the website, 44746 in the example below, Also a date 01/15/2012.
    Not all days have an searchid or a page, sometimes all the results are on 1 page.
    <a href="javascript:void(0)" onclick="loadInfoID(44746,'Criterium 01/15/2012')">Criterium</a>

    Multiple day example
    https://www.usacycling.org/results/?permit=2012-860
    This is the rusults for the second race of the first day.
    https://www.usacycling.org/results/index.php?ajax=1&act=loadresults&race_id=598962
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    search_id = models.IntegerField(default=None, null=True)
    day = models.DateField(null=False)
    # url: https://www.usacycling.org/results/?permit=2012-860
    url = models.URLField(max_length=255, null=False)
    # TODO Maybe need a switch for single page or multi page. Trying this below
    multi_page = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.day)


class Race(models.Model):
    """
    Each race and results
    """
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    event_day = models.ForeignKey(EventDay, null=True,
                                  on_delete=models.SET_NULL)
    # this is often a class or race category
    name = models.CharField(max_length=255, null=False)
    race_id = models.IntegerField(null=False)
    # "https://www.usacycling.org/results/index.php?ajax=1&act=loadresults&race_id=598962"
    url = models.URLField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Participant(models.Model):
    """
    Racers
    """
    fname = models.CharField(max_length=255, null=False)
    lname = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    license = models.CharField(max_length=255, null=False)

    def __str__(self):
        return '{0} {1}'.format(self.fname, self.lname)

# TODO RaceResults class
