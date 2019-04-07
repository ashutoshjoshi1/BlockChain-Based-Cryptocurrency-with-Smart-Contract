pragma solidity ^0.5.1;

contract samriddhicoin_ico {

    // Introducing the maximum number of samriddhicoins available for sale
    uint public max_samriddhicoins = 100000;

    // Introducing the INR to samriddhicoins conversion rate
    uint public INR_to_samriddhicoins = 10;

    // Introducing the total number of samriddhicoins that have been bought by the inventors
    uint public total_samriddhicoins_bought = 0;

    // Mapping from the investor address to its equity in samriddhicoins and INR
    mapping(address => uint) equity_samriddhicoins;
    mapping(address => uint) equity_INR;

    // Checking if an investor can buy samriddhicoins
    modifier can_buy_samriddhicoins(uint INR_invested) {
        require (INR_invested * INR_to_samriddhicoins + total_samriddhicoins_bought <= max_samriddhicoins);
        _;//if above statement is correct
    }

    // Getting the equity in samriddhicoins of an investor
    function equity_in_samriddhicoins(address investor) external view returns (uint) {
        return equity_samriddhicoins[investor];
    }

    // Getting the equity in INR of an investor
    function equity_in_INR(address investor) external view returns (uint) {
        return equity_INR[investor];
    }

    // Buying samriddhicoins
    function buy_samriddhicoins(address investor, uint INR_invested) external
    can_buy_samriddhicoins(INR_invested) {
        uint samriddhicoins_bought = INR_invested * INR_to_samriddhicoins;
        equity_samriddhicoins[investor] += samriddhicoins_bought;
        equity_INR[investor] = equity_samriddhicoins[investor] / INR_to_samriddhicoins;
        total_samriddhicoins_bought += samriddhicoins_bought;
    }

    // Selling samriddhicoins
    function sell_samriddhicoins(address investor, uint samriddhicoins_sold) external {
        equity_samriddhicoins[investor] -= samriddhicoins_sold;
        equity_INR[investor] = equity_samriddhicoins[investor] / INR_to_samriddhicoins;
        total_samriddhicoins_bought -= samriddhicoins_sold;
    }

}
