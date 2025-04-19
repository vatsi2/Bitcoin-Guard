<?php
/**
 * Strategy: Binance Order
 * Language: PHP
 * Exchange: Binance (Spot)
 */
require 'vendor/autoload.php';
use Binance\API;

$api = new API('KEY','SECRET');
$order = $api->order([
    'symbol'=>'BTCUSDT','side'=>'BUY','type'=>'LIMIT','quantity'=>0.01,'price'=>29000
]);
print_r($order);
