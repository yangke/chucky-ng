
import logging

from job.Symbol import Symbol
from job.SourceSinkSet import SourceSinkSet


class ChuckyJob(object):
    
    # When implementing additional command-line flags, the
    # constructor's parameter list is likely to become
    # longer and longer.
    # Suggested improvement: provide setters for each of the
    # configurable fields and remove the constructor
    
    def __init__(self,function,needcache=False,callee_set=set(),parameter_set=set(),variable_set=set()):
        self.function=function
        self.sourcesinks = SourceSinkSet(callee_set.copy(),parameter_set.copy(),variable_set.copy())
        self.needcache=needcache
        #When analyse limited functions or the specified one function, this should be None.
        #To notify the SymbolUser Selector to select the symbol users rather than directly use the jobset.
        self.job_set=None         
        self.logger = logging.getLogger('chucky')
        
    def getSourceSinks(self):
        return self.sourcesinks
    
    def setJobSet(self,job_set):
        self.job_set=job_set
        
    def getJobSet(self):
        return self.job_set
    
    def addSourceSinkByString(self,code,decl_type,identifierType):
        self.sourcesinks.addSourceSinkByString(code,decl_type,identifierType)
        
    def addSourceSinkByDBIdentifier(self,db_identifier,identifierType):
        self.sourcesinks.addSourceSinkByDBIdentifier(db_identifier,identifierType)
    
    def split(self):
        c_itemset,p_itemset,v_itemset=self.sourcesinks.genCombination()
        c_itemset.append('callee_combination')
        p_itemset.append('parameter_combination')
        v_itemset.append('variable_combination')
        jobset=set()
        if(len(c_itemset)+len(p_itemset)+len(v_itemset)==3):
            raise Exception("Error:Zero sourc/sink in this job!!")
        for cs in c_itemset:
            if len(c_itemset)==1:
                cs=set()
            elif cs=='callee_combination':
                continue                
            for ps in p_itemset:
                if len(p_itemset)==1:
                    ps=set()
                elif ps=='parameter_combination':
                    continue
                for vs in v_itemset:
                    if len(v_itemset)==1:
                        vs=set()
                    elif vs=='variable_combination':
                        continue                    
                    job=ChuckyJob(self.function,True,cs,ps,vs)
                    jobset.add(job)
        return jobset       
    
                
    def __eq__(self, other):
        if self.function==other.function and self.sourcesinks == other.sourcesinks:
            return True
        else:
            return False
        
    def __hash__(self):
        ss=self.getSourceSinks()
        return hash(ss) ^ hash(self.function) ^ hash(self.needcache)
        #return hash(ss) ^ hash(self.function) ^ hash (self.n_neighbors) ^ hash(self.needcache)
    
    def __str__(self):
        s = '{} ({}) - {}'
        s = s.format(
            self.function,
            self.function.node_id,
            str(self.sourcesinks))
        return s
