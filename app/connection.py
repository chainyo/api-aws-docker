import psycopg2

class DB():

    @classmethod
    def open_con(cls):
        cls.con = psycopg2.connect(
            database="exercises", 
            user="postgres", 
            password="123456789", 
            host="brief.crpjihsrdbrj.eu-west-3.rds.amazonaws.com", 
            port="5431")
        print("Connection opened successfully.")
        cls.cur = cls.con.cursor()

    @classmethod
    def close_con(cls):
        cls.con.commit()
        print("Commit done.")
        cls.con.close()
        print("Connection closed.")

    @classmethod
    def get_member_by_name(cls, name):
        cls.open_con()
        cls.cur.execute(f"SELECT surname, firstname, address, zipcode, telephone, recommendedby, joindate FROM cd.members WHERE surname like '{name}'")
        data = cls.cur.fetchall()
        return_li = []
        for row in data:
            item_dic = {}
            item_dic['surname'] = row[0]
            item_dic['firstname'] = row[1]
            item_dic['address'] = row[2]
            item_dic['zipcode'] = row[3]
            item_dic['telephone'] = row[4]
            item_dic['recommendedby'] = row[5]
            item_dic['joindate'] = row[6]
            return_li.append(item_dic)
        cls.close_con()
        return {'data': return_li}
    
    @classmethod
    def get_members(cls):
        cls.open_con()
        cls.cur.execute("SELECT surname, firstname, address, zipcode, telephone, recommendedby, joindate FROM cd.members")
        data = cls.cur.fetchall()
        return_li = []
        for row in data:
            item_dic = {}
            item_dic['surname'] = row[0]
            item_dic['firstname'] = row[1]
            item_dic['address'] = row[2]
            item_dic['zipcode'] = row[3]
            item_dic['telephone'] = row[4]
            item_dic['recommendedby'] = row[5]
            item_dic['joindate'] = row[6]
            return_li.append(item_dic)
        cls.close_con()
        return {'data': return_li}

    @classmethod
    def get_bookings(cls):
        cls.open_con()
        cls.cur.execute("SELECT bookid, facid, memid, starttime, slots FROM cd.bookings")
        data = cls.cur.fetchall()
        return_li = []
        for row in data:
            item_dic = {}
            item_dic['bookid'] = row[0]
            item_dic['facid'] = row[1]
            item_dic['memid'] = row[2]
            item_dic['starttime'] = row[3]
            item_dic['slots'] = row[4]
            return_li.append(item_dic)
        cls.close_con()
        return {'data': return_li}

    @classmethod
    def get_facilities(cls):
        cls.open_con()
        cls.cur.execute("SELECT facid, name, membercost, guestcost, initialoutlay, monthlymaintenance FROM cd.facilities")
        data = cls.cur.fetchall()
        return_li = []
        for row in data:
            item_dic = {}
            item_dic['facid'] = row[0]
            item_dic['name'] = row[1]
            item_dic['membercost'] = row[2]
            item_dic['guestcode'] = row[3]
            item_dic['initialoutlay'] = row[4]
            item_dic['monthlymaintenance'] = row[5]
            return_li.append(item_dic)
        cls.close_con()
        return {'data': return_li}
