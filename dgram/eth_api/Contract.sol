// SPDX-License-Identifier: MIT
//pragma solidity 0.8.10;

pragma solidity >=0.5.16;

contract Contract {
    string public name = "ImgTip";
    uint public imageCount = 0;
    mapping(uint => Image) public images;

    struct Image {
        uint id;
        string hash;
        string description;
        uint tipAmount;
        address payable author;
        uint timestamp;
    }

    event ImageCreated(
        uint id,
        string hash,
        string description,
        uint tipAmount,
        address payable author,
        uint timestamp
    );

    event ImageTipped(
        uint id,
        string hash,
        string description,
        uint tipAmount,
        address payable author,
        uint timestamp
    );


    function uploadImage(string memory _imgHash, string memory _description) public {
        require(bytes(_imgHash).length > 0);
        require(bytes(_description).length > 0);
        require(msg.sender != address(0));

        imageCount ++;

        images[imageCount] = Image(imageCount, _imgHash, _description, 0, payable(msg.sender), block.timestamp);
        emit ImageCreated(imageCount, _imgHash, _description, 0, payable(msg.sender), block.timestamp);
    }

    function tipImageOwner(uint _id) public payable {
        require(_id > 0 && _id <= imageCount);
        Image memory _image = images[_id];
        address payable _author = _image.author;
        payable(_author).transfer(msg.value);
        _image.tipAmount = _image.tipAmount + msg.value;
        images[_id] = _image;
        emit ImageTipped(_id, _image.hash, _image.description, _image.tipAmount, _author, block.timestamp);
    }
}