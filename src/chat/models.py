from django.contrib.auth.models import User
from django.db import models


class DocumentContent(models.Model):
    file = models.FileField(upload_to='documents/')


class ImageContent(models.Model):
    image = models.ImageField(upload_to='images/')


class TaskContent(models.Model):
    task_description = models.TextField()


class Message(models.Model):
    MESSAGE_TYPES = [
        ('TEXT', 'Text'),
        ('DOC', 'Document'),
        ('IMG', 'Image'),
        ('TASK', 'Task'),
    ]

    content = models.TextField(blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    type = models.CharField(max_length=20, choices=MESSAGE_TYPES, default='TEXT')
    created_at = models.DateTimeField(auto_now_add=True)

    # Dynamic content fields based on the type
    document_content = models.ForeignKey(DocumentContent, on_delete=models.SET_NULL, blank=True, null=True)
    image_content = models.ForeignKey(ImageContent, on_delete=models.SET_NULL, blank=True, null=True)
    task_content = models.ForeignKey(TaskContent, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.sender}: {self.content} ({self.get_type_display()})'

