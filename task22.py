#QQS bilan mahsulot narxini hisoblash (15%)

narx=20_000.0
QQS=15
#1-usul
narx_qqs=narx*QQS/100
haqiqiy_narx=narx+narx_qqs
#2-ususl 
narx_qqs=narx*(1+QQS/100)

print(narx_qqs)