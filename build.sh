set -o errexit

pip install --no-cache-dir -r requirements.txt

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

python manage.py runserver
