import json
ahorradores={}
with open("Ahorradores.json","r") as file:
    ahorradores=json.load(file)
intermedio=[{"NumCuenta":ahorradores["cliente"][i]["NumCuenta"],"Saldo":ahorradores["cliente"][i]["Saldo"] } for i in range(len(ahorradores["cliente"])) if ahorradores["cliente"][i]["Saldo"]> 35_000_000 ]
final=[{"Consecutivo":i+1,"NumCuenta":intermedio[i]["NumCuenta"],"Saldo":intermedio[i]["Saldo"]} for i in range(len(intermedio)) ]
with open('Dian.json','w') as file:
    json.dump(final,file,indent=4)
