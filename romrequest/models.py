from django.db import models
import datetime


c_categories = (
    ('C','Contract'),
    ('F', 'Full Time Employee'),
)

c_types = (
    ('S','Support'),
    ('P', 'Project Agreement'),
)

c_additions = (
    ('A','New Hire'),
    ('R', 'Replacement'),
    ('T','Until fulltime is hired'),
    ('EXT', 'Extension'),
)

sbu = {
    ('club car','Club Car'),
    ('cts','CTS'),
    ('fluid','Fluid'),
    ('power tools and lifting','Power Tools and Lifting'),
}

loction = {
    ('bangalore','Bangalore'),
    ('chennai','Chennai'),
    ('coimbatore','Coimbatore'),
}

project = {
    ('sample','Sample'),
    ('sample1','Sample1')
}


class RomRequest(models.Model):
    c_categories = models.CharField(max_length=2, choices=c_categories, default='C')
    c_types = models.CharField(max_length=2, choices=c_types, default='S')
    c_additions = models.CharField(max_length=3, choices=c_additions, default='A')
    sbu = models.CharField(max_length=30, choices=sbu, default='cts')
    loction = models.CharField(max_length=30, choices=loction, default='bangalore')
    project = models.CharField(max_length=30, choices=project, default='sample')
    no_of_resources_required = models.IntegerField(default=1)
    skillset_needed = models.TextField(default="Python")
    attachment = models.FileField(blank=True, null=True)
    expected_onboard_date = models.DateField(default=datetime.date.today)
    request_date = models.DateTimeField(auto_now_add=True)
    duration_of_contract = models.IntegerField(default=5)
    comments = models.TextField(default="Test")
    requested_by = models.CharField(max_length=100,default="admin")
    requested_user_email = models.CharField(max_length=100,default="email@sample.com")
    manager_id_1 = models.CharField(max_length=100,default="Name")
    manager_id_1_email = models.CharField(max_length=100,default="email@sample.com")
    manager_id_2 = models.CharField(max_length=100,default="Name")
    manager_id_2_email = models.CharField(max_length=100,default="email@sample.com")
    request_status = models.CharField(max_length=10,default=0)

    def __str__(self):
        return self.project

class Employees(models.Model):
    emp_ps_id = models.CharField(max_length=15)
    alternate_id = models.CharField(max_length=15)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emp_type = models.CharField(max_length=20)
    emp_domain_id = models.CharField(unique=True, max_length=25)
    group = models.CharField(max_length=50)
    m_leader_list_id = models.IntegerField()
    sector = models.CharField(max_length=25)
    email_id = models.CharField(max_length=50)
    location = models.CharField(max_length=10)
    alternate_location = models.CharField(max_length=150)
    m_location_id = models.IntegerField()
    date_of_joining = models.DateField(null=True)
    manager_ps_id = models.CharField(max_length=15)
    manager_name = models.CharField(max_length=50)
    mgr_domain_id = models.CharField(max_length=15)
    country_code = models.CharField(max_length=3)
    emp_report = models.IntegerField()
    emp_loc_change = models.IntegerField()
    epm_name = models.CharField(max_length=100)
    epm_group = models.IntegerField()
    cost_center = models.CharField(max_length=50)
    non_etc = models.IntegerField()
    long_term_contract = models.IntegerField()
    delete_flag = models.CharField(max_length=2)
    deleted_by = models.CharField(max_length=22)
    deleted_date = models.DateField(null=True)
    created_by = models.CharField(max_length=15)
    created_date = models.DateField(null=True)
    modified_by = models.CharField(max_length=15)
    modified_date = models.DateField(null=True)

    def __str__(self):
        return self.emp_domain_id

class CEmployees(models.Model):
    contract_id = models.IntegerField()
    con_first_name = models.CharField(max_length=40)
    con_last_name = models.CharField(max_length=20, null=True)
    con_middle_name = models.CharField(max_length=40, null=True)
    con_domain_id = models.CharField(max_length=25)
    con_email = models.CharField(max_length=50)
    c_location_id = models.IntegerField()
    con_join_date = models.DateField(null=True)
    con_extended_date = models.DateField(null=True)
    onboard_date = models.DateField(null=True)
    con_end_date = models.DateField(null=True)
    con_notice_period = models.IntegerField()
    c_employer_id = models.IntegerField()
    con_manager_ps_id = models.IntegerField()
    con_manager_name = models.CharField(max_length=250, null=True)
    con_duration = models.CharField(max_length=10, null=True)
    pa_number = models.CharField(max_length=25, null=True)
    current_hc_pa = models.IntegerField()
    actual_hc_deployed = models.IntegerField()
    comments = models.CharField(max_length=300, null=True)
    mgr_approval_status = models.CharField(max_length=3, null=True)
    contract_category = models.IntegerField()
    contract_type = models.CharField(max_length=10)
    pmo_head = models.CharField(max_length=1)
    pmo_comments = models.CharField(max_length=950, null=True)
    c_requisition_id = models.IntegerField()
    con_price = models.CharField(max_length=250, null=True)
    con_price_per_hour = models.CharField(max_length=100, null=True)
    con_attachement = models.IntegerField()
    extension_status = models.IntegerField()
    long_term_contract = models.IntegerField()
    delete_flag_status = models.IntegerField()
    delete_flag = models.CharField(max_length=1)
    deleted_by = models.CharField(max_length=25)
    deleted_date = models.DateField(null=True)
    created_by = models.CharField(max_length=25, null=True)
    created_date = models.DateField(null=True)
    modified_by = models.CharField(max_length=25, null=True)
    modified_date = models.DateField(null=True)

    def __str__(self):
        return self.con_domain_id