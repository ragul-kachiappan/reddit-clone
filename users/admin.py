from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.LanguageMaster)
admin.site.register(models.CountryMaster)
admin.site.register(models.ContentViewMaster)
admin.site.register(models.SocialMediaMaster)
admin.site.register(models.SortOptionsMaster)
admin.site.register(models.SubscriptionsMaster)
admin.site.register(models.TrophyMaster)
admin.site.register(models.UserLoginDetails)
admin.site.register(models.ResetTokenLog)
admin.site.register(models.UserSettingDetails)
admin.site.register(models.UserProfileDetails)
admin.site.register(models.UserFeedSettings)
admin.site.register(models.UserNotificationSettings)
admin.site.register(models.UserEmailSettings)
admin.site.register(models.UserContentLanguages)
admin.site.register(models.UserBlockList)
admin.site.register(models.UserSocialLink)
admin.site.register(models.UserSubscriptionsDetails)
admin.site.register(models.UserTrophyCase)
admin.site.register(models.CommunityMuteList)
