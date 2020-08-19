# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:23:19 2020

@author: MUHAMMAD
"""
import re
import numpy as np
class learnkit:
    
    class ImbalanceError(Exception):
        def __init__(self,message):
            print(message)
    
    class _FitError(Exception):
        def __init__(self,message):
            print(message)
                    
    
    class imputer:
        
                
        import numpy as np
        
        class Multi_Imputer():
                
            def __init__(self, strategy=['mean'], ratio=None, random_state=12):
                
                self.mean = {}
                self.mode = {}
                self.median = {}
                self.seed = random_state
                
                if ratio == None:
                    def_ratio = {'mean':0.3,'median':0.3,'mode':0.4}
            
                    if len(strategy) == 3:
                        self.ratio = def_ratio
                        
                    elif len(strategy) == 2:
                        self.ratio = {strategy[0]:0.5,strategy[1]:0.5}
                    else:
                        self.ratio = {strategy[0]:1}
                    ratio = list(self.ratio.values())
                else:
                    if isinstance(ratio,str):
                        ratio = ratio.strip()
                        try:
                            split_ratio = ratio.split(':')
                            split_ratio  = list(map(float,split_ratio))
                            
                        except ValueError:
                            split_ratio = ratio.split(',')
                            split_ratio  = list(map(float,split_ratio))
                        except ValueError:
                            
                            raise ValueError("Could not convert %s to float" % ratio)
                        if sum(split_ratio) != 1:
                                raise learnkit.ImbalanceError("Imbalance ratio: total ratio must sum to 1")
                        ratio = split_ratio
                        
                        
                    elif isinstance(ratio,(list,tuple)):
                        for r in ratio:
                            if isinstance(r,float) == False:
                                try:
                                    float(r)
                                except ValueError:
                                    raise ValueError(r,"str object is not a valid ratio")
                    else:
                        raise ValueError("ratio should be a list of value or string but %s was passed" % type(ratio))
                    
                if len(strategy) > 3 or len(ratio) >3:
                    raise ValueError("Too many values of strategy or ratio")
        
                if len(strategy) > len(ratio):
                    raise learnkit.ImbalanceError('too many values of strategy than ratio')
        
                elif len(strategy) < len(ratio):
                    raise learnkit.ImbalanceError('too many values of ratio than strategy')
        
        
        
                ratio = list(map(float,ratio))    
                
                for s in strategy:
                        if s not in ['mean','median','mode']:
                            raise ValueError(s,"is not recognize as a valid strategy")
        
                if len(ratio) == 3:
                    self.ratio = {strategy[i]:ratio[i] for i in range(len(ratio))}
        
        
                elif len(ratio) == 2:
                    self.ratio = {strategy[i]:ratio[i] for i in range(len(ratio))}
        
                elif len(ratio) ==1:
                    self.ratio = {strategy[0]:ratio[0]}
                        
                
                        
                self.strategy = strategy
                            
                    #np.random.__init__(self,seed)
                    
            
            
            def transform(self,df):
                
                if self.mean == {}:
                    raise learnkit.FitError("Can not transform unfitted data")
                    
                np.random.seed(self.seed)
                ratio = self.ratio
                X = df.copy()
               
                columns = X.columns
                index = X.index
                array = list(index)
                
                
                df_size = len(index)
                
                for stra in self.strategy:
                    array = list(index)
                    np.random.shuffle(array)
                    
                    fill = np.random.choice(array,size=round((df_size*self.ratio[stra])), replace = False)
                    
                    if stra == 'mean':
        
                        X.loc[fill] = X.loc[fill].fillna({column:self.mean[column] for column in columns})
        
        
                    elif stra == 'median':
        
                        X.loc[fill] = X.loc[fill].fillna({column:self.median[column] for column in columns})
                        
        
                    elif stra == 'mode':
                        X.loc[fill] = X.loc[fill].fillna({column:self.mode[column] for column in columns})
                       
                if sum(X.isna().sum()) > 0:
                    
                    strat = {'mode':self.mode,'mean':self.mean,'median':self.median}
                    
                    max_column = max(self.ratio)
                    X = X.fillna({column:strat[max_column][column] for column in columns})
                
                return X
                
            def fit(self,df,label):
                X = df.copy()
                columns = X.columns
                
                for column in columns:
                    self.mean[column] = X[column].mean()
                    self.median[column] = X[column].median()
                    self.mode[column] = X[column].mode().values[0]
                    
                return self
                    
    class dropper():
        def __init__(self,columns=None):
            
            self.columns = columns
            
        def transform(self,df):
            X = df.copy()
            return X.drop(self.columns,axis=1)
            
            
        def fit(self,*_):
            return self
class exctract():
    
    class date:
        def __init__(self,line):
            self.line = line
        #
        import re
        def extract_date(line):
            """Returns an extracted date from a line of text text"""
            
           
            pattern_1 = '((\d{1,2}\s?)?((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[\.\,]?)) \d{4,4}'
            pattern_2 = '(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[\.,]?[\s-](\d{1,2}[th|st|rd|nd]?,?[\s-])?\d{4,4}'
            pattern_3 = '((\d{,2}[/-])(\d{,2}[/-])\d{2,4})'
            pattern_4 = '((\d{,2}/)\d{2,4})|\d{4,4}'
            
            patterns = [pattern_1,pattern_2,pattern_3,pattern_4]
            for pattern in patterns:
                match = re.search(pattern, line)
                if match:
                    return match.group()
        
        def separate_date(date):
            """ Returns a string of date, that can be coverted to a timeStammp,
            from extracted date from a text 
            """
            
            month_list_1 = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
                            
            months_1 = {month : val+1 for val, month in enumerate(month_list_1)}
            
            
            dates = re.findall(r'\d{1,4}',date)
            if len(dates) == 3:
                
                #if re.search(r'\d{1,2}-\d{1,2}-\d{2,4}', date):
                 #   day, month, year = dates[0], dates[1], dates[2]  
                
                day, month, year = dates[1], dates[0], dates[2]
                
            elif len(dates) == 2:
                found = re.search(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*',date)
                if found:
                    day, month, year = dates[0], found.group(), dates[1]
                else:
                    day, month, year = '01', dates[0], dates[1]
                    
            elif len(dates) == 1:
                found = re.search(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*',date)
                if found:
                    day, month, year = '01', found.group(), dates[0]
                else:
                    day, month, year = '01', 'Jan', dates[0]
                
                
            # Checking and correcting year format
            
            if len(year) == 2:
                tens = year
                year = '19'+tens
                
            #checking and uniforming month label
            
            if month.isdigit() == False:
                try:
                    month = months_1[month]
                
                except KeyError:
                    month = months_1[month[:3]]
            elif len(month) > 2:
                month = month.lstrip('0')
            # Filling in missing months and day
            time = '-'.join([str(day),str(month),str(year)])
            return time
