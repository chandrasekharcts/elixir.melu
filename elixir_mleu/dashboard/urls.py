from django.urls import path, re_path
from . import views

urlpatterns = [

# --------------------------------- LOGIN REDIRECT ---------------------------------------------------------------------
    # Redirect domain to Login URL
    path('',views.userRedirrectLogin, name="redirect_view"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- LOGIN ------------------------------------------------------------------------------
    # User Login Authentication
    re_path(r'^accounts/login/$', views.user_login, name="user_login"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- LOGOUT -----------------------------------------------------------------------------
    # User Logout
    path('account/logout/', views.user_logout, name="user_logout"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- VERSION HISTORY --------------------------------------------------------------------
    # User Logout
    path('version_history/', views.version_history, name="version_history"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- DASHBOARD --------------------------------------------------------------------------
    # Redirect To Dashboard
    path('dashboard/', views.dashbaord, name="dashboard"),
    # Load User Related Accounts List
    path("user_account_list/", views.user_account_list, name="user_account_list"),
    # Load User Related Projects List
    path("user_project_list/", views.user_project_list, name="user_project_list"),
    # Business Vertical Statistics
    path('business_statistics', views.business_statistics, name='business_statistics'),
    # Filter Business Vertical Customised Data on PickUp Date
    path('dashboard_vertical_data_filter', views.dashboard_vertical_data_filter, name='dashboard_vertical_data_filter'),
    # Filter User Customised Data on PickUp Date
    path('dashboard_user_data_filter', views.dashboard_user_data_filter, name='dashboard_user_data_filter'),
#-----------------------------------------------------------------------------------------------------------------------


# --------------------------------- REPORTING --------------------------------------------------------------------------
    # Redirect To Dashboard
    path('dashboard/reporting/', views.reporting, name="reporting"),
    # Filter Associates on PickUp Date of Updates/PKT
    path('reporting_data_filter', views.reporting_data_filter, name='reporting_data_filter'),
    # Filter Associates List of Updates
    path('reporting_emp_update_list', views.reporting_emp_update_list, name='reporting_emp_update_list'),
    # Filter Associates List of Knowledge Checks
    path('reporting_emp_kc_list', views.reporting_emp_kc_list, name='reporting_emp_kc_list'),
#-----------------------------------------------------------------------------------------------------------------------


# --------------------------------- My TASKS - UPDATE + KNOWLEDGE CHECK ------------------------------------------------
    # Redirect to My Task - Update + Knowledgement Check
    path('dashboard/mytasks_up_kc/', views.mytasks_up_kc, name="mytasks_up_kc"),
    # Filter list fo updates+knowledge check as per the Date Selected
    path('mytask_up_kc_date_filter', views.mytask_up_kc_date_filter, name='mytask_up_kc_date_filter'),
    # Save the acknowledgement and Answers of Knowledge Test
    path('save_user_ack', views.save_user_ack, name='save_user_ack'),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- My TASKS - KNOWLEDGE CHECK ---------------------------------------------------------
    # Redirect to My Tasks - Knowledge Check List
    path('dashboard/mytasks_kc/', views.mytasks_kc, name="mytasks_kc"),
    # Filter list fo knowledge check as per the Date Selected
    path('mytask_kc_date_filter', views.mytask_kc_date_filter, name='mytask_kc_date_filter'),
    # Details of Knowledge Test as per the Selection
    path("kc_data", views.kc_data, name="kc_data"),
    # Save Details of Knowledge Test submitted by User
    path("save_user_kc_data", views.save_user_kc_data, name="save_user_kc_data"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- KNOWLEDGE CHECK EVALUATION ---------------------------------------------------------
    # Redirect to Knowledge Check Evaluation
    path('dashboard/knowledge-check-evaluation/', views.knowledge_check_evaluation, name="knowledge_check_evaluation"),
    # Users list of selected Knowledge Check
    path('conquest_user_list', views.conquest_user_list, name="conquest_user_list"),
    # Users Data of selected Knowledge Check
    path('conquest_user_data', views.conquest_user_data, name="conquest_user_data"),
    # Users Submitted Knowledge Check Evaluation Score
    path('user_kc_eval', views.user_kc_eval, name="user_kc_eval"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- ELIXIR -----------------------------------------------------------------------------
    # Redirect To Elixir
    path('dashboard/elixir/', views.elixir, name="elixir"),
    # Details of Employees who received the selected Update
    path("update_data", views.update_data, name="update_data"),
    # Details of Updates sent by selected POC
    path("update_poc_data", views.update_poc_data, name="update_poc_data"),
    # Filtered Sub-Categories When Categories Selected for Elixir List
    path("elixir_sub_categories", views.elixir_sub_categories, name="elixir_sub_categories"),
    # Filtered Elixir List when filters selected
    path("elixir_filtered_list", views.elixir_filtered_list, name="elixir_filtered_list"),
    # Change Update Validity
    path("change_update_validity", views.change_update_validity, name="change_update_validity"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- CREATE NEW UPDATE ------------------------------------------------------------------
    # Redirect to Create New Update
    path("dashboard/create-new-update/", views.createUpdate, name="createUpdate"),
    #Upload Attachment
    path("upload_attachment_file", views.upload_attachment_file, name="upload_attachment_file"),
    #Send Update with the Provided details to the users of the Subprocess Selected
    path("send_update", views.send_update, name="send_update"),
    #Send Knowledge Test
    path("send_kc", views.send_kc, name="send_kc"),
    # Save all the questions and correct answer of the Knowledge Test
    path('save_up_conq', views.save_up_conq, name='save_up_conq'),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- ALL UPDATES ------------------------------------------------------------------------
    # Redirect to All Updates
    path("dashboard/all-update/", views.allUpdate, name="allUpdate"),
    # Filter All Updates as per the Date Range Selected
    path('allupdates_date_filter', views.allupdates_date_filter, name='allupdates_date_filter'),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- SENT UPDATES -----------------------------------------------------------------------
    # Redirect to Sent Updates
    path("dashboard/sent-update/", views.sentUpdate, name="sentUpdate"),
    # Filter Sent Updates as per the Date Range Selected
    path('sentupdates_date_filter', views.sentupdates_date_filter, name='sentupdates_date_filter'),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- PENDING UPDATES --------------------------------------------------------------------
    # Redirect to Pending Updates
    path("dashboard/pending-update/", views.pendingUpdate, name="pendingUpdate"),
    # Filter Pending Updates as per the Date Range Selected
    path('pendingupdates_date_filter', views.pendingupdates_date_filter, name='pendingupdates_date_filter'),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- ACKNOWLEDGED UPDATES ---------------------------------------------------------------
    # Redirect to Acknowledged Updates
    path("dashboard/acknowledged-update/", views.ackUpdate, name="ackUpdate"),
    # Filter Acknowledged Updates as per the Date Range Selected
    path('ackupdates_date_filter', views.ackupdates_date_filter, name='ackupdates_date_filter'),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- CONQUEST ---------------------------------------------------------------------------
    # Redirect To Conquest
    path("dashboard/conquest/", views.conquest, name="conquest"),
    # List of Associates Who received the Selected Knwoledge Check
    path('conquest_data', views.conquest_data, name='conquest_data'),
    # Filtered Conquest List when filters selected
    path("conquest_filtered_list", views.conquest_filtered_list, name="conquest_filtered_list"),
    # Change Knowledge Test Validity
    path("change_kc_validity", views.change_kc_validity, name="change_kc_validity"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- QUESTION BANK ----------------------------------------------------------------------
    # Redirect To QUESTION BANK
    path("dashboard/question_bank/", views.question_bank, name="question_bank"),
    #Save Knowledge Test from Question Bank
    path("send_kc_ques", views.send_kc_ques, name="send_kc_ques"),
    # Details of Selected Question
    path('question_data', views.question_data, name='question_data'),
    # Upload Questions in bulk using Excel template
    path('upload_questions_file', views.upload_questions_file, name="upload_questions_file"),
    # Download the Questions template
    path('download_questions_template', views.download_questions_template, name="download_questions_template"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- CONQUEST Response ------------------------------------------------------------------
    # Redirect To Conquest Response
    path("dashboard/conquest_response/", views.conquest_response, name="conquest_response"),
    # Details of Conquest Responses as per Knowledge Test  Selected
    path("conquest_responses_data", views.conquest_responses_data, name="conquest_responses_data"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- CREATE KNOWLEDGE CHECK -------------------------------------------------------------
    # Redirect to Create Knowledge Check
    path("dashboard/create-knowledge-check/", views.createKC, name="createKC"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- CREATE A QUESTION ------------------------------------------------------------------
    # Redirect to Create Question
    path("dashboard/create-a-question/", views.createQuestion, name="createQuestion"),
    # Save the details of Question Submitted
    path('save_question', views.save_question, name='save_question'),
    # Save the details of Question's Options Submitted
    path('save_option', views.save_option, name='save_option'),
    # Save the question with Knowledge Check ID
    path('save_conquest_question', views.save_conquest_question, name='save_conquest_question'),
    # Upload the Media File
    path('upload_media_file', views.upload_media_file, name='upload_media_file'),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- ALL KNOWLEDGE CHECK ----------------------------------------------------------------
    # Redirect to All Knowledge Check
    path("dashboard/all-knowledge-check/", views.all_KC, name="all_KC"),
    # Filter All Knowledge Tests as per the Date Range Selected
    path("allkc_date_filter", views.allkc_date_filter, name="allkc_date_filter"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- SENT KNOWLEDGE CHECK ---------------------------------------------------------------
    # Redirect to Sent Knowledge Check
    path("dashboard/sent-knowledge-check/", views.sent_KC, name="sent_KC"),
    # Filter Sent Knowledge Tests as per the Date Range Selected
    path("sentkc_date_filter", views.sentkc_date_filter, name="sentkc_date_filter"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- PENDING KNOWLEDGE CHECK ------------------------------------------------------------
    # Redirect to Pending Knowledge Check
    path("dashboard/pending-knowledge-check/", views.pending_KC, name="pending_KC"),
    # Filter Pending Knowledge Tests as per the Date Range Selected
    path("pendingkc_date_filter", views.pendingkc_date_filter, name="pendingkc_date_filter"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- COMPLETED KNOWLEDGE CHECK ----------------------------------------------------------
    # Redirect to Completed Knowledge Check
    path("dashboard/completed-knowledge-check/", views.completed_KC, name="completed_KC"),
    # Filter Completed Knowledge Tests as per the Date Range Selected
    path("completedkc_date_filter", views.completedkc_date_filter, name="completedkc_date_filter"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- UPDATE SOURCE ----------------------------------------------------------------------
    # Redirect to Update Source
    path("dashboard/update_source_type/", views.listUpdateSource, name="listUpdateSource"),
    # CREATE NEW Update Source
    path('create_update_source', views.create_update_source, name='create_update_source'),
    # DELETE SELECTED Update Source
    path('delete_update_source', views.delete_update_source, name='delete_update_source'),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- UPDATE TYPE ------------------------------------------------------------------------
    # Redirect to Update Type
    path("dashboard/update_type/", views.listUpdateType, name="listUpdateType"),
    # Create Update Type
    path('create_UpdateType', views.create_UpdateType, name='create_UpdateType'),
    # Delete Update Type
    path('delete_UpdateType', views.delete_UpdateType, name='delete_UpdateType'),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- USERS ------------------------------------------------------------------------------
    # Redirect to Users
    path("dashboard/users/", views.listUsers, name="listUsers"),
    # Create/Register user with the associated account and project details provided
    path('create_user', views.create_user, name='create_user'),
    # Delete the user details from the account and project associated
    path('delete_user', views.delete_user, name='delete_user'),
    # Load the projects list as per the account selected from DropDown
    path("load_d_projects/", views.load_d_projects, name="load_d_projects"),
    # Upload/ Regsiter users in bulk using Excel template
    path('upload_users_file', views.upload_users_file, name="upload_users_file"),
    # Download the Users template
    path('download_user_template', views.download_user_template, name="download_user_template"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- SUB PROCESS ------------------------------------------------------------------------
    # Redirect to Sub-Process
    path("dashboard/sub_process/", views.listsub_process, name="listsub_process"),
    # Create Sub Process in a project
    path('create_sub_process', views.create_sub_process, name='create_sub_process'),
    # Delete Sub Process from the project
    path('delete_sub_process', views.delete_sub_process, name='delete_sub_process'),
    #Load the list of Sub Process for the accounts/projects User is associated
    path("load_sub_process/", views.load_sub_process, name="load_sub_process"),
    # Add User in a Selected Sub Process
    path('sub_process_add_user', views.sub_process_add_user, name='sub_process_add_user'),
    # Delete User from Associated Sub Process
    path('sub_process_del_user', views.sub_process_del_user, name='sub_process_del_user'),
    # Load List of Users in the selected project
    path("load_project_users/", views.load_project_users, name="load_project_users"),
    # Load List of Users in the selected project
    path("load_project_users_from_sp/", views.load_project_users_from_sp, name="load_project_users_from_sp"),
    # Load List of Users in the selected Sub Process
    path("load_sub_process_users/", views.load_sub_process_users, name="load_sub_process_users"),
    # Upload users in bulk in Subprocess using Excel template
    path('upload_subprocess_users_file', views.upload_subprocess_users_file, name="upload_subprocess_users_file"),
    # Download the Subprocess template
    path('download_sp_user_template', views.download_sp_user_template, name="download_sp_user_template"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- ADD ACCOUNTS -----------------------------------------------------------------------
    #Redirect to Add Account
    path("accounts/", views.listAccount, name="listAccount"),
    # Create Account
    path('sup_add_account', views.sup_add_account, name='sup_add_account'),
    # Delete Selected Account
    path('sup_del_account', views.sup_del_account, name='sup_del_account'),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- ADD PROJECTS -----------------------------------------------------------------------
    # Redirect to Add Project
    path("projects/", views.listProject, name="listProject"),
    # Add Project with the Selected Account
    path('sup_add_project', views.sup_add_project, name='sup_add_project'),
    # Delete Selected Project
    path('sup_del_project', views.sup_del_project, name='sup_del_project'),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- CREATE ADMIN -----------------------------------------------------------------------
    # Redirect to Create Admin
    path("admins/", views.listAdmin, name="listAdmin"),
    # Create Admin with the Account and Project Details
    path('sup_create_admin', views.sup_create_admin, name='sup_create_admin'),
    # Delete the Admin from the Account and Project
    path('sup_del_admin_entry', views.sup_del_admin_entry, name='sup_del_admin_entry'),
    # Change User Type
    path("change_user_type", views.change_user_type, name="change_user_type"),
# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- CREATE EMAIL TRIGGERS --------------------------------------------------------------
    # Send Pending Updates Reminders to Associates
    path('send_reminder', views.send_reminder, name='send_reminder'),
    # Send Pending Knowledge Test Reminders to Associates
    path('send_reminder_kc', views.send_reminder_kc, name='send_reminder_kc')
# ----------------------------------------------------------------------------------------------------------------------

]
