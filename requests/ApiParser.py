from SchemasParser import Table, RingPage, RingInform, TablePlayerResult, HandPage, TableHandResult   #, MemberTable, MemberPage
from pprint import pprint
import json, os
import requests
from UtilsParser import UtilsParser




cookies = {
    'AWSALB': '0vto+pd6WZGcNYRT68So22dxxXrQ6AmCkqlBj9yUltRHjmvQJVyzToGxvWYRb4XgcYzyQoeffFlp5oH/J/KUYvKno6wLhN/kBEssuQpMh0deutxGWyld9ruPGqm+',
    'AWSALBCORS': '0vto+pd6WZGcNYRT68So22dxxXrQ6AmCkqlBj9yUltRHjmvQJVyzToGxvWYRb4XgcYzyQoeffFlp5oH/J/KUYvKno6wLhN/kBEssuQpMh0deutxGWyld9ruPGqm+',
    'connect.sid': 's%3ANNH5SyVSdNszd8oiX3D0zozDhUN8lT5o.1cnu6kVppRLALoLrKQd1Y8XCouEtplpXSiOsLjutOTo'
}

headers = {
    'Accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': f'connect.sid={cookies["connect.sid"]}; AWSALB={cookies["AWSALB"]}; AWSALBCORS={cookies["AWSALBCORS"]}',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Opera GX";v="91", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.106',
    'x-requested-with': 'XMLHttpRequest',
}


class ApiParser():
    def __init__(self, headers, cookies) -> None:
        self.headers = headers
        self.cookies = cookies
        self.path = './'
        self.table = ''


    def getRingList(self):
        RingList = requests.post(url="https://union.clubgg.net:8888/ringlist", headers=self.headers, cookies=self.cookies, data="iam=list&from=03%2F06%2F2023&to=03%2F13%2F2023&type=2&game=0&state=3&blindstr=&cur_page=1").json()
        data = RingPage.parse_obj(RingList['PAGE'])
        data.table_list = [Table(**UtilsParser.FixRingDict(table_info)) for table_info in RingList['DATA']]
        return data
    
    def getTablesInRingList(self) -> list[int]:
        rings_page = self.getRingList()
        return [table.rno for table in rings_page.table_list]

# получаем  ringinfo 
    def getRingInfo(self, table_id)-> list[RingInform]:
        RingInfo = requests.post(url="https://union.clubgg.net:8888/ringinfo", headers=self.headers, cookies=self.cookies, data="iam=playerlist&rno=468100&nick=&cur_page=1").json()
        data = RingInform.parse_obj(RingInfo['PAGE'])
        for ring_info in RingInfo['DATA']:
            ring_info_fix = UtilsParser.FixRingInfDict(ring_info)
            ring_schema = TablePlayerResult(**ring_info_fix)
            data.players_list.append(ring_schema)
        return data
    
    def getTablesInRingInfo(self) -> list[int]:
        ring_inform = self.getRingInfo()
        table_ids_list = []
        for table_ring_inform in ring_inform.players_list:
            table_ids_list.append(table_ring_inform.players_list)
        return table_ids_list
    
    # получаем hand History
    # def getHandList(self, hand_id)-> list[HandPage]:
    #     #Получаю данные json
    #     HandList = requests.post(url="https://union.clubgg.net:8888/memberinfo", headers=self.headers, cookies=self.cookies, data="iam=handhistory_option&rg_yn=1&no=459360&memberno=395719").json()
    #     #Загоняю в схему
    #     data = HandPage.parse_obj(HandList['PAGE'])
    #     #Добовля. информацию в hand_list в котором находиться схема 
    #     #Из словоря с ключем ДАТА поочередо будет достоваться информация
    #     for hand_info in HandList['DATA']:
    #         #Исправляю значение словаря
    #         hand_info_fix = UtilsParser.FixHandDict(hand_info)
    #         #Добовляем в схему ** озночают что словарь будет расспакован в аргументы и их значение
    #         hand_schema = TableHandResult(**hand_info_fix)
    #         #обращаемся к переменной data и добовляем в нее обьект нашей схемы
    #         data.hand_list.append(hand_schema)
    #     return data
    
    # def getHandTable(self) -> list[int]:
    #     #Получаю заполненную схему HandPage
    #     hand_page = self.getHandList()
    #     # создаю список хенд тейбл он пустой мы будем его заполнять
    #     hand_table = []
    #     # в переменной схемы hand_list лежит список со схемами TableHandResult нам надо пройтись по каждой схеме из цыкла 
    #     # for hand in hand_page.hand_list:
    #     #     #добавим какое то значение из каждой раздачи
    #     #     hand_table.append(hand.hand_list)
    #     #     #Возвращаем получившийся список
    #     # return hand_table
    
    
    

    
    def main(self):
        '''Вся логика'''
        table_ids_list = self.getTablesInRingList()
        
        # Выведем данные с каждого стола 
        for table_id in table_ids_list:
            data = self.getRingInfo(table_id)     
            print(data)
        # for all_hand in table_ids_list:
        #     data = self.getHandList(all_hand)
        #     print(data)
       
        return table_ids_list
    
    
test = ApiParser(headers=headers, cookies=cookies).main()
pprint(test)
    