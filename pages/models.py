from django.db import models


class Navigation(models.Model):
    nav_parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父导航栏", related_name="nav_sub",
                                   on_delete=models.CASCADE)
    nav_img = models.CharField(max_length=20, null=True, blank=True, verbose_name="显示图标")
    nav_text = models.CharField(max_length=100, verbose_name="显示文本")
    nav_url = models.CharField(max_length=100, null=True, blank=True, verbose_name="导航地址")
    is_enable = models.BooleanField(default=True, verbose_name="是否可用")
    orders = models.IntegerField(default=0, verbose_name="排序")
    permission_code = models.CharField(max_length=50, verbose_name="权限编码", null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "导航栏"
        verbose_name_plural = verbose_name
        ordering = ["orders"]

    def __str__(self):
        return self.nav_text

    def has_submenu(self):
        return self.nav_sub.count() > 0
