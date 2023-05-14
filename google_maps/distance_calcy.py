
import time
import json
from google_maps.all import *
from google_maps import store

def place_search(Place_origin, Place_dest):
    Place_1 = Place_origin + ',india'
    Place_2 = Place_dest + ',india'
    # Place_1 = "goa"+','+"india"
    # Place_2 = "bangalore"+','+"india"
    print(Place_1)
    print(Place_2)
    if Place_1 and Place_2:
        if Place_1 != Place_2:
            print("We are searching. Please wait...")
            driver.get(urls.maps)
            print("driver open")
        else:
            raise Exception("Origin and destination cannot be the same.")
    else:
        raise Exception("Origin and/or destination not entered.")
    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, store.search_box)))
    except:
        raise Exception("Could not find search box element. The website may be too heavy or the connection is weak.")



    def searchplace():
        Place=driver.find_element(By.XPATH,store.search_box)
        Place.send_keys(Place_1)
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, store.directions1)))
        Place.send_keys(Keys.RETURN)
        WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, store.save)))

    searchplace()


    def directions():
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, store.directions)))
        directions = driver.find_element(By.XPATH,store.directions)
        directions.click()
        time.sleep(2)

    directions()

    def find():
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, store.find_position)))
        time.sleep(1)
        find = driver.find_element(By.XPATH, store.find_position)
        find.send_keys(Place_2)
        find.send_keys(Keys.RETURN)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, store.details)))
        time.sleep(1)

    find()


    def kilometers():
        time.sleep(2)
        Totalkilometers=driver.find_element(By.XPATH,store.kms)
        Total_kms=Totalkilometers.text
        Bus=driver.find_element(By.XPATH,store.bus)
        Bus_tr=Bus.text
        Train=driver.find_element(By.XPATH,store.train)
        train_tr=Train.text
        return {"total_kms": Total_kms, "bus_info": Bus_tr, "train_info": train_tr}

    kms_bus_train = kilometers()

    def available():
        name_elements = driver.find_elements(By.XPATH, store.train_name)
        express_names = []

        for name_element in name_elements:
            name_text = name_element.text
            if "express" in name_text.lower() and "bypass" not in name_text.lower():
                express_names.append(name_text)
        if not express_names:
            express_names = "No express trains available."

        return {"express_trains_available": express_names}

    express_trains = available()


    def flights():
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, store.flight)))
        click_button = driver.find_element(By.XPATH, store.flight)
        click_button.click()
        try:
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, store.find_flight)))
        except:
            pass
        flight_infos = []
        try:
            flight_info_elements = driver.find_elements(By.XPATH, store.fecth_flight)
            for flight_info_element in flight_info_elements:
                flight_info_text = flight_info_element.text
                flight_infos.append(flight_info_text)
        except:
            flight_infos = "Error: Could not fetch flight details."
            return {"Flight Details": flight_infos}

        if not flight_infos:
            flight_infos = "No flights available."
            return {"Flight Details": flight_infos}
        else:
            return {"Flight Details": {"Fly Time": flight_infos[0],
                                       "Flights": "Air-Asia <--> Indigo <--> Spice-Jet"}}


    experess_flights=flights()
    driver.quit()
    # Create a dictionary to store all the information
    result_dict = {**kms_bus_train, **express_trains,**experess_flights}
    return (result_dict)
    # with open('data.json', 'w') as f:
    #     json.dump(result_dict, f, indent=4)

