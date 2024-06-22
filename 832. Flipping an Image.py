class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output = []
        for i in range(len(image)):
            sub_L = []
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    sub_L.insert(0, 1)
                else:
                    sub_L.insert(0, 0)
            output.append(sub_L)

        return output
    #https://leetcode.com/problems/flipping-an-image/