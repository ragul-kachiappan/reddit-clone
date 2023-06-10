from django.contrib import auth
from django.db import models

User = auth.get_user_model()


class LanguageMaster(models.Model):
    name = models.CharField(max_length=100)
    language_code = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "language_master"


class TrophyMaster(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "trophy_master"


class SocialMediaMaster(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "social_media_master"


class CountryMaster(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "country_master"


class SortOptionsMaster(models.Model):
    sort_option = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sort_option

    class Meta:
        db_table = "sort_options_master"


class ContentViewMaster(models.Model):
    content_option = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content_option

    class Meta:
        db_table = "content_view_master"


class SubscriptionsMaster(models.Model):
    plan_name = models.CharField(max_length=100)
    plan_cost = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plan_name

    class Meta:
        db_table = "subscriptions_master"


class UserLoginDetails(models.Model):
    user = models.ForeignKey(
        User,
        related_name="auth_user",
        on_delete=models.CASCADE,
        verbose_name="auth user table",
    )
    device_id = models.CharField(max_length=255, blank=True, default="")
    platform = models.CharField(max_length=32, blank=True, default="")
    notification_id = models.CharField(max_length=2054, blank=True, default="")
    ip_address = models.CharField(max_length=128, blank=True, default="")
    login_time = models.CharField(max_length=256, blank=True, default="")
    logout_time = models.CharField(max_length=256, blank=True, default="")
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "user_login_details"


class ResetTokenLog(models.Model):
    """
    Used to store password reset token information.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=500, blank=True, default="")
    is_expired = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "reset_token_log"


class UserProfileDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, blank=True, null=True)
    about = models.CharField(max_length=300, blank=True, null=True)
    is_nsfw = models.BooleanField(default=False)
    allow_profile_follow = models.BooleanField(default=True)
    allow_visibility = models.BooleanField(default=True)
    allow_community_visibility = models.BooleanField(default=True)
    allow_search_visibility = models.BooleanField(default=True)
    allow_personalize_outbound_link = models.BooleanField(default=True)
    allow_personalize_ads_activity = models.BooleanField(default=True)
    allow_personalize_ads_partner_info = models.BooleanField(default=True)
    allow_personalize_ads_partner_activity = models.BooleanField(default=True)
    allow_personalize_recomm_location = models.BooleanField(default=True)
    allow_personalize_recomm_partner_activity = models.BooleanField(
        default=True
    )
    allow_2FA = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name

    class Meta:
        db_table = "user_profile_details"


class UserSettingDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_link = models.CharField(max_length=1024, blank=True, null=True)
    cover_link = models.CharField(max_length=1024, blank=True, null=True)
    online_status = models.BooleanField(default=False)
    dark_mode = models.BooleanField(default=False)
    GENDER_CHOICES = [
        ("man", "Man"),
        ("woman", "Woman"),
        ("prefer_not_to_say", "Prefer Not to Say"),
        ("custom", "I Refer to Myself As"),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    custom_gender = models.CharField(max_length=100, blank=True, null=True)
    display_language = models.ForeignKey(
        LanguageMaster, on_delete=models.CASCADE
    )
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE)
    allow_beta_tests = models.BooleanField(default=False)
    opt_out_of_redesign = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def set_online(self):
        self.is_online = True
        self.save(update_fields=["is_online"])

    def set_offline(self):
        self.is_online = False
        self.save(update_fields=["is_online"])

    def save(self, *args, **kwargs):
        if self.gender != "custom":
            self.custom_gender = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "user_setting_details"


class UserBlockList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user"
    )
    blocked_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blocked_users"
    )
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} blocked {self.blocked_user}"

    class Meta:
        db_table = "user_block_list"
        constraints = [
            models.CheckConstraint(
                check=~models.Q(user=models.F("blocked_user")),
                name="user_not_equal_blocked_user",
            )
        ]
        unique_together = ("user", "blocked_user")


class UserSocialLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    social_media = models.CharField(max_length=500)
    link = models.CharField(max_length=1024)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.social_media}"

    class Meta:
        db_table = "user_social_link"


class UserTrophyCase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trophy = models.ForeignKey(TrophyMaster, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.trophy.name}"

    class Meta:
        db_table = "user_trophy_case"


class UserContentLanguages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(LanguageMaster, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.language.name}"

    class Meta:
        db_table = "user_content_languages"


class CommunityMuteList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subreddit = models.CharField(
        max_length=1024
    )  # to be changed into a foreign key once subreddit model is added
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.subreddit}"

    class Meta:
        db_table = "community_mute_list"


class UserFeedSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    allow_nsfw = models.BooleanField(default=False)
    blur_nsfw = models.BooleanField(default=False)
    allow_home_feed_recomm = models.BooleanField(default=True)
    allow_autoplay_media = models.BooleanField(default=True)
    allow_reduce_animations = models.BooleanField(default=False)
    allow_community_themes = models.BooleanField(default=True)
    community_content_sort = models.ForeignKey(
        SortOptionsMaster, on_delete=models.CASCADE
    )
    remember_sort_per_comm = models.BooleanField(default=False)
    global_content_view = models.ForeignKey(
        ContentViewMaster, on_delete=models.CASCADE
    )
    remember_content_view_per_comm = models.BooleanField(default=False)
    open_post_in_new_tab = models.BooleanField(default=False)
    markdown_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "user_feed_settings"


class UserNotificationSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    allow_inbox_messages = models.BooleanField(default=True)
    allow_chat_messages = models.BooleanField(default=True)
    allow_chat_requests = models.BooleanField(default=True)
    allow_mentions_of_username = models.BooleanField(default=True)
    allow_comments_user_posts = models.BooleanField(default=True)
    allow_upvotes_on_user_posts = models.BooleanField(default=True)
    allow_replies_to_user_comments = models.BooleanField(default=True)
    allow_activity_on_user_comments = models.BooleanField(default=True)
    allow_activity_on_user_threads = models.BooleanField(default=True)
    allow_activity_on_user_chat_posts = models.BooleanField(default=True)
    allow_new_followers = models.BooleanField(default=True)
    allow_new_post_flair = models.BooleanField(default=True)
    allow_new_user_flair = models.BooleanField(default=True)
    allow_pinned_posts = models.BooleanField(default=True)
    allow_awards_user_receive = models.BooleanField(default=True)
    allow_posts_user_follow = models.BooleanField(default=True)
    allow_comments_user_follow = models.BooleanField(default=True)
    allow_reddit_talk_in_user_comm = models.BooleanField(default=True)
    allow_trending_posts = models.BooleanField(default=True)
    allow_broadcast_recommendations = models.BooleanField(default=True)
    allow_community_recommendations = models.BooleanField(default=True)
    allow_rereddit = models.BooleanField(default=True)
    allow_reddit_announcements = models.BooleanField(default=True)
    allow_cake_day = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "user_notification_settings"


class UserEmailSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    allow_inbox_messages = models.BooleanField(default=True)
    allow_chat_requests = models.BooleanField(default=True)
    new_user_welcome = models.BooleanField(default=False)
    allow_comments_on_user_posts = models.BooleanField(default=True)
    allow_replies_to_user_comments = models.BooleanField(default=True)
    allow_upvotes_on_user_posts = models.BooleanField(default=True)
    allow_upvotes_on_user_comments = models.BooleanField(default=True)
    allow_username_mentions = models.BooleanField(default=True)
    allow_new_followers = models.BooleanField(default=True)
    allow_daily_digest = models.BooleanField(default=False)
    allow_weekly_recap = models.BooleanField(default=False)
    allow_community_discovery = models.BooleanField(default=False)
    unsubscribe_all = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "user_email_settings"


class UserSubscriptionsDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(
        SubscriptionsMaster, on_delete=models.CASCADE
    )
    subscription_start_date = models.DateTimeField(null=True, blank=True)
    subscription_end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.subscription_plan.plan_name}"

    class Meta:
        db_table = "user_subscriptions_details"
