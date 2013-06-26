#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'pistalo', 'local_settings.py')):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pistalo.local_settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pistalo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)