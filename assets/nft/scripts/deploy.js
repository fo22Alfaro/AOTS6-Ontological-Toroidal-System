const hre = require("hardhat");

async function main() {
  if (!process.env.RECIPIENT_ADDRESS) {
    throw new Error("Set RECIPIENT_ADDRESS to the intended collection owner/recipient address.");
  }
  const [signer] = await hre.ethers.getSigners();
  const signerAddress = await signer.getAddress();
  if (signerAddress.toLowerCase() !== process.env.RECIPIENT_ADDRESS.toLowerCase()) {
    throw new Error("Signer and RECIPIENT_ADDRESS differ. Set the intended owner explicitly; no transaction sent.");
  }

  const Factory = await hre.ethers.getContractFactory("AOTS6AssetRegistry");
  const contract = await Factory.deploy(process.env.RECIPIENT_ADDRESS);
  await contract.waitForDeployment();

  const address = await contract.getAddress();
  const network = await hre.ethers.provider.getNetwork();
  console.log(JSON.stringify({
    status: "DEPLOYED_WAIT_FOR_EXTERNAL_VERIFICATION",
    contractAddress: address,
    chainId: network.chainId.toString(),
    deployer: signerAddress,
    txHash: contract.deploymentTransaction()?.hash ?? null
  }, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
