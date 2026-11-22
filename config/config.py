# 环境基准地址
BASE_URL = "http://127.0.0.1:8080/api"

# excel格式的测试用例文件配置
EXCEL_FILE = "./data/测试数据.xlsx"
SHEET_NAME = "Sheet1"

# mysql配置
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_NAME = "minsu"
DB_USER = "root"
DB_PASSWORD = "123456"

# mysql资源销毁
SQL1 = 'delete from room_type where type_name = "E2E测试大床房"'
# SQL2 = 'delete from sp_attribute where attr_name = "VIP尺码"'
# SQL3 = 'delete from sp_goods where goods_name = "大码牛仔裤+"'
