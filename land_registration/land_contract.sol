pragma solidity ^0.4.4;

// contract starts
contract land_bargain {

    // Define the Structure
    struct Land {
      uint id;
      address owner;
      string name;
      string city;
      string land_address;
      string latitude;
      string longitude;
      uint value;
    }
    
    // define the mappping for the owner_properties;
    mapping(address => uint[]) owner_properties;

    uint[] public land_availabe_to_sell;
    
    function add_property(address _owner_address, uint _x) public {
        owner_properties[_owner_address].push(_x);
    }

    function get_property(address _address) view public returns(uint[]){
        return owner_properties[_address];
    }
    
    function add_land_available_to_sell(uint _x) public{
        land_availabe_to_sell.push(_x);
    }
    
    function get_land_availabe_to_sell() view public returns(uint[]){
        return land_availabe_to_sell;
    }
    // State variables
    
    
    mapping(uint => Land) public landList;
    
    //variable to store the list counter
    uint landListCounter;
    
    event registerLandEvent (
      uint indexed _id,
      address indexed _landOwner,
      string _ownerName,
      string _city,
      string land_address,
      string latitude,
      string longitude,
      uint value
    );
    
    // register land
    function registerLand(address _landOwner, string _name, string _city, string _land_address, string _latitude, string _longitude) public {

        // store the Land title
        landList[landListCounter] = Land(landListCounter, _landOwner, _name, _city, _land_address, _latitude, _longitude, 0);
        // add property to the list
        add_property(_landOwner, landListCounter);
        landListCounter++;

        // trigger the event
        // registerLandEvent(landListCounter, msg.sender, _name, _city);
    }
    
    //fetch the number of Land registered in the contract
    function getNumberOfLandRegistered() public constant returns (uint) {
      return landListCounter;
    }
    
    // fetch and returns all land IDs getNumberOfLandRegistered
    function getRegisteredLandList() public constant returns (uint[]) {
      // we check whether there is at least one registered Land
      require(landListCounter > 0);

      if (landListCounter  == 0) {
        return new uint[](0);
      }

      //prepare output arrays
      uint[] memory registeredLandList = new uint[] (landListCounter);
      for (uint i = 0; i < landListCounter; i++) {
        registeredLandList[i] = landList[i].id;
      }
      
      // return the result
      return (registeredLandList);
    }

}
 
