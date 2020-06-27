from textwrap import shorten


from django.db.models import (
                              Model,
                              TextField,
                              IntegerField,
                              DateTimeField,
                              )

# Create your models here.

class Quote(Model):
    text = TextField(max_length=1024)

    created = DateTimeField(auto_now_add=True)
    edited = DateTimeField(auto_now=True)
    approved = DateTimeField(blank=True, null=True)

    votes = IntegerField(default=0, editable=False, help_text="Number of votes")

    def __str__(self):
        return self.preview

    class Meta:
        ordering = ["-created",]

    @property
    def preview(self):
        '''preview of quote'''
        return shorten(self.text, 200, placeholder="...")

    def is_approved(self):
        '''return True if approved (and on the main page)'''
        return self.approved is not None

    def upvote(self):
        '''vote quote up'''
        self.votes += 1
        self.save()

    def downvote(self):
        '''vote quote down'''
        self.votes -= 1
        self.save()
