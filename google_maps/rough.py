a = {'Total KMS': '593 km', 'Bus_Time': '11 hr 15 min', 'Train_time': '13 hr 54 min', 'Express_Trains_Available': ['Madgaon Tejas Express'], 'Flight Details': {'Fly Time': '1 hr 5 min', 'Flights': 'Air-Asia <--> Indigo <--> Spice-Jet'}}
output_str = "\n".join([f"{k}======{v}" for k, v in a.items()])
print(output_str)
