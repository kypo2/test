from pydantic import BaseModel
from typing import Dict


class Table(BaseModel):
    authyn: int
    btn_yn: int
    cno: int
    DATE: str #  DATE
    rake: str # rake
    insurance: str # insurance
    f11_ty: str
    type: str # type
    game: str # game
    table_name: str # table name
    limit: str # limit
    rake: str # rake
    players: str # players
    status: str # status
    f8_ty: int
    end_date: str # end_date
    num: int 
    p_yn: bool
    rno: int
    tno: int

# class TableList(BaseModel):
#     tables: Dict[str, Table] # Ключем будет id

class RingPage(BaseModel):
    cur_page: int
    page_rows: int
    tot_pages: int
    tot_rows: int
    table_list: list[Table] = []
    
class TablePlayerResult(BaseModel):
    f1: str
    f2: str
    f3: str
    f4: str
    f5: str
    f6: str
    f7: str
    f7_ty: int
    f8: str
    f8_ty: int
    num: str
    uno: str

class RingInform(BaseModel):
    cur_page: str
    page_rows: int
    tot_pages: int
    tot_rows: int
    players_list: list[TablePlayerResult] = []


class TableHandResult(BaseModel):
    f1: str
    f2: str
    # f3: "<img src=\"./images/hh_cards/HH_5d.png\" height=\"30\"><img src=\"./images/hh_cards/HH_3c.png\" height=\"30\">"
    f4: str
    f5: str
    f5_ty: int


class HandPage(BaseModel):
    cur_page: int
    page_rows: int
    tot_pages: int
    tot_rows: int
    hand_list: list[TableHandResult] = []



