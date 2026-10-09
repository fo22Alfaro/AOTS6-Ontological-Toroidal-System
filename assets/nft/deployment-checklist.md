# AOTS⁶ NFT deployment checklist

## Current status
- [x] Six metadata records drafted.
- [x] Six original SVG image assets drafted.
- [x] ERC-721 source drafted with fixed supply of six.
- [ ] Install and pin OpenZeppelin Contracts v5.x in a reproducible build.
- [ ] Compile and run automated contract tests.
- [ ] Compute SHA-256 hashes for source, metadata and images.
- [ ] Upload images and metadata to IPFS or another content-addressed store; record CIDs.
- [ ] Review final metadata and rights statement.
- [ ] Select network and confirm chain ID.
- [ ] Deploy contract from the owner's wallet; retain signed transaction and receipt.
- [ ] Verify contract source on the network's explorer.
- [ ] Mint each token with its final immutable/content-addressed metadata URI.
- [ ] Verify `ownerOf`, `tokenURI`, transfer logs and total supply from an independent RPC/explorer.
- [ ] Add contract address, chain ID, token IDs, CIDs, transaction hashes and block numbers to the registry.
- [ ] Only activate reward logic after a separate written eligibility/funding policy is approved.

## Signing and security
The deployment and minting transactions require an authorized wallet signature. Never commit a private key or seed phrase. A wallet address alone does not authorize a transaction. Do not send funds to an address until its role and network are verified.
