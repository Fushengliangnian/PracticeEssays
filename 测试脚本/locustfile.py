from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task
    def router0(self):
        self.client.get('/v3/test/?')
    @task
    def router1(self):
        self.client.get('/v3/test/(\w+)/?')
    @task
    def router2(self):
        self.client.get('/v3/test/(\w+)/(.+)/?')
    @task
    def router3(self):
        self.client.get('/v3/?')
    @task
    def router4(self):
        self.client.get('/v3/help/?')
    @task
    def router5(self):
        self.client.get('/v3/help/test_log/?')
    @task
    def router6(self):
        self.client.get('/v3/help/promo_code/?')
    @task
    def router7(self):
        self.client.get('/v3/help/payment_info/(\d+)/?')
    @task
    def router8(self):
        self.client.get('/v3/help/payment_code_info/(\d+)/?')
    @task
    def router9(self):
        self.client.get('/v3/start/?')
    @task
    def router10(self):
        self.client.get('/v3/query_configs/?')
    @task
    def router11(self):
        self.client.get('/v3/update_configs/?')
    @task
    def router12(self):
        self.client.get('/v3/get_purcahse_data/?')
    @task
    def router13(self):
        self.client.get('/v3/tiyan_login/?')
    @task
    def router14(self):
        self.client.get('/v3/account/profile/?')
    @task
    def router15(self):
        self.client.get('/v3/account/token/?')
    @task
    def router16(self):
        self.client.get('/v3/account/rapid_login/wait/(\w+)/?')
    @task
    def router17(self):
        self.client.get('/v3/account/rapid_login/confirm/(\w+)/?')
    @task
    def router18(self):
        self.client.get('/v3/uploads/token/?')
    @task
    def router19(self):
        self.client.get('/v3/uploads/callback/?')
    @task
    def router20(self):
        self.client.get('/v3/users/?')
    @task
    def router21(self):
        self.client.get('/v3/users/(\d+)/?')
    @task
    def router22(self):
        self.client.get('/v3/users/reg/?')
    @task
    def router23(self):
        self.client.get('/v3/me/?')
    @task
    def router24(self):
        self.client.get('/v3/users/create_admin/?')
    @task
    def router25(self):
        self.client.get('/v3/users/update_admin_menus/?')
    @task
    def router26(self):
        self.client.get('/v3/users/login/?')
    @task
    def router27(self):
        self.client.get('/v3/users/(\d+)/courses/?')
    @task
    def router28(self):
        self.client.get('/v3/courses/?')
    @task
    def router29(self):
        self.client.get('/v3/courses/index?')
    @task
    def router30(self):
        self.client.get('/v3/courses/(\d+)/share/?')
    @task
    def router31(self):
        self.client.get('/v3/courses/(\d+)/share_info/?')
    @task
    def router32(self):
        self.client.get('/v3/courses/(\d+)/?')
    @task
    def router33(self):
        self.client.get('/v3/courses/(\d+)/highlights/?')
    @task
    def router34(self):
        self.client.get('/v3/courses/payment_callback/?')
    @task
    def router35(self):
        self.client.get('/v3/course_purchases/?')
    @task
    def router36(self):
        self.client.get('/v3/course_purchases/(\d+)/?')
    @task
    def router37(self):
        self.client.get('/v3/channel_active_course/?')
    @task
    def router38(self):
        self.client.get('/v3/course_phone_purchases?')
    @task
    def router39(self):
        self.client.get('/v3/active_course/?')
    @task
    def router40(self):
        self.client.get('/v3/deactive_course/?')
    @task
    def router41(self):
        self.client.get('/v3/courses/apple_pay/?')
    @task
    def router42(self):
        self.client.get('/v3/courses/all_materials/(\d+)/?')
    @task
    def router43(self):
        self.client.get('/v3/courses/guitar_tutorial_info/?')
    @task
    def router44(self):
        self.client.get('/v3/courses/my_required_courses/?')
    @task
    def router45(self):
        self.client.get('/v3/courses/(\d+)/required_info?')
    @task
    def router46(self):
        self.client.get('/v3/courses/elective_course?')
    @task
    def router47(self):
        self.client.get('/v3/courses/elective_buyed/?')
    @task
    def router48(self):
        self.client.get('/v3/courses/recommend_course?')
    @task
    def router49(self):
        self.client.get('/v3/courses/switch_course/?')
    @task
    def router50(self):
        self.client.get('/v3/courses/record_recmmends')
    @task
    def router51(self):
        self.client.get('/v3/courses/payment_back_class')
    @task
    def router52(self):
        self.client.get('/v3/courses/feedback')
    @task
    def router53(self):
        self.client.get('/v3/courses/hongbao_coupon')
    @task
    def router54(self):
        self.client.get('/v3/courses/active_users')
    @task
    def router55(self):
        self.client.get('/v3/courses/study_schedule')
    @task
    def router56(self):
        self.client.get('/v3/courses/my_course')
    @task
    def router57(self):
        self.client.get('/v3/invite/invite_fission')
    @task
    def router58(self):
        self.client.get('/v3/invite/get_invite_info')
    @task
    def router59(self):
        self.client.get('/v3/invite/invite_coupon')
    @task
    def router60(self):
        self.client.get('/v3/invite/invite_count')
    @task
    def router61(self):
        self.client.get('/v3/invite/invite_count_qr')
    @task
    def router62(self):
        self.client.get('/v3/courses/(\d+)/lessons/?')
    @task
    def router63(self):
        self.client.get('/v3/lessons/?')
    @task
    def router64(self):
        self.client.get('/v3/lessons/(\d+)/?')
    @task
    def router65(self):
        self.client.get('/v3/lessons/(\d+)/materials/?')
    @task
    def router66(self):
        self.client.get('/v3/lessons/(\d+)/bind_material/(\d+)/?')
    @task
    def router67(self):
        self.client.get('/v3/lessons/update_material_binding/(\d+)/?')
    @task
    def router68(self):
        self.client.get('/v3/lessons/unbind_material/(\d+)/?')
    @task
    def router69(self):
        self.client.get('/v3/lessons/(\d+)/submit_review/?')
    @task
    def router70(self):
        self.client.get('/v3/lessons/(\d+)/review/?')
    @task
    def router71(self):
        self.client.get('/v3/lessons/(\d+)/home_work?')
    @task
    def router72(self):
        self.client.get('/v3/lessons/lesson_pass/?')
    @task
    def router73(self):
        self.client.get('/v3/lessons/lesson_info/?')
    @task
    def router74(self):
        self.client.get('/v3/materials/?')
    @task
    def router75(self):
        self.client.get('/v3/materials/(\d+)/?')
    @task
    def router76(self):
        self.client.get('/v3/materials/tuning_methods/(\w+)/?')
    @task
    def router77(self):
        self.client.get('/v3/teachers/?')
    @task
    def router78(self):
        self.client.get('/v3/teachers/(\d+)/?')
    @task
    def router79(self):
        self.client.get('/v3/teachers/(\d+)/courses/?')
    @task
    def router80(self):
        self.client.get('/v3/teachers/my_courses_ui/?')
    @task
    def router81(self):
        self.client.get('/v3/teachers/my_tutorial_course/?')
    @task
    def router82(self):
        self.client.get('/v3/teachers/my_demos/?')
    @task
    def router83(self):
        self.client.get('/v3/teachers/(\d+)/tutorial_course/?')
    @task
    def router84(self):
        self.client.get('/v3/students/practice_home_ui/?')
    @task
    def router85(self):
        self.client.get('/v3/students/my_tutorial_course/?')
    @task
    def router86(self):
        self.client.get('/v3/students/my_studied_courses/?')
    @task
    def router87(self):
        self.client.get('/v3/students/study_lesson/(\d+)/?')
    @task
    def router88(self):
        self.client.get('/v3/students/complete_lesson/(\d+)/?')
    @task
    def router89(self):
        self.client.get('/v3/students/play_score/(\d+)/?')
    @task
    def router90(self):
        self.client.get('/v3/students/practice_score/?')
    @task
    def router91(self):
        self.client.get('/v3/students/practice_score_new/?')
    @task
    def router92(self):
        self.client.get('/v3/course_studies/?')
    @task
    def router93(self):
        self.client.get('/v3/score_plays/?')
    @task
    def router94(self):
        self.client.get('/v3/data_statistics/?')
    @task
    def router95(self):
        self.client.get('/v3/ucsms/?')
    @task
    def router96(self):
        self.client.get('/v3/ucsms/?')
    @task
    def router97(self):
        self.client.get('/v3/ucsms_voice/?')
    @task
    def router98(self):
        self.client.get('/v3/ucsms_voice/?')
    @task
    def router99(self):
        self.client.get('/v3/txsms/?')
    @task
    def router100(self):
        self.client.get('/v3/txsms_voice/?')
    @task
    def router101(self):
        self.client.get('/v3/txsms_active/?')
    @task
    def router102(self):
        self.client.get('/v3/ucsms/verify/?')
    @task
    def router103(self):
        self.client.get('/v3/logs/?')
    @task
    def router104(self):
        self.client.get('/v3/logs/clear/?')
    @task
    def router105(self):
        self.client.get('/v3/gen_active_code/?')
    @task
    def router106(self):
        self.client.get('/v3/exchange/?')
    @task
    def router107(self):
        self.client.get('/v3/valentine/?')
    @task
    def router108(self):
        self.client.get('/v3/gen_promo_code/?')
    @task
    def router109(self):
        self.client.get('/v3/bind_promo_code/?')
    @task
    def router110(self):
        self.client.get('/v3/check_valid/?')
    @task
    def router111(self):
        self.client.get('/v3/promo/promo_info/?')
    @task
    def router112(self):
        self.client.get('/v3/promo/promo_channel/?')
    @task
    def router113(self):
        self.client.get('/v3/promo/promo_description/?')
    @task
    def router114(self):
        self.client.get('/v3/promo/promo_generation/?')
    @task
    def router115(self):
        self.client.get('/v3/promo/zhuanhua/?')
    @task
    def router116(self):
        self.client.get('/v3/device_delay/?')
    @task
    def router117(self):
        self.client.get('/v3/push_control/?')
    @task
    def router118(self):
        self.client.get('/v3/purchase/purchase_summary')
    @task
    def router119(self):
        self.client.get('/v3/purchase/active_summary')
    @task
    def router120(self):
        self.client.get('/v3/purchase/purchase_summary')
    @task
    def router121(self):
        self.client.get('/v3/purchase/active_summary')
    @task
    def router122(self):
        self.client.get('/v3/scores/?')
    @task
    def router123(self):
        self.client.get('/v3/scores/hotest')
    @task
    def router124(self):
        self.client.get('/v3/score/guide')
    @task
    def router125(self):
        self.client.get('/v3/score/piano_score/([a-f0-9]{24})')
    @task
    def router126(self):
        self.client.get('/v3/scores/uk_detail/?')
    @task
    def router127(self):
        self.client.get('/v3/scores/gt_detail/?')
    @task
    def router128(self):
        self.client.get('/v3/scores/detail/?')
    @task
    def router129(self):
        self.client.get('/v3/asset_boudle_info/?')
    @task
    def router130(self):
        self.client.get('/v3/product_token/?')
    @task
    def router131(self):
        self.client.get('/v3/persistent/?')
    @task
    def router132(self):
        self.client.get('/v3/my_product_list/?')
    @task
    def router133(self):
        self.client.get('/v3/delete_product/?')
    @task
    def router134(self):
        self.client.get('/v3/shore_product/?')
    @task
    def router135(self):
        self.client.get('/v3/deliver_homework/?')
    @task
    def router136(self):
        self.client.get('/v3/product/(\d+)/shore_info/?')
    @task
    def router137(self):
        self.client.get('/v3/complaint/?')
    @task
    def router138(self):
        self.client.get('/v3/complaints/?')
    @task
    def router139(self):
        self.client.get('/v3/purchase/downStatistics')
    @task
    def router140(self):
        self.client.get('/v3/paymentStatistics')
    @task
    def router141(self):
        self.client.get('/v3/paymentStatistics/purchase')
    @task
    def router142(self):
        self.client.get('/v3/paymentStatistics/promo')
    @task
    def router143(self):
        self.client.get('/v3/paymentStatistics/detail')
    @task
    def router144(self):
        self.client.get('/v3/favor/click/?')
    @task
    def router145(self):
        self.client.get('/v3/favor/myfavor/?')
    @task
    def router146(self):
        self.client.get('/v3/web/study/?')
    @task
    def router147(self):
        self.client.get('/v3/coupon/?')
    @task
    def router148(self):
        self.client.get('/v3/web_bug_coupon?')
    @task
    def router149(self):
        self.client.get('/v3/coupon/send_coupon/?')
    @task
    def router150(self):
        self.client.get('/v3/coupon/send_annals_coupon/?')
    @task
    def router151(self):
        self.client.get('/v3/coupon/get_coupon/?')
    @task
    def router152(self):
        self.client.get('/v3/coupon/coupons/?')
    @task
    def router153(self):
        self.client.get('/v3/message/message_push/?')
    @task
    def router154(self):
        self.client.get('/v3/message/message_read/?')
    @task
    def router155(self):
        self.client.get('/v3/message/message_push_iguitar/?')
    @task
    def router156(self):
        self.client.get('/v3/message/message_read_iguitar/?')
    @task
    def router157(self):
        self.client.get('/d')
    @task
    def router158(self):
        self.client.get('/v3/get_download_click/?')
    @task
    def router159(self):
        self.client.get('/v3/scores/new_scores/?')
    @task
    def router160(self):
        self.client.get('/v3/location/?')
    @task
    def router161(self):
        self.client.get('/v3/register_save/?')
    @task
    def router162(self):
        self.client.get('/v3/practice_info/?')
    @task
    def router163(self):
        self.client.get('/v3/practice_save/?')
    @task
    def router164(self):
        self.client.get('/v3/liveroom/teacher_operation/?')
    @task
    def router165(self):
        self.client.get('/v3/liveroom/liveroom_operation/?')
    @task
    def router166(self):
        self.client.get('/v3/liveroom/establish_contact/?')
    @task
    def router167(self):
        self.client.get('/v3/liveroom/get_liveroom_info/?')
    @task
    def router168(self):
        self.client.get('/v3/liveroom/liveroom_list_info/?')
    @task
    def router169(self):
        self.client.get('/v3/wechats/?')
    @task
    def router170(self):
        self.client.get('/v3/wechats/(\d+)/?')
    @task
    def router171(self):
        self.client.get('/v3/wechats/hot_word/')
    @task
    def router172(self):
        self.client.get('/v3/wechat/decodeUserInfo')
    @task
    def router173(self):
        self.client.get('/v3/wechat/my_login')
    @task
    def router174(self):
        self.client.get('/v3/wechat/tel_login?')
    @task
    def router175(self):
        self.client.get('/v3/wechat/dank')
    @task
    def router176(self):
        self.client.get('/v3/wechat/create_class')
    @task
    def router177(self):
        self.client.get('/v3/wechat/class')
    @task
    def router178(self):
        self.client.get('/v3/wechat/class/(\d+)/?')
    @task
    def router179(self):
        self.client.get('/v3/wechat/delete_class/(\d+)/?')
    @task
    def router180(self):
        self.client.get('/v3/wechat/classs/(\d+)/?')
    @task
    def router181(self):
        self.client.get('/v3/wechat/Classs')
    @task
    def router182(self):
        self.client.get('/v3/wechat/web')
    @task
    def router183(self):
        self.client.get('/v3/wechat/my_class')
    @task
    def router184(self):
        self.client.get('/v3/wechat/class_purchase')
    @task
    def router185(self):
        self.client.get('/v3/wechat/wechat_qrcode')
    @task
    def router186(self):
        self.client.get('/v3/wechat/my_classs')
    @task
    def router187(self):
        self.client.get('/v3/wechat/auto_class_login')
    @task
    def router188(self):
        self.client.get('/v3/wechat/get_wechat_qr')
    @task
    def router189(self):
        self.client.get('/v3/wechat/class_data')
    @task
    def router190(self):
        self.client.get('/v3/wechat/is_bright')
    @task
    def router191(self):
        self.client.get('/v3/wechat/get_class_payment_data')
    @task
    def router192(self):
        self.client.get('/v3/wechat/get_class_active_data')
    @task
    def router193(self):
        self.client.get('/v3/wechat/help')
    @task
    def router194(self):
        self.client.get('/v3/wechat/home')
    @task
    def router195(self):
        self.client.get('/v3/wechat/course_list')
    @task
    def router196(self):
        self.client.get('/v3/wechat/course_detail')
    @task
    def router197(self):
        self.client.get('/v3/wechat/payment')
    @task
    def router198(self):
        self.client.get('/v3/wechat/payment_callback')
    @task
    def router199(self):
        self.client.get('/v3/wechat/payment_info')
    @task
    def router200(self):
        self.client.get('/v3/wechat/wechat_msg_push')
    @task
    def router201(self):
        self.client.get('/v3/wechat/check')
    @task
    def router202(self):
        self.client.get('/v3/itv/itvs?')
    @task
    def router203(self):
        self.client.get('/v3/itv/itvs/(\d+)/?')
    @task
    def router204(self):
        self.client.get('/v3/itv/del_itv?')
    @task
    def router205(self):
        self.client.get('/v3/itv/get_itvs?')
    @task
    def router206(self):
        self.client.get('/v3/itv/(.*)/share_info/?')
    @task
    def router207(self):
        self.client.get('/v3/itv/(.*)/new/like?')
    @task
    def router208(self):
        self.client.get('/v3/ShareAccount/get_account/?')
    @task
    def router209(self):
        self.client.get('/v3/ShareAccount/change_share/?')
    @task
    def router210(self):
        self.client.get('/v3/ShareAccount/clear_share/?')
    @task
    def router211(self):
        self.client.get('/v3/ShareAccount/get_all_count/?')
    @task
    def router212(self):
        self.client.get('/v3/rank/get_rank/?')
    @task
    def router213(self):
        self.client.get('/v3/itv/like?')
    @task
    def router214(self):
        self.client.get('/v3/ShareAccount/get_all?')
    @task
    def router215(self):
        self.client.get('/v3/measurement/get_result?')
    @task
    def router216(self):
        self.client.get('/v3/challenge/?')
    @task
    def router217(self):
        self.client.get('/v3/challenge/(\d+)/?')
    @task
    def router218(self):
        self.client.get('/v3/challenge/home')
    @task
    def router219(self):
        self.client.get('/v3/challenge/rank')
    @task
    def router220(self):
        self.client.get('/v3/challenge/work?')
    @task
    def router221(self):
        self.client.get('/v3/challenge/work_like?')
    @task
    def router222(self):
        self.client.get('/v3/challenge/work_dlike?')
    @task
    def router223(self):
        self.client.get('/v3/challenge/work_detail')
    @task
    def router224(self):
        self.client.get('/v3/challenge/share_like?')
    @task
    def router225(self):
        self.client.get('/v3/prase_score/?')
    @task
    def router226(self):
        self.client.get('/v3/challenge/challenge_user_data')
    @task
    def router227(self):
        self.client.get('/v3/recommend/?')
    @task
    def router228(self):
        self.client.get('/v3/recommend/(\d+)/?')
    @task
    def router229(self):
        self.client.get('/v3/recommend_detail/?')
    @task
    def router230(self):
        self.client.get('/v3/recommend_detail/(\d+)/?')
    @task
    def router231(self):
        self.client.get('/v3/recommend_detail/items/(\d+)/?')
    @task
    def router232(self):
        self.client.get('/v3/red_point/?')
    @task
    def router233(self):
        self.client.get('/v3/red_point/(\d+)/?')
    @task
    def router234(self):
        self.client.get('/v3/expired/?')
    @task
    def router235(self):
        self.client.get('/v3/active_template/?')
    @task
    def router236(self):
        self.client.get('/v3/active_template/(\d+)/?')
    @task
    def router237(self):
        self.client.get('/v3/active_template/export_code/(\d+)/?')
    @task
    def router238(self):
        self.client.get('/v3/active_template/block_create/(\d+)/?')
    @task
    def router239(self):
        self.client.get('/v3/active_template/copy/(\d+)/?')
    @task
    def router240(self):
        self.client.get('/v3/active_code/?')
    @task
    def router241(self):
        self.client.get('/v3/active_code/activate/?')
    @task
    def router242(self):
        self.client.get('/v3/active_template/stats/batch/?')
    @task
    def router243(self):
        self.client.get('/v3/active_template/stats/group/?')
    @task
    def router244(self):
        self.client.get('/v3/active_template/batches/(\d+)/?')
    @task
    def router245(self):
        self.client.get('/v3/active_template/batch/change/?')
    @task
    def router246(self):
        self.client.get('/v3/active_code/batch/detail/?')
    @task
    def router247(self):
        self.client.get('/v3/active_code/group/detail/?')
    @task
    def router248(self):
        self.client.get('/v3/active_code/export_detail/(\w+)/?')
    @task
    def router249(self):
        self.client.get('/v3/active_code/export_group/(\w+)/?')
    @task
    def router250(self):
        self.client.get('/v3/active_code/search/?')
    @task
    def router251(self):
        self.client.get('/v3/get_coupon_stas/?')
    @task
    def router252(self):
        self.client.get('/v3/user_info/?')
    @task
    def router253(self):
        self.client.get('/v3/user_view/?')
    @task
    def router254(self):
        self.client.get('/v3/user_share/?')
    @task
    def router255(self):
        self.client.get('/v3/is_user_info/?')
    @task
    def router256(self):
        self.client.get('/v3/channel_sta/?')
    @task
    def router257(self):
        self.client.get('/v3/bind_channel/?')
    @task
    def router258(self):
        self.client.get('/v3/record_count/?')
    @task
    def router259(self):
        self.client.get('/v3/operating/date_count/?')
    @task
    def router260(self):
        self.client.get('/v3/operating/channels/?')
    @task
    def router261(self):
        self.client.get('/v3/operating/share_channels/?')
    @task
    def router262(self):
        self.client.get('/v3/payment/day_detail/?')
    @task
    def router263(self):
        self.client.get('/v3/operating/day_channel_detail/?')
    @task
    def router264(self):
        self.client.get('/v3/operating/day_channel_ranking/?')
    @task
    def router265(self):
        self.client.get('/v3/payment/date_detail/?')
    @task
    def router266(self):
        self.client.get('/v3/operating/date_channel_detail/?')
    @task
    def router267(self):
        self.client.get('/v3/operating/date_channel_ranking/?')
    @task
    def router268(self):
        self.client.get('/v3/operating/payment_channel_detail/?')
    @task
    def router269(self):
        self.client.get('/v3/operating/course_detail/?')
    @task
    def router270(self):
        self.client.get('/v3/operating/re_purchase/?')
    @task
    def router271(self):
        self.client.get('/v3/operating/pay_sta/?')
    @task
    def router272(self):
        self.client.get('/v3/operating/devices/?')
    @task
    def router273(self):
        self.client.get('/v3/payment/type/?')
    @task
    def router274(self):
        self.client.get('/v3/operating/payment_type/?')
    @task
    def router275(self):
        self.client.get('/v3/payment/study/?')
    @task
    def router276(self):
        self.client.get('/v3/register/count/?')
    @task
    def router277(self):
        self.client.get('/v3/register/seven/?')
    @task
    def router278(self):
        self.client.get('/v3/register/channel/?')
    @task
    def router279(self):
        self.client.get('/v3/register/day_channel_ranking/?')
    @task
    def router280(self):
        self.client.get('/v3/register/date_channel_detail/?')
    @task
    def router281(self):
        self.client.get('/v3/register/date_channel_ranking/?')
    @task
    def router282(self):
        self.client.get('/v3/operating/pay_or_reg/?')
    @task
    def router283(self):
        self.client.get('/v3/operating/pay_or_reg_platform/?')
    @task
    def router284(self):
        self.client.get('/v3/operating/pay_or_reg_channel/?')
    @task
    def router285(self):
        self.client.get('/v3/operating/course_kind/?')
    @task
    def router286(self):
        self.client.get('/v3/operating/course_bxq/?')
    @task
    def router287(self):
        self.client.get('/v3/operating/course_bxq_type/?')
    @task
    def router288(self):
        self.client.get('/v3/channel/date_channel/?')
    @task
    def router289(self):
        self.client.get('/v3/channel/date_j_channel/?')
    @task
    def router290(self):
        self.client.get('/v3/channel/date_share_channel/?')
    @task
    def router291(self):
        self.client.get('/v3/channel/date_instrument_share_channel/?')
    @task
    def router292(self):
        self.client.get('/v3/operating/users/?')
    @task
    def router293(self):
        self.client.get('/v3/operating/payments/?')
    @task
    def router294(self):
        self.client.get('/v3/channel/pay_channel/?')
    @task
    def router295(self):
        self.client.get('/v3/channel/shareinstall/?')
    @task
    def router296(self):
        self.client.get('/v3/operating/date_instrument_platform/?')
    @task
    def router297(self):
        self.client.get('/v3/operating/date_total_platform/?')
    @task
    def router298(self):
        self.client.get('/v3/operating/date_total_instrument/?')
    @task
    def router299(self):
        self.client.get('/v3/operating/date_total_payment_type/?')
    @task
    def router300(self):
        self.client.get('/v3/operating/date_total_re_purchase/?')
    @task
    def router301(self):
        self.client.get('/v3/operating/total/?')
