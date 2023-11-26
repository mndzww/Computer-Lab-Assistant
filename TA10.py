import csv
with open('tabel.csv','w') as csv_file: 
  keterangan = ['NO','NPM','NAMA','Tugas','Kuis','UTS','UAS','Jumlah','Nilai Mutu']
  input_data = csv.DictWriter(csv_file,fieldnames=keterangan) input_data.writeheader()
  input_data.writerow({'NO': '1','NPM':'140310130046' ,'NAMA': 'Rina Diana', 'Tugas':'88','Kuis':'82', 'UTS':'87', 'UAS':'78','Jumlah':'84','Nilai Mutu':'A'})
  input_data.writerow({'NO': '2','NPM':'140310130062' ,'NAMA': 'Mariana', 'Tugas':'86', 'Kuis':'84', 'UTS':'75', 'UAS':'76', 'Jumlah':'80','Nilai Mutu':'A'})
  input_data.writerow({'NO': '3','NPM':'140310140047' ,'NAMA': 'Maulana', 'Tugas':'68', 'Kuis':'65', 'UTS':'80', 'UAS':'80', 'Jumlah':'73','Nilai Mutu':'B'})
  input_data.writerow({'NO': '4','NPM':'140310140047' ,'NAMA': 'Akhmad', 'Tugas':'90', 'Kuis':'89', 'UTS':'82', 'UAS':'84', 'Jumlah':'86','Nilai Mutu':'A'})
  input_data.writerow({'NO': '5','NPM':'140310150028' ,'NAMA': 'Hutomo', 'Tugas':'95', 'Kuis':'90', 'UTS':'80', 'UAS':'90', 'Jumlah':'89','Nilai Mutu':'A'}) 
nilai = []
with open('tabel.csv') as csv_file: 
  baca_data = csv.reader(csv_file) 
  for row in baca_data:
    nilai.append(row)
labels = nilai.pop(0) for i in range(6):
  del nilai [i]
print(f'{labels[0]} \t {labels[1]} \t\t\t{labels[2]} \t\t {labels[3]} \t {labels[4]} \t{labels[5]} \t {labels[6]} \t {labels[7]}	{labels[8]}') 
print(" ---------------------------------------------------------------------------- ")
for data in nilai:
  print (f'{data[0]} \t {data[1]} \t\t{data[2]}	\t {data[3]} \t {data[4]} \t {data[5]} \t{data[6]} \t {data[7]}	{data[8]}')
