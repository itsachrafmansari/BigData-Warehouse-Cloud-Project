from data_generator import run

if __name__ == "__main__":
    # Constants initialisation
    FAKER_SEED = 22
    ORDERS_COUNT = 500000
    ORDERS_CHANNEL = "mobile_sales"
    ORDER_CANCELING_RATE = 0.1
    DAYS_COUNT = 4
    OUTPUT_FOLDER = "data"

    run(FAKER_SEED, ORDERS_COUNT, ORDERS_CHANNEL, ORDER_CANCELING_RATE, DAYS_COUNT, OUTPUT_FOLDER)
