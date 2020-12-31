import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

jsonf = "gspread-sample-300316-8b4103787009.json"

# (1) Google Spread Sheetsにアクセス
def connect_gspread(jsonf,key):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    return worksheet

# ここでjsonfile名と2-2で用意したkeyを入力

def update_gspr(index,data,spread_sheet_key):
    ws = connect_gspread(jsonf,spread_sheet_key)
    length = len(index)
    if length > 10:
        length = 10
    #(２−１)あるセルの値を更新（行と列を指定）
    for i in range(length):
        ws.update_cell(i+2,1,index[i])
        ws.update_cell(i+2,2,data[i])

    # #(２−２)あるセルの値を更新（ラベルを指定）
    # ws.update_acell('C1','test2')
    # ws.update_acell('C2',1)
    # ws.update_acell('C3',2)

    # #(2-3)ある範囲のセルの値を更新
    # ds= ws.range('E1:G3')
    # ds[0].value = 1
    # ds[1].value = 2
    # ds[2].value = 3
    # ds[3].value = 4
    # ds[4].value = 5
    # ds[5].value = 6
    # ds[6].value = 7
    # ds[7].value = 8
    # ds[8].value = 9
    #ws.update_cells(ds)