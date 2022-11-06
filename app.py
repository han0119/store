import streamlit as st
import requests

def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res
    # 回傳值

def getCountyOption(items):
    optionList = []# 創建一個空的 List 並命名為 optionList
    for item in items:
        # 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
        # hint: 想辦法處理 item['cityName'] 的內容
        name = item['cityName'][:3]
        if name in optionList:
            continue
        else:
            optionList.append(name)
        # 如果 name 不在 optionList 之中，便把它放入 optionList
        # hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
    return optionList

def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
    if county in name:
        specificBookstoreList.append(item)
    # 如果 name 不是我們選取的 county 則跳過
	# hint: 用 if-else 判斷並用 continue 跳過
    return specificBookstoreList

def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        expander.write(item['intro'])# 用 expander.write 呈現書店的 Introduction
        expander.subheader('Address')
        expander.write(item['address'])# 用 expander.write 呈現書店的 Address
        expander.subheader('Open Time')
        expander.write(item['openTime'])# 用 expander.write 呈現書店的 Open Time
        expander.subheader('Email')
        expander.write(item['email'])# 用 expander.write 呈現書店的 Email
        expanderList.append(expander)# 將該 expander 放到 expanderList 中
    return expanderList

def app():
    bookstoreList = getAllBookstore()

    countyOption = getCountyOption(bookstoreList)

    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('請選擇縣市', countyOption)
    # district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])

    specificBookstore = getSpecificBookstore(bookstoreList, county)
    num = len(specificBookstore)
    st.write(f'總共有{num}間書店', num)

if __name__ == '__main__':
    app()