# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-15 16:09
# @Author  : lidong@immusician.com
# @Site    :
# @File    : demo.py


def get_mg_current_top_star():
    label_visits_dao = LabelVisitsDao()    #实例化类
    labels, total = label_visits_dao.query_labels({'recent_days': 2})
    num = 10
    today = time.strftime("%Y-%m-%d")
    yesterday = get_yesterday()
    label_ids = list(set([label[0] for label in labels]))
    for label_id in label_ids:
        query_args = {
            'date': today,
            'label_id': label_id
        }
        today_top_star = miaogou_api.query_label_top_star(query_args)
        yesterday_query_args = {
            'date': yesterday,
            'label_id': label_id
        }
        yesterday_top_star = miaogou_api.query_label_top_star(yesterday_query_args)
        yesterday_temp_data = {}
        for i in yesterday_top_star:
            yesterday_temp_data[i.get('star_name')] = i.get('rank')
        today_top_star += list(filter(
            lambda x: x.get('start_time') + x.get('live_duration') > datetime.datetime.strptime(today,
                '%Y-%m-%d').timestamp() if x.get('start_time') and x.get('live_duration') else False, yesterday_top_star))
        today_top_star.sort(key=operator.itemgetter('uv'), reverse=True)  #按uv排序
        rank = 1
        star_info_dao = StarInfoDao()
        for i in today_top_star[0:int(num)]:
            i['rank'] = rank
            star_info = star_info_dao.get_star_info_by_star_id(i.get('creator').get('anchor_id'))
            yesterday_rank = yesterday_temp_data.get(i.get('creator').get('nick')) if yesterday_temp_data.get(
                i.get('creator').get('nick')) else 99999
            if rank < yesterday_rank:
                i['is_up'] = 1
            elif rank == yesterday_rank:
                i['is_up'] = 0
            elif rank > yesterday_rank:
                i['is_up'] = 2
            i['areas'] = json.loads(star_info.areas) if star_info and star_info.areas else []
            rank += 1

        other_total_uv = sum([i.get('uv') for i in today_top_star[int(num):]])
        other_total_pv = sum([i.get('pv') for i in today_top_star[int(num):]])
        other = {'title': '其他', 'uv': other_total_uv, 'pv': other_total_pv}

        data = today_top_star[0:int(num)]
        data.append(other)
        cache_redis.set('top_star_%s' % label_id, json.dumps(data), ex=3600 * 24)


def get_mg_top_star():
    from tasks.tasks import init_miaogou_star_info_task
    top_star_dao = TopStarDao()
    get_recent_date_nums = 7
    dates = get_date_list(get_recent_date_nums + 1)[1:]

    args = {
        'recent_days': get_recent_date_nums,
    }
    label_visits_dao = LabelVisitsDao()
    labels, total = label_visits_dao.query_labels(args)
    labels = {i[1]: i[0] for i in labels}

    try:
        for i in dates:
            for k, v in labels.items():
                args = {
                    'label_id': v,
                    'date': i
                }
                raw_data = miaogou_api.query_label_top_star(args)
                raw_data.sort(key=operator.itemgetter('uv'), reverse=True)
                rank = 1
                for j in raw_data:
                    top_star_item = dict()
                    top_star_item['label_id'] = v
                    top_star_item['live_id'] = j.get('live_id')
                    top_star_item['date'] = i
                    top_star_item['title'] = j.get('title')
                    top_star_item['cover_url'] = j.get('creator').get('pic_url')
                    top_star_item['star_id'] = j.get('creator').get('anchor_id')
                    top_star_item['star_name'] = j.get('creator').get('nick')
                    top_star_item['uv'] = j.get('uv')
                    top_star_item['pv'] = j.get('pv')
                    top_star_item['rank'] = rank
                    rank += 1
                    top_star = TopStar()
                    top_star_dao.save_top_star(top_star, top_star_item)    #更新值

                    init_miaogou_star_info_task.delay(top_star_item['star_id'], '')

    except Exception:
        logger.error(traceback.format_exc())
