class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mydict = {}
        for string in cpdomains:
            rep, domain = string.split()
            domainch = domain.split('.')
            for i in range(len(domainch)):
                usedomain = '.'.join(domainch[i:])
                mydict[usedomain]=mydict.get(usedomain,0)+int(rep)
                
        res = []
        for key in mydict.keys():
            res.append(' '.join([str(mydict[key]), key]))
            
        return res
      
      
##A more brief version
class Solution:
  def subdomainVisits(self, cpdomains):
    ans = collections.Counter()
    for domain in cpdomains:
      count,domain = domain.split()
      count = int(count)
      frags = domain.split('.')
      for i in range(len(frags)):
        ans['.'.join(frags[i:])]+=count
       
      return ["{} {}".format(cnt,dom) for dom, cnt in ans.items()]

###Space complexity: O(n), time complexity: O(n), because the domain length has maximum limit, a constant.  
