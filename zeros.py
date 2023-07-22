import time
import Jetson.GPIO as GPIO

# Pin definitions for the servos
servo_pins = [3, 5, 7]

def setup_servos():
    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set up the servo pins as output pins
    for pin in servo_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def stop_servos():
    # Set the duty cycle of all servo pins to 0 to stop the servos
    for pin in servo_pins:
        servo_pwm = GPIO.PWM(pin, 50)  # 50 Hz frequency
        servo_pwm.start(0)
        time.sleep(0.5)  # Give some time to set the duty cycle
        servo_pwm.stop()

def cleanup():
    # Cleanup the GPIO configuration
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup_servos()
        stop_servos()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
