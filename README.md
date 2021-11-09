# Financial-Quant-Works

There are several tools here that can be used mostly for stock selection purposes as well as economic analyses.
1) deltaMAV_Foreks:
This tool uses a simple rolling moving average calculation but counts the increases in the results in sliding windows. The purpose, code and results are explained here:
https://medium.com/@kecandir/simple-momentum-tool-for-stock-selection-be69463c9700

2) DTW_USDTRYvsTCMB:
This is a Dynamic Time Warping work that measures the minimum distance between the changes in USD/TRY cross currency vs Turkish Central Bank's (TCMB) policy decisions. 

3) FactorMultiModel:
This is a multi factor stock selection algorithm that uses several methods covering both value and momentum investing fields. It utilizes Bloomberg's interal Jupyter Notebook environment called BQNT as well as its BQL query abilities. The data is pulled directly from Bloomberg without any API requests. The end results are output into two dataframes which are then visualized using an interactive scatter plot class.
