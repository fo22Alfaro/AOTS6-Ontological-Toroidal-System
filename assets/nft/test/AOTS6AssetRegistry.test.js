const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("AOTS6AssetRegistry", function () {
  async function deploy() {
    const [owner, recipient, outsider] = await ethers.getSigners();
    const Factory = await ethers.getContractFactory("AOTS6AssetRegistry");
    const contract = await Factory.deploy(owner.address);
    await contract.waitForDeployment();
    return { contract, owner, recipient, outsider };
  }

  it("starts empty with six slots", async function () {
    const { contract } = await deploy();
    expect(await contract.totalMinted()).to.equal(0n);
    expect(await contract.remainingSupply()).to.equal(6n);
  });

  it("mints token 1 and stores its metadata URI", async function () {
    const { contract, recipient } = await deploy();
    await expect(contract.mint(recipient.address, "ipfs://bafy-example/1.json"))
      .to.emit(contract, "AOTS6AssetMinted")
      .withArgs(1n, recipient.address, "ipfs://bafy-example/1.json");
    expect(await contract.ownerOf(1n)).to.equal(recipient.address);
    expect(await contract.tokenURI(1n)).to.equal("ipfs://bafy-example/1.json");
  });

  it("restricts minting to owner", async function () {
    const { contract, recipient, outsider } = await deploy();
    await expect(contract.connect(outsider).mint(recipient.address, "ipfs://metadata.json"))
      .to.be.revertedWithCustomError(contract, "OwnableUnauthorizedAccount");
  });

  it("rejects an empty URI", async function () {
    const { contract, recipient } = await deploy();
    await expect(contract.mint(recipient.address, ""))
      .to.be.revertedWithCustomError(contract, "EmptyMetadataURI");
  });

  it("caps supply at six", async function () {
    const { contract, recipient } = await deploy();
    for (let i = 1; i <= 6; i++) {
      await contract.mint(recipient.address, `ipfs://collection/${i}.json`);
    }
    expect(await contract.totalMinted()).to.equal(6n);
    expect(await contract.remainingSupply()).to.equal(0n);
    await expect(contract.mint(recipient.address, "ipfs://collection/7.json"))
      .to.be.revertedWithCustomError(contract, "CollectionComplete");
  });
});
