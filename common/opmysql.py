import os,logging,pymysql
from public import config
class OperationDbInterface():
    def __init__(self,host_db='',user_db='',passwd_db='',name_db='',port_db='',link_type=0):
        '''
        :param host_db:
        :param user_db:
        :param passwd_db:
        :param name_db:
        :param port_db:
        :param link_type:
        '''
        try :
            if link_type==0:
                self.conn=pymysql.connect(host=host_db,user=user_db,passwd=passwd_db,db=name_db,port=passwd_db,charset='utf-8',cursorclass=pymysql.cursors.DictCursor)
            else:
                self.conn=pymysql.connect(host=host_db,user=user_db,passwd=passwd_db,db=name_db,port=passwd_db,charset='utf-8')
                self.cur=self.conn.cursor()
        except pymysql.Error as e:
            print("create db error | mysql error %d: %s"%(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.src_path+'/log/syserror.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger=logging.getLogger(__name__)
            logger.exception(e)
    def op_sql(self,condition):
        '''

        :param condition:
        :return:
        '''
        try:
            self.cur.execute(condition)
            self.conn.commit()
            result={'code':'000','message':'success','data':[]}
        except pymysql.Error as e:
            self.conn.rollback()
            result={'code':'999','message':'fail','data':[]}
            print("db error|op_sql %d %s"%(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.src_path+'/log/syserror.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result