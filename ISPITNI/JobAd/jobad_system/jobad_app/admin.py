from django.contrib import admin
from .models import SystemUser, JobAd, Application


# Register your models here.

class SystemUserAdmin (admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_delete_permission(self, request, obj = None):
        return False

class JobAdAdmin (admin.ModelAdmin):
    exclude = ('recruiter',)
    def has_add_permission(self, request):
        return SystemUser.objects.filter(user = request.user,role='recruiter').exists()

    def save_model(self, request, obj, form, change):
        if not change:
            recruiter = SystemUser.objects.filter(user= request.user).first()
            obj.recruiter = recruiter
        return super().save_model(request, obj, form, change)
    def has_change_permission(self, request, obj:JobAd = None):
        if obj:
            kreator_kompanija = obj.recruiter.company
            menuvach = SystemUser.objects.filter(user = request.user, role='recruiter').first()
            if menuvach:
                return menuvach.company == kreator_kompanija
            # return SystemUser.objects.filter(  )
            return False

    def has_delete_permission(self, request, obj = ...):
        return not Application.objects.filter(job_ad=obj).exists()

class ApplicationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = Application.objects.all()
        recruiter = SystemUser.objects.filter(user=request.user,role='recruiter').first()
        if not recruiter:
            return qs.none()
        return qs.filter(job_ad__recruiter__company = recruiter.company)
