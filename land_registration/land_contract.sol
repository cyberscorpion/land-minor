pragma solidity ^0.4.4;
// 0.4.25
contract land_bargain {

    // enum Status { NotExist, Pending, Approved, Rejected }
    struct Land {
      uint id;
      address owner;
      string name;
      string city;
      string area;
      string land_address;
      string latitude;
      string longitude;
      uint value;
    }
    
    mapping(address => uint[]) owner_properties;

    // uint[] public land_availabe_to_sell;
    
    function add_property(address _owner_address, uint _x) public {
        owner_properties[_owner_address].push(_x);
    }

    function get_property(address _address) view public returns(uint[]){
        return owner_properties[_address];
    }
    function change_ownership(uint _x,address _oldOwner, address _newOwner, string _name) payable public returns(uint[]){
        uint[] storage temp_arr;
        for(uint i = 0; i < owner_properties[_oldOwner].length; i++) {
            temp_arr.push(owner_properties[_oldOwner][i]);
            // delete owner_properties[_oldOwner][i] ;
        }
        delete owner_properties[_oldOwner];
        for(uint j = 0; j < temp_arr.length; j++) {
            if(temp_arr[j] != _x){
                 owner_properties[_oldOwner].push(temp_arr[j]);
            }
        }
        landList[_x].owner = _newOwner;
        landList[_x].name = _name;
        owner_properties[_newOwner].push(_x);
        return temp_arr;
    }
    
    // function add_land_available_to_sell(uint _x, uint _value) public{
    //     landList[_x].value = _value;
    //     land_availabe_to_sell.push(_x);
    // }
    
    // function get_land_availabe_to_sell() view public returns(uint[]){
    //     return land_availabe_to_sell;
    // }
    // State variables
    
    
    mapping(uint => Land) public landList;
    uint landListCounter;
    
    event registerLandEvent (
      uint indexed _id,
      address indexed _landOwner,
      string _ownerName,
      string _city,
      string _area,
      string land_address,
      string latitude,
      string longitude,
      uint value
    );
    
    // register land
    function registerLand(address _landOwner, string _name, string _city, string _area, string _land_address, string _latitude, string _longitude) public {

        // store the Land title
        landList[landListCounter] = Land(landListCounter, _landOwner, _name, _city, _area, _land_address, _latitude, _longitude, 0);
        // owner_properties[_landOwner].push(landListCounter);
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

      return (registeredLandList);
    }
    
    // function getcheck() public returns(string){
    //     landList[0].value = 9898;
    //     return landList[0].name;
    // }
    
//     struct PropertyDetail {
// // 		Status status;
// 		uint value;
// 		uint area;
// 		address currOwner;
// 	}
// 	mapping(address => PropertyDetail) public properties;
	
// 	address[] public registerdProperties;
// 	address[] public availableProperties;
    
//     function setRegistedProperty(address _land_address ,uint _value, uint _area, address _currOwner) public {
//         var property = properties[_land_address];
        
//         property.value = _value;
//         property.area = _area;
//         property.currOwner = _currOwner;
        
//         registerdProperties.push(_land_address) -1;
//     }
//     function getPropertyDetail(address _land_address) view public returns(uint, uint, address){
//         return(properties[_land_address].value, properties[_land_address].area, properties[_land_address].currOwner);
//     }
    
//     function setAvailableProperty(address _land_address) public {
//         availableProperties.push(_land_address);
//     }
    
    // function removeAvailableProperty(address _land_address) public{
        
    // }
    
    // function getAvailableProperty() view public returns(address[]){
    //     return availableProperties;
    // }

}
