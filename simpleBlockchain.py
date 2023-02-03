import hashlib
import json
import os

# class ของ blockchain ระบุรายละเอียดของ blockchain
class estateBlock:
    def __init__(self, blockID, land_of_deed_number, owner, date_of_deed_issuance, size, sub_district, district, province, price, date_bought, land_location, prv_block_hash) :
        self.blockID = blockID
        self.land_of_deed_number = land_of_deed_number
        self.owner = owner
        self.date_of_deed_issuance = date_of_deed_issuance
        self.size = size
        self.sub_district = sub_district
        self.district = district
        self.province = province
        self.price = price
        self.date_bought = date_bought
        self.land_location = land_location
        self.prv_block_hash = prv_block_hash
        block_data = (self.blockID + land_of_deed_number + self.owner + date_of_deed_issuance + self.size + sub_district + district + province + price + date_bought + land_location + prv_block_hash)
        self.block_hash = hashlib.sha256(block_data.encode()).hexdigest()

# function บันทึกข้อมูลลง block
def record_data():
    print("input land of deed number")
    inputLandOfDeed = input()
    print("input owner")
    inputOwner = input()
    print("input date of deed issuance")
    inputDateOfDeed = input()
    print("input size(km^2)")
    inputSize = input()
    print("input sub_district")
    inputSubDistrict = input()
    print("input district")
    inputDistrict = input()
    print("input province")
    inputProvince = input()
    print("input price")
    inputPrice = input()
    print("input date bought")
    inputDateBought = input()
    print("input land location")
    inputLandLocation = input()
    currentBlock = estateBlock(blockID, inputLandOfDeed, inputOwner, inputDateOfDeed, inputSize, inputSubDistrict, inputDistrict, inputProvince, inputPrice, inputDateBought, inputLandLocation, prv_hash)
    j = open("data.json", "w")

    bh = "{ \"block_hash\": \"" + currentBlock.block_hash + "\","
    id = "\"blockID\": \"" + blockID + "\","
    ln = "\"land_of_deed_number\": \"" + inputLandOfDeed + "\"," #
    ow = "\"owner\": \"" + inputOwner + "\"," #
    di = "\"date_of_deed_issuance\": \"" + inputDateOfDeed + "\"," #
    si = "\"size\": \"" + inputSize + "\"," #
    sdis = "\"sub_district\": \"" + inputSubDistrict + "\"," #
    dis = "\"district\": \"" + inputDistrict + "\"," #
    pro = "\"province\": \"" + inputProvince + "\","
    pri = "\"price\": \"" + inputPrice + "\","
    db = "\"date_bought\": \"" + inputDateBought + "\","
    ll = "\"land_location\": \"" + inputLandLocation + "\","
    pr = "\"prv_block_hash\": \"" + prv_hash + "\"}"

    blockchain_data = json.loads(bh+id+ln+ow+di+si+sdis+dis+pro+pri+db+ll+pr)
    jsonData.append(blockchain_data)
    json.dump(jsonData, j, sort_keys=True, indent=4)
    if data_verification():
        print("Blockchain data is valid")
    else:
        print("Blockchain data is invalid")
    print("")

# function สร้าง genesis block
def genesis_block():
    print("input land of deed number")
    inputLandOfDeed = input()
    print("input owner")
    inputOwner = input()
    print("input date of deed issuance")
    inputDateOfDeed = input()
    print("input size(km^2)")
    inputSize = input()
    print("input sub_district")
    inputSubDistrict = input()
    print("input district")
    inputDistrict = input()
    print("input province")
    inputProvince = input()
    print("input price")
    inputPrice = input()
    print("input date bought")
    inputDateBought = input()
    print("input land location")
    inputLandLocation = input()
    currentBlock = estateBlock(iniID, inputLandOfDeed,inputOwner, inputDateOfDeed, inputSize, inputSubDistrict, inputDistrict, inputProvince, inputPrice, inputDateBought, inputLandLocation, "genesis block")
    j = open("data.json", "w")
    blockchain_data = [currentBlock.__dict__]
    json.dump(blockchain_data, j, sort_keys=True, indent=4)

# function ยืนยันข้อมูลทั้งหมดใน blockchain
def data_verification():
    for i in range(1, len(jsonData)):
        current_block = jsonData[i]
        search_key = "blockID"
        search_value = str(i-1)
        for item in jsonData:
            if search_key in item and item[search_key] == search_value:
                block_data = (item["blockID"] + item["land_of_deed_number"] + item["owner"] + item["date_of_deed_issuance"] + item["size"] + item["sub_district"] + item["district"] + item["province"] + item["price"] + item["date_bought"] + item["land_location"] + item["prv_block_hash"])
                if current_block["prv_block_hash"] != hashlib.sha256(block_data.encode()).hexdigest():
                    print("Invalid!!!! blockID: " + item["blockID"])
                    print("digest from invalid data   :" + current_block["prv_block_hash"])
                    print("digest from hash by sha256 :" +hashlib.sha256(block_data.encode()).hexdigest())
                    return False
    return True

# function ค้นหาข้อมูลจากชื่อเจ้าของ
def search_by_owner():
    print("Input owner name:")
    search_value = input()
    search_key = "owner"
    for item in jsonData:
        if search_key in item and item[search_key] == search_value:
            print("From blockID: " + item["blockID"])
            print(item)
            print("")
    else:
        print("Does not has this owner")

# โปรแกรมเริ่มรันตรงนี้ (:
# เริ่มจากเช็คก่อนว่าเคยมี block มาก่อนรึเปล่า
# ถ้าเคยมี block ก่อนหน้านี้ก็สร้าง block ต่อไปตามปกติ
if os.path.exists("data.json"): 
    with open("data.json", "r") as file:
        jsonData = json.load(file)
# ถ้าไม่เคยมี block มาก่อนต้องเริ่มจากสร้าง genesis block
else:
    print("START CREATE GENESIS THE BLOCK")
    prv_hash = "genesis block"
    iniID = "0"
    genesis_block()
    with open("data.json", "r") as file:
        jsonData = json.load(file)

print("WELCOME TO myBLOCKCHAIN")
while True :
    for item in jsonData:
        prv_hash = item["block_hash"]
        blockID = str(int(item["blockID"]) + 1)
    print("press 1 to record data")
    print("press 2 to check if data is valid")
    print("press 3 to search information by input owner name")
    print("press 0 to exit")
    x = input()
    print("")
    if x == "1":
        record_data()
    elif x == "2":
        if data_verification():
            print("blockchain data is valid")
            print("")
        else:
            print("blockchain data is invalid")
            print("")
    elif x == "3":
        if data_verification():
            search_by_owner()
        else:
            print("blockchain data is invalid")
            print("data should be correct before search")
            print("")
    elif x == "0":
        print("GoodBye")
        break
