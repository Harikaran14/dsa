class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        f=0
        s=0
        while  f<len(name)  :
            
            if name[f]==typed[s]:
                f+=1
                s+=1
            elif typed[s]==name[max(0,f-1)]:
                s+=1
            else:
                return False

            if s==len(typed)-1 and f<len(name)-1:
                return False    

        return True                

x=Solution()
print(x.isLongPressedName('alex','aaleexa'))