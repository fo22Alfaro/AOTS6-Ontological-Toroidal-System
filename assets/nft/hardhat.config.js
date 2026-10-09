require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

const networks = {};
if (process.env.RPC_URL && process.env.WALLET_KEY) {
  networks.configured = {
    url: process.env.RPC_URL,
    accounts: [process.env.WALLET_KEY],
    ...(process.env.CHAIN_ID ? { chainId: Number(process.env.CHAIN_ID) } : {})
  };
}

module.exports = {
  solidity: {
    version: "0.8.24",
    settings: { optimizer: { enabled: true, runs: 200 } }
  },
  paths: {
    sources: "./assets/nft/contracts",
    tests: "./assets/nft/test",
    cache: "./assets/nft/cache",
    artifacts: "./assets/nft/artifacts"
  },
  networks
};
