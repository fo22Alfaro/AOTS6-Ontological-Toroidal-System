const hre = require("hardhat");

const slugs = [
  "aots6-core",
  "global-network",
  "zk-core",
  "unification-ledger",
  "unified-kernel",
  "provenance-rewards"
];

async function main() {
  const contractAddress = process.env.NFT_CONTRACT_ADDRESS;
  const recipient = process.env.RECIPIENT_ADDRESS;
  const metadataBase = process.env.METADATA_BASE_URI;

  if (!contractAddress || !recipient || !metadataBase) {
    throw new Error("Set NFT_CONTRACT_ADDRESS, RECIPIENT_ADDRESS and METADATA_BASE_URI. Use an immutable/content-addressed metadata base for production.");
  }
  if (!metadataBase.endsWith("/")) {
    throw new Error("METADATA_BASE_URI must end with '/'. No transaction sent.");
  }

  const [signer] = await hre.ethers.getSigners();
  const contract = await hre.ethers.getContractAt("AOTS6AssetRegistry", contractAddress, signer);
  const owner = await contract.owner();
  if (owner.toLowerCase() !== (await signer.getAddress()).toLowerCase()) {
    throw new Error("Signer is not contract owner. No transaction sent.");
  }

  for (let i = 0; i < slugs.length; i++) {
    const tokenId = i + 1;
    const uri = `${metadataBase}${tokenId}.json`;
    const tx = await contract.mint(recipient, uri);
    const receipt = await tx.wait();
    console.log(JSON.stringify({
      tokenId,
      recipient,
      metadataURI: uri,
      transactionHash: receipt.hash,
      blockNumber: receipt.blockNumber,
      status: receipt.status
    }));
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
