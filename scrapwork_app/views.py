from django.shortcuts import render
from django.http import HttpResponse
from .forms import workScrapForm
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

def nameScrap(request): 
    if request.method == 'POST':
        form = workScrapForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            result=workScraper(name)
            return render(request, 'works.html', {'name': name, 'result':result})
    else:
        form = workScrapForm()
    
    return render(request, 'nameScrap.html', {'form': form})


def workScraper(word):

    service = Service(ChromeDriverManager().install()) 
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")  

    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    resultados = []
    
    driver.get("https://www.tecnoempleo.com/")
    time.sleep(5)  
    
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "te")
    ))

    search_box.send_keys(word)
    search_box.submit()

    driver.implicitly_wait(10)

    titles = driver.find_elements(By.XPATH, "//h3[@class='fs-5 mb-2']//a")

    print(f"Se han encontrado {len(titles)} resultados.")
    
    for title in titles:
        work = title.text.strip() 

        if work and word.lower() in work.lower():
            print(f"Resultado encontrado: {work}") 
            resultados.append(work) 

    driver.quit()  
    
    if resultados:
        return resultados
    else:
        return ["No se encontraron resultados para la búsqueda."]