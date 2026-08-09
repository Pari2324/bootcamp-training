# spiral matrix
res = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while left <= right and top <= bottom:

            # Top Row
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # Right Column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Bottom Row
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # Left Column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res