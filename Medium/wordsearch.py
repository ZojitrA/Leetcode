class Solution(object):
    def exist(self, board, word):

        unvisited = [[True for el in row] for row in board]

        for i in range(len(board)):
            for j in range(len(board[i])):
                unvisited[i][j] = False
                truthy = self.finder(i, j, word, unvisited, board)
                if truthy:
                    return truthy
                unvisited[i][j] = True

        return False

    def finder(self, k, m, s, arr, board):
        if not len(s):
            return True

        first = s[0]
        rest = s[1:]

        if board[k][m] != first:
            return

        if not len(rest):
            return True

        if k-1 >= 0 and arr[k-1][m]:
            arr[k-1][m] = False
            truthy = self.finder(k-1, m, rest, arr, board)
            if truthy:
                return truthy
            arr[k-1][m] = True

        if k+1 < len(board) and arr[k+1][m]:
            arr[k+1][m] = False
            truthy = self.finder(k+1, m, rest, arr, board)
            if truthy:
                return truthy
            arr[k+1][m] = True

        if m-1 >=0 and arr[k][m-1]:
            arr[k][m-1] = False
            truthy = self.finder(k, m-1, rest, arr, board)
            if truthy:
                return truthy
            arr[k][m -1] = True

        if m+1 < len(board[k]) and arr[k][m+1]:
            arr[k][m+1] = False
            truthy = self.finder(k, m+1, rest, arr, board)
            if truthy:
                return truthy
            arr[k][m+1] = True

        return False

#back tracking problem set
# faster than 97% python3 solutions
