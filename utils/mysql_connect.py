import pymysql

class MysqlHelper:
    # 初始化数据库信息
    def __init__(self, host, username, password, db, charset='utf8', port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.charset = charset
        self.port = port

    # 数据库连接
    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password,
                                    db=self.db, charset=self.charset, cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    # 查询单条数据
    def get_one(self, sql, params=()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result

    # 查询多条数据
    def get_all(self, sql, params=()):
        list_data = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            list_data = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return list_data

    def execute(self, sql, params=()):
        # SQL删除、提交、修改语句
        try:
            self.cursor.execute(sql, params)  # 执行SQL语句
            self.db.commit()  # 提交修改
        except Exception as e:
            # 发生错误时回滚
            print(e)
            self.db.rollback()

    # 关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()
