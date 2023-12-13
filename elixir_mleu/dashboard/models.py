from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class user_details(models.Model):
    emp_id       = models.CharField(max_length=10)
    full_name    = models.CharField(max_length=100)
    email_id     = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)

    class Meta:
        db_table = "elxr_user_details"


class account_list(models.Model):
    account_name = models.CharField(max_length=50)

    class Meta:
        db_table = "elxr_accounts_list"

class projects_list(models.Model):
    project_name    = models.CharField(max_length=50)
    account_name  = models.CharField(max_length=50)

    class Meta:
        db_table = "elxr_projects_list"

class sub_process_list(models.Model):
    sub_process_name    = models.CharField(max_length=50)
    account_name  = models.CharField(max_length=50)
    project_name  = models.CharField(max_length=50)

    class Meta:
        db_table = "elxr_sub_process_list"

class update_type_list(models.Model):
    update_type_name = models.CharField(max_length=50)

    class Meta:
        db_table = "elxr_update_type_list"

class update_source_list(models.Model):
    update_source_name = models.CharField(max_length=100)

    class Meta:
        db_table = "elxr_update_source_list"

class update_details(models.Model):
    timestamp       = models.CharField(max_length = 100)
    deadline        = models.CharField(max_length = 100)
    title           = models.CharField(max_length = 250)
    sub_process     = models.CharField(max_length = 50)
    update_type     = models.CharField(max_length = 50)
    update_source   = models.CharField(max_length = 50)
    update_message  = RichTextUploadingField(blank=True, null=True)
    sender          = models.CharField(max_length = 100)

    class Meta:
        db_table = "elxr_update_details"

class update_recipients(models.Model):
    timestamp   = models.CharField(max_length=100)
    update_id   = models.CharField(max_length = 10)
    user_email  = models.CharField(max_length = 100)
    ack_status  = models.CharField(max_length = 20)
    ack_comment = models.CharField(max_length = 200)

    class Meta:
        db_table = "elxr_update_recipients"

class sub_process_details(models.Model):
    account_name = models.CharField(max_length = 100)
    project_name = models.CharField(max_length = 100)
    sub_process_name = models.CharField(max_length = 100)
    user_email = models.CharField(max_length = 100)

    class Meta:
        db_table = "elxr_sub_process_details"

class question_list(models.Model):
    timestamp = models.CharField(max_length = 100)
    creator = models.CharField(max_length=100)
    question = RichTextUploadingField(blank=True, null=True)
    type = models.CharField(max_length = 100)
    marks = models.CharField(max_length = 10)
    media_type = models.CharField(max_length = 100)
    media_url = models.CharField(max_length = 200)

    class Meta:
        db_table = "elxr_question_list"

class question_details(models.Model):
    question_id = models.CharField(max_length = 100)
    question_option = RichTextUploadingField(blank=True, null=True)
    question_answer = RichTextUploadingField(blank=True, null=True)

    class Meta:
        db_table = "elxr_question_details"

class conquest_list(models.Model):
    timestamp = models.CharField(max_length = 100)
    sub_process = models.CharField(max_length = 100)
    title = models.CharField(max_length=250)
    questions_count = models.CharField(max_length = 10)
    passing_score = models.CharField(max_length = 100)
    max_attempts = models.CharField(max_length = 100)
    sender = models.CharField(max_length = 100)
    deadline = models.CharField(max_length = 100)

    class Meta:
        db_table = "elxr_conquest_list"

class conquest_questions(models.Model):
    conquest_id = models.CharField(max_length = 100)
    question_id = models.CharField(max_length = 100)

    class Meta:
        db_table = "elxr_conquest_questions"

class conquest_recipients(models.Model):
    timestamp = models.CharField(max_length=100)
    conquest_id = models.CharField(max_length = 100)
    user_email = models.CharField(max_length = 100)
    attempts = models.CharField(max_length = 10)
    score = models.CharField(max_length = 10)
    status = models.CharField(max_length = 10)

    class Meta:
        db_table = "elxr_conquest_recipients"

class conquest_recipients_answers(models.Model):
    conquest_id = models.CharField(max_length = 100)
    question_id = models.CharField(max_length = 100)
    user_email = models.CharField(max_length = 100)
    attempt_no = models.CharField(max_length = 10)
    answers = RichTextUploadingField(blank=True, null=True)

    class Meta:
        db_table = "elxr_conquest_recipients_answers"

class update_conquest(models.Model):
    update_id = models.CharField(max_length = 100)
    conquest_id = models.CharField(max_length = 100)

    class Meta:
        db_table = "elxr_update_conquest"
