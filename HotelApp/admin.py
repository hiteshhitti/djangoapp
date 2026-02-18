from django.contrib import admin
from .models import (
    Authorregis,
    Online_Booking,
    Offline_Booking,
    Add_Employee,
    Add_Room,
    Add_Salarys
)

@admin.register(Authorregis)
class AuthorregisAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Fname', 'Lname', 'Email', 'Phone_Number', 'Date')
    search_fields = ('Fname', 'Lname', 'Email')

@admin.register(Online_Booking)
class OnlineBookingAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Name', 'Email', 'Phone_Number', 'Check_in', 'Check_out')
    search_fields = ('Name', 'Email')
    list_filter = ('Date',)

@admin.register(Offline_Booking)
class OfflineBookingAdmin(admin.ModelAdmin):
    list_display = ('Customer_Id', 'First_Name', 'Email', 'Mobile_Number', 'Select_Room')
    search_fields = ('First_Name', 'Email')
    list_filter = ('Date',)

@admin.register(Add_Employee)
class AddEmployeeAdmin(admin.ModelAdmin):
    list_display = ('Employee_Id', 'First_Name', 'Last_Name', 'Departments', 'Mobile_Number')
    search_fields = ('First_Name', 'Last_Name', 'Employee_Id')
    list_filter = ('Departments',)

@admin.register(Add_Room)
class AddRoomAdmin(admin.ModelAdmin):
    list_display = ('Room_Number', 'Room_Type', 'Room_Floor', 'Room_Price')
    search_fields = ('Room_Number', 'Room_Type')
    list_filter = ('Room_Type', 'Room_Floor')

@admin.register(Add_Salarys)
class AddSalaryAdmin(admin.ModelAdmin):
    list_display = ('Employee_Id', 'Employee_Name', 'Departments', 'Salary', 'Date')
    search_fields = ('Employee_Name', 'Departments')
