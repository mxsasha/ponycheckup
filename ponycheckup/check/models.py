from django.db import models
from django_extensions.db.models import TimeStampedModel


class Check(TimeStampedModel):
    url                     = models.URLField()

    no_of_recommendations   = models.IntegerField(default=0)

    runs_debug              = models.BooleanField()

    supports_https          = models.BooleanField()
    heartbleed_vuln         = models.BooleanField()
    hsts_header_found       = models.BooleanField()
    xframe_header_found     = models.BooleanField()

    admin_found             = models.BooleanField()
    admin_forces_https      = models.NullBooleanField()

    login_found             = models.BooleanField()
    login_forces_https      = models.NullBooleanField()

    allows_trace            = models.BooleanField()

    csrf_cookie_found       = models.BooleanField()
    session_cookie_found    = models.BooleanField()
    session_cookie_secure   = models.NullBooleanField()
    session_cookie_httponly = models.NullBooleanField()

    def update_recommendation_count(self):
        self.no_of_recommendations = 0

        if self.runs_debug:                                  self.no_of_recommendations += 1
        if not self.supports_https:                          self.no_of_recommendations += 1
        if self.heartbleed_vuln:                             self.no_of_recommendations += 1
        if not self.hsts_header_found:                       self.no_of_recommendations += 1
        if not self.xframe_header_found:                     self.no_of_recommendations += 1
        if self.admin_found and not self.admin_forces_https: self.no_of_recommendations += 1
        if self.login_found and not self.login_forces_https: self.no_of_recommendations += 1
        if self.allows_trace:                                self.no_of_recommendations += 1
        #if not self.csrf_cookie_found:                       self.no_of_recommendations += 1
        if self.session_cookie_found and not self.session_cookie_secure:   self.no_of_recommendations += 1
        if self.session_cookie_found and not self.session_cookie_httponly: self.no_of_recommendations += 1

    @property
    def secure_percentage(self):
        # worst is 10, best is 0
        return int(100-round(10*self.no_of_recommendations))

    @property
    def proven_django(self):
        return self.runs_debug or self.csrf_cookie_found or self.session_cookie_found or self.admin_found
