from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('menu_item', 'quantity')
    can_delete = False
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'created_at', 'is_completed')
    list_filter = ('is_completed', 'created_at')
    inlines = [OrderItemInline]
    actions = ['mark_as_completed']

    @admin.action(description='Mark selected orders as completed')
    def mark_as_completed(self, request, queryset):
        queryset.update(is_completed=True)
