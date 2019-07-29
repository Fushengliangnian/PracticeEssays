#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :
# from applepush import ApplePush
#
# apns = ApplePush('证书文件名称', 'bundle ID')
# resp = apns.single_push('苹果设备token', "推送内容")


# s = "https:\/\/accounts.google.com\/o\/oauth2\/auth?scope=https:\/\/www.googleapis.com\/auth\/androidpublisher&response_type=code&access_type=offline&redirect_uri=http:\/\/localhost:8007\/v1\/subscription\/auth_callback&client_id=620346855846-tvpld1acij94b2jhav0l5glci4cqdvfa.apps.googleusercontent.com".replace("\\", "")
# print(s)

if __name__ == '__main__':
    s = "ads\nasdd\n"
    a = s.strip("\n")

    # def fun(a, b, c, d):
    #     print(a, b, c, d)
    #
    #
    # fun(b=1, a=2, d=3, c=4)

    d1 = {'monthly_amount': '%s / month ', 'annual_amount': ' / year ',
          'all_instrument_subtitle': 'Unlock All Courses(Guitar & Ukulele)\nUnlimited Weekly Updated Songs\nUnlimited Chords Library Access\nUnlimited 3D Fingering Demostrating\nUnlimited Reverse Chords Finder',
          'single_instrument_subtitle': 'Unlock %s Lessons\nUnlimited %s Songs(Weekly update)\nUnlimited Chords Library Access\nUnlimited 3D Fingering Demostrating\nUnlimited Reverse Chords Finder',
          'monthly_free_trial_days': '3 DAYS FREE TRIAL', 'annual_free_trial_days': '7 DAYS FREE TRIAL',
          'guitar_title': 'null', 'ukulele_title': 'null', 'all_title': 'null'}
    d2 = {"ukulele_monthly": "okmusician.monthly.ukulele", "ukulele_amount": "okmusician.yearly.ukulele",
          "guitar_monthly": "okmusician.monthly.guitar", "guitar_amount": "okmusician.yearly.guitar",
          "all_monthly": "okmusician.monthly.all", "all_amount": "okmusician.yearly.all"}

    d1.update(d2)
    print(d1)
