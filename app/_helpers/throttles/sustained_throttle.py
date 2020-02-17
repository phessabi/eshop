from rest_framework.throttling import AnonRateThrottle


class SustainedAnonRateThrottle(AnonRateThrottle):
    scope = 'sustained'
