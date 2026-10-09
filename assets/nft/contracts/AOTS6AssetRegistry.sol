// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

// Build with OpenZeppelin Contracts v5.x.
// Deployment/minting is NOT performed by committing this source file.
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AOTS6AssetRegistry
 * @notice Fixed six-token collection for AOTS6 artifact provenance.
 * @dev A token records an identifier and metadata URI. It does not itself
 * grant copyright, a licence, equity, revenue share, or a financial reward.
 * Minting requires deployment and a signed transaction by the owner.
 */
contract AOTS6AssetRegistry is ERC721URIStorage, Ownable {
    uint256 public constant MAX_SUPPLY = 6;
    uint256 private _nextTokenId = 1;

    error CollectionComplete();
    error EmptyRecipient();
    error EmptyMetadataURI();

    event AOTS6AssetMinted(
        uint256 indexed tokenId,
        address indexed recipient,
        string metadataURI
    );

    constructor(address initialOwner)
        ERC721("AOTS6 Provenance Assets", "AOTS6")
        Ownable(initialOwner)
    {
        if (initialOwner == address(0)) revert EmptyRecipient();
    }

    function mint(address recipient, string calldata metadataURI)
        external
        onlyOwner
        returns (uint256 tokenId)
    {
        if (recipient == address(0)) revert EmptyRecipient();
        if (bytes(metadataURI).length == 0) revert EmptyMetadataURI();
        if (_nextTokenId > MAX_SUPPLY) revert CollectionComplete();

        tokenId = _nextTokenId++;
        _safeMint(recipient, tokenId);
        _setTokenURI(tokenId, metadataURI);
        emit AOTS6AssetMinted(tokenId, recipient, metadataURI);
    }

    function totalMinted() external view returns (uint256) {
        return _nextTokenId - 1;
    }

    function remainingSupply() external view returns (uint256) {
        return MAX_SUPPLY - (_nextTokenId - 1);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
