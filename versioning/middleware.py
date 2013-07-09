from __future__ import absolute_import, unicode_literals
# -*- mode: python; coding: utf-8; -*-

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()


def get_request():
    """Get request object from any location of code."""
    return getattr(_thread_locals, 'request', None)


class VersioningMiddleware(object):
    """Middleware that saves request in thread local storage"""
    def process_request(self, request):
        _thread_locals.request = request
