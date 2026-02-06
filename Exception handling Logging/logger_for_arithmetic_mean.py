import logging

logging.basicConfig(
    filename='app.log',
    filemode='w',
    format= '%(name)s - %(levelname)s - %(message)s',
    level= logging.DEBUG
)

def average(numbers):
    if not numbers:
        logging.debug("The list is empty")
        try:
            result = 0 / 0
        except ZeroDivisionError:
            logging.warning("Division by zero")
    else:
        try:
            all_numbers = True
            for n in numbers:
                if not isinstance(n, (float, int)):
                    all_numbers = False
            if not all_numbers:
                logging.critical("Incorrect data entered")
            else:
                result = sum(numbers) / len(numbers)
                logging.info(result)
        except ZeroDivisionError:
            logging.warning("Division by zero")
        except ValueError:
            logging.error("ValueError")


average([1, 2, 3, 4, 5])
average([10, -20, -30])
average([])
average([1, 2, 3, 0, 5])
average([1, 2, "three", 4, 5])
#root - INFO - 3.0
#root - INFO - -13.333333333333334
#root - DEBUG - The list is empty
#root - WARNING - Division by zero
#root - INFO - 2.2
#root - CRITICAL - Incorrect data entered