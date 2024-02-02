import time

def scroll_down_to_bottom(driver, scroll_speed=50):
    while True:
        # Get the current scroll position
        current_position = driver.execute_script("return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;")

        # Scroll down by the specified speed
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(0.1)  # Adjust sleep time based on your preference

        # Get the updated scroll position
        updated_position = driver.execute_script("return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;")

        # Check if the scroll position remains the same (indicating we are at the bottom)
        if current_position == updated_position:
            print("Reached the bottom of the page. Stopping scrolling.")
            break