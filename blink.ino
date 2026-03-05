#include "pico/stdlib.h"
#include "pico/cyw43_arch.h" // Required for Pico W Wi-Fi chip access

int main() {
    // Initialize the Wi-Fi chip and its GPIOs for LED control
    if (cyw43_arch_init()) {
        // Handle error if init fails
        return -1;
    }

    while (true) {
        // Turn the LED on
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1);
        sleep_ms(250); // Wait for 250 milliseconds

        // Turn the LED off
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 0);
        sleep_ms(250); // Wait for another 250 milliseconds
    }
}
