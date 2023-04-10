from django.contrib import admin
# 导入和导出
from import_export.admin import ImportExportModelAdmin
# 只导出
# from import_export.admin import ExportActionModelAdmin
from yn_museum.models import Visitor,Order,Order_Type,Group
from import_export import resources
from django.utils.html import format_html

# 访客管理
class ProxyResource1(resources.ModelResource):
    # 让导入导出的表头为中文
    def __init__(self):
        super(ProxyResource1, self).__init__()
        # 获取模型的字段列表,
        field_list = Visitor._meta.fields
        # 做成一个{字段名:中文名}的字典，作为成员变量
        self.vname_dict = {i.name: i.verbose_name for i in field_list}

    def get_fields(self, **kwargs):
        fields = super().get_fields(**kwargs)
        for field in fields:
            field_name = self.get_field_name(field)
            # 自定义导出字段里可能有关联关系，但vname_dict肯定没有双下划线，所以必须处理
            if field_name.find("__") > 0:
                # 如果是关联关系的，只取字段名，不找关联，因为关联内容不在vname_dict里
                field_name = field_name.split("__")[0]
            # 如果此字段有verbose_name，就用
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    class Meta:
        model = Visitor
        excloud = (
            "ID"
        )

class Visitoradmin(ImportExportModelAdmin):
    list_per_page = 100
    list_display = ['name', 'idnumber']
    list_display_links = ('name',)
    resource_class = ProxyResource1
    save_as_continue = False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        return super(Visitoradmin, self).change_view(request, object_id,
                                                     form_url, extra_context=extra_context)

# 预约管理
class ProxyResource(resources.ModelResource):
    # 让导入导出的表头为中文
    def __init__(self):
        super(ProxyResource, self).__init__()
        # 获取模型的字段列表,
        field_list = Order._meta.fields
        # 做成一个{字段名:中文名}的字典，作为成员变量
        self.vname_dict = {i.name: i.verbose_name for i in field_list}

    def get_fields(self, **kwargs):
        fields = super().get_fields(**kwargs)
        for field in fields:
            field_name = self.get_field_name(field)
            # 自定义导出字段里可能有关联关系，但vname_dict肯定没有双下划线，所以必须处理
            if field_name.find("__") > 0:
                # 如果是关联关系的，只取字段名，不找关联，因为关联内容不在vname_dict里
                field_name = field_name.split("__")[0]
            # 如果此字段有verbose_name，就用
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    class Meta:
        model = Order
        excloud = (
            "ID"
        )


class Orderadmin(ImportExportModelAdmin):
    list_per_page = 100
    list_display = ['Encoded', 'Type', 'EnterTime', "Name","idnumber2", "State_color"]
    list_display_links = ('Encoded',)
    resource_class = ProxyResource
    save_as_continue = False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        return super(Orderadmin, self).change_view(request, object_id,
                                                   form_url, extra_context=extra_context)
    def State_color(self,object):
        return format_html(
            '<span style="color:black;">{}</span>',
            object.State
        )
    State_color.short_description = '预约状态'
# 预约类型：
class ProxyResource2(resources.ModelResource):
    # 让导入导出的表头为中文
    def __init__(self):
        super(ProxyResource2, self).__init__()
        # 获取模型的字段列表,
        field_list = Order_type._meta.fields
        # 做成一个{字段名:中文名}的字典，作为成员变量
        self.vname_dict = {i.name: i.verbose_name for i in field_list}

    def get_fields(self, **kwargs):
        fields = super().get_fields(**kwargs)
        for field in fields:
            field_name = self.get_field_name(field)
            # 自定义导出字段里可能有关联关系，但vname_dict肯定没有双下划线，所以必须处理
            if field_name.find("__") > 0:
                # 如果是关联关系的，只取字段名，不找关联，因为关联内容不在vname_dict里
                field_name = field_name.split("__")[0]
            # 如果此字段有verbose_name，就用
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    class Meta:
        model = Order_Type
        excloud = (
            "ID"
        )
class Order_type_admin(ImportExportModelAdmin):
    list_per_page = 10
    list_display = ["type_color"]
    resource_class = ProxyResource2
    save_as_continue = False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        return super(Order_type_admin, self).change_view(request, object_id,
                                                   form_url, extra_context=extra_context)

# 修改字体颜色
    def type_color(self,object):
        return format_html(
            '<span style="color:#2b669a;">{}</span>',
            object.Type
        )

    type_color.short_description = '预约类型'


    # 团体预约管理
class ProxyResource3(resources.ModelResource):
    # 让导入导出的表头为中文
    def __init__(self):
        super(ProxyResource3, self).__init__()
        # 获取模型的字段列表,
        field_list = Group._meta.fields
        # 做成一个{字段名:中文名}的字典，作为成员变量
        self.vname_dict = {i.name: i.verbose_name for i in field_list}

    def get_fields(self, **kwargs):
        fields = super().get_fields(**kwargs)
        for field in fields:
            field_name = self.get_field_name(field)
            # 自定义导出字段里可能有关联关系，但vname_dict肯定没有双下划线，所以必须处理
            if field_name.find("__") > 0:
                # 如果是关联关系的，只取字段名，不找关联，因为关联内容不在vname_dict里
                field_name = field_name.split("__")[0]
            # 如果此字段有verbose_name，就用
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    class Meta:
        model = Group
        excloud = (
            "ID"
        )
class Group_admin(ImportExportModelAdmin):
    list_per_page = 20
    list_display = ["Name","Date","number","state","notes"]
    resource_class = ProxyResource3
    save_as_continue = False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        return super(Group_admin, self).change_view(request, object_id,
                                                   form_url, extra_context=extra_context)


admin.site.register(Visitor, Visitoradmin)
admin.site.register(Order, Orderadmin)
admin.site.register(Order_Type, Order_type_admin)
admin.site.register(Group, Group_admin)


admin.site.site_header = "上饶市博物馆管理后台"
admin.site.site_title = "上饶市博物馆管理后台"
admin.site.index_title = "上饶市博物馆管理后台"
