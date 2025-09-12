#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <limits>

/**
 * @class Item
 * @brief Represents an item with a supplier code, item code, and price.
 *
 * This class encapsulates the data for a single item, providing methods
 * to access its properties and display its information.
 */
class Item {
public:
    /**
     * @brief Constructor for the Item class.
     * @param supplierCode The code of the supplier.
     * @param itemCode The code of the item.
     * @param price The price of the item.
     */
    Item(const std::string& supplierCode, const std::string& itemCode, double price)
        : supplierCode_(supplierCode), itemCode_(itemCode), price_(price) {}

    /**
     * @brief Gets the supplier code.
     * @return The supplier code as a string.
     */
    std::string getSupplierCode() const {
        return supplierCode_;
    }

    /**
     * @brief Gets the item code.
     * @return The item code as a string.
     */
    std::string getItemCode() const {
        return itemCode_;
    }

    /**
     * @brief Gets the price of the item.
     * @return The price as a double.
     */
    double getPrice() const {
        return price_;
    }

    /**
     * @brief Displays the item information to the standard output.
     */
    void display() const {
        std::cout << supplierCode_ << " " << itemCode_ << " " << price_ << std::endl;
    }

private:
    std::string supplierCode_;
    std::string itemCode_;
    double price_;
};

/**
 * @brief Reads item data from a file and populates a vector of Item objects.
 * @param fileName The name of the input file.
 * @param items A reference to a vector of Item objects to be populated.
 */
void readItemsFromFile(const std::string& fileName, std::vector<Item>& items) {
    std::ifstream inputFile(fileName);
    if (!inputFile) {
        std::cerr << "Error opening input file." << std::endl;
        return;
    }

    std::string line;
    while (std::getline(inputFile, line)) {
        std::stringstream ss(line);
        std::string supplierCode, itemCode;
        double price;
        if (ss >> supplierCode >> itemCode >> price) {
            items.emplace_back(supplierCode, itemCode, price);
        }
    }
}

/**
 * @brief Finds and displays the item with the lowest price for a given item code.
 *
 * This function iterates through the provided vector of items and finds the one
 * that matches the target item code and has the minimum price.
 *
 * @param items A constant reference to a vector of Item objects.
 * @param targetItemCode The item code to search for.
 */
void findLowestPrice(const std::vector<Item>& items, const std::string& targetItemCode) {
    const Item* lowestPriceItem = nullptr;
    double minPrice = std::numeric_limits<double>::max();
    bool found = false;

    for (const auto& item : items) {
        if (item.getItemCode() == targetItemCode) {
            found = true;
            if (item.getPrice() < minPrice) {
                minPrice = item.getPrice();
                lowestPriceItem = &item;
            }
        } else {
            // Since the input is sorted by item code, we can stop searching
            // once we've passed the block of target item codes.
            if (found) {
                break;
            }
        }
    }

    if (lowestPriceItem) {
        std::cout << "lowest price:" << std::endl;
        lowestPriceItem->display();
    } else {
        std::cout << "not found" << std::endl;
    }
}

/**
 * @brief The main function of the program.
 *
 * It orchestrates the reading of the input file, prompting the user for an
 * item code, and finding and displaying the item with the lowest price.
 *
 * @return 0 on successful execution.
 */
int main() {
    std::string fileName;
    std::cout << "please enter input file name" << std::endl;
    std::getline(std::cin, fileName);

    std::vector<Item> items;
    readItemsFromFile(fileName, items);

    if (!items.empty()) {
        std::string itemCode;
        std::cout << "please enter item code" << std::endl;
        std::cin >> itemCode;
        findLowestPrice(items, itemCode);    
    }

    return 0;
}