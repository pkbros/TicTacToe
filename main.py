import streamlit as st
from data import boardData



def makeBoard():
    global boardData
    board_size = 7
    cols = st.columns(board_size)
    cols[0].text(f"|")
    cols[1].button(label = boardData['0'][0], key = boardData['0'][1], on_click=clicked, args = ('0',))
    cols[2].text(f"|")
    cols[3].button(label = boardData['1'][0], key = boardData['1'][1])
    cols[4].text(f"|")
    cols[5].button(label = boardData['2'][0], key = boardData['2'][1])
    cols[6].text(f" |")
    st.text("-----------------------------------------------------------------------------------------------------------------------------")
    cols1 = st.columns(board_size)
    cols1[0].text(f"|")
    cols1[1].button(label = boardData['3'][0], key = boardData['3'][1])
    cols1[2].text(f"|")
    cols1[3].button(label = boardData['4'][0], key = boardData['4'][1])
    cols1[4].text(f"|")
    cols1[5].button(label = boardData['5'][0], key = boardData['5'][1])
    cols1[6].text(f"|")
    st.text("-----------------------------------------------------------------------------------------------------------------------------")
    cols2 = st.columns(board_size)
    cols2[0].text(f"|")
    cols2[1].button(label = boardData['6'][0], key = boardData['6'][1])
    cols2[2].text(f"|")
    cols2[3].button(label = boardData['7'][0], key = boardData['7'][1])
    cols2[4].text(f"|")
    cols2[5].button(label = boardData['8'][0], key = boardData['8'][1])
    cols2[6].text(f"|")


def clicked(key):
    if(boardData[key][0] == 'X' or boardData[key][0] == 'O'):
        print("Invalid Move")
    else:
        boardData[key][0] = 'X'


if __name__ =="__main__":
    print(boardData['0'][0], boardData['0'][1])
    makeBoard()
