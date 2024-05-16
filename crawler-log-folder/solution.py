class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        count = 0
        for log in logs:
            if log == "../":
                if count > 0:
                    count -= 1
            elif log != "./":
                count += 1
        return count
        
