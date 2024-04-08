from django.db import models

class ServiceRequest(models.Model):
    REQUEST_TYPES = (
        ('gas_leak', 'Gas Leak'),
        ('gas_meter_installation', 'Gas Meter Installation'),
        # Add more request types as needed
    )
    status = models.CharField(max_length=50, default='Pending')
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_request_type_display()} - {self.date_submitted}"
