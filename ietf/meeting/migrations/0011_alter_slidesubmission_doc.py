# Generated by Django 4.2.19 on 2025-03-17 09:37

from django.db import migrations
import django.db.models.deletion
import ietf.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ("doc", "0025_storedobject_storedobject_unique_name_per_store"),
        ("meeting", "0010_alter_floorplan_image_alter_meetinghost_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slidesubmission",
            name="doc",
            field=ietf.utils.models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="doc.document",
            ),
        ),
    ]
