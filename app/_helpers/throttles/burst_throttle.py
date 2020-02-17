from rest_framework.throttling import AnonRateThrottle


class BurstAnonRateThrottle(AnonRateThrottle):
    scope = 'burst'
