from django.db import models

SIGN_USER_CHOICES = (
    ("0", "球员"),
    ("1", "球迷")
)

USER_POSITION = (
    ("gk","守门员"),
    ("sw", "清道夫"),
    ("cb", "中后卫"),
    ("lcb", "左中后卫"),
    ("rcb", "右中后卫"),
    ("lb", "左后卫"),
    ("rb", "右后卫"),
    ("lwb","左边后卫"),
    ("rwb","右边后卫"),
    ("dmf", "后腰"),
    ("swf", "边前卫"),
    ("lmf", "左边前卫"),
    ("rmf", "右边前卫"),
    ("AMF", "前卫"),
    ("lwm", "左边中场"),
    ("lm", "左中场"),
    ("lcm", "左中中场"),
    ("cm", "中场"),
    ("lwm", "右边中场"),
    ("lm", "右中场"),
    ("lcm", "右中中场"),
    ("OMF", "前腰"),
    ("wf", "边锋"),
    ("lwf", "左边锋"),
    ("lf", "左前锋"),
    ("ls", "左中锋"),
    ("cf", "中锋"),
    ("rs", "右中锋"),
    ("rf", "右前锋"),
    ("rwf", "右边锋"),
    ("ss", "影子前锋")
    )

class User(models.Model):
    username = models.CharField(max_length=100, verbose_name="昵称")
    wechat_username = models.CharField(max_length=100, verbose_name="微信用户名")
    realname = models.CharField(max_length=100, null=True, blank=True, verbose_name="真实姓名")
    birth = models.DateField(null=True, blank=True, verbose_name="生日")
    user_tag = models.CharField(choices=SIGN_USER_CHOICES, max_length=5, verbose_name="用户类型")
    position = models.CharField(choices=USER_POSITION, null=True, blank=True, max_length=5, verbose_name="常踢位置")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    image = models.ImageField(upload_to="images/%Y/%m", blank=True, max_length=100,
                              verbose_name="头像")

    class Meta:
        verbose_name = "注册用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class RealUser(models.Model):
    realname = models.CharField(max_length=100, verbose_name="姓名")

    class Meta:
        verbose_name = "真实用户姓名"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
