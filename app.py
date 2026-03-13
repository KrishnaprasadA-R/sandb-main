"""Legacy entrypoint kept only to avoid confusion.

This project has been migrated from Flask to Django.
Use Django commands instead:
- python manage.py runserver
- gunicorn sbspices_site.wsgi:application
"""

if __name__ == "__main__":
    raise SystemExit(
        "This project now runs on Django. Use: python manage.py runserver"
    )
