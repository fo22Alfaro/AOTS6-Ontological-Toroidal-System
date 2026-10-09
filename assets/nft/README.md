# AOTS⁶ NFT collection — deploy-ready source package

This package prepares a six-item ERC-721 provenance collection. It is **not yet deployed or minted**. A GitHub commit does not mint an NFT.

## Items
1. Núcleo Toroidal
2. Global Network
3. ZK Core
4. Unification Ledger
5. Unified Kernel
6. Provenance & Rewards

## Files
- `AOTS6AssetRegistry.sol`: fixed-supply ERC-721 contract (OpenZeppelin Contracts v5.x).
- `metadata/1.json` … `metadata/6.json`: item metadata.
- `images/*.svg`: original vector artworks referenced by metadata.
- `deployment-checklist.md`: steps required to turn this package into a verifiable on-chain collection.

## Important status
- Source and metadata: prepared in this repository.
- Contract address: not deployed.
- Token IDs: not minted.
- Transaction hashes/receipts: none yet.
- IPFS CIDs: not generated.
- Reward policy and funding: not activated.

Do not mark any token as minted or verified until the contract address, network/chain ID, token ID, transaction receipt, and retrievable metadata have been checked independently. The metadata's GitHub raw image URLs are mutable publication URLs; use IPFS or another content-addressed store for durable token metadata before mainnet minting.

The NFTs are provenance markers, not automatic transfers of copyright, licences, revenue, equity, or guaranteed rewards. Any reward must have a separate published policy and confirmed funding.
