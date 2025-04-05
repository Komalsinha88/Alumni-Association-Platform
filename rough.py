class Solution:   
    def peakElement(arr):
        # Code here
        mull=[]
        if arr[len(arr)-1]==max(arr):
            
            return mull.append(len(arr)-1)
        for h,i in enumerate(arr):
       
            if h <len(arr)-1:
                print("i",h,len(arr)-2) 
                print("!!!!",arr[h],arr[h+1],arr[h+2])
                if arr[i]<arr[i+1]>arr[i+2]:
                     arr.append(i+1)
                if len(mull)>1:
                    return mull[0]
                elif len(mull)==1:
                    return "true"
            



re=Solution.peakElement([1,2,4,5,7,8,3])
print(re)