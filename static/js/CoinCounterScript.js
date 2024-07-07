function add_coin_to_counter(){
    const coin_counter_element = document.getElementById("coin-counter-text");
    const coin_counter_str = coin_counter_element.textContent;
    const coin_counter_int = parseInt(coin_counter_str);
    const coin_counter_int_plus_one = coin_counter_int + 1;
    coin_counter_element.textContent = coin_counter_int_plus_one;
}