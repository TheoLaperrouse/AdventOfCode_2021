file = open('input.txt', "r")
lines = file.readlines()
file.close()

coords=[]
res = {}
for line in lines:
    coords.append([a.strip() for a in line.strip().split('->')])

coords_value = [{'x1': int(coord[0].split(',')[0]) ,'y1': int(coord[0].split(',')[1]),'x2': int(coord[1].split(',')[0]),'y2': int(coord[1].split(',')[1])} for coord in coords]

for coord_value in coords_value:
    if coord_value['x1'] == coord_value['x2']:
        yMax = max(coord_value['y1'],coord_value['y2'])
        yMin = min(coord_value['y1'],coord_value['y2'])
        delta = abs(int(yMax) - int(yMin))
        while delta >= 0:
            key = f'{coord_value["x1"]}-{int(yMax)-int(delta)}'
            if key in res:
                res[key] +=1
            else:
                res[key] = 1
            delta -= 1
    elif coord_value['y1'] == coord_value['y2']:
        xMax = max(coord_value['x1'],coord_value['x2'])
        xMin = min(coord_value['x1'],coord_value['x2'])
        delta = abs(int(xMax) - int(xMin))
        
        while delta >= 0:
            key = f'{int(xMax)-int(delta)}-{coord_value["y1"]}'
            
            if key in res:
                res[key] +=1
            else:
                res[key] = 1
            delta -= 1       

counter = 0  
for key in res.keys():
    if res[key] >= 2:
        counter += 1
print(f'Résultat : {counter}')