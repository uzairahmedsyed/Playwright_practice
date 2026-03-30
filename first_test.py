from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 1. Browser kholna (headless=False taake aapko nazar aaye)
    browser_Khonla = p.chromium.launch(headless=False, slow_mo=1000) 
    
    # 2. Naya page kholna
    browser_tab = browser_Khonla.new_page()
    
    # 3. Kisi website par jana
    browser_tab.goto("https://dev.fashionpass.com" , wait_until="load")
    
    # 4. Check karna ke kya hum sahi jagah hain (Assertion)
    # print("Page Title is:", browser_tab.title())
    
    # cookie aur popup ko handle krne k liye 
    acc_cookie_button = browser_tab.locator(".cookie-popup_accept_cookie_button__BUG8H").first
    acc_cookie_button.wait_for(state = "visible")
    acc_cookie_button.click()

    klaviyo_popup = browser_tab.locator(".klaviyo-close-form")
    klaviyo_popup.wait_for(state="visible", timeout=25000)
    klaviyo_popup.click()


    # login per click krne k liye

    signup_btn = browser_tab.locator(".header_logincomp_loginBtn")
    signup_btn.wait_for(state="visible")
    signup_btn.click()


    # email per abhi autofocus hai toh sirf text field mein input krna hai 

    email_field = browser_tab.locator("#email")
    email_field.wait_for(state="visible")
    email_field.fill("testuzair28march26dev1@yopmail.com")


    # password per abhi autofocus hai toh sirf text field mein input krna hai 

    password_field = browser_tab.locator("#password")
    password_field.wait_for(state="visible")
    password_field.fill("testing")


    login_btn = browser_tab.locator(".login-btn")
    login_btn.click()


    clothing_tab = browser_tab.locator("label.text").filter(has_text="Clothing")
    clothing_tab.wait_for(timeout=10000)
    clothing_tab.click()


    vendor_name = browser_tab.locator(".product-info-inner").filter(has_text="just pret kjh")
    vendor_name.locator(".collection_product_vendor_heading").filter(has_text="just pret kjh")
    vendor_name.click()


    # 5. Browser band karna
    # browser.close()
    browser_tab.wait_for_timeout(100000)
