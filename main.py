import services
import logging

def main():

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    # print(services.data_operator.collect_data())
    # print(services.analytics.average_price(services.data_operator.collect_data()))
    # print(services.analytics.average_price_by_location(services.data_operator.collect_data()))
    # print(services.analytics.properties_below_average(services.data_operator.collect_data()))
    print(services.data_operator.spread_data(services.analytics.average_price(services.data_operator.collect_data())))

if __name__ == "__main__":
    main()