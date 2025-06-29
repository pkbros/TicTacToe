import streamlit as st

class Board:

    def __init__(self, dim):
        self.dim = dim
        self.board = [['i' for _ in range(self.dim)] for _ in range(self.dim)]

    def createBoard(self):
        st.write("Displaying the Board:")
        
        cols = st.columns(3)
        cols[0].button("_",key = "0")
        cols[1].button("_",key = "1")
        cols[2].button("_",key = "2")
        cols1 = st.columns(3)
        cols1[0].button("_",key = "3")
        cols1[1].button("_",key = "4")
        cols1[2].button("_",key = "5")
        cols2 = st.columns(3)
        cols2[0].button("_",key = "6")
        cols2[1].button("_",key = "7")
        cols2[2].button("_",key = "8")


if __name__ == "__main__":
    board = Board(3)
    board.createBoard()