import time
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = None
xpath = None
element = None

app = Flask(__name__)

@app.route("/setURL", methods=["POST"])
def setURLMethod():
    content = request.get_json()
    url = content['url']
    global driver
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(url)
    print(url)
    return jsonify({"url":url})

@app.route("/setXPATH", methods=["POST"])
def setXpath():
    content = request.get_json()
    xpath= content['xpath']
    global element
    element = driver.find_element_by_xpath(xpath)
    return jsonify({"xpath":xpath})

@app.route("/click", methods=["POST"])
def click():
    global element
    element.click()
    return "done"

@app.route("/hover", methods=["POST"])
def hover():
     global element
     global driver
     hover = ActionChains(driver).move_to_element(element)
     hover.perform()
     return "done"

@app.route("/close", methods=["POST"])
def close():
    global driver
    driver.close()
    return "done"

if __name__=="__main__":
    app.run(debug=True)


