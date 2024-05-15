import psycopg2,uuid,os,json,pytz
from psycopg2 import sql
from datetime import datetime,timedelta

class dbc:
    def __init__(self,un,pw,host,port,db) -> None:
        self.connection = psycopg2.connect(user=un,password=pw,host=host,port=port,database=db)
        self.cursor = self.connection.cursor()
        self.cursor.connection.autocommit = True
        pass

    def addvisit(self,ip=''):
        try:
            stmt = sql.SQL(f"insert into sitevisits (id,site,timestamp,ip) values ('{str(uuid.uuid4())}','hartzell.io',now(),'{str(ip)}')")
            self.cursor.execute(stmt)
            return True
        except Exception as e:
            print(e)
            return False
        
    def personalsitevisits(self):
        try:
            stmt = sql.SQL("select timestamp,site from sitevisits where site = 'hartzell.io' and timestamp >= date_trunc('month',now()) order by timestamp desc")
            self.cursor.execute(stmt)
            out = []
            for row in self.cursor.fetchall():
                out.append({'timestamp':row[0],'site':row[1]})
            return out
        except Exception as e:
            print(e)
            return False
        
    def motd(self):
        try:
            stmt = sql.SQL('select motd from motd limit 1')
            self.cursor.execute(stmt)
            return self.cursor.fetchone()[0]
        except:
            return "Enormous Nerd, Dev, & Car Enthusiast"
    
    def addcontact(self,c):
        try:
            stmt = sql.SQL(f"insert into contact (id,email,phone,fn,ln,salt) values ('{str(uuid.uuid4())}','{c['email']}','{c['phone']}','{c['fn']}','{c['ln']}','{str(uuid.uuid4())}')")
            self.cursor.execute(stmt)
            return True
        except Exception as e:
            print(e)
            return False
        
    def getcbyemail(self,email:str):
        try:
            stmt = sql.SQL(f"select id,email,fn,ln,salt,hash,created from contact where email = '{email}'")
            self.cursor.execute(stmt)
            rs = self.cursor.fetchall()
            if rs: return {'id':rs[0][0],'email':rs[0][1],'fn':rs[0][2],'ln':rs[0][3],'salt':rs[0][4],'hash':rs[0][5],'created':str(rs[0][6])}
            else: return False
        except Exception as e:
            print(e)
            return False
        
    def contactrept(self):
        try:
            stmt = sql.SQL("select id,email,fn,ln from contact")
            self.cursor.execute(stmt)
            out = []
            for row in self.cursor.fetchall():
                out.append({'id':row[0],'email':row[1],'fn':row[2],'ln':row[3]})
            return out
        except Exception as e:
            print(e)
            return False
        
    def addsesh(self,cid):
        try:
            id = str(uuid.uuid4())
            now = datetime.now(tz=pytz.utc)
            exp = now+timedelta(weeks=1)
            stmt = sql.SQL(f"insert into sessions (id,cid,exp,latest,created) values ('{id}','{cid}','{exp.strftime('%Y-%m-%dT%H:%M:%SZ')}','{now}','{now}')")
            self.cursor.execute(stmt)
            return {'id':id,'exp':exp.strftime('%Y-%m-%dT%H:%M:%SZ')}
        except Exception as e:
            print(e)
            return False
        
    def getsesh(self,cid):
        try:
            stmt = sql.SQL(f"select id,exp from sessions where cid = '{cid}' order by created desc")
            self.cursor.execute(stmt)
            rs = self.cursor.fetchall()
            if rs: return {'id':rs[0][0],'exp':rs[0][1]}
            else: return False
        except Exception as e:
            print(e)
            return False