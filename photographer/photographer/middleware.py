# coding: utf-8
import re

MOBILE_AGENT_RE = re.compile(r".*(iphone|mobile|androidtouch)",
                             re.IGNORECASE)


class MobileMiddleware(object):
    def process_request(self, request):
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            request.urlconf = "photographer.mobile_urls"
