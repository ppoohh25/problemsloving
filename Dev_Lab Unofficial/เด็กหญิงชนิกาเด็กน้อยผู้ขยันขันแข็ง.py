must =['เรียนคณิตศาสตร์online','เรียนอังกฤษonline','เรียนไทยonline','เรียนวิทย์online','อ่านเตรียมสอบ o-net','ทำงานบ้าน','เรียนวาดรูป','เรียนร้องเพลง']
do = list(map(str,input().split(',')))
for i in range(len(must)):
  if must[i] == 'เรียนคณิตศาสตร์online':
    must[i] = 1
  if must[i] == 'เรียนอังกฤษonline':
    must[i] = 2
  if must[i] == 'เรียนไทยonline':
    must[i] = 3
  if must[i] == 'เรียนวิทย์online':
    must[i] = 4
  if must[i] == 'อ่านเตรียมสอบ o-net':
    must[i] = 5
  if must[i] == 'ทำงานบ้าน':
    must[i] = 6
  if must[i] == 'เรียนวาดรูป':
    must[i] = 7
  if must[i] == 'เรียนร้องเพลง':
    must[i] = 8
for i in range(len(do)):
  if do[i] == 'เรียนคณิตศาสตร์online':
    do[i] = 1
  if do[i] == 'เรียนอังกฤษonline':
    do[i] = 2
  if do[i] == 'เรียนไทยonline':
    do[i] = 3
  if do[i] == 'เรียนวิทย์online':
    do[i] = 4
  if do[i] == 'อ่านเตรียมสอบ o-net':
    do[i] = 5
  if do[i] == 'ทำงานบ้าน':
    do[i] = 6
  if do[i] == 'เรียนวาดรูป':
    do[i] = 7
  if do[i] == 'เรียนร้องเพลง':
    do[i] = 8
diff = list(set(must)-set(do))
for i in range(len(diff)):
  if diff[i] == 1: 
    diff[i] = 'เรียนคณิตศาสตร์online'
  if diff[i] == 2: 
    diff[i] = 'เรียนอังกฤษonline'
  if diff[i] == 3: 
    diff[i] = 'เรียนไทยonline'
  if diff[i] == 4: 
    diff[i] = 'เรียนวิทย์online'
  if diff[i] == 5: 
    diff[i] = 'อ่านเตรียมสอบ o-net'
  if diff[i] == 6: 
    diff[i] = 'ทำงานบ้าน'
  if diff[i] == 7: 
    diff[i] = 'เรียนวาดรูป'
  if diff[i] == 8: 
    diff[i] = 'เรียนร้องเพลง'
print('ยังเหลือสิ่งที่ต้องทำอีก {} อย่าง'.format(len(diff)))
for i in range(len(diff)):
  print('- {}'.format(diff[i]))