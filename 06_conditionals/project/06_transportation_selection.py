try:

  distance = int(input('Please enter distance in km : ').strip())

  if distance < 0 or distance > 50_000:
    print ('Please enter realistic distance')
    exit()
 
  if distance < 3:
    transport = 'Walk'
  elif distance <= 15: # distance >= 3 and distance <= 15
    transport = 'Bike'
  elif distance <= 100:
    transport = 'Car'
  elif distance <= 500:
    transport = 'train'
  else:
    transport = 'Aeroplane'

  print(f"\nDistance: {distance} km")
  print(f"Recommended Transport: {transport}")

except ValueError:
  print ("Invalid input! Please enter a whole number.")