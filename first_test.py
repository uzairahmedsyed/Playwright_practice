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
    
    browser_tab.wait_for_load_state("networkidle")

    # cookie aur popup ko handle krne k liye 
    acc_cookie_button = browser_tab.locator(".cookie-popup_accept_cookie_button__BUG8H").first
    acc_cookie_button.wait_for(state="visible")
    acc_cookie_button.click()

    klaviyo_popup = browser_tab.locator(".klaviyo-close-form").last
    
    if klaviyo_popup.is_visible():
        klaviyo_popup.click()
    
    #klaviyo_popup.wait_for(state="",timeout=10000)
    #klaviyo_popup.click()


    ## login per click krne k liye

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


    browser_tab.wait_for_load_state("networkidle")


    # Captcha locator define karen
    captcha_popup_close = browser_tab.locator("button.close[aria-label='Close']")

    # 3 seconds tak wait karo, agar popup nazar aaye toh close kar do
    if captcha_popup_close.is_visible(timeout=3000):
        print("Captcha popup detected. Closing now...")
        captcha_popup_close.click()
        # Click ke baad thora intezar taake popup animation khatam ho jaye
        
        browser_tab.wait_for_timeout(1000)

    else:
        print("No Captcha popup appeared. Proceeding...")


    captcha_popup_close.wait_for(state="hidden")
    print("captcha close hogaya")



    clothing_tab = browser_tab.locator("label.text").filter(has_text="Clothing", )
    clothing_tab.wait_for(timeout=20000)
    clothing_tab.click()


    vendor_name = browser_tab.locator(".product-info-inner").filter(has_text="just pret kjh")
    vendor_name.locator(".collection_product_vendor_heading").filter(has_text="just pret kjh")
    vendor_name.click()


    sku_select = browser_tab.locator("label.swatch_sku_KU100-1")
    sku_select.click()

    add_to_cart = browser_tab.locator("#add-to-cart-btn")
    add_to_cart.click()

    
    cart_icon = browser_tab.locator(".header_cart_btn")
    cart_icon.wait_for(timeout=10000)
    cart_icon.click()

    
    browser_tab.wait_for_load_state("networkidle")


    cart_timer_popup = browser_tab.locator(".rental-cart-timer_button__yDKJ4")
    cart_timer_popup.click()


    browser_tab.wait_for_load_state("networkidle")

    #checkout_btn = browser_tab.locator(".mt-30 cart-checkout ")
    #checkout_btn.click()

    chk_btn = browser_tab.get_by_text("Proceed to checkout")
    chk_btn.wait_for(state="visible")
    chk_btn.click()


    browser_tab.wait_for_load_state("networkidle")

    ship_cost = browser_tab.locator(".shippingRadio").first
    #ship_cost.wait_for(state="visible", timeout=5000)
    ship_cost.wait_for(state="visible")
    ship_cost.check()

    

    checkbox_TermAndCondition = browser_tab.locator(".accept-terms input[name=termCondition]").first
    checkbox_TermAndCondition.wait_for(state="visible")
    checkbox_TermAndCondition.check()

    
    place_order =browser_tab.locator(".btn placeYourOrder").first
    place_order.click()

    browser_tab.wait_for_load_state("networkidle")


    # 5. Browser band karna
    browser_tab.close()
    
