# Generated manually for initial schema
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Enquiry",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("company", models.CharField(blank=True, max_length=150)),
                ("place", models.CharField(blank=True, max_length=100)),
                ("email", models.EmailField(max_length=120)),
                ("phone", models.CharField(max_length=50)),
                ("grade", models.CharField(blank=True, max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.FileField(blank=True, null=True, upload_to="uploads/")),
                (
                    "availability",
                    models.CharField(
                        choices=[("In Stock", "In Stock"), ("Out of Stock", "Out of Stock")],
                        default="In Stock",
                        max_length=50,
                    ),
                ),
                ("grade", models.CharField(blank=True, max_length=50)),
                ("rating", models.FloatField(default=5.0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
