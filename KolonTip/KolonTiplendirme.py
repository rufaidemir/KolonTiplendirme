import pandas



class KolonTiplendirme:
    tipDetayHarfleri = ["","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    def __init__(self, df:pandas.DataFrame, param1:str, otherColumns:list):
        self.df=df
        self.param1=param1
        self.otherColumns=otherColumns
    
    
    def typerCol(self):
        try:
            df = self.df.dropna(how="all").reset_index(drop=True)
            otherColumns=self.otherColumns
            
            df["TipNumarasi"] = 1
            df["DetayTipNumarasi"] = 1
            df["KEY"] = ""
            df["TIPHARF"]=""
            df["TIPADI"]="TIP."
            uniqueNames = list(df[self.param1].unique())
            for i in range(df.shape[0]):
                df.loc[i, "TipNumarasi"] = uniqueNames.index(df[self.param1][i])+1
            
            for i in otherColumns:
                df["KEY"] = df["KEY"]+df[i].astype(str)
                
            uniqueTypeList = []
            for i in list(df['TipNumarasi'].unique()):
                fdf = df[df["TipNumarasi"]==i]
                
                flag=0
                for j in fdf['KEY'].unique():
                    fdf_j = fdf[fdf['KEY']==j]
                    if j in uniqueTypeList:
                        df.loc[fdf_j.index, "DetayTipNumarasi"] = flag
                    else:
                        uniqueTypeList.append(j)
                        df.loc[fdf_j.index, "DetayTipNumarasi"] = flag
                        flag +=1
                    # print(i,"---",j,"---",flag, j in uniqueTypeList)
        
            for i in range(df.shape[0]):
                try:
                    df.loc[i, "TIPHARF"] = self.tipDetayHarfleri[df["DetayTipNumarasi"][i]]
                except Exception as e:
                    print(e)

            df.drop(['KEY'], axis = 1, inplace = True) 
            df["TIPADI"] = "TIP."+df["TipNumarasi"].astype(str)+df['TIPHARF']
            return df
        except Exception as e:
            print(e)
    
    @property
    def getTypedDf(self)->pandas.DataFrame:
        return self.typerCol()