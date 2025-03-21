// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface ITornado {
    function deposit(bytes32 commitment) external payable;
    function withdraw(
        bytes calldata _proof,
        bytes32 _root,
        bytes32 _nullifierHash,
        address payable _recipient,
        address payable _relayer,
        uint256 _fee,
        uint256 _refund
    ) external payable;
}

contract AnonDAO {
    ITornado public tornado;

    constructor(address _tornado) {
        tornado = ITornado(_tornado);
    }

    function anonymizeDeposit(bytes32 commitment) external payable {
        tornado.deposit{value: msg.value}(commitment);
    }
}
