from selenium import webdriver
import multiprocessing
import time
from tokens import Tokens

def add_to_blocklist():
    driver = webdriver.Safari()

    driver.get('http://192.168.0.21/admin/groups-domains.php?type=black')

    field = driver.find_element_by_name('pw')
    field.click()

    field.send_keys(Tokens['password'])

    submit = driver.find_element_by_class_name('btn-primary')
    submit.click()

    time.sleep(5)

    black_list = driver.find_element_by_id('new_domain')
    black_list.click()
    sub_black = driver.find_element_by_id('add2black')
    
    with open('domainlist.txt') as domains:
        domain = domains.readlines()

        for line in domain:
            print(line)
            black_list.send_keys(line)
            sub_black.click()
            time.sleep(1)



 
if __name__ == '__main__':


    # start = time.perf_counter()
    # processes = []
    # for _ in range(2):
    #     p = multiprocessing.Process(target=login)
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()
    add_to_blocklist()

