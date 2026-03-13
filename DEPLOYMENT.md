# S&B Spices Django Deployment Guide

This project is Django-based with a custom themed admin.

## 1) What You Need From Your Side

1. GitHub repository with latest code
2. Render account
3. Domain DNS access (GoDaddy/Namecheap/etc.)
4. Production environment values:
- `SECRET_KEY`
- `ALLOWED_HOSTS` (example: `yourdomain.com,www.yourdomain.com,your-app.onrender.com`)
- `CSRF_TRUSTED_ORIGINS` (example: `https://yourdomain.com,https://www.yourdomain.com,https://your-app.onrender.com`)
- `DATABASE_URL` (from Render PostgreSQL)

## 2) Render Setup

1. Create a PostgreSQL service in Render.
2. Create a Web Service from your GitHub repo.
3. Use:
- Root Directory: `sbspices/cardamom`
- Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- Start Command: `gunicorn sbspices_site.wsgi:application`
4. Add environment variables from section 1.
5. Deploy.

## 3) First-Time Commands (Render Shell)

Run once after first deploy:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Login URLs:
- Django admin: `/admin/`
- Site login page: `/login/`

## 4) Make It Live on Your Domain

1. In Render Web Service -> Settings -> Custom Domains, add:
- `yourdomain.com`
- `www.yourdomain.com`
2. Add DNS records in registrar exactly as Render shows.
3. Wait for DNS propagation and SSL issuance.
4. Set env vars with your real domain values:
- `ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,your-app.onrender.com`
- `CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com,https://your-app.onrender.com`
5. Redeploy.

## 5) Final Production Checklist

1. Open `https://yourdomain.com/`
2. Open `https://yourdomain.com/admin/`
3. Verify custom admin theme loads
4. Add/Edit/Delete Product works
5. Enquiry submission and admin view work
6. Static files load without 404

## 6) Important Note

`/media/uploads/` is local filesystem storage. For long-term production reliability, move media files to S3/Cloudinary later.
