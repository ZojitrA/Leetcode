class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vgrid = [["Unvisited" for el in els] for els in grid]
        grid = [[int(el) for el in els] for els in grid]
        check_stack = []
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if vgrid[i][j] == "Unvisited" and grid[i][j] == 1:

                    islands += 1
                    vgrid[i][j] == "Visited"
                    check_stack.append([i,j])

                    while len(check_stack) > 0:
                        k,l = check_stack.pop()

                        if k-1 >= 0 and vgrid[k - 1][l] == "Unvisited":
                            vgrid[k-1][l] = "Visited"
                            if grid[k - 1][l] == 1:
                                check_stack.append([k-1,l])

                        if k + 1 < len(vgrid) and vgrid[k + 1][l] == "Unvisited":
                            vgrid[k+1][l] = "Visited"
                            if grid[k + 1][l] == 1:
                                check_stack.append([k+1,l])

                        if l - 1 >= 0 and vgrid[k][l-1] == "Unvisited":
                            vgrid[k][l-1] = "Visited"
                            if grid[k][l-1] == 1:
                                check_stack.append([k,l-1])

                        if l+1 < len(vgrid[k]) and vgrid[k][l+1] == "Unvisited":
                            vgrid[k][l+1] = "Visited"
                            if grid[k][l+1] == 1:
                                check_stack.append([k,l+1])

        return islands


# Runtime: 164 ms, faster than 51.11% of Python3 online submissions for Number of Islands.
# Memory Usage: 15.3 MB, less than 9.40% of Python3 online submissions for Number of Islands.
