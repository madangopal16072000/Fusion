from django.contrib import admin

from .models import (Bonafide, BranchChange, CourseRequested, CoursesMtech, FeePayments, FinalRegistration, InitialRegistration, InitialRegistrations,
                     MinimumCredits, Register, StudentRegistrationChecks, Thesis,
                     StudentRegistrationCheck, FinalRegistrations,
                     ThesisTopicProcess, FeePayment, TeachingCreditRegistration,
                     SemesterMarks, MarkSubmissionCheck,Dues,MTechGraduateSeminarReport,PhDProgressExamination,AssistantshipClaim,MessDue,Assistantship_status, course_registration)

class RegisterAdmin(admin.ModelAdmin):
    model = Register
    search_fields = ('curr_id__course_code',)

class InitialRegistrationsAdmin(admin.ModelAdmin):
    model = InitialRegistrations
    raw_id_fields = ("student_id",)
    search_fields = ('student_id__id__id',)

class StudentRegistrationCheckAdmin(admin.ModelAdmin):
    model = StudentRegistrationCheck
    raw_id_fields = ("student",)


admin.site.register(Thesis)
admin.site.register(Register,RegisterAdmin)
admin.site.register(InitialRegistrations,InitialRegistrationsAdmin)
admin.site.register(BranchChange)
admin.site.register(CoursesMtech)
admin.site.register(MinimumCredits)
admin.site.register(StudentRegistrationCheck, StudentRegistrationCheckAdmin)
admin.site.register(FinalRegistrations)
admin.site.register(ThesisTopicProcess)
admin.site.register(FeePayment)
admin.site.register(TeachingCreditRegistration)
admin.site.register(SemesterMarks)
admin.site.register(MarkSubmissionCheck)
admin.site.register(Dues)
admin.site.register(AssistantshipClaim)
admin.site.register(PhDProgressExamination)
admin.site.register(MTechGraduateSeminarReport)
admin.site.register(MessDue)
admin.site.register(Assistantship_status)
#These are new tables as a replcement of existing ones
admin.site.register(course_registration)
admin.site.register(FeePayments)
admin.site.register(CourseRequested)
admin.site.register(InitialRegistration)
admin.site.register(FinalRegistration)
admin.site.register(StudentRegistrationChecks)
#TODO: Remove the old tables