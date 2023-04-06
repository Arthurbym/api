#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql, json, math, time

from common.log import Logger
from config.config_data import mysqldb

log = Logger(__name__).get_logger()


class DoSql(object):
    def __init__(self, **sql_dc):
        '''

        :param sql_dc:连接参数
        host = '127.0.0.1',   服务端地址
        port = 3306,    服务端端口
        user = 'root',   用户名
        password = 'mysql',   密码
        database = 'mydb',   要连接的数据库
        charset = 'utf8'    设置数据库编码
        "cursorclass": pymysql.cursors.DictCursor 设置返回类型为字典

        '''
        if sql_dc == {}:
            sql_dc = mysqldb
            sql_dc['cursorclass'] = pymysql.cursors.DictCursor
        self.db = pymysql.connect(**sql_dc)
        self.cur = self.db.cursor()

    def select_value(self, sql_line):
        '''
        查询
        :param sql_line:
        :return:
        '''
        try:
            self.cur.execute(sql_line)
            sql_data = self.cur.fetchall()
            # self.close_db()
        except Exception as e:
            log.exception("execute sql [%s] failed! " % sql_line)
            raise e
        else:
            log.info("execute sql [%s] succeed!" % sql_line)
            return sql_data

    def change_value(self, sql_line):
        '''
        插入、更新
        :param sql_line:
        :return:
        '''
        try:
            self.cur.execute(sql_line)
            self.db.commit()
            # self.close_db()
        except Exception as e:
            log.exception("execute sql [%s] failed! " % sql_line)
            raise e
        else:
            log.info("execute sql [%s] succeed!" % sql_line)

    def beautiful_json(self, sql_line):
        '''
        json美化,转换时间，ensure_ascii=False，防止中文转换
        '''
        values = self.select_value(sql_line)
        values_json = json.dumps(values, default=str, ensure_ascii=False)
        # return values_json
        return json.loads(values_json)

    def close_db(self):
        '''
        关闭连接
        :return:
        '''
        self.cur.close()
        self.db.close()

    def auto_dosql_team_up(self, activity_title='\'bym_test\'', is_delete=0, activity_config_id=1,
                            activity_route_id=3,
                            activity_start_time='', complete_rule_type=1, run_mileage=1000, run_time=0,
                            bonus_rule_type=0, activity_entry_fee=0, activity_total_bonus=0, activity_state=0,
                            sub_state=-1, activity_type=1, user_count=2, is_robot_start=0, is_homepage=0,
                            classify_type=0, application_start_time='Null', application_end_time='Null',
                            application_user_limit=-1, activity_object_type=-1, status=0, remark='\'bym_test\'',
                            rate_limiting=-1,
                            mutex_activity_ids='\'\'', actual_off_time='Null', is_public=0, has_robot=0,
                            demand_medal_config_id=0, demand_user_level=0, is_test=1):
        '''
        发起组队跑

        '''
        create_time = '\'' + time.strftime('%Y-%m-%d %H:%M:%S') + '\''
        in_activity_start_time = '\'' + time.strftime('%Y-%m-%d %H:%M') + '\''
        DoSql().change_value(
            "INSERT INTO `pitpat`.`zns_run_activity`(`is_delete`, `create_time`, `modifie_time`, `activity_config_id`, `activity_route_id`, `activity_title`, `activity_start_time`, `activity_end_time`, `complete_rule_type`, `run_mileage`, `run_time`, `bonus_rule_type`, `activity_entry_fee`, `activity_total_bonus`, `activity_state`, `sub_state`, `activity_introduce`, `activity_config`, `activity_type`, `user_count`, `award_rule`, `challenge_rule`, `is_robot_start`, `is_homepage`, `classify_type`, `application_start_time`, `application_end_time`, `application_user_limit`, `activity_object_type`, `status`, `activity_no`, `remark`, `off_remark`, `rate_limiting`, `mutex_activity_ids`, `actual_off_time`, `is_public`, `has_robot`, `demand_medal_config_id`, `demand_user_level`, `is_test`) "
            "VALUES (%s,%s,'2022-08-04 15:57:00', %s, %s, %s, %s, NULL, %s, %s, %s, %s, %s, %s, %s, %s, NULL, '{\"mileageList\":\"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42\",\"participateAward\":\"0.5\",\"margin\":\"1,3,5,48\",\"completeAward\":1.6,\"backgroundImage\":\"https://tkjh5.ldxinyong.com/admin/profile/upload/2022/01/12/78feee06-bda6-4473-a52f-0f83178635ca.jpg\",\"completeAwardPerKm\":1,\"baseExtraAward\":1,\"completeAwardPerMiles\":1.6,\"teamRunLastEnter\":30,\"miles\":\"1,3,5,7,10,16\",\"advertisingImage\":\"https://tkjh5.ldxinyong.com/admin/profile/upload/2022/01/12/78feee06-bda6-4473-a52f-0f83178635ca.jpg\",\"activityRequire\":\"Participants should be in a good health condition and behavior properly\",\"activityTitle\":\"call XXX to win the bonus\",\"coverImage\":\"https://pitpat-oss.s3.us-east-2.amazonaws.com/headPortrait/iGg10FSR891L9185.png\",\"runTime\":\"1,2,3,30,40,50\",\"mileList\":\"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26\",\"winnerAward\":\"2.4\",\"activityIntroduce\":\"You can invite any registered users to Team Run, and all participants will be running on the same track.\",\"mileage\":\"1,3,5,7,10,16\",\"activityRule\":\"1. If no one accepts the invitation before the start time, the event will be automatically cancelled.\\n2. If users are late more than 30 minutes, users will not be able to participate in the game anymore. No reward will be granted and the deposit will not be returned.\\n3. The race needs to be completed at one time. Please do not quit halfway.\"}', %s, %s, '1、Ranking reward：\n(1)The 1st place:$0\n(2)The 2nd place:$0\n(3)The 3rd place:$0\n2、Completion Reward:$1.60\n3、Split Deposit: Total amount of deposit / the number of users who complete the game\nThe Final Reward: Ranking Reward+Completion Reward+Split Deposit\nNote: If the number of participants is equal to or greater than 5, you may get a ranking reward.', '', %s, %s, %s, %s, %s, %s,%s, %s, '', %s, '',%s, %s, %s,%s, %s, %s, %s, %s)"
            % (is_delete, create_time, activity_config_id,
               activity_route_id, activity_title, in_activity_start_time, complete_rule_type, run_mileage, run_time,
               bonus_rule_type, activity_entry_fee, activity_total_bonus, activity_state, sub_state, activity_type,
               user_count, is_robot_start, is_homepage, classify_type, application_start_time, application_end_time,
               application_user_limit, activity_object_type, status, remark, rate_limiting, mutex_activity_ids,
               actual_off_time, is_public, has_robot, demand_medal_config_id, demand_user_level, is_test))






if __name__ == "__main__":
    # i = DoSql().beautiful_json("select * from zns_run_activity_config where id = 1")
    # i = DoSql().beautiful_json('select b.amount from zns_user_account b inner join zns_user a on a.id = b.user_id where a.first_name like \'bym4\'')
    # print(i[0]['amount'])
    # print(type(i[0]['amount']))
    # print('Balance($*)'.replace('*',i[0]['amount']))

    # goal_list = \
    #     json.loads(i[0]['activity_config'])[
    #         'mileList'].split(',')
    # completeAwardPerMiles1 =float(json.loads(i[0]['activity_config'])[
    #         'completeAwardPerMiles'])
    # # sda = []
    # # for x in goal_list:
    # #     sda.append(int(x))
    # # print(goal_list)
    # # print(max(sda))
    # print(completeAwardPerMiles1)
    # print(len(goal_list)/5)
    # print(math.ceil(len(goal_list)/5))
    # wallet_value = DoSql().beautiful_json('select b.amount from zns_user_account b inner join zns_user a on a.id = b.user_id where a.first_name like \'bym4\'' )
    # print(wallet_value)
    # wallet_value_text = 'Balance($*)'
    # asd = wallet_value_text.replace('*', wallet_value[0]['amount'])
    # print(asd)
    # print("INSERT INTO `pitpat`.`zns_run_activity`(`is_delete`, `create_time`, `modifie_time`, `activity_config_id`, `activity_route_id`, `activity_title`, `activity_start_time`, `activity_end_time`, `complete_rule_type`, `run_mileage`, `run_time`, `bonus_rule_type`, `activity_entry_fee`, `activity_total_bonus`, `activity_state`, `sub_state`, `activity_introduce`, `activity_config`, `activity_type`, `user_count`, `award_rule`, `challenge_rule`, `is_robot_start`, `is_homepage`, `classify_type`, `application_start_time`, `application_end_time`, `application_user_limit`, `activity_object_type`, `status`, `activity_no`, `remark`, `off_remark`, `rate_limiting`, `mutex_activity_ids`, `actual_off_time`, `is_public`, `has_robot`, `demand_medal_config_id`, `demand_user_level`, `is_test`) VALUES (%s,%s,'2022-08-04 15:57:00', %s, %s, %s, %s, NULL, 1, 1600.00, 0.00, 2, 1.00, 3.60, -1, 3, NULL, '{\"mileageList\":\"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42\",\"participateAward\":\"0.5\",\"margin\":\"1,3,5,48\",\"completeAward\":1.6,\"backgroundImage\":\"https://tkjh5.ldxinyong.com/admin/profile/upload/2022/01/12/78feee06-bda6-4473-a52f-0f83178635ca.jpg\",\"completeAwardPerKm\":1,\"baseExtraAward\":1,\"completeAwardPerMiles\":1.6,\"teamRunLastEnter\":30,\"miles\":\"1,3,5,7,10,16\",\"advertisingImage\":\"https://tkjh5.ldxinyong.com/admin/profile/upload/2022/01/12/78feee06-bda6-4473-a52f-0f83178635ca.jpg\",\"activityRequire\":\"Participants should be in a good health condition and behavior properly\",\"activityTitle\":\"call XXX to win the bonus\",\"coverImage\":\"https://pitpat-oss.s3.us-east-2.amazonaws.com/headPortrait/iGg10FSR891L9185.png\",\"runTime\":\"1,2,3,30,40,50\",\"mileList\":\"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26\",\"winnerAward\":\"2.4\",\"activityIntroduce\":\"You can invite any registered users to Team Run, and all participants will be running on the same track.\",\"mileage\":\"1,3,5,7,10,16\",\"activityRule\":\"1. If no one accepts the invitation before the start time, the event will be automatically cancelled.\\n2. If users are late more than 30 minutes, users will not be able to participate in the game anymore. No reward will be granted and the deposit will not be returned.\\n3. The race needs to be completed at one time. Please do not quit halfway.\"}', 1, 1, '1、Ranking reward：\n(1)The 1st place:$0\n(2)The 2nd place:$0\n(3)The 3rd place:$0\n2、Completion Reward:$1.60\n3、Split Deposit: Total amount of deposit / the number of users who complete the game\nThe Final Reward: Ranking Reward+Completion Reward+Split Deposit\nNote: If the number of participants is equal to or greater than 5, you may get a ranking reward.', '', 0, 0, 0, NULL, NULL, -1, -1, 0, '', '', '', -1, '', NULL, 1, 0, 0, 0, 0)"
    #         %(is_delete, create_time, activity_config_id,
    #             activity_route_id,activity_title,activity_start_time))
    # DoSql().auto_dosql_team_up1()
    # DoSql()
    # sda= DoSql().beautiful_json('select amount from zns_user_account where user_id = 81085')[0]['amount']
    sda= float(DoSql().beautiful_json('select amount from zns_user_account where user_id = 81085')[0]['amount'])
    print(type(sda))
    print(sda)
