import streamlit as st
import data
from time import sleep


def makeBoard():
    boardData = data.boardData
    board_size = 7
    cols = st.columns(board_size)
    cols[0].text(f"|")
    cols[1].button(label = boardData['0'][0], key = boardData['0'][1], on_click=clicked, args = ('0',))
    cols[2].text(f"|")
    cols[3].button(label = boardData['1'][0], key = boardData['1'][1], on_click=clicked, args = ('1',))
    cols[4].text(f"|")
    cols[5].button(label = boardData['2'][0], key = boardData['2'][1], on_click=clicked, args = ('2',))
    cols[6].text(f" |")
    st.text("-----------------------------------------------------------------------------------------------------------------------------")
    cols1 = st.columns(board_size)
    cols1[0].text(f"|")
    cols1[1].button(label = boardData['3'][0], key = boardData['3'][1], on_click=clicked, args = ('3',))
    cols1[2].text(f"|")
    cols1[3].button(label = boardData['4'][0], key = boardData['4'][1], on_click=clicked, args = ('4',))
    cols1[4].text(f"|")
    cols1[5].button(label = boardData['5'][0], key = boardData['5'][1], on_click=clicked, args = ('5',))
    cols1[6].text(f"|")
    st.text("-----------------------------------------------------------------------------------------------------------------------------")
    cols2 = st.columns(board_size)
    cols2[0].text(f"|")
    cols2[1].button(label = boardData['6'][0], key = boardData['6'][1], on_click=clicked, args = ('6',))
    cols2[2].text(f"|")
    cols2[3].button(label = boardData['7'][0], key = boardData['7'][1], on_click=clicked, args = ('7',))
    cols2[4].text(f"|")
    cols2[5].button(label = boardData['8'][0], key = boardData['8'][1], on_click=clicked, args = ('8',))
    cols2[6].text(f"|")



def clicked(key):
    boardData = data.boardData
    cp = data.getPlayer()

    if(boardData[key][0] == 'X' or boardData[key][0] == 'O'):
        print("Invalid Move")
        return
    else:
        boardData[key][0] = 'X' if cp == 'p1' else 'O'
    
    nextPlayer = 'p1' if cp == 'p2' else 'p2'
    data.setPlayer(nextPlayer)
    print(f"Current Player = {cp}")
    data.setMoves(data.getMoves() - 1) 


if __name__ =="__main__":

    inputCols = st.columns(2,vertical_alignment = "center")

    p1Name = inputCols[0].text_input("Player 1 Name", placeholder= "player1")
    p2Name = inputCols[1].text_input("Player 2 Name", placeholder= "player2")
    
    if(p1Name == ""):
        p1Name = "player1"
    if(p2Name == ""):
        p2Name = "player2"

    turnCols = st.columns(3)
    turnCols[0].warning(f"{p1Name if data.getPlayer() == 'p1' else p2Name}'s Turn")
    turnCols[1].error(f"Moves Left: {data.getMoves()}")
    turnCols[2].button(label = "RESET BOARD", on_click= data.resetBoard)
    
    
    # print(board)
    makeBoard()
    if(data.checkWin('O' if data.getPlayer() == 'p1' else 'X')):
        win = p1Name if data.getPlayer() == 'p2' else p2Name
        print("Winnnner: ", win)
        st.success(f"Winnnner: {win}")   
        st.warning(f"Please RESET to replay")     

if(data.getMoves() == 0):
    sleep(1)
    st.error(f"Board will be RESET")
    data.resetBoard()
    data.setMoves(9)
    sleep(2)
    st.rerun()
