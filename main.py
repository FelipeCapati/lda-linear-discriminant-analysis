from lda import LDA, LdaType
import pandas as pd

data = pd.read_csv("./data/fisher.csv")

lda = LDA()
lda.fit(data=data, target_column_name='target')
conversion_data = lda.conversion(LdaType.Two)
print(conversion_data)
