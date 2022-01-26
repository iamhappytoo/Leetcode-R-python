class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[""]
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        answer.pop(0)
        return answer
      
###Remove condition times
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        for i in range(1,n+1):
            ansstr=""
            if i % 3 == 0:
                ansstr+="Fizz"
            if i % 5 == 0:
                ansstr+="Buzz"
            if not ansstr:
                ansstr = str(i)
            ans.append(ansstr)
        return ans
###Use hash to enable for loop for thousands of mapping cases
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}
        
        for num in range(1,n+1):
            ansstr = ""
            for key in fizz_buzz_dict:
                if num % key == 0:
                    ansstr += fizz_buzz_dict[key]
            if not ansstr:
                ansstr += str(num)
            ans.append(ansstr)
        return ans
    
