from django.db import models


# Create your models here.

class Tag(models.Model):
    state_type_choices = ((1, "正常"), (2, "尚未激活"), (3, "标签冻结"))

    name = models.CharField(max_length=30, db_column="name")
    created_on = models.DateTimeField(db_column="created_on", auto_now_add=True)
    created_by = models.CharField(max_length=255, db_column="created_by")
    is_deleted = models.BooleanField(default=False, db_column="is_deleted")
    state = models.IntegerField(db_column="state", default=1, choices=state_type_choices)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    state_type_choices = ((1, "正常"), (2, "尚未激活"), (3, "冻结"))

    tag = models.ForeignKey(db_column="tag_id", null=False,
                            on_delete=models.CASCADE, to="Tag", to_field="id")
    title = models.CharField(max_length=255, db_column="title", null=False)
    desc = models.CharField(max_length=255, db_column="desc", null=False)
    content = models.TextField(db_column="content", null=False)

    cover_image = models.ImageField("图片", db_column="cover_image", upload_to='article_img/%Y/%m/%d')

    created_on = models.DateTimeField(db_column="created_on", auto_now_add=True)
    created_by = models.CharField(max_length=255, db_column="created_by")
    is_deleted = models.BooleanField(default=False, db_column="is_deleted")
    state = models.IntegerField(db_column="state", default=1, choices=state_type_choices)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
