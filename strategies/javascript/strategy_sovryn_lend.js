const { Client } = require("bitcoin-core");  // Bitcoin Core RPC client

async function sovrynLend() {
  const client = new Client({ network: "mainnet", username: "user", password: "pass" });
  // TODO: interact with Sovryn smart contracts via RSK bridge
}

sovrynLend().catch(console.error);
