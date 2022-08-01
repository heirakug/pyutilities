import pandas as pd
import os
import datetime

#param
CURRENDIR = os.getcwd()
CSVPATH= CURRENDIR + '/report.csv'
cols = ['time','addr','a1x_a','a1y_d','a1z_v']
dt_now = datetime.datetime.now()

def getMatchCsv(df,ls):
    for addr in ls:
        s_addr = addr.replace(':', '') #とりあえず使っている、たぶん削除
        df[df['addr']==addr].to_csv('./salesDataFiles/' + str(dt_now.year) + str(dt_now.month) + str(dt_now.day) + s_addr + '.csv', index=None)

def getUniqueAddrList(df):
    ser_addr = df['addr']
    ser_uqnique_addr = ser_addr.drop_duplicates()
    ls = ser_uqnique_addr.to_list()

    return ls

def loadCsvDf():
    global cols
    
    try:
        df = pd.read_csv(CSVPATH,usecols=cols) # csvのデータで読み込み
    except:
        #df = pd.DataFrame(columns=cols)  # 空のデータフレーム作成
        print("ファイルがありません。")

    return df

if __name__ == '__main__':
    df = loadCsvDf()
    ls_unique_addr = getUniqueAddrList(df)
    getMatchCsv(df,ls_unique_addr)
